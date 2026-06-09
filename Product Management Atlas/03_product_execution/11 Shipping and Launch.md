---
tags: [product-execution, launch, rollout, dark-launch, phased-rollout]
aliases: [Shipping and Launch, Launch, Rollout Strategy, Shipping]
domain: Product Execution
---

# Shipping and Launch

Shipping is the moment all of [[Product Execution]] gets graded. A great [[Feature Specification|spec]], clean [[Product Delivery|delivery]], and a held [[Product Quality|quality]] bar all converge here, and a sloppy launch can squander every bit of it. My core belief about launches is simple: **a launch is a process you control, not an event that happens to you.**

## "Launch" is the wrong mental model

The word "launch" implies a single date, a big-bang moment, confetti. That framing is a trap. Big-bang launches maximize risk, because you expose 100% of users to 0% of your real-world learning, all at once. Almost everything I ship rolls out *gradually*, on a dial I can turn down. The question isn't "is it launch day?" It's "how much exposure have we earned, and how fast can we react if it goes wrong?"

## The rollout toolkit

| Technique | What it is | When I use it |
|---|---|---|
| **Feature flag** | A switch to turn functionality on/off without redeploying | Always. The cheapest [[Risk Identification and Mitigation\|contingency plan]] in software. |
| **Dark launch** | Ship the code to production *off*, or serve traffic with output hidden | To de-risk performance/scale before anyone sees it |
| **Phased / staged rollout** | Release to 1% → 10% → 50% → 100% (or by region/segment) | Default for anything non-trivial; watch metrics at each step |
| **Canary release** | Route a small slice of traffic to the new version, compare | Infra and backend changes where you watch error rates |
| **A/B test** | Randomized exposure to measure causal impact | When you need to *prove* the outcome moved ([[Experimentation and A-B Testing]]) |

> [!tip] Phased rollout is the default, not the fancy option
> A staged rollout turns a one-way door into a series of two-way doors ([[Sound Product Decision-Making]]). At 1% you can kill it with almost no blast radius. By the time you're at 100%, you've earned the confidence the hard way, by watching it work on real users. The only things I big-bang are launches that *require* simultaneity (a coordinated marketing moment, a regulatory cutover), and even then I want a flag to kill it.

## Launch readiness

Before I turn the dial, I run a readiness check. Lightweight for small work, formal for big. It's a final [[Risk Identification and Mitigation|risk]] gate, the practical face of the [[The 10-50-90 Execution Framework|90% checkpoint]].

> [!example] My launch-readiness checklist
> - **Quality bar met.** Known blockers cleared, severity-triaged ([[Product Quality]]).
> - **Instrumentation live.** The success metric is actually being measured *before* you ship, not bolted on after.
> - **Rollback path defined.** You know exactly how to turn it off and who pulls the trigger.
> - **Rollout plan set.** The percentage steps and the metrics that gate each one.
> - **Stakeholders informed.** Support, marketing, and leadership know what's coming and when ([[Stakeholder Management]]).
> - **GTM aligned.** The [[Writing PRDs and Specs|spec's]] go-to-market section is real and owned.

The instrumentation point is the one I refuse to compromise on. **If you launch without measurement live, you've decided in advance never to know if it worked,** which guarantees the next section never happens.

## Post-launch measurement: the launch isn't done at 100%

Here's the failure mode I see most: the team hits 100%, declares victory, and moves on. **Shipping is the start of the learning, not the finish line.** The point of the launch was to move an [[Outcomes Over Outputs|outcome]], and you don't know if you did until you measure it against the prediction you wrote in the spec.

- Compare the result to the **success metric you committed to** ([[Product Analytics and Metrics]]).
- Decide, with evidence: **iterate, double down, or sunset.** [[theScore Product Principles|"Don't beat a dead horse"]] applies here. A feature that didn't move the number deserves an honest look, not loyalty.
- **Share what you learned.** Talk it up: ship-and-share, breadcrumbs not loaves. A launch nobody learns from is a launch half-wasted.

## How AI is changing it

The launch *mechanics* are stable. Flags, phased rollout, and canaries predate AI and still apply. What changes is launching *AI features*, where "ready" can't mean "bug-free" because behavior is probabilistic. Launch readiness for an AI feature adds an **eval gate**, meaning it has to clear the rubric on the golden set ([[Writing Evals for AI Products]]), plus online monitoring of model behavior, not just error rates, and explicit human-in-the-loop checkpoints for high-stakes actions. The data-flywheel logic also reframes launch: usage generates the feedback data that improves the model, so the rollout *is* part of the training loop. See [[Designing for Trust and Probabilistic Systems]].

## Continue Reading
- [[Outcomes Over Outputs]] for why post-launch measurement is the only thing that makes a launch "done."
- [[Experimentation and A-B Testing]] for proving the outcome moved, not just assuming it.
- [[Risk Identification and Mitigation]] for rollback paths and phased rollout as risk controls.
- [[The 10-50-90 Execution Framework]] for launch readiness as the 90% confidence gate.
- [[Product Analytics and Metrics]] for instrumenting the success metric before you ship.
