---
tags: [ai, modern-pm, trust, hallucination, guardrails, hitl]
aliases: [Designing for Trust and Probabilistic Systems, Designing for Trust, Trust in AI Products]
domain: AI and the Modern PM
---

# Designing for Trust and Probabilistic Systems

A probabilistic system will be wrong sometimes. That isn't a bug you'll eventually fix. It's a property of the technology. So the product question isn't "how do we eliminate errors?" It's "how do we design a trustworthy experience *given* that errors will happen?" The PMs who internalize that build durable products. The ones who don't ship demos that fall apart the first time a real user hits the long tail.

## Don't promise zero hallucinations

> [!warning] The promise that breaks products
> The fastest way to destroy trust in an AI product is to imply it's always right and then be confidently wrong, even once. **Don't promise zero hallucinations.** You can't deliver it, and the gap between that promise and reality is precisely where trust dies. Design *around* hallucination instead. Make the system's uncertainty legible, make it recoverable, and bound it by the stakes.

A model that says "I'm not sure, here's my source, go check it" earns more trust than one that's silently confident and occasionally catastrophic. Calibrated humility beats false certainty, every time.

## Tier your guardrails by stakes

The single most useful framework here is to **match the guardrail to the cost of being wrong.** Not every feature needs the same protection, and over-guarding a low-stakes feature just piles on friction.

| Stakes | Example | Appropriate guardrail |
|---|---|---|
| **Low** | Draft email, brainstorm, summary | Citations, confidence cues, easy edit/undo |
| **Medium** | Customer-facing answer, code suggestion | Grounding in retrieved sources; show the source |
| **High** | Medical, legal, financial, irreversible actions | Hard guardrails; **human verification**; abstention when unsure |

The principle is simple. As the cost of an error rises, you move from *soft* signals the user can catch toward *hard* controls where the system refuses or a human has to confirm. A low-stakes feature designed like a high-stakes one is merely annoying. The reverse is dangerous.

## Human-in-the-loop is non-negotiable for high stakes

> [!tip] HITL as a design primitive
> For anything high-stakes or irreversible, a **human-in-the-loop** checkpoint is not optional. The pattern is that the AI proposes and a human disposes. Use confidence thresholds to route the work: high-confidence outputs flow straight through, low-confidence ones get held back for review. This is the heart of agentic experience design, where intent leads to a plan, the plan passes through **human oversight**, and only then does execution and monitoring follow. The control point is where trust lives.

Design the review step as a real, usable surface rather than a buried toggle. If checking the AI's work is harder than just doing the work yourself, people will either switch off the safeguard or walk away from the product. The HITL UI is the product.

## Designing reliability around failure

The patterns I reach for, roughly in the order errors get more expensive:

- **Show your work.** Citations and sources, so the user can verify cheaply.
- **Express uncertainty.** Surface confidence and let the user calibrate trust answer by answer.
- **Make recovery trivial.** Undo, edit, regenerate. A reversible error is a small error.
- **Abstain gracefully.** "I don't have enough to answer that" is a feature, not a failure. A system that knows its limits is more trustworthy than one that always guesses.
- **Constrain the blast radius.** For agents taking actions, confirm before anything irreversible.

This is where [[Writing Evals for AI Products|evals]] and trust design meet. Your evals measure the failure rate, and your UX makes that failure rate *survivable*. They're two halves of the same problem.

## My take

Trust is the entire product in AI. A model that's 95% accurate and *feels* trustworthy beats one that's 98% accurate and feels like a coin flip, because users adopt the one they can rely on, and adoption is the only metric that compounds. Designing for failure isn't pessimism. It's the realism that makes a probabilistic product usable at all. Think of it as [[Product Quality]] and [[Risk Identification and Mitigation]] applied to a system that, by design, will surprise you.

## Continue Reading
- [[Building AI Products]] for the build philosophy this design layer sits on.
- [[Writing Evals for AI Products]] for measuring the failure rate you're designing around.
- [[The 70% Problem]] for why the last 30% (edge cases, trust) is the hard part.
- [[Risk Identification and Mitigation]] for the competency this extends.
- [[Product Quality]] for quality redefined for probabilistic systems.
- [[AI Ethics and Governance]] for trust at the policy and accountability level.
