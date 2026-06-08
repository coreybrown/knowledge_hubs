---
tags: [customer-insight, data, experimentation, ab-testing, statistics]
aliases: [Experimentation and A-B Testing, A/B Testing, Experimentation, Controlled Experiments]
domain: Customer Insight
---

# Experimentation and A-B Testing

An A/B test is the closest thing product management has to a controlled experiment, and that makes it the most honest tool in the kit — *if* you run it honestly. My experience is that most teams don't. They treat the experiment as a ritual that blesses a decision they already made, and they torture the data until it confesses. So this note is mostly about the pitfalls, because the mechanics are easy and the discipline is hard.

## What an experiment actually is

You split users randomly into a **control** (current experience) and one or more **variants**, change one thing, and measure whether a pre-defined metric moves by more than chance would explain. Randomization is what buys you causation: because the only systematic difference between the groups is your change, a real difference in outcomes is *caused* by it. That's why the A/B test answers the question a [[Product Analytics and Metrics|funnel or cohort]] can't — those show correlation; the experiment shows cause.

## Start with a real hypothesis

> [!tip] The shape of a good hypothesis
> **"We believe** [change] **will cause** [measurable effect] **for** [segment] **because** [reason]**. We'll know we're right if** [primary metric] **moves by** [amount]**."**
> Write it before you build anything. The "because" forces a mechanism instead of a wish, and the "we'll know" forces you to pre-commit to what success means — which is the only thing standing between you and reading whatever you wanted into the result. This is the experimental backbone of [[Hypothesis-Driven Development]].

The most important word above is **primary**. Pick *one* metric in advance. If you measure twenty and let any winner count, you've guaranteed a false positive — which is the first pitfall.

## The pitfalls (where teams lie to themselves)

**Peeking.** Checking daily and stopping the moment it looks significant. This is the cardinal sin. P-values wander randomly during a test; stop at the first green moment and you'll "find" wins that evaporate, quietly inflating your real false-positive rate far above the 5% you think you're running. **Decide the end date up front** — or use a sequential method built for continuous monitoring.

**Underpowered tests (too-small samples).** If you only have traffic to detect a 20% lift, a real 3% lift looks like noise and you'll wrongly call it "no effect." Estimate the **minimum detectable effect** and required sample size *before* you start. A test you can't power is one you shouldn't run — ship it as a judgment call instead of pretending it was rigorous.

**Multiple-comparisons fishing.** At a 5% threshold, run 20 comparisons and on average *one looks significant by pure chance*. Slicing by every segment until something pops ("it worked for left-handed users in Ohio!") manufactures exactly these phantoms. Pre-register your metric and segments.

**Statistical vs practical significance.** With enough traffic a 0.1% lift becomes "significant" and still isn't worth the engineering or the complexity. Significance says the effect is *real*; only judgment says it's *worth it* ([[Prioritization Frameworks]]).

| Pitfall | What it produces | The fix |
|---|---|---|
| Peeking | Wins that vanish in production | Fixed end date, or sequential testing |
| Too-small sample | "No effect" on real effects | Power the test up front (MDE + sample size) |
| Multiple comparisons | Phantom segment "wins" | Pre-register metric & segments |
| Stat ≠ practical significance | Shipping trivial lifts | Judge magnitude vs effort |

## When *not* to A/B test

Experiments need traffic and a clean metric. Don't reach for one when you have too few users to power it, when the change is a one-way door with high stakes (don't A/B test a rebrand), or when you're early in discovery and still don't know *what* problem you're solving — there you want interviews and prototypes ([[User Research and Discovery]], [[Continuous Discovery]]), not a controlled rollout. A/B testing optimizes a known thing; it doesn't tell you what thing to build.

## How AI is changing it

AI assistants can now propose a sensible hypothesis, do the sample-size math, and flag when a result fails a significance or peeking check — lowering the statistical barrier that used to gate good experimentation. The risk is the inverse: it's never been easier to spin up a hundred variants and let a model surface the "winners," which is multiple-comparisons fishing at industrial scale. The PM's job becomes guarding the *discipline* — one primary metric, honest stopping rules — not running the math. See [[Competencies AI Commoditizes vs Elevates]].

## Continue Reading
- [[Fluency with Data]] — the competency this is a core behavior of.
- [[Product Analytics and Metrics]] — the funnels and cohorts an experiment moves.
- [[Hypothesis-Driven Development]] — running the whole product process as a series of bets.
- [[Build-Measure-Learn and the MVP]] — experimentation as the engine of the build-measure-learn loop.
- [[Sound Product Decision-Making]] — weighing a result against effort, alignment, and risk.
