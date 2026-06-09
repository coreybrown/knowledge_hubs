---
tags: [product-strategy, okrs, goals, outcomes]
aliases: [OKRs and Goal-Setting, OKRs, Objectives and Key Results, Goal-Setting]
domain: Product Strategy
---

# OKRs and Goal-Setting

OKRs (Objectives and Key Results) are the most adopted and most cargo-culted goal-setting system in tech. Popularized by Andy Grove at Intel and spread through Google (and John Doerr's *Measure What Matters*), they're a genuinely good tool that most companies implement as a quarterly busywork ritual. This note is OKRs done right versus OKRs done as theater, and why the difference is entirely about [[Outcomes Over Outputs|outcomes versus output]].

## The structure

An OKR has two parts:

- **Objective**: a qualitative, inspirational statement of *what you want to achieve.* It should be memorable and a little ambitious. ("Become the default way fans check live scores.")
- **Key Results**: 2 to 4 quantitative, measurable statements of *how you'll know you got there.* These must be **outcomes**, not tasks. ("Grow daily active score-checkers from 1.2M to 2M"; "lift D7 retention from 38% to 45%.")

The Objective is the destination; the Key Results are the instruments on the dashboard that tell you you've arrived.

> [!tip] The acid test for a Key Result
> A Key Result is correct only if it's a *result* (a change in user or business behavior), not a thing you did. "Ship the new onboarding flow" is not a Key Result; it's a task masquerading as one. "Increase activation rate from 60% to 75%" is a Key Result. If your team could complete the KR by *working hard* rather than by *succeeding,* it's an output. Rewrite it.

## OKRs done right vs cargo-culted

Here's the table I keep in my head, because the gap between these two columns is where almost all OKR disappointment lives.

| Dimension | Done right | Cargo-culted |
|---|---|---|
| **Key Results** | Outcomes (behavior/metric change) | Output (features shipped, tasks done) |
| **Origin** | Team co-authors them; tied to [[Strategic Impact\|strategy]] | Handed down; disconnected from a bet |
| **Count** | One clear objective, 2 to 4 KRs | Ten objectives, no focus |
| **Ambition** | Stretch, ~70% is a "win" | Sandbagged to be 100% hittable |
| **Cadence** | Reviewed continuously, used to decide | Set in Jan, ignored till the Dec review |
| **Link to comp** | Deliberately *decoupled* | Bonus-linked → everyone sandbags |
| **The roadmap** | KRs are the goal; roadmap is *how* | Roadmap items relabeled as "KRs" |

The single most common failure is the first row: teams write their roadmap, then relabel each feature as a "Key Result." Now you have a [[Product Teams vs Feature Teams|feature factory]] wearing an OKR costume. Real Key Results state the *outcome you're betting the feature will produce*, which means you can ship the feature, miss the outcome, and have *learned something.* That gap between output and result is the entire point.

## My beliefs about goal-setting

**Outcomes, not output. Always.** This is the hill. A goal that measures activity ("ran 5 experiments," "shipped 3 features") rewards motion over progress. A goal that measures the outcome ("moved retention 7 points") rewards the only thing that matters. The whole reason [[Business Outcome Ownership]] exists as a competency is to enforce this.

**Stretch, with permission to miss.** Grove's original insight: if you hit 100% of your OKRs, you set them too low. I aim for ~70% as a genuine success. This *only* works if OKRs are decoupled from compensation. The moment a bonus rides on the number, every smart person sandbags, and you've engineered the timidity you were trying to avoid. Doerr is explicit on this and most companies ignore it.

**Fewer, sharper.** A team with one objective and three key results has focus. A team with five objectives has none. OKRs are a [[Prioritization Frameworks|prioritization]] device disguised as a goals device, and the discipline is in what you *leave out.*

> [!warning] The myth: OKRs are a performance-management tool
> Tying OKRs to performance reviews and bonuses is the most common and most destructive mistake. It converts an honest goal-setting and learning instrument into a negotiation, where people lowball targets to protect their comp. Goal-setting and [[Calibration and Promotion|performance evaluation]] are different systems for a reason; fuse them and you corrupt both.

## How AI is changing it

AI is quietly improving the *quality* of goal-setting in a way I didn't expect. Drafting OKRs, sanity-checking that Key Results are outcomes rather than disguised tasks, and pressure-testing whether a KR actually ladders to the [[Strategic Impact|strategy]] are things a model does well. Point it at a draft and ask "which of these are output dressed as outcomes" and it'll catch the relabeled-roadmap trap better than most managers. The judgment AI doesn't replace is *which* outcomes are worth committing to and how much ambition to set, because that's a strategic bet tied to conviction about the business. Same pattern as everywhere in [[Product Strategy|strategy]]: the model sharpens the artifact; the choice of what to chase stays human.

## Continue Reading
- [[Outcomes Over Outputs]] is the core belief that makes OKRs work or fail.
- [[The North Star Framework]] is an alternative and complement: one durable value metric plus its inputs.
- [[Business Outcome Ownership]] is the competency that holds you accountable to the Key Results.
- [[Prioritization Frameworks]] for OKRs as a focusing device and how they shape the roadmap.
- [[Calibration and Promotion]] for why goal-setting must stay separate from performance evaluation.
