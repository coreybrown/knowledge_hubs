---
tags: [ai, modern-pm, economics, inference, pricing, margins]
aliases: [The Unit Economics of AI, AI Unit Economics, Unit Economics of AI]
domain: AI and the Modern PM
---

# The Unit Economics of AI

This is the part of AI product management that SaaS instincts get most wrong, and it's the term in "[[The AI Product Manager|need × model behavior × economics]]" that most PMs are weakest on. If you build AI features without understanding inference economics, you will ship something users love and the business can't afford. I've watched it happen. The unit economics are *different*, and you have to internalize how.

## Inference cost is not SaaS margin

In classic SaaS, the marginal cost of one more user is ~zero — you've built the software, serving another customer is rounding-error cheap. That's why SaaS runs **80–90% gross margins**. AI breaks this. **Every single inference costs real money** — the model has to run, burning compute, every time a user does the thing. That marginal cost doesn't vanish at scale.

> [!warning] The margin reset
> AI products commonly run **~50–60% gross margins** versus SaaS's 80–90%. If you price and plan an AI product on SaaS-margin assumptions, your unit economics are upside down and you won't see it until usage scales. Orchestration — multi-step agents, retrieval, chained calls — can add another **30–60%** to per-request cost on top of the base model call. The "agent" that delights users in the demo may be three to five model calls per interaction in production. (Treat the margin and cost figures here as directional industry rules of thumb — they vary widely by product and shift fast as model prices fall.)

## The levers a PM controls

The good news: a lot of cost is a *product* decision, not just an infra one. These are PM levers, and owning them is part of the job now:

| Lever | What it does | The trade-off |
|---|---|---|
| **Prompt / response length** | Fewer tokens in and out = lower cost | Terser context or output vs quality |
| **Model selection** | Smaller/cheaper model for easy tasks | Cost vs capability (route by difficulty) |
| **Concurrency / batching** | Smooth load, batch where latency allows | Throughput vs responsiveness |
| **Caching** | Reuse results for repeated inputs | Freshness vs cost |
| **Retrieval scope** | Send only relevant context | Precision vs completeness |

The highest-leverage move is usually **routing**: use a cheap, fast model for the 80% of requests that are easy, and reserve the expensive model for the hard 20%. That's a product decision about quality thresholds — exactly the kind of call an AI PM owns, and exactly what [[Writing Evals for AI Products|evals]] let you make safely.

## The counterintuitive trend

> [!tip] Per-token falling, total spend rising
> Cost per token is collapsing — roughly **10× cheaper per year**. So AI gets cheaper, right? No. **Total spend is going *up*,** because reasoning models burn far more tokens per task and we keep handing AI bigger jobs. Cheaper unit, more units, larger total. Don't assume falling token prices bail out your margins — they're being outrun by consumption. Plan for the bill you'll have at scale, not the one the calculator shows today.

## Pricing implications

Per-seat SaaS pricing is structurally mismatched with usage-driven cost. If cost scales with tokens and price scales with seats, your heaviest users destroy your margins. The market is moving toward **base + usage** (a platform fee plus consumption), or credits, or outcome-based pricing. The PM has to connect the pricing model to the cost driver — this is [[Business Acumen and Models]] and viability ([[The Four Big Product Risks]]) made unavoidably concrete. A flat-rate AI product with unbounded usage is a business design error, not a feature.

## My take

You don't need to run the finance model, but you must be able to reason about it: *what does this feature cost per use, what drives that cost, and does the price cover it as usage grows?* An AI PM who can't answer that is missing a third of [[The AI Product Manager|AI product sense]]. The economics aren't a constraint to hand off to finance — they're a design dimension you build around from day one.

## Continue Reading
- [[The AI Product Manager]] — economics as a core part of AI product sense.
- [[Building AI Products]] — designing within cost constraints.
- [[Business Acumen and Models]] — the business-model competency this extends.
- [[The Four Big Product Risks]] — viability risk, made concrete.
- [[Writing Evals for AI Products]] — how evals let you route cheaply without losing quality.
- [[The 70% Problem]] — quality-vs-cost trade-offs in the last mile.
