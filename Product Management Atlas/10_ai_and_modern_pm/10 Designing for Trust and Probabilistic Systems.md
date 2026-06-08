---
tags: [ai, modern-pm, trust, hallucination, guardrails, hitl]
aliases: [Designing for Trust and Probabilistic Systems, Designing for Trust, Trust in AI Products]
domain: AI and the Modern PM
---

# Designing for Trust and Probabilistic Systems

A probabilistic system will be wrong sometimes. That is not a bug you will fix — it's a property of the technology. The product question is therefore not "how do we eliminate errors?" but "how do we design a trustworthy experience *given* that errors will happen?" The PMs who get this build durable products. The ones who don't ship demos that collapse the first time a real user hits the long tail.

## Don't promise zero hallucinations

> [!warning] The promise that breaks products
> The fastest way to destroy trust in an AI product is to imply it's always right and then be confidently wrong once. **Don't promise zero hallucinations.** You can't deliver it, and the gap between the promise and reality is exactly where trust dies. Design *around* hallucination instead — make the system's uncertainty legible, recoverable, and bounded by the stakes.

A model that says "I'm not sure, here's my source, check it" earns more trust than one that's silently confident and occasionally catastrophic. Calibrated humility beats false certainty.

## Tier your guardrails by stakes

The single most useful framework here: **match the guardrail to the cost of being wrong.** Not every feature needs the same protection, and over-guarding a low-stakes feature just adds friction.

| Stakes | Example | Appropriate guardrail |
|---|---|---|
| **Low** | Draft email, brainstorm, summary | Citations, confidence cues, easy edit/undo |
| **Medium** | Customer-facing answer, code suggestion | Grounding in retrieved sources; show the source |
| **High** | Medical, legal, financial, irreversible actions | Hard guardrails; **human verification**; abstention when unsure |

The principle: as the cost of an error rises, you move from *soft* signals (the user can catch it) toward *hard* controls (the system refuses, or a human must confirm). A low-stakes feature designed like a high-stakes one is annoying; the reverse is dangerous.

## Human-in-the-loop is non-negotiable for high stakes

> [!tip] HITL as a design primitive
> For anything high-stakes or irreversible, a **human-in-the-loop** checkpoint is not optional. The pattern: the AI proposes, a human disposes. Use confidence thresholds to route — high-confidence outputs flow through, low-confidence ones get held for review. This is the heart of "agentic experience" design: intent → plan → **human oversight** → execution → monitoring. The control point is where trust lives.

Design the review step as a real, usable surface — not a buried toggle. If checking the AI's work is harder than doing the work yourself, people will either disable the safeguard or stop using the product. The HITL UI is the product.

## Designing reliability around failure

Concrete patterns I reach for, roughly in the order errors get more expensive:

- **Show your work** — citations and sources, so the user can verify cheaply.
- **Express uncertainty** — surface confidence; let the user calibrate trust per-answer.
- **Make recovery trivial** — undo, edit, regenerate. A reversible error is a small error.
- **Abstain gracefully** — "I don't have enough to answer that" is a feature, not a failure. A system that knows its limits is more trustworthy than one that always guesses.
- **Constrain the blast radius** — for agents taking actions, confirm before anything irreversible.

This is where [[Writing Evals for AI Products|evals]] and trust design meet: your evals should measure the failure rate, and your UX should make that failure rate *survivable*. Two halves of the same problem.

## My take

Trust is the entire product in AI. A model that's 95% accurate and *feels* trustworthy beats one that's 98% accurate and feels like a coin flip — because users adopt the one they can rely on, and adoption is the only metric that compounds. Designing for failure isn't pessimism; it's the realism that makes a probabilistic product usable. This is [[Product Quality]] and [[Risk Identification and Mitigation]] applied to a system that, by design, will surprise you.

## Continue Reading
- [[Building AI Products]] — the build philosophy this design layer sits on.
- [[Writing Evals for AI Products]] — measuring the failure rate you're designing around.
- [[The 70% Problem]] — why the last 30% (edge cases, trust) is the hard part.
- [[Risk Identification and Mitigation]] — the competency this extends.
- [[Product Quality]] — quality redefined for probabilistic systems.
- [[AI Ethics and Governance]] — trust at the policy and accountability level.
