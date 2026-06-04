/**
 * /api/ask — grounded Q&A for a Field Guide. Plain CommonJS, zero dependencies.
 *
 * Flow: validate → rate-limit (per-IP + global, via Upstash/Vercel KV REST) →
 * retrieve the most relevant notes from that guide's ask-corpus.json (keyword
 * overlap, title-weighted) → ask Claude to answer using ONLY those excerpts →
 * stream the answer back as plain text. The slugs of the notes used go in the
 * X-Ask-Sources header so the client renders "Go deeper" links.
 *
 * Uses native Node req/res and global fetch only (no @vercel/node helpers, no
 * build step) so it runs on the plain Node function runtime.
 *
 * Env (Vercel project): ANTHROPIC_API_KEY (required);
 *   KV_REST_API_URL/KV_REST_API_TOKEN or UPSTASH_REDIS_REST_URL/_TOKEN
 *   (optional — without it the endpoint runs but is NOT rate-limited).
 */
const MODEL = "claude-sonnet-4-6";
const MAX_Q = 500;
const TOP_NOTES = 3;
const SECS_PER_NOTE = 2;
const SEC_CHARS = 700;
const MAX_TOKENS = 400;
const RELEVANCE_FLOOR = 3;

const GUIDES = {
  "ipas": { name: "IPA Knowledge Base", topic: "the India Pale Ale (IPA) style of beer" },
  "pour-over": { name: "Pour Over Knowledge Base", topic: "pour over (manual filter) coffee" },
};

// ---- corpus (cached per warm instance) ----
const corpusCache = {};
async function loadCorpus(host, guide) {
  if (corpusCache[guide]) return corpusCache[guide];
  const proto = /^(localhost|127\.|0\.0\.0\.0)/.test(host) ? "http" : "https";
  const res = await fetch(`${proto}://${host}/${guide}/assets/ask-corpus.json`);
  if (!res.ok) throw new Error("corpus " + res.status);
  const data = await res.json();
  corpusCache[guide] = data;
  return data;
}

// ---- retrieval (token overlap, title-weighted) ----
const STOP = new Set(
  ("the a an is are of for to and or in on with vs it this that can should do does " +
   "did my me i you what whats how why when which who was be").split(" ")
);
function tokenize(q) {
  return q.toLowerCase().split(/[^a-z0-9]+/).filter((t) => t.length > 2 && !STOP.has(t));
}
function retrieve(corpus, q) {
  const toks = tokenize(q);
  if (!toks.length) return [];
  const scored = corpus.map((note) => {
    const title = note.title.toLowerCase();
    const secs = note.sections.map((s) => {
      const text = (s.h + " " + s.t).toLowerCase();
      let sc = 0;
      for (const w of toks) if (text.includes(w)) sc += 1;
      return { s, sc };
    });
    let score = secs.reduce((a, b) => a + b.sc, 0);
    for (const w of toks) if (title.includes(w)) score += 5;
    secs.sort((a, b) => b.sc - a.sc);
    return { note, score, secs };
  });
  scored.sort((a, b) => b.score - a.score);
  return scored.filter((x) => x.score >= RELEVANCE_FLOOR).slice(0, TOP_NOTES);
}
function buildContext(top) {
  const slugs = [];
  const blocks = top.map(({ note, secs }) => {
    slugs.push(note.slug);
    const chosen = secs.filter((x) => x.sc > 0).slice(0, SECS_PER_NOTE);
    const use = chosen.length ? chosen : secs.slice(0, 1);
    const body = use
      .map(({ s }) => (s.h ? `### ${s.h}\n` : "") + s.t.slice(0, SEC_CHARS))
      .join("\n\n");
    return `# ${note.title}\n${body}`;
  });
  return { context: blocks.join("\n\n---\n\n"), slugs };
}

// ---- rate limit (Upstash/Vercel KV REST; optional) ----
const KV_URL = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL || "";
const KV_TOKEN = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN || "";
const LIMITS = [
  { key: (ip) => `ask:min:${ip}`, ttl: 60, max: 3 },
  { key: (ip) => `ask:day:${ip}`, ttl: 86400, max: 12 },
  { key: () => `ask:global:day`, ttl: 86400, max: 20 },
];
async function isRateLimited(ip) {
  if (!KV_URL || !KV_TOKEN) return false;
  try {
    const cmds = LIMITS.flatMap((l) => [
      ["INCR", l.key(ip)],
      ["EXPIRE", l.key(ip), String(l.ttl), "NX"],
    ]);
    const res = await fetch(`${KV_URL}/pipeline`, {
      method: "POST",
      headers: { Authorization: `Bearer ${KV_TOKEN}`, "Content-Type": "application/json" },
      body: JSON.stringify(cmds),
    });
    if (!res.ok) return false;
    const out = await res.json();
    for (let i = 0; i < LIMITS.length; i++) {
      const count = Number((out[i * 2] && out[i * 2].result) || 0);
      if (count > LIMITS[i].max) return true;
    }
    return false;
  } catch {
    return false;
  }
}

