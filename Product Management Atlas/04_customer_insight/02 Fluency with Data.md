---
tags: [customer-insight, competency, data, analytics, experimentation]
aliases: [Fluency with Data, Data Fluency, Data-Informed Product Management]
domain: Customer Insight
---

# Fluency with Data

## What it is

The verbatim definition from my competency model: **the ability to use data to generate actionable insights, to leverage those insights to achieve goals set for the product, and to connect those quantified goals to meaningful outcomes for the business.**

Read that closely, because the order matters. The competency is not "knows SQL" or "makes pretty dashboards." It's a chain: *data → insight → goal → business outcome*. A PM who can write a query but can't tell you what the result means, or who hits a metric that doesn't move the business, has failed the competency even if every number is correct. Fluency with Data is literacy, not engineering — the ability to read the language the product is speaking back to you.

## The behaviors

My model breaks this into two named behaviors.

**Feature Evaluation & A/B Testing.** Forming clear hypotheses, designing tests with valid sample sizes and minimal bias, interpreting conversion and retention results *with statistical significance*, and then making the call: roll out, iterate, or sunset. The discipline here is honesty — running the test is easy; respecting the result when it kills your favorite idea is the skill. Full mechanics in [[Experimentation and A-B Testing]].

**Actionable Insight Generation.** Asking the right questions of the data, interpreting it *in context*, separating trends from anomalies and — the one everyone gets wrong — **causation from correlation**. Then translating the finding into an opportunity and presenting it so it actually drives a decision. An insight nobody acts on isn't an insight; it's trivia. The toolkit lives in [[Product Analytics and Metrics]].

> [!warning] The myth of "data-driven"
> I don't say "data-driven." I say **data-informed**. Data-driven implies the numbers decide, and they don't — they can't tell you about the feature you haven't built, the user who already churned, or the brand you're trying to become. theScore's principle was "balance game sense *with* data," and I hold to it: data is the most reliable voice in the room, not the only one. A PM who hides behind "the data says" is dodging the judgment they're paid for ([[Product Sense and Judgment]]).

## How it shows up by level

| Level | What Fluency with Data looks like |
|---|---|
| [[Associate Product Manager\|APM]] | Pulls a funnel or retention report; reads a dashboard; runs an experiment someone else designed. |
| [[Product Manager\|PM]] | Designs valid A/B tests independently; builds the metrics for a feature; spots a real insight in the noise. |
| [[Senior Product Manager\|Sr PM]] | Decides *which* questions are worth answering; connects a metric to a [[Business Outcome Ownership\|business outcome]]; calls roll-out/sunset confidently. |
| [[Director and VP of Product\|Director/VP]] | Builds the org's analytics muscle — instrumentation standards, experimentation platform, a culture that won't ship without a hypothesis. |

## How to grow it

Concrete coaching I give:

- **Learn enough SQL to be dangerous.** You don't need to be an analyst, but waiting two days for someone to answer "how many users did X" will kneecap your judgment. Self-serve answers compound.
- **Write the hypothesis *before* the dashboard.** "I believe X because Y; I'll know I'm right if Z moves." It forces you to define success up front instead of reverse-rationalizing whatever the chart shows.
- **Audit one vanity metric a quarter.** Pick a number your team celebrates and ask: if this doubled and nothing else changed, would the business be better off? If not, you found a vanity metric ([[Product Analytics and Metrics]]).
- **Pair every quant finding with a qual "why."** The number tells you conversion dropped; an interview tells you the new screen confused people. Connect to [[Voice of the Customer]].

## How AI is changing it

Natural-language analytics now lets a PM ask the warehouse a question in plain English and get a chart back, collapsing the "learn SQL" barrier and the wait on an analyst. That commoditizes the *mechanics* of pulling and slicing data. What it doesn't touch — and arguably raises the premium on — is knowing which question is worth asking, smelling when a too-clean result is a measurement artifact, and resisting the false causation a confident model will happily hand you. More in [[Competencies AI Commoditizes vs Elevates]].

## Continue Reading
- [[Product Analytics and Metrics]] — funnels, retention, cohorts, and vanity vs actionable metrics.
- [[Experimentation and A-B Testing]] — hypotheses, significance, and the pitfalls that produce false wins.
- [[Voice of the Customer]] — the qualitative partner that explains *why* the numbers move.
- [[Storytelling with Data]] — turning an insight into a decision people actually make.
- [[Customer Insight]] — how data fluency fits the wider area.
