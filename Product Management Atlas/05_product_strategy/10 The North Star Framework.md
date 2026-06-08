---
tags: [product-strategy, north-star, metrics, outcomes]
aliases: [The North Star Framework, North Star Metric, North Star Framework]
domain: Product Strategy
---

# The North Star Framework

The North Star Framework is the cleanest answer I know to a question every growing product faces: *what is the one number this whole team should orient around?* It was formalized by **John Cutler and the team at Amplitude** (building on the "North Star Metric," a term coined by **Sean Ellis**), and it's earned a permanent place in how I think about [[Business Outcome Ownership|outcome ownership]]. This note is the framework as its authors define it, plus where I push back.

> [!quote] Attribution
> The North Star Framework as described here is the work of **John Cutler and Amplitude**. The underlying "North Star Metric" term was coined by **Sean Ellis**. I'm presenting their model, not mine.

## The core idea: one value metric, plus its inputs

Most metric programs fail in one of two ways: a single top-line number (revenue, DAU) that's too lagging and too gameable to guide daily work, or a dashboard of fifty metrics that guides nothing. The North Star Framework threads the needle with a two-layer structure:

- **The North Star Metric (NSM)** — the single metric that best captures the **core value your product delivers to customers.** Crucially, it's a *leading indicator of sustainable business results* — value delivered to users that *predicts* revenue, not revenue itself. Amplitude's canonical examples: Spotify's "time spent listening," Airbnb's "nights booked."
- **Input Metrics** — typically **three to five** metrics that the team can *directly influence* and that *together drive* the North Star. They're the levers; the NSM is the dashboard.

The relationship is the whole point: if you move the inputs, the North Star should move, and if the North Star moves, the business should follow. It's a causal chain from *daily work → user value → business result.*

## A worked shape

Amplitude often frames the inputs along dimensions like breadth, depth, frequency, and efficiency. A simplified media example (my illustration, in the spirit of the framework):

| Layer | Metric | Who owns the lever |
|---|---|---|
| **North Star** | Weekly engaged readers | The whole product org |
| Input — breadth | New readers activated / week | Growth team |
| Input — depth | Articles read per session | Content + UX |
| Input — frequency | Return visits / reader / week | Retention / notifications |
| Input — efficiency | Time-to-first-article | Onboarding |

Each team can see *their* lever and how it ladders up. That's the framework's real gift: it connects an individual PM's [[Product Analytics and Metrics|metrics]] to a value metric the [[Director and VP of Product|exec team]] cares about, so [[Strategic Impact|strategy]] and daily execution share one number.

## Why I rate it

The thing the North Star does better than [[OKRs and Goal-Setting|OKRs]] is **durability.** OKRs reset quarterly; a North Star is meant to persist for years, giving the org a stable orientation while the OKRs underneath it change. It also enforces my favorite discipline — picking a metric that's *user value*, not just business extraction. A team optimizing "nights booked" is forced to make the product genuinely better; a team optimizing raw revenue can degrade the experience to hit a quarter. The North Star is [[Outcomes Over Outputs]] crystallized into a single, shared, leading number.

## Where I push back

> [!warning] The myth: one metric can capture everything
> A North Star is a *simplification,* and simplifications can be weaponized. Optimize any single metric hard enough and you'll find the perverse path — Goodhart's law always wins eventually. "Time spent" can mean addictive dark patterns; "nights booked" can mean ignoring host quality. A North Star needs **guardrail metrics** (things you refuse to harm — churn, trust, unit cost) sitting alongside it, or you'll optimize the company into a corner.

Two more cautions. First, picking the NSM is *hard and high-stakes* — choose the wrong metric and you point the whole org at the wrong hill, so it's worth real [[User Research and Discovery|discovery]] before committing. Second, the causal links between inputs and the North Star are *hypotheses,* not facts — they need validating with [[Experimentation and A-B Testing|experiments]], or you end up religiously moving an input that turns out not to drive the star at all.

## North Star vs OKRs vs the metrics you already have

They're complementary, not competing — each layer answers a different question. The North Star points the *durable direction*; the input metrics name the levers; [[OKRs and Goal-Setting|OKRs]] are the *quarterly bets* on which levers to push; and [[RICE and Scoring Models|RICE]] picks which features might move an input.

## How AI is changing it

AI doesn't change the framework, but it makes living inside it far easier. Self-serve, natural-language analytics — increasingly built into platforms like Amplitude — let a PM interrogate the input-to-North-Star relationship conversationally and spot when an input is *decoupling* from the star far sooner. What stays human is the choice of the metric and its guardrails: a model can compute correlations between candidate inputs and the star, but deciding *which* value metric represents the company's soul, and which harms are unacceptable in pursuit of it, is a strategic and ethical call the org must own.

## Continue Reading
- [[OKRs and Goal-Setting]] — the quarterly bets that push the North Star's input metrics.
- [[Outcomes Over Outputs]] — the belief the North Star operationalizes.
- [[Product Analytics and Metrics]] — the measurement foundation the framework sits on.
- [[Business Outcome Ownership]] — connecting your work to a value metric that predicts the business.
- [[Fluency with Data]] — validating that the input-to-star causal links are real.
