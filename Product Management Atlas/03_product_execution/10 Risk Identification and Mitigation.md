---
tags: [product-execution, risk, mitigation, contingency, monitoring]
aliases: [Risk Identification and Mitigation, Risk Management, Risk Mitigation, Identifying Risk]
domain: Product Execution
---

# Risk Identification and Mitigation

This is the second behavior under [[Product Quality]]. If [[Sound Product Decision-Making]] is about making good calls, this is about seeing the bad outcomes coming *before* they arrive — and having a plan when they do. It's the least glamorous part of execution and one of the most senior-defining, because spotting risk early is mostly pattern recognition you earn by getting burned.

## What it is

From my model: **early detection; classifying risks by impact × likelihood; building contingency plans; transparent communication; and ongoing monitoring.** Five verbs, and the first one — *early* — does most of the work. A risk caught at the spec stage is a sentence in a doc. The same risk caught at launch is a fire drill, a slipped date, and a credibility hit. Almost everything about good risk management is moving the detection point earlier.

This is distinct from [[The Four Big Product Risks|the four big product risks]] (value, usability, feasibility, viability), which are about *whether to build a thing at all*. This behavior is about *execution risk* — the things that threaten a project you've already committed to.

## Classify by impact × likelihood

You cannot mitigate every risk; trying to is its own failure. The triage tool is a 2×2 of **impact × likelihood**, the same logic as [[The Impact-Likelihood Matrix]].

| | Low likelihood | High likelihood |
|---|---|---|
| **High impact** | **Plan a contingency** — unlikely but catastrophic; have an answer ready | **Mitigate now** — your top priority; act before it lands |
| **Low impact** | **Accept / ignore** — don't waste energy here | **Monitor** — annoying but survivable; watch it |

> [!tip] The two quadrants people get wrong
> Two errors dominate. First, obsessing over **low-impact, high-likelihood** noise (the constant small annoyances) while a **high-impact, low-likelihood** killer sits unplanned — the rare event that sinks the launch. Second, *accepting* a high-impact/high-likelihood risk because confronting it is uncomfortable. The whole point of the matrix is to spend your limited mitigation energy where impact is highest, not where the risk is loudest.

## Contingency plans: pre-decide the bad day

A contingency plan is a [[Sound Product Decision-Making|decision]] made *before* the pressure hits, when you're calm and rational instead of panicked at 11pm on launch eve. "If the migration fails, we roll back to the read-only snapshot." "If conversion drops more than X%, we kill the experiment." Pre-deciding the trigger and the response is how you avoid making your worst calls at your worst moment. The [[Shipping and Launch|rollout plan]] should name the rollback path explicitly — and a [[Shipping and Launch|feature flag]] is the cheapest contingency plan in software.

## Transparent communication: the part that takes courage

> [!warning] Hiding a risk is the cardinal sin
> The behavior says **transparent communication**, and this is where I've seen the most careers stall. The temptation under pressure is to downplay a risk and hope. Don't. A risk you flag early, with a plan, makes you look like a pro even if it materializes. A risk you concealed that then blows up destroys trust permanently — and trust is what lets you keep [[Managing Up|escalating]] credibly. The [[Product Delivery|"minimal surprises"]] standard is really a risk-communication standard: surprises are just risks you failed to telegraph.

Communicate risk *with a recommendation*, not as a worry. "Here's the risk, here's its impact × likelihood, here's my mitigation, here's what I need from you." That's [[RACI and Decision Rights|escalation]] done right.

## Ongoing monitoring: risk is not a one-time scan

The last verb is *ongoing*. Risks aren't a kickoff checklist you file away — likelihoods shift as the project moves and as you cross [[The 10-50-90 Execution Framework|confidence checkpoints]]. A feasibility risk that was high at 10% confidence may be retired by 50%; a market risk may *appear* late. Revisit the register at each checkpoint. Post-launch, monitoring means watching the [[Product Analytics and Metrics|metrics]] and error rates for the risks you couldn't fully eliminate.

## How to grow it

- **Run a pre-mortem.** Before kickoff, ask the team: "It's launch day and this failed badly — why?" People surface risks in the imagined-past tense that they'd never volunteer in the optimistic present. It's the highest-leverage 30 minutes in any project.
- **Keep a one-line risk register in the [[Writing PRDs and Specs|spec]].** Risk, impact × likelihood, mitigation, owner. Revisit it at each checkpoint.
- **Separate the risk from the panic.** Plot it on the matrix before reacting. Most "emergencies" are low-impact noise; the real killers are often quiet.

## How AI is changing it

AI introduces a whole new risk class to identify and mitigate. Probabilistic systems carry **hallucination, trust, and reliability risks** that deterministic software never had — the discipline is tiering them by stakes (citations and confidence scores for low-stakes, hard guardrails and human verification for high-stakes) rather than promising they won't happen. The "70% problem" sharpens this: AI gets you to a working 70% fast, but the last 30% — edge cases, security, production hardening — is exactly where risk concentrates, so a PM's risk attention should move *toward* that tail. AI also helps the other direction, scanning feedback, logs, and tickets to surface emerging risks earlier. See [[Designing for Trust and Probabilistic Systems]] and [[The 70% Problem]].

## Continue Reading
- [[The Impact-Likelihood Matrix]] — the 2×2 in full, with the four named quadrants.
- [[Sound Product Decision-Making]] — the sibling behavior under Product Quality.
- [[The Four Big Product Risks]] — the discovery-stage risks: value, usability, feasibility, viability.
- [[Shipping and Launch]] — rollback paths, phased rollout, and launch-readiness as risk controls.
- [[Designing for Trust and Probabilistic Systems]] — the new risk class AI products introduce.
