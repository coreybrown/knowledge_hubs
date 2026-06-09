---
tags: [product-execution, agile, scrum, kanban, cadence, process]
aliases: [Agile Delivery and Team Cadence, Agile, Scrum and Kanban, Team Cadence]
domain: Product Execution
---

# Agile Delivery and Team Cadence

This is the "how the work actually moves" note under [[Product Delivery]]. It is also the note where I am most opinionated, because process is where teams waste the most energy arguing about the wrong things.

## My take: agile is a means, and too many teams worship it as an end

The Agile Manifesto valued *individuals and interactions over processes and tools.* The irony is that "agile" has become the heaviest process-and-tools religion in software. I have sat in three-hour sprint plannings, story-point poker that takes longer than the work it estimates, and retros that produce action items nobody owns. None of that ships product.

My rule: **the cadence exists to create a predictable rhythm of shipping and learning. If a ceremony is not doing that, kill it.** Be a [[theScore Product Principles|shooter]] about process too, bold enough to drop the rituals that do not earn their keep.

## Scrum vs Kanban: pick by the shape of the work

Both work. The choice is about the *shape* of your work, not which one is "more agile."

| | Scrum | Kanban |
|---|---|---|
| **Cadence** | Fixed sprints (1 to 2 wks) | Continuous flow |
| **Best for** | Roadmapped feature work with planning rhythm | Interrupt-driven work, ops, support, fast iteration |
| **Core mechanic** | Commit to a sprint backlog | Limit work-in-progress |
| **Where it breaks** | Becomes mini-waterfall; ceremonies bloat | No natural planning beat; can drift |

In my B2C mobile life I have mostly run a Scrum-ish backbone with a Kanban lane for the inevitable production fires. Hybrids are normal and fine. The enemy is process orthodoxy, not any particular method.

## The PM's real role in delivery

> [!warning] You are not the scrum master
> This is the most important sentence in the note. The PM owns the *what* and the *why*: the priorities, the goals, the trade-offs. The scrum master (or eng lead, or the team itself) owns the *how* of the process: the board, the ceremonies, the flow. When a PM annexes the scrum-master role, two bad things happen. The PM gets sucked into process administration instead of product thinking, and the team loses its own ownership of how it works. Hold the *what*. Let the team own the *how*.

So what *is* the PM doing in the cadence?

- **Standup:** Listening for blockers, not collecting status. If your standup is people reading yesterday's commits aloud, it is a tax. Your job is to hear "I'm stuck on X" and go remove X. ([[Product Delivery|Team Coordination]].)
- **Planning / backlog:** Making sure the top of the backlog is the highest-leverage work and is *actually ready*: spec'd, [[Prioritization Frameworks|prioritized]], dependencies known. A groomed backlog is the PM's deliverable to the team.
- **Review / demo:** Connecting what shipped back to the goal, the "why this mattered" ([[Outcomes Over Outputs]]).
- **Retro:** Showing up, listening, and acting on what you own. You are a participant, not the facilitator.

> [!tip] Protect the team's focus
> The highest-leverage thing I do in any cadence is say *no* and *not now* on the team's behalf, absorbing the random asks so engineers get uninterrupted build time. Velocity is mostly a function of focus, not heroics.

## On velocity and story points

Here is a myth worth puncturing: velocity is a *planning aid*, not a performance metric. The moment "increase velocity" becomes a goal, teams inflate estimates and the number goes meaningless. Points measure relative effort to help *you* plan a sprint. They are not productivity, and they are definitely not [[Outcomes Over Outputs|outcomes]]. Estimates belong to engineering ([[Product Delivery]]); your job is to protect them, not to game them.

## How AI is changing the cadence

The mechanical layer of agile is dissolving fastest. Standups are increasingly replaced by async AI summaries, and ticket-writing and status reporting are the single easiest things to automate in the whole job, with the pure "product owner" backlog-administration role being, in SVPG's words, an easy AI target. Cat Wu at Anthropic has noted that on AI-product teams, demos are starting to replace standups: you show the working thing instead of narrating progress. The takeaway for you is simple. If your value in the cadence is running the ceremonies, that value is evaporating. If it is judgment about what to build and the focus to protect the team, it is rising. See [[AI in Prototyping and Delivery]].

## Continue Reading
- [[Product Delivery]] for the competency this cadence serves.
- [[The 10-50-90 Execution Framework]] for the confidence-checkpoint layer that sits above sprint mechanics.
- [[Build-Measure-Learn and the MVP]] for why "iteratively and quickly" is the point of the whole rhythm.
- [[Outcomes Over Outputs]] for the antidote to velocity-as-a-goal.
- [[RACI and Decision Rights]] for who decides what when the cadence surfaces a hard call.
