---
tags: [product-execution, competency, feature-specification, requirements]
aliases: [Feature Specification, Spec'ing, Defining Functionality]
domain: Product Execution
---

# Feature Specification

> [!quote] The definition I use
> The ability for a PM to gather requirements, define functionality, and set goals in a clear, actionable format that can be used to communicate with the team and drive product delivery.

This is the first competency in [[Product Execution]], and it's where the job begins. But I want to reframe it immediately, because most PMs get the framing wrong.

## What it is

A spec is not a document. The document is the *artifact*; the spec is the **shared understanding** it creates. I've seen beautiful 12-page PRDs that nobody read and one-paragraph Slack messages that aligned an entire team. The first failed and the second succeeded. The deliverable is alignment — engineers know what to build, designers know the problem, stakeholders know what's coming, and everyone agrees on what "done" and "good" mean. If you produced a perfect document and the team still doesn't share that picture, you haven't spec'd anything. You've filed paperwork.

The craft of producing the document — formats, structure, the one-pager — lives in [[Writing PRDs and Specs]]. This note is about the competency: the *thinking* a great spec demonstrates.

## The behaviors

My model breaks Feature Specification into three named behaviors.

> [!note] Outcome Oriented
> Value and impact over implementation; the "why" applied throughout. A spec that opens with a list of features is a feature factory in miniature. A great one opens with the problem and the outcome you expect to move, and every requirement traces back to it. When an engineer asks "why are we building it this way," the answer should already be in the doc. This is [[Outcomes Over Outputs]] applied at the smallest unit of work.

> [!note] Comprehensive Documentation
> The problem, the objective, the scope (user stories + acceptance criteria), UX and technical considerations, success metrics — plus the things juniors forget: **edge cases, data/instrumentation, risks, and go-to-market.** The instrumentation point is the one I push hardest. If you didn't spec how you'll measure it, you've pre-decided that you'll never know if it worked. Tie this to [[Product Analytics and Metrics]] before a line of code is written.

> [!note] Clarity
> Concise, easy to align across teams; organized decisions; clear impacts, actions, and next steps. Clarity is a forcing function for thinking. Vague specs are almost always a sign the PM hasn't done the thinking yet and is hoping the team will fill the gap. They will — just not the way you wanted.

## How it shows up by level

The skill doesn't change; the scope and the altitude do (see [[What Changes at Each Level]]).

| Level | What good looks like |
|---|---|
| [[Associate Product Manager\|APM]] | Writes a clear spec for a *minor* feature; contributes to major ones; gathers what's needed from the immediate team; defines a clear, achievable goal. |
| [[Product Manager\|PM]] | Specs *major*, complex functionality independently; finds the right level of detail (no over/under-spec); uses comps and prototypes; gets feedback at each phase. |
| [[Senior Product Manager\|Senior]] | Sequences *multiple interrelated* specs; considers all devices and points of sale even when the launch targets a subset; estimates effort and factors it into requirements. |
| [[Staff and Principal Product Manager\|Staff/Principal]] | Reviews the team's specs and coaches to clarity; improves the *specification process itself*; influences company-wide spec standards. |
| [[Director and VP of Product\|VP]] | Owns continuous improvement of how the whole org writes and reviews specs — the process to create and the process to give feedback. |

## How to grow it

- **Write the success metric first.** Force yourself to state the number you expect to move before you describe the feature. If you can't, you have a discovery problem, not a spec problem ([[Continuous Discovery]]).
- **Read specs back to engineers and ask them to explain the feature to you.** Every gap in their explanation is a gap in your spec. This is the single fastest feedback loop I know.
- **Kill the over-spec habit.** Junior PMs over-specify to feel in control and end up dictating implementation to engineers who know better. Specify the *what* and the *why*; leave the *how* to the people who build it.
- **Steal formats, not templates.** A template is a checklist; a format is a way of thinking. Learn several ([[Writing PRDs and Specs]]) and match the format to the risk.

## How AI is changing it

This is one of the most disrupted competencies in the model. AI drafts PRDs in minutes — ChatPRD and Dovetail's evidence-backed docs are already standard — and spec-driven development frameworks now treat "intent as the source of truth," which makes the standalone document less central than the *clarity of intent* behind it. The mechanical writing is commoditizing. The premium moves entirely to the judgment AI can't supply: framing the right problem, choosing the outcome, and deciding what *not* to build. The bottleneck was never typing; it was thinking, and that's exactly the part AI hands back to you. More in [[Competencies AI Commoditizes vs Elevates]].

## Continue Reading
- [[Writing PRDs and Specs]] — the craft: formats, the one-pager, and the anti-patterns to avoid.
- [[Product Delivery]] — what happens after the spec: working with the team to ship it.
- [[The 10-50-90 Execution Framework]] — where spec'ing sits in my Define → Explore → Refine flow.
- [[Outcomes Over Outputs]] — why "Outcome Oriented" is the behavior that matters most.
- [[Continuous Discovery]] — the upstream work that makes a spec worth writing.