// ---- read JSON body (works with or without framework body parsing) ----
function readJson(req) {
  if (req.body && typeof req.body === "object") return Promise.resolve(req.body);
  if (typeof req.body === "string") {
    try { return Promise.resolve(JSON.parse(req.body)); } catch { return Promise.resolve({}); }
  }
  return new Promise((resolve) => {
    let data = "";
    req.on("data", (c) => (data += c));
    req.on("end", () => { try { resolve(JSON.parse(data || "{}")); } catch { resolve({}); } });
    req.on("error", () => resolve({}));
  });
}

// ---- Claude (Messages API, streamed via fetch + SSE parse) ----
async function streamClaude(apiKey, system, q, context, onText) {
  const resp = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "x-api-key": apiKey,
      "anthropic-version": "2023-06-01",
      "content-type": "application/json",
    },
    body: JSON.stringify({
      model: MODEL,
      max_tokens: MAX_TOKENS,
      stream: true,
      system: [{ type: "text", text: system, cache_control: { type: "ephemeral" } }],
      messages: [{ role: "user", content: `Question: ${q}\n\nGuide excerpts:\n\n${context}` }],
    }),
  });
  if (!resp.ok || !resp.body) throw new Error("anthropic " + resp.status);
  const reader = resp.body.getReader();
  const decoder = new TextDecoder();
  let buf = "";
  for (;;) {
    const { done, value } = await reader.read();
    if (done) break;
    buf += decoder.decode(value, { stream: true });
    let nl;
    while ((nl = buf.indexOf("\n")) >= 0) {
      const line = buf.slice(0, nl).trim();
      buf = buf.slice(nl + 1);
      if (!line.startsWith("data:")) continue;
      const payload = line.slice(5).trim();
      if (!payload || payload === "[DONE]") continue;
      try {
        const ev = JSON.parse(payload);
        if (ev.type === "content_block_delta" && ev.delta && ev.delta.type === "text_delta") {
          onText(ev.delta.text);
        }
      } catch { /* keep-alive / non-JSON */ }
    }
  }
}

function send(res, status, text) {
  res.statusCode = status;
  res.setHeader("Content-Type", "text/plain; charset=utf-8");
  res.end(text);
}

module.exports = async function handler(req, res) {
  if (req.method !== "POST") return send(res, 405, "Method Not Allowed");

  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) return send(res, 500, "Assistant not configured.");

  const body = await readJson(req);
  const guide = String((body && body.guide) || "");
  const q = String((body && body.q) || "").replace(/\s+/g, " ").trim();
  const meta = GUIDES[guide];
  if (!meta) return send(res, 400, "Unknown guide.");
  if (!q || q.length > MAX_Q) return send(res, 400, "Question missing or too long.");

  const ip =
    String(req.headers["x-forwarded-for"] || "").split(",")[0].trim() ||
    String(req.headers["x-real-ip"] || "") ||
    "anon";
  if (await isRateLimited(ip)) return send(res, 429, "Rate limited.");

  let top;
  try {
    const corpus = await loadCorpus(String(req.headers.host || ""), guide);
    top = retrieve(corpus, q);
  } catch {
    return send(res, 500, "Could not load the guide.");
  }

  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain; charset=utf-8");
  res.setHeader("Cache-Control", "no-store");

  if (!top.length) {
    res.setHeader("X-Ask-Sources", "[]");
    return res.end("This guide doesn’t appear to cover that. Try rephrasing, or browse the notes.");
  }

  const { context, slugs } = buildContext(top);
  res.setHeader("X-Ask-Sources", JSON.stringify(slugs));

  const system =
    `You are the assistant for the ${meta.name}, a reference guide on ${meta.topic}. ` +
    `Answer the reader's question using ONLY the excerpts from the guide provided below. ` +
    `Be concise and direct: 2–4 sentences of plain prose, no markdown headings or lists. ` +
    `If the excerpts do not contain the answer, say the guide doesn't cover it and point to ` +
    `the closest topic. Never invent facts, numbers, brands, or recipes that are not in the ` +
    `excerpts. Speak as the guide; do not mention "excerpts", "notes", or "context".`;

  try {
    await streamClaude(apiKey, system, q, context, (t) => res.write(t));
    res.end();
  } catch {
    res.end();
  }
};
