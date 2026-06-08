---
tags: [customer-insight, data, analytics, metrics, retention]
aliases: [Product Analytics and Metrics, Product Analytics, Metrics, The Metrics Tree]
domain: Customer Insight
---

# Product Analytics and Metrics

My strongest opinion about analytics: **the goal is fewer metrics, not more.** Every dashboard I've inherited had thirty charts and answered zero questions. A team that watches thirty numbers is watching none of them. The skill is not instrumentation — engineers can instrument anything — it's deciding which two or three numbers actually mean the product is working, and having the nerve to ignore the rest.

## The four families of metrics

Most product questions reduce to four kinds of measurement:

- **Acquisition** — how people arrive. Useful, but the cheapest to game and the easiest to mistake for success.
- **Activation** — whether a new user reaches the moment the product's value clicks (the "aha"). In my B2C mobile world this is where most of the leverage lives, and most teams underinvest in it.
- **Retention** — whether people come back. This is the one that doesn't lie. You can buy acquisition and inflate activation, but retention is the market grading your product.
- **Monetization** — whether the value converts to revenue, the bridge to [[Business Outcome Ownership]].

> [!tip] Retention is the truth serum
> If I could keep one chart, it's the **retention curve** — day-1 / day-7 / day-30 cohorts. A curve that decays to zero means you have a leaky bucket, and no amount of acquisition spend fixes a leaky bucket; it just pays for water to pour out faster. A curve that *flattens* means you've found a population the product genuinely serves. Flattening before zero is the single best signal of product-market fit I know.

## The metrics tree

I make teams draw a **metrics tree**: one top-line number that the product is responsible for, decomposed into the inputs we can actually move. Top-line is a *lagging* outcome ("monthly active bettors"); the inputs are *leading* and controllable ("% of signups who place a first bet within 24h"). The discipline is that every team metric must trace upward to the top — if you can't draw the line from your number to the business, you're measuring something that doesn't matter. This is the same logic as [[The North Star Framework]]: one value metric plus the inputs that drive it.

## Funnels and cohorts

A **funnel** is just a sequence of steps with drop-off at each. Its value is diagnostic: it tells you *where* users fall out, which points your research at *why* ([[User Research and Discovery]]). A **cohort** groups users by when they started or what they did, so you compare like with like — without cohorting, a product can look healthy while every new cohort is worse than the last, because the loyal old guard masks the rot. Cohorting is how you see the present instead of the cumulative past.

## Vanity vs actionable metrics

This is the distinction that matters most, so I'll be precise about it.

| | Vanity metric | Actionable metric |
|---|---|---|
| **Direction** | Only goes up (cumulative totals, "total users ever") | Can go down; reflects current reality |
| **Decision** | Changing it changes no behavior | Tells you what to do differently |
| **Test** | "If this doubled, would we act?" → no | → yes |

Total registered users, total downloads, page views — these feel good in a board deck and inform nothing. The test I apply: *if this number doubled overnight and nothing else changed, would the business actually be better off, and would I do anything differently?* If the answer is no, it's vanity. Note this is not the same as a **guardrail** metric, which you watch precisely *because* you hope it doesn't move — that's a legitimate, non-vanity use of a number you don't act on.

A second trap, even with actionable metrics: confusing **correlation with causation**. The dashboard shows engaged users retain better; that does not mean *making* users engage will make them retain — engagement may just be how already-committed users show up. Disentangling that is the job of [[Experimentation and A-B Testing]].

## How AI is changing it

Self-serve, natural-language analytics is the headline shift: a PM asks "what's day-7 retention for users who used feature X" and gets a cohorted chart back, no SQL, no ticket to the data team. That collapses the time from question to answer and pushes basic reporting toward zero effort. The premium moves to asking the *right* question and catching when a too-tidy answer is really an instrumentation bug or a correlation masquerading as cause — see [[AI in Discovery and Research]] and [[Fluency with Data]].

## Continue Reading
- [[Fluency with Data]] — the competency this toolkit serves.
- [[Experimentation and A-B Testing]] — how to prove causation instead of guessing at it.
- [[The North Star Framework]] — one value metric plus its input drivers, formalized.
- [[Outcomes Over Outputs]] — why we measure what changes, not what ships.
- [[Storytelling with Data]] — turning a metric into a decision.
