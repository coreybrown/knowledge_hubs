# "Ask the Guide" — grounded Q&A for the Field Guides

A natural-language question box on each field guide that answers from *that guide's*
content, succinctly, with links to go deeper. Decided design is locked below.

*Status: spec / pre-build. Drafted 2026-06-04.*

---

## Decisions (locked)

| Area | Choice |
|---|---|
| Model | **Claude Sonnet 4.6** (`claude-sonnet-4-6`) |
| Retrieval | **Keyword/BM25** over a per-guide corpus (Claude-only, no embeddings key) |
| UX | **Ask-first** — the search box leads with a question field; keyword matches shown as fallback |
| Abuse/cost | **Per-IP rate limit** (Vercel KV/Upstash) + input cap + Anthropic monthly spend ceiling |
| Backend | **Vercel Serverless Function** at `/api/ask` — **Node/TypeScript** (same-origin) |
| Scope | Per-guide (IPAs, Pour Over). Each answers only from its own notes. |
| Budget | **$5/month** hard Anthropic ceiling |
| Rate limits | **3/min, 12/day per IP** + **~20/day global** soft backstop |

---

## How it works (data flow)

```
Browser (search overlay, "Ask" mode)
  │  POST /api/ask   { guide: "pour-over", q: "What's the best V60 recipe?" }
  ▼
Vercel function  /api/ask
  1. Rate-limit check (per-IP, KV)         → 429 if exceeded
  2. Validate + cap input length
  3. BM25 retrieve top ~5 notes from ask-corpus.<guide>.json
  4. Call Claude (Sonnet 4.6), streaming:
       system: grounding rules (+ prompt cache)
       user:   question + the 5 notes' text + their slugs
  5. Stream answer tokens back to the browser
  ▼
Browser renders streamed answer + "Go deeper" source cards
  (cards reuse the existing search-result style: domain icon + accent color)
```

Same-origin `/api/ask` means the current CSP (`connect-src 'self'`) already allows
it — **no CSP change, and the API key never reaches the browser.**

---

## Retrieval

- Build step emits one `ask-corpus.<guide>.json` per guide:
  `[{ slug, title, domain, url, text }]` — plain text of each note, ~1–2 MB total.
- BM25 (or simple TF-IDF) over the corpus, in the function, returns the top ~5 notes.
  Corpus is ~150 notes, so this is trivial in-memory work — no vector DB.
- Upgrade path (later, if recall on conceptual questions disappoints): add Voyage AI
  embeddings as a second retrieval signal. Not in v1.

## Generation (grounding + citations)

System prompt rules:
- Answer **only** from the supplied notes. If they don't cover it, say so plainly.
- Be succinct (≈2–4 sentences). No invented brands, numbers, or recipes.
- Identify which note slugs the answer drew from.

The frontend turns those slugs into "Go deeper" links to the source pages. Prompt
caching on the system prompt keeps per-call cost down.

---

## UX — ask-first search overlay

The existing `/`-triggered search modal is reworked:

- Lead input is a **question** field ("Ask anything about pour over…").
- As you type, show instant keyword matches live (current behavior, kept).
- On **Enter**, switch to Ask: stream an answer above, with source cards below it,
  and keep keyword matches available as "Or jump to a page".
- States: idle / typing (keyword matches) / streaming answer / answered (+sources) /
  error / rate-limited. Esc closes; no inline scripts (CSP-safe, lives in `app.js`).

---

## Cost & abuse controls

Budget is **$5/month** — tight, so the design is sized to fit it:

- **Per-question cost:** ~2–3¢ at top-5 whole notes → trimmed to **top-3 notes +
  section-level snippets** + **answer caching** → ~1–1.5¢. Realistic capacity on $5:
  **~350–450 fresh questions/month** (more with cache hits).
- **Rate limit:** per-IP sliding window — **3/min, 12/day** — via Vercel KV / Upstash.
- **Global soft cap:** **~20/day** so a traffic spike can't drain the month in a day.
- **Input cap:** reject questions over ~500 chars; one question per request.
- **Spend ceiling:** hard $5 monthly limit in the Anthropic console (the real backstop).
- **Graceful degrade:** when any cap is hit, the box shows an "assistant is resting —
  use search" state, not an error. Keyword search always works.
- Answer cache (KV) for repeated/common questions; simple bot heuristic.

---

## Risks / tradeoffs (honest)

- Ends the site's pure-static, $0, no-backend property.
- Hallucination risk → mitigated by strict grounding + "not covered" fallback.
- ~1–4s latency per answer.
- Ongoing upkeep: key rotation, usage monitoring, dependency updates.

---

## Build plan (files)

- `api/ask.ts` — function: rate limit → validate → BM25 retrieve → Claude stream.
  *(Node/TypeScript recommended: best Vercel streaming + Anthropic TS SDK. Python
  possible to match the build scripts, but streaming is clunkier.)*
- `build_ask_corpus.py` (or extend `build_site.py`) — emit `ask-corpus.<guide>.json`
  into each guide's `assets/`; `build_landing.py` copies it into `docs/<guide>/assets/`.
- `build_assets.py` — rework the search overlay JS + CSS for ask-first mode.
- `package.json` — `@anthropic-ai/sdk` (+ rate-limit/KV client) if Node.
- `vercel.json` — Node `/api` functions auto-detected; **CSP unchanged.**

## Provisioning needed (yours to create; I wire it up)

1. **`ANTHROPIC_API_KEY`** — create at console.anthropic.com, add to Vercel project env.
2. Green light to add a **serverless backend** (function + env vars) to the project.
3. A **monthly spend ceiling** ($ figure) for the Anthropic usage limit + rate sizing.
4. A **KV store** (Vercel KV or Upstash Redis, free tier) with its env vars added to Vercel.

## Build status

**Done (no secrets / no backend) — shipped into both generators:**
- `build_site.py` → `write_ask_corpus()` emits `assets/ask-corpus.json` per guide
  (per-note, split into H2 sections; nav sections dropped). 154/144 notes.
- Ask-first search overlay (`build_site.py` `search_overlay()` + `build_assets.py`
  JS/CSS): question-led box, token-based retrieval, streamed answer, "Go deeper"
  source cards, "Jump to a note" fallback, example-question chips, and the
  resting/error states. Token scorer fixes natural-language matching.
- **Preview mode:** `ASK_ENABLED=false` in the overlay JS → answers are a local
  stub (real keyword retrieval + simulated stream) so the UX is fully clickable
  before the backend exists. Dev: type `:resting` or `:error` to preview states.

**Backend wiring (needs the provisioning below) — integration points already in place:**
- Flip `ASK_ENABLED=true` in the overlay JS (build_assets.py, both guides).
- `streamReal()` already POSTs `/api/ask {guide,q}` and reads a streamed body;
  finalize it to use server-returned sources instead of the client-side guess.
- Build `api/ask.ts`: rate-limit → validate → BM25 over `ask-corpus.json`
  (top-3 + section snippets) → Claude Sonnet 4.6 stream.

## Open items before build

All resolved — ready to build once provisioning lands:
- ✅ Spend ceiling: **$5/month**
- ✅ Runtime: **Node/TypeScript**
- ✅ Rate limits: **3/min, 12/day per IP + ~20/day global**
- ✅ Retrieval trimmed to **top-3 notes + section snippets** + **answer caching** to fit $5
