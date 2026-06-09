---
tags: [product-execution, competency, feature-specification, requirements]
aliases: [Feature Specification, Spec'ing, Defining Functionality]
domain: Product Execution
---

# Feature Specification

> [!quote] The definition I use
> The ability for a PM to gather requirements, define functionality, and set goals in a clear, actionable format that can be used to communicate with the team and drive product delivery.

This is the first competency in [[Product Execution]], and it is where the job begins. It is also the thing I coach people on most often, so let me get the framing right before anything else.

## What it is

A spec is not the document. The document is just the artifact. The spec is the shared understanding it creates. I have watched a beautiful twelve-page PRD get ignored by everyone on the team, and I have watched a three-sentence Slack message align that same team in an afternoon. The short message did the job. The PRD did not. What you are really producing is alignment: engineers know what to build, design knows the problem, stakeholders know what is coming, and everyone agrees on what "done" and "good" mean. If you wrote a perfect document and the team still does not share that picture, you have not spec'd anything yet. You have filed paperwork. I have done it, and it is a humbling way to learn the difference.

The craft of producing the document, the formats and the one-pager and the structure, lives in [[Writing PRDs and Specs]]. This note is about the competency underneath it: the thinking a good spec makes visible.

## The behaviors

I break Feature Specification into three behaviors.

> [!note] Outcome Oriented
> Lead with the value, not the implementation, and keep the "why" in front of the reader the whole way through. A spec that opens with a feature list is a tiny feature factory. A good one opens with the problem and the outcome you expect to move, and every requirement ladders back to it. When an engineer asks why you are building it this way, the answer should already be on the page. This is [[Outcomes Over Outputs]] applied at the smallest unit of work.

> [!note] Comprehensive Documentation
> Cover the problem, the objective, the scope (user stories and acceptance criteria), the UX and technical considerations, and the success metrics. Then cover the things people forget: edge cases, data and instrumentation, risks, and the go-to-market. Instrumentation is the one I push hardest on. If you did not say how you will measure it, you have quietly decided you will never know whether it worked. Settle that with [[Product Analytics and Metrics]] before a line of code gets written.

> [!note] Clarity
> Write it so it is easy to read and easy to align on. Clarity is a forcing function for thinking, and a vague spec is usually a sign the thinking is not finished and the PM is hoping the team will close the gap. They will close it. Just not the way you wanted.

## How it shows up by level

The skill does not change as you climb. The scope and the altitude do (see [[What Changes at Each Level]]).

| Level | What good looks like |
|---|---|
| [[Associate Product Manager\|APM]] | Writes a clear spec for a minor feature, contributes to major ones, gathers what the immediate team needs, and sets a clear, achievable goal. |
| [[Product Manager\|PM]] | Specs major, complex functionality on their own, finds the right level of detail without over or under specifying, uses comps and prototypes, and gets feedback at each phase. |
| [[Senior Product Manager\|Senior]] | Sequences several interrelated specs, considers every device and point of sale even when the launch targets a subset, and folds effort estimates into the requirements. |
| [[Staff and Principal Product Manager\|Staff/Principal]] | Reviews the team's specs, coaches them to clarity, and improves the specification process itself. |
| [[Director and VP of Product\|VP]] | Owns how the whole org writes and reviews specs, both the process to create them and the process to give feedback on them. |

## How to grow it

A few things I actually ask people to try:

- Write the success metric first. Before you describe the feature, state the number you expect to move. If you cannot name it, you have a discovery problem, not a spec problem, and [[Continuous Discovery]] is where to go next.
- Read the spec back to your engineers and ask them to explain the feature to you. Every gap in their explanation is a gap in your spec. It is the fastest feedback loop I know of.
- Watch the urge to over-specify. A lot of us do it to feel in control, and we end up dictating implementation to engineers who understand the how far better than we do. Own the what and the why. Leave the how to the people building it.
- Steal formats, not templates. A template is a checklist. A format is a way of thinking. Learn a few of them in [[Writing PRDs and Specs]] and match the format to the risk in front of you.

## How AI is changing it

Drafting a PRD is close to free now, so the mechanical writing is no longer where your value sits. What AI cannot do for you is decide which problem is worth solving, choose the outcome, and rule things out of scope. The bottleneck was never the typing. It was the thinking, and that is the part AI quietly hands back to you. Spend the time you save there rather than on a longer document. See [[Competencies AI Commoditizes vs Elevates]].

## Continue Reading
- [[Writing PRDs and Specs]] for the craft itself: formats, the one-pager, and the traps to avoid.
- [[Product Delivery]] for what happens after the spec, when you work with the team to ship it.
- [[The 10-50-90 Execution Framework]] for where spec'ing sits in how I run Define, Explore, and Refine.
- [[Outcomes Over Outputs]] for why Outcome Oriented is the behavior that matters most.
- [[Continuous Discovery]] for the upstream work that makes a spec worth writing.
