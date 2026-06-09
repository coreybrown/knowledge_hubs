---
tags: [customer-insight, data, analytics, metrics, retention]
aliases: [Product Analytics and Metrics, Product Analytics, Metrics, The Metrics Tree]
domain: Customer Insight
---

# Product Analytics and Metrics

My strongest opinion about analytics is that the goal is fewer metrics, not more. Almost every dashboard I have inherited had thirty charts and answered zero questions, because a team that watches thirty numbers is really watching none of them. The skill here was never instrumentation. Engineers can instrument anything you ask for. The skill is deciding which two or three numbers actually tell you the product is working, and then having the nerve to ignore the rest.

## The four families of metrics

Most product questions come down to four kinds of measurement:

- **Acquisition** is how people arrive. It is useful, but it is the cheapest number to game and the easiest to mistake for success.
- **Activation** is whether a new user reaches the moment the product's value finally clicks, the "aha". In my B2C mobile world this is where most of the leverage lives, and in my experience most teams underinvest in it.
- **Retention** is whether people come back, and it is the one number that does not lie to you. You can buy acquisition and you can inflate activation, but retention is the market grading your product.
- **Monetization** is whether the value converts to revenue. That is the bridge to [[Business Outcome Ownership]].

> [!tip] Retention is the truth serum
> If I could keep one chart, it would be the **retention curve**, the day-1, day-7, and day-30 cohorts. A curve that decays to zero means you have a leaky bucket, and no amount of acquisition spend fixes a leaky bucket. It just pays for the water to pour out faster. A curve that *flattens* means you have found a population the product genuinely serves. Flattening before zero is the single best signal of product-market fit I know of.

## The metrics tree

I ask teams to draw a **metrics tree**: one top-line number the product is responsible for, broken down into the inputs we can actually move. The top-line is a lagging outcome, something like "monthly active bettors". The inputs are leading and controllable, something like "percent of signups who place a first bet within 24h". The discipline is that every team metric has to trace upward to the top. If you cannot draw the line from your number to the business, you are measuring something that does not matter, and I would gently push you to find a better number. This is the same logic as [[The North Star Framework]]: one value metric plus the inputs that drive it.

## Funnels and cohorts

A **funnel** is just a sequence of steps with drop-off at each one. Its value is diagnostic, because it tells you *where* users fall out, which then points your research at *why* ([[User Research and Discovery]]). A **cohort** groups users by when they started or what they did, so you compare like with like. Without cohorting, a product can look healthy while every new cohort is quietly worse than the last, because the loyal old guard masks the rot. Cohorting is how you see the present instead of the cumulative past.

## Vanity vs actionable metrics

This is the distinction that matters most, so let me be precise about it.

| | Vanity metric | Actionable metric |
|---|---|---|
| **Direction** | Only goes up (cumulative totals, "total users ever") | Can go down; reflects current reality |
| **Decision** | Changing it changes no behavior | Tells you what to do differently |
| **Test** | "If this doubled, would we act?" → no | → yes |

Total registered users, total downloads, page views: these feel good in a board deck and inform nothing. Here is the test I apply. If this number doubled overnight and nothing else changed, would the business actually be better off, and would I do anything differently? If the answer is no, it is vanity. This is not the same as a **guardrail** metric, which you watch precisely *because* you hope it does not move. That is a legitimate use of a number you do not act on.

There is a second trap that catches you even with actionable metrics: confusing correlation with causation. The dashboard shows that engaged users retain better. That does not mean *making* users engage will make them retain, because engagement may just be how already-committed users show up. Disentangling that is the job of [[Experimentation and A-B Testing]].

## How AI is changing it

The headline shift in analytics is self-serve, natural-language querying. A PM types "what's day-7 retention for users who used feature X" and gets a cohorted chart back, no SQL, no ticket to the data team. That collapses the time from question to answer and pushes basic reporting close to zero effort. So where does your value go? It moves to asking the *right* question in the first place, and to catching when a suspiciously tidy answer is really an instrumentation bug or a correlation wearing a causation costume. A machine will hand you a clean chart with no warning label. See [[AI in Discovery and Research]] and [[Fluency with Data]].

## Continue Reading
- [[Fluency with Data]] for the competency this toolkit serves.
- [[Experimentation and A-B Testing]] for how to prove causation instead of guessing at it.
- [[The North Star Framework]] for one value metric plus its input drivers, formalized.
- [[Outcomes Over Outputs]] for why we measure what changes, not what ships.
- [[Storytelling with Data]] for turning a metric into a decision.
