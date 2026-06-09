---
tags: [product-execution, decision-making, judgment, one-way-doors, reversibility]
aliases: [Sound Product Decision-Making, Decision Making, Product Decisions, One-Way and Two-Way Doors]
domain: Product Execution
---

# Sound Product Decision-Making

This is the first behavior under [[Product Quality]], and in my view it's the single most concentrated expression of what a PM is *for*. Strip away the artifacts and the meetings and the job comes down to this: make good calls, quickly, with incomplete information, and own what happens. Everything else is in service of this.

## What it is

From my model: **qual + quant data; grounded in real user needs; balancing impact, effort, and alignment; collaborating for input; and making accountable, timely decisions.** Read that again and notice it does not say "make correct decisions." It says *sound* decisions: defensible, well-reasoned, timely, owned. You will be wrong sometimes. Soundness is about the quality of the process and the accountability, not perfect outcomes.

## Qual + quant, both, always

The fastest way to spot a junior PM is which leg they stand on. Data-only PMs optimize the measurable and miss what users actually feel. Intuition-only PMs ship their own taste and call it vision. [[theScore Product Principles|"Balance game sense with data"]] is the principle I hold here: quant tells you *what* is happening, qual tells you *why*, and judgment fuses them. Lean on [[Fluency with Data]] for the what and [[Voice of the Customer]] for the why, because a decision built on one without the other is half a decision.

> [!warning] Analysis paralysis is also a decision
> Waiting for more data *is a choice*, and usually a bad one, because you have traded a timely sound call for a late one while the cost of delay compounds. The principle is explicit: avoid analysis paralysis, don't beat a dead horse, and let the data inform the *next* iteration rather than demanding certainty before you move.

## The most useful mental model: one-way vs two-way doors

This is the framework I reach for most, borrowed from Amazon and worth internalizing completely.

| | Two-way door (reversible) | One-way door (irreversible) |
|---|---|---|
| **Cost of being wrong** | Low; you can walk back | High; hard or impossible to undo |
| **How to treat it** | Decide *fast*, mostly solo, low ceremony | Slow down, gather input, get it right |
| **Examples** | A copy test, a feature flag, a flow tweak | A data-model migration, a pricing change, a public API, a brand promise |

> [!tip] Match the rigor to the door
> The error in both directions is expensive. Agonizing over a two-way door wastes time and signals indecisiveness. Treating a one-way door like a two-way door is how you ship the migration you can't undo. **Most product decisions are two-way doors,** which means the right default is *bias to action*, with the discipline to recognize the rare one-way door and slow down for it. This maps cleanly onto the [[The 10-50-90 Execution Framework|10/50/90]] checkpoints: low-confidence two-way doors get a cheap bet, and one-way doors need real confidence before you commit.

## Decisiveness and owning the outcome

The behavior says **accountable, timely.** Two non-negotiables:

- **Timely.** A decision delivered after the team needed it is a non-decision. Velocity of judgment is a skill, and the senior [[Product Quality]] bar rewards *efficiently* assessing a release and calling it. Be a [[theScore Product Principles|shooter]]: decide, and accept that some shots miss.
- **Accountable.** You own the call *and the result*. Not "the data said so," not "the stakeholders wanted it." When it works, the team gets credit. When it doesn't, you take the hit and the learning. PMs who launder their decisions through other people lose the team's trust, and trust is the currency that lets you make the *next* call fast.

## How to grow it

- **Label the door out loud.** Before any meaningful decision, say "this is a two-way door, let's just try it" or "this is one-way, let's slow down." It instantly calibrates how much process the room should spend.
- **Decide with a recommendation, not a poll.** Gather input, then *commit to a position*. "I recommend X because Y; tell me why I'm wrong" produces better decisions and faster meetings than open-floor consensus-seeking.
- **Write down what you expected.** Record the outcome you predicted ([[Outcomes Over Outputs]]). Comparing prediction to result is the only way decision-making actually improves. Skip it and you just collect anecdotes.
- **Disagree and commit.** Once the call is made, even one you lost, execute it fully ([[RACI and Decision Rights]]).

## How AI is changing it

This is the competency AI elevates most, not least. AI can generate options, surface data, and pressure-test reasoning in seconds, and Claire Vo describes strategy work compressing from weeks to a commute conversation. But the *call itself*, meaning weighing impact against effort against alignment, knowing which user signal to trust, owning the result, is irreducibly human, and Reforge argues the premium on judgment and taste has never been higher. Here is the twist worth internalizing. AI multiplies the *number* of options you can consider, which makes the burden of choice heavier, not lighter. More inputs, same decider. See [[Product Sense and Judgment]] and [[Competencies AI Commoditizes vs Elevates]].

## Continue Reading
- [[Risk Identification and Mitigation]] for the sibling behavior: deciding well when the downside is what's uncertain.
- [[Product Quality]] for the competency both behaviors define.
- [[Product Sense and Judgment]] for the deeper well sound decisions draw from.
- [[Understanding Trade-offs]] for the impact/effort/alignment balancing at the core of every call.
- [[The 10-50-90 Execution Framework]] for confidence checkpoints as a decision-forcing rhythm.
