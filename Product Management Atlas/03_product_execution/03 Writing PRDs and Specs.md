---
tags: [product-execution, prd, specs, documentation, craft]
aliases: [Writing PRDs and Specs, Writing PRDs, PRD, Product Requirements Document]
domain: Product Execution
---

# Writing PRDs and Specs

This is the craft note for [[Feature Specification]]. The competency note argues that a spec is *shared understanding*, not a document. This one is about the document — because the document is still the tool you use to create that understanding, and most PMs write bad ones.

## My one rule: match the format to the risk

There is no single correct spec format, and anyone who tells you there is hasn't shipped enough different things. A copy change does not need a PRD. A new payments flow needs more than a Slack message. The amount of spec should scale with the [[The Four Big Product Risks|risk and reversibility]] of what you're building — high-risk, irreversible, multi-team work gets a real document; a [[Sound Product Decision-Making|two-way door]] gets a paragraph. The skill the [[Senior Product Manager|senior]] level explicitly rewards is *finding the right level of detail*: not over-spec, not under-spec.

## What a great PRD contains

When the work does warrant a full doc, here's the spine I use. This maps directly onto the **Comprehensive Documentation** behavior.

| Section | What goes here | Why it matters |
|---|---|---|
| **Problem & context** | Who hurts, how much, what we know | Anchors everything in the "why" |
| **Objective & success metrics** | The outcome, the number, how you'll measure | No metric = you've decided not to learn |
| **Scope** | User stories + acceptance criteria | Defines what "done" means |
| **Out of scope** | What you're explicitly *not* doing | Prevents scope creep and protects the timeline |
| **UX & technical considerations** | Flows, comps, constraints, dependencies | Surfaces feasibility risk early |
| **Edge cases** | The unhappy paths | Where quality goes to die ([[Product Quality]]) |
| **Risks & open questions** | What could go wrong, what's undecided | Honesty here saves you later |
| **Go-to-market & rollout** | How it ships and who needs to know | See [[Shipping and Launch]] |

> [!tip] The "Out of Scope" section is the most underrated
> Saying what you *won't* build is more powerful than the feature list. It's where you make trade-offs visible, kill gold-plating, and give engineering a hard edge to estimate against. A PRD without an out-of-scope section is a PRD that will grow until the deadline slips.

## The one-pager

For most work, I default to a **one-pager**, not a full PRD: problem, objective + metric, the few user stories that matter, and the open questions. It fits on a screen, people actually read it, and it forces ruthless prioritization of what to communicate. Amazon's six-pager and the lean one-pager are cousins — both bet that *narrative prose* exposes fuzzy thinking that a bulleted template hides. I agree with that bet. If you can't write the problem in three clear sentences, you don't understand it yet.

## The anti-patterns

> [!warning] Over-spec
> The PM dictates implementation detail to engineers who know the system better than they do. It signals distrust, wastes everyone's time, and produces brittle specs that break the moment reality intervenes. **Specify the what and the why; let the team own the how.**

> [!warning] Under-spec
> The PM hand-waves the hard parts — edge cases, error states, the metric — and lets the team backfill the thinking mid-sprint. This is the more common failure and the more expensive one, because the gaps surface as rework, missed acceptance criteria, and launch-day surprises that [[Product Delivery|blow the schedule]].

> [!warning] The write-once spec
> Treating the doc as a contract you write and abandon. A spec is a living artifact through [[The 10-50-90 Execution Framework|Define → Explore → Refine]]; it should change as you learn. A spec that looks identical at ship as it did at kickoff means you ran the project with your eyes closed.

## How AI changes the craft

This is where AI hits hardest in [[Product Execution]]. First drafts that took a day now take minutes — ChatPRD is the most-used PM-specific AI tool for exactly this reason, and tools like Dovetail now generate evidence-backed PRDs that cite the research behind each claim. Use it. But treat AI as a *fast intern*, not an author: it's excellent at structure, completeness, and turning your bullet points into prose; it's useless at choosing the right problem or knowing which edge case will actually bite you in production. The "intent is the source of truth" shift in spec-driven development means your value is the quality of the intent, not the polish of the prose. See [[AI in Prototyping and Delivery]] and [[Competencies AI Commoditizes vs Elevates]].

## Continue Reading
- [[Feature Specification]] — the competency this craft serves; the three behaviors behind a good spec.
- [[Product Management Templates]] — reusable starting points for the formats above.
- [[The 10-50-90 Execution Framework]] — how the spec evolves across phases and confidence checkpoints.
- [[Shipping and Launch]] — turning the GTM section into an actual rollout.
- [[Product Analytics and Metrics]] — how to define success metrics that are worth instrumenting.
