---
tags: [ai, modern-pm, ethics, governance, responsible-ai]
aliases: [AI Ethics and Governance, AI Ethics, AI Governance]
domain: AI and the Modern PM
---

# AI Ethics and Governance

Ethics is the part of AI product work that's easiest to file under "someone else's job" — legal's, the trust-and-safety team's, the policy org's. That's a mistake. The PM decides what gets built, what data it uses, and what metric defines success. Those *are* the ethical decisions. There's no separate "ethics step"; ethics is baked into the choices you're already making. The modern PM is, as Product School puts it, a **guardian of ethics, trust, and responsibility** — whether or not the title says so.

## The accountability gap is real

> [!warning] The incentive problem
> One stat I find clarifying: only about **19% of PMs report clear incentives around responsible generative AI.** Treat it as directional, but the direction is the point — the vast majority of PMs are shipping AI with no structural reason to prioritize doing it responsibly. That gap is exactly where harm ships. If the org won't create the incentive, the individual PM has to supply the discipline. Don't wait for a mandate.

## Bake ethics into the artifacts you already write

The practical move is not a separate ethics review bolted on at the end. It's threading these considerations through the [[Feature Specification|specs]], metrics, and roadmaps you produce anyway:

- **In the PRD** — a section on potential harms, failure modes, and affected populations. As routine as the success-metrics section ([[Feature Specification]]).
- **In the metrics** — what does a misaligned incentive optimize *toward*? An engagement metric can quietly optimize for outrage or addiction. The metric encodes the ethics. ([[Product Analytics and Metrics]])
- **In the roadmap** — sequencing safeguards alongside capabilities, not "later." Later means never.

The three pillars I keep front of mind:

| Pillar | The question | Where it bites |
|---|---|---|
| **Bias** | Does the model treat groups inequitably? | Training data, evals, who's in the [[Writing Evals for AI Products\|golden set]] |
| **Privacy** | What user data feeds the model, and where does it go? | Data flywheels, retention, third-party model calls |
| **Accountability** | When it's wrong, who's responsible and how is it caught? | [[Designing for Trust and Probabilistic Systems\|HITL]], audit, recourse |

## The regulatory layer

This is no longer voluntary in much of the world. PMs building AI need a working awareness — not legal expertise, but enough to know when to pull in the people who have it:

- **EU AI Act** (phasing in through 2025–2026) — a **risk-tiered** regime: unacceptable-risk uses banned, high-risk uses (hiring, credit, biometrics, and more) carry hard obligations. If your product touches the EU, this shapes what you can ship and how.
- **Responsible-AI frameworks** — Google's RAI principles, Microsoft's RAI Standard, the OECD AI Principles. These give you a vocabulary and a checklist; use them as scaffolding for your own process rather than reinventing one.

The regulatory tiering mirrors the product instinct from [[Designing for Trust and Probabilistic Systems|trust design]]: **match scrutiny to stakes.** Higher-risk use, higher bar. Good ethics and good regulation point the same direction.

## My take

The cynical read is that ethics is a compliance tax. I don't buy it. In a market where [[Designing for Trust and Probabilistic Systems|trust is the entire product]], doing this well is a *competitive advantage*, not a cost. The products that earn durable trust are the ones that took bias, privacy, and accountability seriously *before* the incident forced them to. The PM who treats ethics as core product work — not a checkbox — builds the thing people keep using. That's not virtue signaling; it's [[Product Sense and Judgment]] extended to consequences.

## Continue Reading
- [[Designing for Trust and Probabilistic Systems]] — the product-level expression of these principles.
- [[Feature Specification]] — where ethical considerations get written down.
- [[Product Analytics and Metrics]] — how the metric encodes the incentive.
- [[Writing Evals for AI Products]] — evals as a bias-detection and accountability tool.
- [[Product Sense and Judgment]] — ethics as judgment about consequences.
- [[AI and the Modern PM]] — back to the domain hub.
