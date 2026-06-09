---
tags: [ai, modern-pm, building, probabilistic, anthropic]
aliases: [Building AI Products, How to Build AI Products, Building with AI]
domain: AI and the Modern PM
---

# Building AI Products

Building an AI product is not building a SaaS product with a chatbot stapled on. The underlying system behaves differently. It's probabilistic rather than deterministic, and that one difference reaches all the way up into how you plan, demo, and decide. This note is the build philosophy. The specific failure-mode design lives in [[Designing for Trust and Probabilistic Systems]].

## The core mental shift: probabilistic, not deterministic

In traditional software, the same input produces the same output, always, and your entire QA mental model leans on that fact. AI breaks it: **the same input can produce different outputs.** Aakash Gupta describes this as a completely different way of thinking, and I'd go a step further. It isn't a harder version of the old job. It's a different job.

> [!tip] What changes when output is non-deterministic
> - You can't fully test a feature by checking it once. You test a *distribution* of behavior, which is the whole reason for [[Writing Evals for AI Products|evals]].
> - "It worked in the demo" means almost nothing, because the demo was a single sample.
> - Quality is a *rate*, not a binary. "Good 92% of the time" is the unit you reason in.
> - You design for the failure case as a first-class path, not an afterthought ([[Designing for Trust and Probabilistic Systems]]).

## Do the simple thing that works

The most useful build advice I've taken on board comes from Anthropic's product org, by way of **Cat Wu**: do the simple thing that works. The temptation with AI is to over-engineer elaborate scaffolding around the model's current limitations, with complex prompt chains, custom workarounds, and baroque retrieval. Resist it. The model you're building on is, per Mollick, the worst one you'll ever use, so much of that clever scaffolding turns into dead weight the moment the next model ships and just does the thing on its own.

> [!note] Stay model-swap-ready
> Architect so you can swap the underlying model with minimal rework, and don't hard-couple your product to one model's quirks. Capability is improving on a steep curve, and the teams that win treat the model as a replaceable component. They keep their moat in the product layer, in the evals and the data flywheel and the UX, rather than in workarounds for this quarter's weaknesses.

This is also the discipline behind the build-decision ladder (prompt, then context, then RAG, then fine-tune): always reach for the simplest, cheapest lever first. Fine-tuning is never your opening move, and roughly 80% of problems resolve before you ever get there.

## Prototype-first, demos over stand-ups

Anthropic's culture, again per Cat Wu, leans **prototype-first**: build the thing, demo the thing, react to the thing. Demos quietly replace a lot of status meetings. This fits hand-in-glove with [[AI in Prototyping and Delivery|PMs building prototypes]]. When you can produce a working artifact, you should, because a working artifact settles the disagreements that documents only drag out. For a probabilistic system it matters even more, because you can't reason about model behavior in the abstract. You have to see it run.

## The eval-driven build loop

Here's how building an AI feature actually flows. Notice how different it is from the old spec, build, ship line:

| Step | What you do |
|---|---|
| 1. AI PRD | Define the job, the user, and what "good" means |
| 2. Golden dataset | Collect representative inputs + desired outputs |
| 3. Rubric | Write down how to judge quality |
| 4. Build | Prompt, context, or RAG, simplest lever first |
| 5. Trace analysis | Read real runs by hand; find failure patterns |
| 6. Automated evaluators | LLM-as-judge against the rubric; iterate |

This loop is the roadmap for an AI feature. The roadmap isn't a list of features. It's a sequence of quality improvements, each one measured against your evals. Internal benchmarks plus public ones like LM Arena give you a bit of outside calibration to check yourself against.

> [!warning] The over-engineering trap
> Every month I watch a team build a sophisticated agent framework to paper over a limitation that the next model release simply erases. They've spent their innovation budget on scaffolding instead of on the product. Doing the simple thing that works isn't laziness. It's the correct bet on a steep capability curve.

## Continue Reading
- [[Designing for Trust and Probabilistic Systems]] for the failure-mode design layer.
- [[Writing Evals for AI Products]] for the measurement loop at the core of building.
- [[The Unit Economics of AI]] for the cost constraints that shape what you build.
- [[AI in Prototyping and Delivery]] for prototype-first in practice.
- [[The AI Product Manager]] for the role that owns this build process.
- [[Sound Product Decision-Making]] for judgment applied to probabilistic systems.
