---
tags: [product-execution, competency, product-quality, decisions, risk]
aliases: [Product Quality, Quality, Product Quality Assurance]
domain: Product Execution
---

# Product Quality

> [!quote] The definition I use
> The ability to identify, prioritize, and resolve technical, functional, and business quality issues across all devices, points of sale, and use cases that are applicable to the product.

This is the third competency in [[Product Execution]]. In the canonical Reforge/Hunt matrix it's called "Product Quality *Assurance*," and I deliberately dropped the "Assurance." Here's why that matters.

## What it is, and what it is not

Quality is **not QA**. QA is a process: a phase, a checklist, sometimes a team. Quality is a *standard of judgment* the PM carries through the entire lifecycle. The PM does not personally test every device, but the PM owns the *bar*: deciding what is a launch blocker and what is not, weighing impact against effort, and being accountable when something ships broken. Reframing it from "assurance" (a gate at the end) to "quality" (a judgment throughout) is the whole point.

The definition's range is deliberately wide: **technical, functional, AND business quality, across all devices, points of sale, and use cases.** In my B2C mobile world that is brutal. iOS, Android, web, tablet, every market, every edge case. Business quality is the one juniors forget, because a feature can be bug-free and still be low quality if it does not move the [[Outcomes Over Outputs|outcome]] it was built for.

## The behaviors

My model breaks Product Quality into two named behaviors. They're the substance of the next two notes.

> [!note] Sound Product Decision Making
> Qual + quant data; grounded in real user needs; balancing impact, effort, and alignment; collaborating for input; and making **accountable, timely** decisions. The "timely" and "accountable" words carry the weight. A perfect decision made too late is a bad decision, and a decision nobody owns is a decision that gets relitigated forever. Full treatment in [[Sound Product Decision-Making]].

> [!note] Risk Identification & Mitigation
> Early detection; classifying risks by **impact × likelihood**; building contingency plans; transparent communication; and ongoing monitoring. The discipline is catching risk *early*, when it's cheap to handle, and being honest about it rather than hoping it goes away. Full treatment in [[Risk Identification and Mitigation]].

## How it shows up by level

The skill is constant; the scope of what you're holding to a bar grows (see [[What Changes at Each Level]]).

| Level | What good looks like |
|---|---|
| [[Associate Product Manager\|APM]] | QAs a feature across all devices and use cases; triages bug severity; recommends launch-blocker vs not. |
| [[Product Manager\|PM]] | Catches *interrelated* bugs across features; makes the right launch-quality calls; organizes a broader bug hunt when needed. |
| [[Senior Product Manager\|Senior]] | Efficiently assesses whether a *release* meets the bar and owns the ship/hold decision. |
| [[Staff and Principal Product Manager\|Staff/Principal]] | Rallies stakeholder support for risky releases; coaches the team to ship quality; builds a **quality-first culture** on the team. |
| [[Director and VP of Product\|VP]] | Ensures the org ships product that's an *asset, not a liability* to strategy; builds a company-wide quality-first culture. |

> [!tip] The culture shift is the senior unlock
> Notice the jump. Junior levels *do* quality: they QA a feature, triage bugs. Senior levels *create the conditions* for quality through coaching, stakeholder cover for risky calls, and ultimately a culture where the team takes pride in the bar without being told. That shift from doing to culture-building is the real promotion.

## How to grow it

- **Define the quality bar *before* you build, in the [[Writing PRDs and Specs|spec]].** What error states are acceptable? What devices are launch-blocking? Deciding this under deadline pressure guarantees you'll cut the wrong corner.
- **Get fluent in severity triage.** Not every bug is a blocker. A PM who can't separate "embarrassing but rare" from "dangerous and common" either ships junk or never ships. This is [[Risk Identification and Mitigation|impact × likelihood]] applied to bugs.
- **Own it out loud when you ship a miss.** Accountability is in the behavior for a reason. The PMs who hide quality misses lose trust far faster than the ones who say "that was my call, here's the fix."
- **Steal a principle.** [[theScore Product Principles|"We win with fans"]] is a quality bar in disguise: painkillers over vitamins, the fan at the core. A sharp product principle does more for day-to-day quality than any checklist.

## How AI is changing it

Quality is being redefined for AI products in a way that does not apply to deterministic software. When the same input can produce different outputs, "bug-free" stops being a coherent bar, because you cannot enumerate correct behavior. The replacement is **evals**. OpenAI's Kevin Weil has called writing them a core skill for product managers, the new equivalent of unit tests. Quality for a probabilistic feature means defining what good looks like in a rubric, building a golden dataset, and measuring against it, while accepting that you will never promise zero hallucinations, only reliability designed *around* them. In my view this is the most consequential shift to this competency in the whole model. See [[Writing Evals for AI Products]] and [[Designing for Trust and Probabilistic Systems]].

## Continue Reading
- [[Sound Product Decision-Making]] for the first behavior: qual + quant, reversible vs irreversible, owning the call.
- [[Risk Identification and Mitigation]] for the second behavior: classify, contingency, communicate, monitor.
- [[The Impact-Likelihood Matrix]] for the 2×2 behind both behaviors.
- [[Writing Evals for AI Products]] for what the quality bar becomes for probabilistic systems.
