---
tags: [customer-insight, data, experimentation, ab-testing, statistics]
aliases: [Experimentation and A-B Testing, A/B Testing, Experimentation, Controlled Experiments]
domain: Customer Insight
---

# Experimentation and A-B Testing

An A/B test is the closest thing product management has to a controlled experiment, and that makes it the most honest tool in the kit, but only if you run it honestly. In my experience most teams do not. They treat the experiment as a ritual that blesses a decision they already made, and they torture the data until it confesses. So this note leans heavily on the pitfalls, because the mechanics are easy and the discipline is the hard part.

## What an experiment actually is

You split users randomly into a **control**, the current experience, and one or more **variants**. You change one thing and measure whether a pre-defined metric moves by more than chance would explain. Randomization is what buys you causation: because the only systematic difference between the groups is your change, a real difference in outcomes was *caused* by it. That is why the A/B test answers the question a [[Product Analytics and Metrics|funnel or cohort]] cannot. Those show correlation. The experiment shows cause.

## Start with a real hypothesis

> [!tip] The shape of a good hypothesis
> **"We believe** [change] **will cause** [measurable effect] **for** [segment] **because** [reason]**. We'll know we're right if** [primary metric] **moves by** [amount]**."**
> Write it before you build anything. The "because" forces a mechanism instead of a wish, and the "we'll know" forces you to pre-commit to what success means. That pre-commitment is the only thing standing between you and reading whatever you wanted into the result. This is the experimental backbone of [[Hypothesis-Driven Development]].

The most important word above is **primary**. Pick *one* metric in advance. If you measure twenty and let any winner count, you have guaranteed yourself a false positive, which happens to be the first pitfall.

## The pitfalls, or where teams lie to themselves

**Peeking.** Checking daily and stopping the moment it looks significant. This is the cardinal sin, so let me be blunt about it. P-values wander randomly during a test, so if you stop at the first green moment you will "find" wins that evaporate in production, quietly inflating your real false-positive rate far above the 5 percent you think you are running. Decide the end date up front, or use a sequential method built for continuous monitoring.

**Underpowered tests, meaning samples that are too small.** If you only have the traffic to detect a 20 percent lift, a real 3 percent lift looks like noise and you will wrongly call it "no effect". Estimate the **minimum detectable effect** and the required sample size *before* you start. A test you cannot power is a test you should not run. Ship the change as a judgment call instead of dressing it up as rigor.

**Multiple-comparisons fishing.** At a 5 percent threshold, run 20 comparisons and on average one looks significant by pure chance. Slicing by every segment until something pops ("it worked for left-handed users in Ohio!") manufactures exactly these phantoms. Pre-register your metric and your segments.

**Statistical versus practical significance.** With enough traffic a 0.1 percent lift becomes "significant" and still is not worth the engineering or the added complexity. Significance tells you the effect is *real*. Only your judgment tells you it is *worth it* ([[Prioritization Frameworks]]).

| Pitfall | What it produces | The fix |
|---|---|---|
| Peeking | Wins that vanish in production | Fixed end date, or sequential testing |
| Too-small sample | "No effect" on real effects | Power the test up front (MDE + sample size) |
| Multiple comparisons | Phantom segment "wins" | Pre-register metric & segments |
| Stat ≠ practical significance | Shipping trivial lifts | Judge magnitude vs effort |

## When *not* to A/B test

Experiments need traffic and a clean metric. Do not reach for one when you have too few users to power it, when the change is a high-stakes one-way door (please do not A/B test a rebrand), or when you are early in discovery and still do not know *what* problem you are solving. In that last case you want interviews and prototypes ([[User Research and Discovery]], [[Continuous Discovery]]), not a controlled rollout. A/B testing optimizes a known thing. It does not tell you what thing to build.

## How AI is changing it

AI assistants can now propose a sensible hypothesis, do the sample-size math, and flag when a result fails a significance or peeking check. That lowers the statistical barrier that used to gate good experimentation, which is genuinely helpful for teams who found the math intimidating. The risk runs the other way. It has never been easier to spin up a hundred variants and let a model surface the "winners", and that is multiple-comparisons fishing at industrial scale. So your job shifts toward guarding the discipline, one primary metric and honest stopping rules, rather than running the calculations yourself. See [[Competencies AI Commoditizes vs Elevates]].

## Continue Reading
- [[Fluency with Data]] for the competency this is a core behavior of.
- [[Product Analytics and Metrics]] for the funnels and cohorts an experiment moves.
- [[Hypothesis-Driven Development]] for running the whole product process as a series of bets.
- [[Build-Measure-Learn and the MVP]] for experimentation as the engine of the build-measure-learn loop.
- [[Sound Product Decision-Making]] for weighing a result against effort, alignment, and risk.
