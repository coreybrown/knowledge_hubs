---
tags: [ai, modern-pm, ethics, governance, responsible-ai]
aliases: [AI Ethics and Governance, AI Ethics, AI Governance]
domain: AI and the Modern PM
---

# AI Ethics and Governance

Ethics is the part of AI product work that's easiest to file under "someone else's job," whether that's legal, the trust-and-safety team, or the policy org. That's a mistake. The PM decides what gets built, what data it uses, and what metric defines success, and those *are* the ethical decisions. There's no separate ethics step bolted on the side. Ethics is baked into the choices you're already making. The modern PM is, as Product School puts it, a **guardian of ethics, trust, and responsibility**, whether or not the title ever says so.

## The accountability gap is real

> [!warning] The incentive problem
> One stat I find clarifying: only about **19% of PMs report clear incentives around responsible generative AI.** Treat the figure as directional, but the direction is the whole point. The vast majority of PMs are shipping AI with no structural reason to prioritize doing it responsibly, and that gap is exactly where harm ships. If the org won't create the incentive, the individual PM has to supply the discipline. Don't wait for a mandate to land.

## Bake ethics into the artifacts you already write

The practical move isn't a separate ethics review tacked on at the end. It's threading these considerations through the [[Feature Specification|specs]], metrics, and roadmaps you produce anyway.

- **In the PRD.** A section on potential harms, failure modes, and affected populations, as routine as the success-metrics section ([[Feature Specification]]).
- **In the metrics.** What does a misaligned incentive optimize *toward*? An engagement metric can quietly optimize for outrage or addiction. The metric encodes the ethics ([[Product Analytics and Metrics]]).
- **In the roadmap.** Sequence the safeguards alongside the capabilities, not "later," because later usually means never.

The three pillars I keep front of mind:

| Pillar | The question | Where it bites |
|---|---|---|
| **Bias** | Does the model treat groups inequitably? | Training data, evals, who's in the [[Writing Evals for AI Products\|golden set]] |
| **Privacy** | What user data feeds the model, and where does it go? | Data flywheels, retention, third-party model calls |
| **Accountability** | When it's wrong, who's responsible and how is it caught? | [[Designing for Trust and Probabilistic Systems\|HITL]], audit, recourse |

## The regulatory layer

This is no longer voluntary in much of the world. A PM building AI needs a working awareness here. Not legal expertise, but enough to know when to pull in the people who have it.

- **EU AI Act** (phasing in through 2025 and 2026). A **risk-tiered** regime: unacceptable-risk uses are banned outright, and high-risk uses such as hiring, credit, and biometrics carry hard obligations. If your product touches the EU, this shapes what you can ship and how.
- **Responsible-AI frameworks.** Google's RAI principles, Microsoft's RAI Standard, and the OECD AI Principles. These hand you a vocabulary and a checklist. Use them as scaffolding for your own process rather than reinventing one from scratch.

The regulatory tiering mirrors the product instinct from [[Designing for Trust and Probabilistic Systems|trust design]]: **match scrutiny to stakes.** Higher-risk use, higher bar. Good ethics and good regulation happen to point the same direction.

## My take

The cynical read is that ethics is a compliance tax. I don't buy it. In a market where [[Designing for Trust and Probabilistic Systems|trust is the entire product]], doing this well is a competitive advantage, not a cost. The products that earn durable trust are the ones that took bias, privacy, and accountability seriously *before* an incident forced the issue. The PM who treats ethics as core product work, rather than a checkbox, builds the thing people keep coming back to. That isn't virtue signaling. It's [[Product Sense and Judgment]] extended to consequences.

## Continue Reading
- [[Designing for Trust and Probabilistic Systems]] for the product-level expression of these principles.
- [[Feature Specification]] for where ethical considerations get written down.
- [[Product Analytics and Metrics]] for how the metric encodes the incentive.
- [[Writing Evals for AI Products]] for evals as a bias-detection and accountability tool.
- [[Product Sense and Judgment]] for ethics as judgment about consequences.
- [[AI and the Modern PM]] for the way back to the domain hub.
