---
tags: [product-execution, framework, 10-50-90, uniform, original]
aliases: [The 10-50-90 Execution Framework, 10/50/90, The Uniform Framework, 10-50-90]
domain: Product Execution
---

# The 10-50-90 Execution Framework

This is the execution operating system I use to run any piece of work bigger than a copy change. I call it the **"Uniform"** framework — it's the one I built and refined at theScore, and it's mine. If you take one thing from the [[Product Execution]] domain, take this. It's the connective tissue between [[Feature Specification|spec]], [[Product Delivery|delivery]], and [[Product Quality|quality]].

## The problem it solves

Most execution failures aren't failures of effort — they're failures of *confidence calibration*. Teams commit to a plan at 10% confidence as if it were 90%, build the wrong thing in high fidelity, and discover the truth at launch when it's expensive. Or they wait for certainty that never comes and ship nothing. The framework fixes this by making confidence *explicit* and tying the fidelity of the work to it.

## Two axes and a role split

It's three phases, three confidence checkpoints, and a clear answer to "who decides."

### The phases: Define → Explore → Refine

| Phase | The question | The work |
|---|---|---|
| **Define** | *Are we solving the right problem?* | Frame the problem, the outcome, the [[The Four Big Product Risks\|risks]]. Output: a sharp [[Feature Specification\|spec]]. |
| **Explore** | *Have we found a solution that works?* | Prototype, test, narrow options. This is where most [[Continuous Discovery\|discovery]] and design iteration happens. |
| **Refine** | *Can we build and ship it well?* | Lock scope, build, [[Product Quality\|QA]], prepare the [[Shipping and Launch\|rollout]]. |

### The confidence checkpoints: 10 / 50 / 90

The numbers are confidence that you're building the right thing, the right way. They are *gates*, and the rule is simple: **don't spend high-fidelity effort at low confidence.**

> [!example] What each checkpoint means
> - **10% — "Is this worth pursuing?"** Rough framing. A one-pager, a sketch, a hypothesis. Cheap to be wrong. Decision: invest in exploring, or drop it.
> - **50% — "Is this the right approach?"** A tested prototype, a validated direction, an engineering gut-check on feasibility. Decision: commit to building, or pivot the approach.
> - **90% — "Are we ready to ship?"** Built, QA'd, instrumented, launch plan in hand. Decision: ship (and how), or hold.

The discipline is matching effort to the checkpoint. At 10% you should have spent almost nothing — a sketch, not a Figma file. By 90% you've earned the right to spend real engineering time because you've retired the big risks. The expensive mistake is doing 90%-fidelity work on a 10%-confidence idea.

> [!tip] Map the checkpoints to the phases
> Define exits at ~10% (we believe in the problem). Explore exits at ~50% (we believe in the solution). Refine exits at ~90% (we believe we can ship it well). The phase tells you *what work to do*; the checkpoint tells you *how confident you must be to proceed* — and how much to spend getting there.

### The role split: Owner / Partner / Consulted

The third dimension is who decides, borrowed from a RACI mindset and tuned for product. The full treatment is in [[RACI and Decision Rights]], but the core split I use:

- **Owner** — accountable for the call and the outcome. **PM owns product success and viability.**
- **Partner** — co-creates and shares the work; their domain is theirs. **Design owns usability; engineering owns feasibility.**
- **Consulted** — has input that must be weighed, but does not decide.

> [!warning] The PM does not own everything
> The single biggest misuse of this framework is a PM treating "Owner" as "I decide all of it." You own product success and viability. You do *not* own usability — that's design's call — or feasibility, which is engineering's. Clarity about who owns which decision at each checkpoint is what makes the framework fast instead of political.

## Putting it together

A real project is a grid: at each **checkpoint** (10/50/90), within each **phase** (Define/Explore/Refine), you know *who owns the decision* (Owner/Partner/Consulted). That's the whole thing. It scales down to a two-day feature (the checkpoints are conversations) and up to a quarter-long initiative (the checkpoints are formal reviews).

## Why I prefer it to "just run sprints"

[[Agile Delivery and Team Cadence|Sprints]] tell you *when* you'll do work. They say nothing about whether you've earned the confidence to do it. 10/50/90 sits *above* the sprint mechanics: it's a confidence-and-decision layer that keeps you from sprinting hard in the wrong direction. It also bakes in [[Sound Product Decision-Making|decisiveness]] — every checkpoint forces an explicit go / pivot / kill call, which kills the "let's keep going because we started" inertia that sinks so many projects.

## How AI is changing it

AI compresses the front of this framework dramatically. The Define and Explore phases — research synthesis, first-draft specs, throwaway prototypes — used to take weeks and now take hours with tools like ChatPRD, Dovetail, and v0/Lovable. That means you can reach the 50% checkpoint far faster and far cheaper, and run more cheap 10% bets in parallel. But the *judgment at each gate* — is this the right problem, is this approach actually right, are we genuinely ready to ship — is exactly the human premium AI raises rather than replaces. AI accelerates the first 70%; the gate decisions are the last 30% where the risk concentrates ([[The 70% Problem]]). See [[AI in Prototyping and Delivery]].

## Continue Reading
- [[RACI and Decision Rights]] — the Owner/Partner/Consulted model in full, plus disagree-and-commit.
- [[Sound Product Decision-Making]] — the go/pivot/kill judgment each checkpoint demands.
- [[The Four Big Product Risks]] — the risks you're retiring as you move 10 → 50 → 90.
- [[Build-Measure-Learn and the MVP]] — the discovery-side cousin of the same confidence logic.
- [[Shipping and Launch]] — what happens after the 90% gate clears.
