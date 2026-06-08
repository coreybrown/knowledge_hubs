---
tags: [product-strategy, prioritization, rice, scoring]
aliases: [RICE and Scoring Models, RICE, RICE Scoring]
domain: Product Strategy
---

# RICE and Scoring Models

RICE is the most widely used prioritization scoring model in product — it's simple, it forces four useful questions, and it produces a comparable number. It's also the framework I most often see misused, because the number *looks* objective while being built entirely on estimates. This note is RICE done honestly: the mechanics, and the failure modes that bite teams who trust the output too much.

## The formula

RICE was popularized by Intercom. It scores each initiative on four factors and combines them:

$$\text{RICE} = \frac{\text{Reach} \times \text{Impact} \times \text{Confidence}}{\text{Effort}}$$

| Factor | What it measures | Typical unit |
|---|---|---|
| **Reach** | How many people/events this affects in a period | # of users per quarter |
| **Impact** | How much it moves the goal *per person* | Scale: 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal |
| **Confidence** | How sure you are of your estimates | % — 100% high, 80% medium, 50% low |
| **Effort** | Total work to deliver | Person-months |

The three numerator factors are *value-ish*; effort is the denominator because you want value per unit of work. The output is a relative score with no inherent meaning — it's only useful for *ranking against other items scored the same way.* A RICE of 32 means nothing alone; it means something next to a 12 and a 90.

## Why it's good

I keep RICE in the toolkit because it does three things well. It **forces the Reach question** — PMs systematically overrate features that delight a tiny segment. The **Confidence multiplier is a humility tax** that discounts the seductive high-impact idea you have no evidence for — the single best thing about the model. And it makes **effort a first-class citizen**, which kills a lot of "great idea, impossible to build" entries. As a [[Prioritization Frameworks|prioritization]] tool for a backlog of comparable features, it earns its place.

## The failure modes — where RICE lies to you

Here's where I get blunt, because the dangerous thing about RICE is that the number *looks* like math.

> [!warning] False precision is the cardinal sin
> RICE produces a decimal. A decimal implies precision. But Reach is a guess, Impact is a five-point opinion, Confidence is a vibe converted to a percentage, and Effort is engineering's estimate (itself a range). You are multiplying four fuzzy numbers and reporting the result to two decimal places. **The output is exactly as reliable as your worst input** — and usually less, because errors compound under multiplication.

The specific traps I watch for:

- **Gameable inputs.** Anyone who knows the formula can reverse-engineer a high score by nudging Impact from 2 to 3 or shaving an effort estimate. If RICE controls the roadmap, people optimize the RICE, not the product. (Goodhart's law, in a spreadsheet.)
- **Effort estimates that don't exist yet.** You're scoring things you haven't designed, so Effort is frequently wrong by 2–3x. Since it's the denominator, an effort error swings the whole ranking.
- **Impact is the soft spot.** A 3 vs a 2 is a *judgment dressed as data,* and it has the largest leverage on score. Two PMs will score the same feature differently and both feel objective.
- **It's blind to strategy and dependencies.** RICE has no idea about your [[Crafting a Product Vision|vision]], your [[The DHM Model|defensibility]], or that feature B is worthless without feature A. A pure RICE sort will happily rank a strategically irrelevant crowd-pleaser at the top.
- **It crushes long-term bets.** High-effort, hard-to-estimate, low-confidence strategic investments score terribly — exactly the work that builds moats. RICE has a structural bias toward small, safe, near-term wins.

## How I actually use it

I treat RICE as a **conversation-starter and a sanity check, never an autopilot.** Concretely: score the backlog, sort it, then read the list against the [[Strategic Impact|strategy]] and override with documented reasons. The overrides are the most interesting output — every time I move a low-RICE item up, I have to articulate *why* it matters beyond the number, and that articulation is usually the real strategic insight. And I never present RICE to [[Executive Communication|executives]] as justification — they should hear the bet and the reasoning, not a spreadsheet's arithmetic.

> [!tip] Use Confidence as a routing signal
> The most underused factor is Confidence. Instead of just discounting low-confidence items, *route* them: high impact + low confidence = run a [[Experimentation and A-B Testing|test]] or discovery sprint before it competes on the roadmap — scoring an idea you don't understand is theater. RICE then becomes a triage tool for what to *learn*, not just what to *build.*

## How AI is changing it

This is squarely in Reforge's "auto-prioritization" bucket — a model will populate a RICE table from your backlog and ticket data in seconds, and that's a real chore eliminated. The risk is that AI makes the *false precision* worse: a confident-sounding, well-formatted score from a model feels even more authoritative than one you built yourself, and it's no less of a guess. My rule holds and tightens: let AI draft the inputs and do the arithmetic, then spend the saved time on the part that was always the actual work — interrogating the Impact and Effort estimates, and deciding which high-score items to *override* because they fight the strategy. The model can't make that call, and it has no stake in defending it.

## Continue Reading
- [[Prioritization Frameworks]] — the full map of methods and when RICE is the right one.
- [[The Impact-Likelihood Matrix]] — a coarser, faster alternative for portfolio triage.
- [[OKRs and Goal-Setting]] — how the goals that define "Impact" should be set.
- [[Experimentation and A-B Testing]] — how to raise Confidence before betting effort on an idea.
- [[Outcomes Over Outputs]] — why the "Impact" you score must be an outcome, not a shipped feature.
