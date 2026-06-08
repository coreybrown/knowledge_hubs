---
tags: [ai, modern-pm, building, probabilistic, anthropic]
aliases: [Building AI Products, How to Build AI Products, Building with AI]
domain: AI and the Modern PM
---

# Building AI Products

Building an AI product is not building a SaaS product with a chatbot stapled on. The underlying system behaves differently — it's probabilistic, not deterministic — and that difference reaches all the way up into how you plan, demo, and decide. This note is the build philosophy; the specific failure-mode design lives in [[Designing for Trust and Probabilistic Systems]].

## The core mental shift: probabilistic, not deterministic

In traditional software, the same input produces the same output. Always. Your entire QA mental model assumes it. AI breaks that: **the same input can produce different outputs.** Aakash Gupta calls this "a completely different way of thinking," and he's right — it's not a harder version of the old job, it's a different one.

> [!tip] What changes when output is non-deterministic
> - You can't fully test a feature by checking it once; you test a *distribution* of behavior — hence [[Writing Evals for AI Products|evals]].
> - "It worked in the demo" means almost nothing; the demo was one sample.
> - Quality is a *rate*, not a binary. "Good 92% of the time" is the unit you reason in.
> - You design for the failure case as a first-class path, not an exception ([[Designing for Trust and Probabilistic Systems]]).

## Do the simple thing that works

The most useful build advice I've internalized comes from Anthropic's product org, via **Cat Wu**: **"do the simple thing that works."** The temptation with AI is to over-engineer elaborate scaffolding around the model's current limitations — complex prompt chains, custom workarounds, baroque retrieval. Resist it. The model you're building on is, per Mollick, the worst one you'll ever use. Much of your clever scaffolding becomes dead weight the moment the next model ships and just *does the thing*.

> [!note] Stay model-swap-ready
> Architect so you can swap the underlying model with minimal rework. Don't hard-couple your product to one model's quirks. Capability is improving on a steep curve; the teams that win treat the model as a replaceable component and keep their moat in the *product* layer — the evals, the data flywheel, the UX — not in workarounds for today's weaknesses.

This is also the discipline behind the build-decision ladder (prompt → context → RAG → fine-tune): always reach for the simplest, cheapest lever first. Fine-tuning is never your opening move; roughly 80% of problems resolve before you get there.

## Prototype-first, demos over stand-ups

Anthropic's culture, again per Cat Wu, leans **prototype-first**: build the thing, demo the thing, react to the thing. Demos replace a lot of status meetings. This fits perfectly with [[AI in Prototyping and Delivery|PMs building prototypes]] — when you can produce a working artifact, you should, because a working artifact resolves disagreement that documents only prolong. For a probabilistic system this matters even more: you can't reason about model behavior in the abstract. You have to see it.

## The eval-driven build loop

Here's how building an AI feature actually flows, and notice how different it is from a feature spec → build → ship line:

| Step | What you do |
|---|---|
| 1. AI PRD | Define the job, the user, and what "good" means |
| 2. Golden dataset | Collect representative inputs + desired outputs |
| 3. Rubric | Write down how to judge quality |
| 4. Build | Prompt / context / RAG — simplest lever first |
| 5. Trace analysis | Read real runs by hand; find failure patterns |
| 6. Automated evaluators | LLM-as-judge against the rubric; iterate |

This loop *is* the roadmap for an AI feature. The roadmap isn't a list of features; it's a sequence of quality improvements measured against evals. Internal benchmarks plus public ones like LM Arena give you outside calibration.

> [!warning] The over-engineering trap
> Every month I see teams build a sophisticated agent framework to compensate for a limitation that the next model release simply erases. They've spent their innovation budget on scaffolding instead of on the product. "Do the simple thing that works" is not laziness — it's the correct bet on a steep capability curve.

## Continue Reading
- [[Designing for Trust and Probabilistic Systems]] — the failure-mode design layer.
- [[Writing Evals for AI Products]] — the measurement loop at the core of building.
- [[The Unit Economics of AI]] — the cost constraints that shape what you build.
- [[AI in Prototyping and Delivery]] — prototype-first in practice.
- [[The AI Product Manager]] — the role that owns this build process.
- [[Sound Product Decision-Making]] — judgment applied to probabilistic systems.
