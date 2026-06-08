---
tags: [ai, modern-pm, literacy, technical-fluency]
aliases: [The PM's AI Literacy, AI Literacy, AI Literacy for PMs]
domain: AI and the Modern PM
---

# The PM's AI Literacy

You do not need to train a transformer. You do need to understand model behavior well enough to make product decisions, write specs, and judge quality. That's the bar. AI literacy for a PM is not ML engineering — it's the working fluency to reason about a probabilistic system the way you already reason about users and markets.

## Interview your model

a16z's most useful piece of advice on staying relevant is also the simplest: **interview your model.** Treat the model the way you'd treat a new user-research subject or a new hire. Push it. Find where it's brilliant and where it falls on its face. Ask the same thing ten different ways. The goal is an intuition for *what this system can reliably do* — because that intuition is the raw material for every product decision you'll make on top of it.

> [!tip] How I actually do this
> When a new model ships, I spend an afternoon trying to break it on tasks my product cares about. Not benchmarks — my tasks. Where does it hallucinate? Where does it refuse? Where does it confidently produce garbage? That session tells me more about what to build than any spec sheet, and it directly feeds the [[Writing Evals for AI Products|eval set]].

## The jagged frontier

Ethan Mollick's "jagged frontier" is the single most important mental model here. AI capability is **not a smooth line**. The frontier is jagged: tasks that look equally hard to a human are wildly uneven for a model. It writes a competent legal summary and then fails a counting problem a child could do. You cannot predict which side of the frontier a given task lands on by intuition — you have to test.

Mollick's rules for working on the jagged frontier are worth internalizing:

- **Always invite AI to the table** — try it on everything; you don't know where it's strong until you do.
- **Be the human in the loop** — you are the judgment, the model is the draft.
- **Treat it like a person** (a specific kind) — tell it who to be and what good looks like.
- **Assume this is the worst AI you'll ever use** — capability is a moving target; design for next year's model too.

This last one matters for [[Building AI Products|how you build]]: don't over-engineer around today's limits.

## The "just enough" technical bar

Here's what I think a modern PM genuinely needs to understand. Not to *do* — to *reason about*.

| Concept | Why a PM needs it |
|---|---|
| Tokens, context windows, latency | They're your cost and UX constraints — see [[The Unit Economics of AI]] |
| Prompting and system prompts | The cheapest lever; "the new literacy" |
| Precision vs recall | The core quality trade-off in any classification or retrieval feature |
| The build-decision ladder | Prompt → context → RAG → fine-tune; *fine-tuning is never your first move* |
| Non-determinism | Same input, different output — the root of [[Designing for Trust and Probabilistic Systems|trust design]] |

On that build ladder: Aakash Gupta's rule of thumb is that roughly 80% of problems are solved before you ever reach fine-tuning. Reach for the cheap, fast lever first.

> [!warning] The trap on both sides
> Under-literacy: you make promises the model can't keep and ship features that erode trust. Over-literacy theater: you learn to recite transformer architecture and mistake it for product judgment. Neither is the goal. The goal is decisions — can I build this, at what quality, at what cost, with what failure modes.

## Continue Reading
- [[Writing Evals for AI Products]] — what you do *after* you've interviewed the model.
- [[The 70% Problem]] — the jagged frontier applied to where AI quality drops off.
- [[Building AI Products]] — turning literacy into a buildable system.
- [[The Unit Economics of AI]] — the cost side of the technical bar.
- [[Fluency with Data]] — the adjacent competency this extends.
- [[Designing for Trust and Probabilistic Systems]] — designing around non-determinism.
