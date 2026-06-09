---
tags: [ai, modern-pm, the-70-percent-problem, jagged-frontier, last-mile]
aliases: [The 70% Problem, The 70 Percent Problem, The Seventy Percent Problem]
domain: AI and the Modern PM
---

# The 70% Problem

"The 70% problem" is the most useful shorthand I have for where AI helps and where it hurts. Two distinct ideas go by this name, from two different people, and they get conflated all the time. They point at the same lesson from opposite directions, so it's worth holding both of them clearly.

## Sense one, Mollick and BCG: quality outside the frontier

The first sense is about **quality**, and it comes from Ethan Mollick reading a large BCG field study. The finding: on tasks *inside* AI's jagged frontier, consultants using AI did dramatically better. But on tasks that *looked* similar yet actually fell *outside* the frontier, people using AI were right about 60 to 70% of the time, versus roughly 84% without it. AI didn't just fail to help there. It actively dragged accuracy down, because people trusted fluent output on problems the model wasn't actually good at. (Those are the study's figures, so read them as directional rather than precise.)

> [!tip] Centaurs vs Cyborgs
> Mollick names two working styles. A **Centaur** divides the labor, handing the model the tasks it's good at and keeping the rest. A **Cyborg** blends with it continuously, checking and steering in real time. Both beat the naive "let the AI do it." The failure mode is **automation complacency**: handing the model a task outside its frontier and rubber-stamping a confident wrong answer. The defense is knowing where the frontier sits, which is exactly why you [[The PM's AI Literacy|interview your model]].

## Sense two, Osmani: the last mile of AI coding

The second sense is about **building**, and it comes from Addy Osmani writing on AI-assisted coding. AI gets you to a working-ish 70% of an app astonishingly fast, and then the **last 30% is where it gets hard and stays hard.** Edge cases, error handling, security, performance, the integration nobody anticipated, the production hardening. The first 70% feels like magic. The last 30% is grinding, expert, unglamorous work that AI struggles to finish.

| Phase | Effort | Who carries it |
|---|---|---|
| First 70% | Fast, easy, exhilarating | AI does most of it |
| Last 30% | Slow, hard, where things break | Human expertise and judgment |

This is exactly the gap between a [[AI in Prototyping and Delivery|vibe-coded prototype]] and a shippable product. The demo is the 70%. The 30% is why "it's basically done" is the most expensive sentence in AI development.

## The unifying lesson for PMs

> [!note] Where PM risk concentrates
> Both senses land on the same point: **AI accelerates the first 70%, and the last 30% is where judgment, taste, and risk concentrate.** AI rips through the first draft of discovery, the first prototype, the first spec, the first 70% of the code. The remaining 30% is the hardening, the trust work, the edge cases, and the taste to know when "good enough" isn't. That's precisely the work AI can't finish, and it's the work the PM owns. As the easy 70% commoditizes, all of the differentiated value migrates into that last 30%.

This is the mechanism underneath the whole [[Competencies AI Commoditizes vs Elevates|commoditize-vs-elevate]] thesis, viewed at the level of a single task. The cheap part got cheaper. The hard part got more concentrated, and more valuable with it.

> [!warning] The 70% illusion
> The danger is mistaking 70% for 95%. The output *looks* nearly done: fluent prose, a working demo, code that compiles. That polish hides how much hard work is still ahead. Executives see the 70% and assume the finish line is right there. Budget, staff, and communicate for the 30%, because that's where products actually ship or die. Manage that expectation out loud, every single time.

## My take

I plan around this explicitly now. I point AI at the first 70% of everything (discovery synthesis, prototypes, drafts, scaffolding) and I reserve human focus, my own included, for the 30% that decides whether it's real. The PMs who lose are the ones who ship the 70% and call it done. The ones who win treat the 70% as a fast start and pour their judgment into the finish. That's [[Product Sense and Judgment]] applied at the unit of every task.

## Continue Reading
- [[The PM's AI Literacy]] for the jagged frontier this builds on.
- [[Competencies AI Commoditizes vs Elevates]] for the same lesson at the competency level.
- [[AI in Prototyping and Delivery]] for why the prototype is only the 70%.
- [[Product Sense and Judgment]] for the judgment the last 30% demands.
- [[Designing for Trust and Probabilistic Systems]] for the hardening the 30% requires.
- [[Building AI Products]] for finishing the last mile of an AI product.
