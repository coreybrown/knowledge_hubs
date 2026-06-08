---
tags: [ai, modern-pm, evals, quality, evaluation]
aliases: [Writing Evals for AI Products, Evals, AI Evals, Writing Evals]
domain: AI and the Modern PM
---

# Writing Evals for AI Products

If you read one note in this domain, read this one. Evals are the most-emphasized new PM skill of the AI era, and I'll go further than most: **evals are the new PRD.** When you build on a probabilistic system, the document that defines "what good looks like" is no longer a spec of features — it's a set of tests that decide whether the output is acceptable. Writing those tests is product work, and it's now table stakes.

## Why this is a PM skill, not an ML skill

OpenAI's CPO **Kevin Weil** said it directly: *"Writing effective evals is becoming a core skill for product managers."* His analogy is unit tests — but for product quality instead of code correctness. I'd frame the deeper point this way:

> [!tip] Evals are product thinking made executable
> An eval is the operational form of the question "what does good look like?" — which is the question PMs have always owned. Reforge makes the same case: defining the rubric *is* defining the product. You're not delegating quality to ML; you're encoding your [[Product Sense and Judgment|judgment]] about quality into something measurable. That's the most PM thing imaginable.

This is why I say evals replace the PRD as the central artifact. The PRD answered "what are we building?" The eval answers "is what we built any good?" — and for a non-deterministic system, that's the harder and more valuable question.

## The anatomy of an eval system

| Piece | What it is | PM's job |
|---|---|---|
| **Golden set** | A curated set of representative inputs with known-good outputs | Choose the cases that matter; cover the [[The 70% Problem\|edge cases]] |
| **Offline evals** | Run the golden set before shipping | Define pass/fail thresholds |
| **Online evals** | Measure quality on real production traffic | Decide what to log and watch |
| **Traces** | The full record of a single run (inputs, steps, output) | Read them — this is where you find real failures |
| **LLM-as-judge** | A model grading outputs against your rubric | Write the rubric + few-shot examples |

On **LLM-as-judge**: when outputs aren't simple right/wrong (summaries, tone, helpfulness), you use a model to grade them against a rubric you write, anchored with a few graded examples. Aakash Gupta has good material on getting the judge to agree with human raters — and that calibration is itself the work. A judge that disagrees with your taste is worse than no judge.

## How to start (my actual playbook)

1. **Write the golden set first** — before building, collect 20–50 real inputs your product must handle, including the nasty edge cases. This *is* discovery.
2. **Define "good" explicitly** — a rubric a stranger could apply. If you can't write it down, you don't know what you're building.
3. **Run offline, set a bar** — what pass rate ships? That's a product decision, not an engineering one.
4. **Instrument online** — log traces, sample production, watch the rate drift as inputs evolve.
5. **Read the failures by hand** — every week. The aggregate number hides the insight; the individual trace contains it.

This connects straight to existing competency: the discipline is the same as [[Experimentation and A-B Testing]] and [[Hypothesis-Driven Development]] — clear hypothesis, valid measurement, act on the result — applied to model quality instead of feature impact.

## Evals as competitive moat

> [!note] The strategic angle
> Reforge's sharpest claim: your eval framework can be your **product's competitive advantage.** Anyone can call the same model. What they can't copy is your accumulated, domain-specific definition of "good" — your golden set and rubrics encode real understanding of your users' problem. The eval suite is proprietary judgment, compounding over time. That's a moat. Build it deliberately.

> [!warning] Don't fake it with vibes
> "We tried it and it seemed good" is not an eval. Spot-checking the demo case while ignoring the long tail is how AI features pass review and then embarrass you in production. If there's no golden set and no rubric, there's no eval — there's hope. Hope is not a quality strategy.

## Continue Reading
- [[The PM's AI Literacy]] — interviewing the model feeds the golden set.
- [[Experimentation and A-B Testing]] — the measurement discipline evals extend.
- [[Building AI Products]] — the eval-driven development loop in full.
- [[The 70% Problem]] — why edge cases dominate the eval set.
- [[Product Quality]] — the competency evals now operationalize.
- [[Designing for Trust and Probabilistic Systems]] — evals as a trust mechanism.
