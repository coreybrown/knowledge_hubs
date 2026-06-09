---
tags: [product-strategy, prioritization, frameworks, decision-making]
aliases: [Prioritization Frameworks, Prioritization, Prioritization Methods]
domain: Product Strategy
---

# Prioritization Frameworks

Prioritization is the daily act of strategy. Every roadmap, every sprint, every "can we just add one thing" is a prioritization decision, and how you make those decisions *is* your strategy whether you've written one down or not. This note is my map of the major methods, when each fits, and the uncomfortable truth underneath all of them.

## The real point of a framework: forcing the conversation, not finding the answer

I want to be clear about this up front, because it's the thing I coach people on most. **No framework produces a correct prioritization.** They produce a *structured argument.* Their value is that they force you to make your criteria explicit, apply them consistently, and show your work, so the decision is auditable instead of political or based on who shouted loudest. The [[Product Vision and Roadmapping]] behavior names exactly this: "structured frameworks... transparent rationale... say 'no' to focus on the highest leverage." The framework is scaffolding for the no.

> [!tip] Pick one and stick with it
> The most common prioritization mistake isn't choosing the "wrong" framework. It's framework-hopping, where a new method appears every quarter and nothing is comparable over time. Consistency beats sophistication. Choose one that fits your context, use it for a year, and let the *comparability* of decisions become the real benefit.

## The major methods and when each fits

| Framework | How it works | Best when | Watch out for |
|---|---|---|---|
| **[[RICE and Scoring Models\|RICE]]** | Reach × Impact × Confidence ÷ Effort | Comparing many similar-sized features with some data | False precision; gameable inputs |
| **[[The Impact-Likelihood Matrix\|Impact × Likelihood]]** | 2×2: high/low impact vs likelihood of success | Quick portfolio triage; separating big bets from busywork | Too coarse for fine-grained calls |
| **[[The Kano Model\|Kano]]** | Classifies features as basic / performance / delight | Deciding *what kind* of value to invest in | Needs user data; categories drift over time |
| **[[MoSCoW Prioritization\|MoSCoW]]** | Must / Should / Could / Won't have | Scoping a release or negotiating with stakeholders | Everything becomes a "Must" without discipline |
| **[[The Eisenhower Matrix\|Eisenhower]]** | Urgent × Important | Personal/team time and triage, not roadmaps | Conflates urgency with importance if rushed |
| **Cost of Delay / WSJF** | Value of shipping sooner ÷ effort | When timing and dependencies dominate | Hard to estimate the cost-of-delay honestly |

The trick is matching the framework to the *decision altitude.* For triaging a big portfolio of bets, I reach for the [[The Impact-Likelihood Matrix|Impact-Likelihood Matrix]], which is fast and cleanly separates "Home Runs" from "Stuff You Shouldn't Be Doing." For comparing a backlog of comparable features, [[RICE and Scoring Models|RICE]] earns its keep. For *what kind* of feature to build (table stakes vs differentiator), [[The Kano Model|Kano]] is the right lens. For release scoping with stakeholders, [[MoSCoW Prioritization|MoSCoW]] gives a shared vocabulary. Don't use a scalpel where a machete works, or vice versa.

A note on effort, separate from value: [[The LNO Framework|Shreyas Doshi's LNO framework]] (Leverage / Neutral / Overhead) prioritizes *how much effort a task deserves* rather than which task to do. It pairs well with any of the above. Once you've decided *what* to do, LNO tells you how much polish each piece warrants.

## The discipline of saying no

The one thing no framework can do for you is actually say the no. The frameworks give you the *rationale*; the courage is on you. Saying no is the core skill of prioritization, and it's hard for three reasons: it disappoints people, it's irreversible-feeling, and a "yes" is always easier in the moment. I've learned to make the no *specific and reasoned*: not "we can't do that," but "we're not doing that because it serves a segment we've deliberately chosen not to prioritize, and here's the bet we're making instead." The reason is the product. A no without a why is a brush-off; a no with a why is strategy.

> [!warning] The myth: a high score means build it
> A scoring framework's output is an *input* to a decision, not the decision. I've seen teams build the top-RICE item reflexively while it actively contradicted the strategy. The score doesn't know your [[Crafting a Product Vision|vision]] or your [[The DHM Model|defensibility]]. Sort by the framework, then apply judgment, never the reverse.

## How AI is changing it

Auto-prioritization is explicitly on Reforge's list of commoditized PM activities, and rightly so. A model can ingest your backlog, estimate RICE inputs, and produce a ranked list faster than you can open the spreadsheet. That's useful for the *grunt* layer: first-pass scoring, surfacing what you might've missed. But it sharpens rather than removes the human job. The inputs (reach, impact, confidence) are estimates that encode judgment and strategy, and AI will estimate them plausibly *and* generically. The decisions that matter (overriding a high score because it fights the vision, making the unpopular no, deciding which segment to starve) are exactly the taste-and-conviction work the model can't own. Let AI do the arithmetic; keep the choosing.

## Continue Reading
- [[RICE and Scoring Models]] is the most popular scoring model, in detail, with its failure modes.
- [[The Impact-Likelihood Matrix]] is my go-to for fast portfolio triage.
- [[Building and Managing a Roadmap]] is where prioritization decisions get sequenced and communicated.
- [[The LNO Framework]] for prioritizing effort per task once you've decided what to do.
- [[Understanding Trade-offs]] is the foundational skill prioritization is built on.
