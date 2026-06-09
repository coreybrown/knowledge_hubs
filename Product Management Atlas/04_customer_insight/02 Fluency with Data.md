---
tags: [customer-insight, competency, data, analytics, experimentation]
aliases: [Fluency with Data, Data Fluency, Data-Informed Product Management]
domain: Customer Insight
---

# Fluency with Data

## What it is

The verbatim definition from my competency model: **the ability to use data to generate actionable insights, to leverage those insights to achieve goals set for the product, and to connect those quantified goals to meaningful outcomes for the business.**

Read that closely, because the order matters. The competency is not "knows SQL" or "makes pretty dashboards." It is a chain that runs from data to insight to goal to business outcome. A PM who can write a query but cannot tell you what the result means, or who hits a metric that does not move the business, has failed the competency even if every number is correct. Think of Fluency with Data as literacy rather than engineering: the ability to read the language the product is speaking back to you.

## The behaviors

My model breaks this into two named behaviors.

**Feature Evaluation & A/B Testing.** Forming clear hypotheses, designing tests with valid sample sizes and minimal bias, interpreting conversion and retention results *with statistical significance*, and then making the call to roll out, iterate, or sunset. The discipline here is honesty. Running the test is easy. Respecting the result when it kills your favorite idea is the skill. Full mechanics in [[Experimentation and A-B Testing]].

**Actionable Insight Generation.** Asking the right questions of the data, interpreting it *in context*, separating trends from anomalies, and (the one I coach hardest) separating **causation from correlation**. Then translating the finding into an opportunity and presenting it so it actually drives a decision. An insight nobody acts on is not an insight. It is trivia. The toolkit lives in [[Product Analytics and Metrics]].

> [!warning] The myth of "data-driven"
> I do not say "data-driven." I say **data-informed**. Data-driven implies the numbers decide, and they cannot. They cannot tell you about the feature you have not built, the user who already churned, or the brand you are trying to become. theScore's principle was "balance game sense *with* data," and I hold to it: data is the most reliable voice in the room, not the only one. A PM who hides behind "the data says" is dodging the judgment they are paid for ([[Product Sense and Judgment]]).

## How it shows up by level

| Level | What Fluency with Data looks like |
|---|---|
| [[Associate Product Manager\|APM]] | Pulls a funnel or retention report; reads a dashboard; runs an experiment someone else designed. |
| [[Product Manager\|PM]] | Designs valid A/B tests independently; builds the metrics for a feature; spots a real insight in the noise. |
| [[Senior Product Manager\|Sr PM]] | Decides *which* questions are worth answering; connects a metric to a [[Business Outcome Ownership\|business outcome]]; calls roll-out/sunset confidently. |
| [[Director and VP of Product\|Director/VP]] | Builds the org's analytics muscle: instrumentation standards, experimentation platform, a culture that won't ship without a hypothesis. |

## How to grow it

Concrete coaching I give:

- **Learn enough SQL to be dangerous.** You do not need to be an analyst, but waiting two days for someone to answer "how many users did X" will kneecap your judgment. Self-serve answers compound.
- **Write the hypothesis *before* the dashboard.** Something like "I believe X because Y, and I will know I am right if Z moves." It forces you to define success up front instead of reverse-rationalizing whatever the chart shows.
- **Audit one vanity metric a quarter.** Pick a number your team celebrates and ask yourself: if this doubled and nothing else changed, would the business be better off? If not, you found a vanity metric ([[Product Analytics and Metrics]]).
- **Pair every quant finding with a qual "why."** The number tells you conversion dropped. An interview tells you the new screen confused people. Connect to [[Voice of the Customer]].

## How AI is changing it

Natural-language analytics now lets a PM ask the warehouse a question in plain English and get a chart back, which collapses both the "learn SQL" barrier and the wait on an analyst. The mechanics of pulling and slicing data are quickly becoming free. What that does not touch, and arguably makes more valuable, is knowing which question is worth asking, smelling when a too-clean result is a measurement artifact, and resisting the false causation a confident model will happily hand you. The tool got faster at answering. It did not get better at deciding what to ask. More in [[Competencies AI Commoditizes vs Elevates]].

## Continue Reading
- [[Product Analytics and Metrics]] for funnels, retention, cohorts, and vanity vs actionable metrics.
- [[Experimentation and A-B Testing]] for hypotheses, significance, and the pitfalls that produce false wins.
- [[Voice of the Customer]] for the qualitative partner that explains *why* the numbers move.
- [[Storytelling with Data]] for turning an insight into a decision people actually make.
- [[Customer Insight]] for how data fluency fits the wider area.
