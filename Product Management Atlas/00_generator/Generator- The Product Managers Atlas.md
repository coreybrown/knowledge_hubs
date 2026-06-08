# Generator — The Product Manager's Atlas

Build brief for the Product Management competency knowledge base (Field Guide 01).

## Identity
- **Display title:** The Product Manager's Atlas
- **Folder:** `Product Management Atlas/`
- **Slug:** `pm-atlas` (must be identical in portal HUBS, `ASK_GUIDE`, `api/ask.js` GUIDES, `test_sites.py` HUB_SLUGS)
- **Kicker:** Field Guide 01 · Product
- **Accent:** slate/indigo `#3B5BA5` / `#5C7CC4` (distinct from coffee-brown and beer-amber)

## Persona & voice
Written in the **first person, opinionated**, as **Corey Brown** — a product leader with 10+ years in B2C mobile across sports, media, and betting (ex-theScore, PENN). This is *"the competency system I've built and use to assess, level, and coach product managers,"* not a neutral encyclopedia.

- Lead with a point of view. Say what I believe and why. Take sides ("the PRD is not the deliverable — the shared understanding is").
- Use "I" / "my" / "in my experience" / "the way I run this" naturally, but earn it — back opinions with reasoning, not bravado. No résumé-dropping; reference theScore/PENN/sports-betting only when it sharpens a concrete point.
- Still a **trustworthy reference**: every framework is accurate, fairly represented, and cross-linked. Opinion sits on top of correct fundamentals, never replaces them.
- Where popular belief is myth or contested, say so.
- Blunt, no filler, no flattery. (Matches Corey's own stated communication preference.)

## Audience
A curious newcomer deciding whether PM is for them, an APM→Senior PM leveling up, and an experienced PM or product leader who wants a sharp, opinionated reference. Useful to all three.

## Objective
The most complete, opinionated, *current* map of the product-management craft — the competencies that define it at every level, how to assess and grow them, and how AI is rewriting the job. A portfolio-grade Field Guide that demonstrates product + knowledge-management capability.

## Source priority
1. **Corey's own frameworks (source #1)** — `sources/SOURCE_DIGEST.md`. The 4-pillar / 12-competency *Product Level Competency Matrix* is the **spine** (domains 03–06 are it, verbatim). The *PM Evaluation Sandbox*, the *theScore Career Journey* (score-gated leveling), the *Uniform 10/50/90* execution framework, and *theScore Product Principles* are Corey's and should be featured as his.
2. **External validation** — `sources/EXTERNAL_MODELS.md`. Used to confirm the spine and to **layer in** what the 4-pillar model under-weights: discovery (Cagan's 4 risks, Torres' continuous discovery/OST), product sense (Lenny), technical/feasibility fluency, GTM (Biddle's DHM), communication-as-skill, ethics, leadership craft above Senior PM, and "optics" (Shreyas). Attribute external models to their authors.
3. **AI layer** — `sources/AI_AND_PM.md`. Its own domain (10) **and** a short "How AI is changing this competency" section inside each of the 12 competency notes.

## Confidentiality (hard rule)
The theScore Career Journey workbook holds real employee names, scores, and personal notes. **Never** reproduce any individual's name, scores, or evaluation. Use only the reusable framework structure (skills, scales, thresholds, governance).

## The 12 competency-note template (domains 03–06)
Each of the 12 competency notes follows this shape:
1. **Definition** — Corey's verbatim definition (from SOURCE_DIGEST).
2. **The behaviors** — Corey's named behaviors + what they look like in practice (his words, expanded).
3. **How it shows up by level** — the escalation APM → … → VP (Corey's ladder + the Hunt/Reforge prose).
4. **How to grow it** — opinionated, concrete coaching.
5. **How AI is changing it** — 2–4 sentences grounded in AI_AND_PM.md.

## Note conventions (every content note)
- Filename = two-digit reading-order prefix + space + exact registry name + `.md`.
- Frontmatter: `tags: [...]`, `aliases: [...]` (first alias = exact registry name), `domain: <Domain Name>`.
- One H1 = the registry name (light punctuation flair ok).
- 350–700 words (index/glossary/matrix notes may run longer).
- Tables + Obsidian callouts (`> [!note] > [!tip] > [!warning] > [!example]`) where they help.
- 6–15 `[[wikilinks]]`, each an exact registry name; cross-domain links encouraged; `[[Name|display]]` for inline phrasing; inside tables escape the pipe as `\|`. Keep each link on one line.
- End with `## Continue Reading`: 3–5 related wikilinks with short descriptions.

## Diagrams (Phase 4)
Two signature SVGs: the **4-pillar / 12-competency model** and the **career ladder** (IC + manager tracks). Others as useful (Impact-Likelihood 2×2, the 10/50/90 flow).

## Ask the Guide
`ASK_GUIDE = "pm-atlas"`. Example starter questions: "What does a Senior PM need that a PM doesn't?" · "How is AI changing product management?" · "How do I write a PRD that actually drives delivery?"
