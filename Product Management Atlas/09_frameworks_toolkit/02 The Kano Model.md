---
tags: [frameworks, kano, prioritization, customer-insight, satisfaction]
aliases: [The Kano Model, Kano, Kano Analysis, Kano Model]
domain: The Frameworks Toolkit
---

# The Kano Model

Most prioritization frameworks ask *which* feature to build. Kano asks a better question: **what kind of value does this feature create, and how does that value decay over time?** That second clause is the part people forget, and it is the whole point. I reach for Kano when a team is arguing about table stakes versus differentiators and talking past each other, usually because they are scoring features on a single axis that does not actually exist.

Noriaki Kano developed the model in 1984 to break a lazy assumption: that satisfaction is linear, that more feature equals more happy. It is not. Kano plots two axes: how *present* a feature is (horizontal) against how *satisfied* the customer is (vertical). Different feature types trace different curves through that space, and once you see the curves you cannot un-see them.

## The categories

> [!note] The three that matter
> **Basic (must-be):** Expected. Their presence earns nothing; their absence is a dealbreaker. A login that works, a checkout that does not lose your cart. You cannot win on these, you can only lose, so invest exactly enough to not lose.
> **Performance (one-dimensional):** Linear. More is better, less is worse, and customers can articulate the trade. Page speed, storage, price. This is where you compete head-to-head and where most roadmap debate lives.
> **Delight (attractive):** Unexpected. Absence costs nothing because nobody asked; presence creates disproportionate love. These are the features that get screenshotted. You will not get them from a survey asking "what do you want," because customers do not know to want them yet.

Two more round it out. **Indifferent** features nobody cares about (kill these), and **Reverse** features that some users actively dislike, which is exactly why one-size-fits-all settings are dangerous.

| Category | Present | Absent | Strategy |
|---|---|---|---|
| Basic | Neutral | Angry | Meet the bar, no more |
| Performance | Happy | Unhappy | Compete; pick your level |
| Delight | Delighted | Neutral | Where differentiation lives |
| Indifferent | Neutral | Neutral | Don't build it |

## The insight people miss: features decay

> [!warning] Today's delight is tomorrow's basic
> Categories are **not fixed**. A front-facing camera was a delighter; now it is a basic, and its absence would be unthinkable. This is the most actionable thing in Kano: a differentiator has a half-life. If your strategy depends on a delighter, assume competitors copy it and the market re-baselines it into a basic. The [[The DHM Model|hard-to-copy]] question is exactly how long you get to enjoy the delight before it commoditizes.

## When it's useful, when it's theater

I use Kano as a **conversation lens**, not a scoring engine. The formal version is a survey with paired functional and dysfunctional questions, then a categorization table. It is rigorous and occasionally worth it for a major investment decision. But most teams do not need the survey. They need the *vocabulary*: "that is a basic, stop gold-plating it," and "that is our one delighter, protect the resourcing." The theater version is running the full survey to justify a decision you had already made, or treating the categories as permanent. Pair Kano with [[The Impact-Likelihood Matrix]] for the *how risky* axis it does not cover, and with [[RICE and Scoring Models|RICE]] when you need to rank within a category.

One trap to watch for: chasing delighters while basics are broken. Delight on top of a broken basic is lipstick. Fix the login first.

## Continue Reading
- [[Prioritization Frameworks]] for where Kano sits among the methods and when to pick it.
- [[The DHM Model]] for Biddle's hard-to-copy lens, the defense against your delighters decaying.
- [[Jobs To Be Done]] for the demand-side view, which pairs with Kano's supply-side feature view.
- [[The North Star Framework]] because performance features are usually what move your value metric.
- [[The Frameworks Toolkit]] for the full index of tools and when each earns its place.
