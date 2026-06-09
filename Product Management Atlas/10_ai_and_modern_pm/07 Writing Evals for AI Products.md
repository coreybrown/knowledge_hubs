---
tags: [ai, modern-pm, evals, quality, evaluation]
aliases: [Writing Evals for AI Products, Evals, AI Evals, Writing Evals]
domain: AI and the Modern PM
---

# Writing Evals for AI Products

If you read one note in this domain, read this one. Evals are the new PM skill I push hardest on, and I'll go further than most: **evals are the new PRD.** When you build on a probabilistic system, the thing that defines what good looks like stops being a list of features. It becomes a set of tests that decide whether the output is acceptable. Writing those tests is product work, and these days it is table stakes.

Before that lands as overstatement, let me reconcile it, because the two artifacts are partners, not rivals. A PRD (or an AI PRD) still describes the intent: who the user is, what job you are solving, what you mean to build. The evals prove the behavior: whether the thing you shipped actually does that job well. The PRD says what you are aiming at. The evals tell you whether you hit it. You want both. Evals raise the PRD's importance, they do not delete it.

## Why this is a PM skill, not an ML skill

Kevin Weil, OpenAI's CPO, has said about as plainly as you can that writing effective evals is becoming a core skill for product managers. His analogy is unit tests, except the thing you are testing is product quality rather than code correctness. Here is how I'd frame the deeper point.

> [!tip] Evals are product thinking made executable
> An eval is the operational form of the question "what does good look like?", and that question has always belonged to PMs. Reforge makes the same case: defining the rubric is how you define the product. You aren't delegating quality to ML. You are taking your [[Product Sense and Judgment|judgment]] about what counts as good and encoding it into something you can measure. I struggle to think of anything more PM than that.

That is what I mean when I call evals the new central artifact. The PRD answered the question of what we are building. The eval answers whether what we built is any good, and for a non-deterministic system, that second question is both harder and worth more.

## The anatomy of an eval system

| Piece | What it is | PM's job |
|---|---|---|
| **Golden set** | A curated set of representative inputs with known-good outputs | Choose the cases that matter; cover the [[The 70% Problem\|edge cases]] |
| **Offline evals** | Run the golden set before shipping | Define pass/fail thresholds |
| **Online evals** | Measure quality on real production traffic | Decide what to log and watch |
| **Traces** | The full record of a single run (inputs, steps, output) | Read them, because this is where the real failures live |
| **LLM-as-judge** | A model grading outputs against your rubric | Write the rubric + few-shot examples |

A word on **LLM-as-judge**. When the output isn't a clean right or wrong (summaries, tone, helpfulness), you have a model grade it against a rubric you write, anchored with a few graded examples. Aakash Gupta has good material on getting the judge to agree with human raters, and that calibration is itself the work. A judge that disagrees with your taste is worse than no judge at all.

## How to start (my actual playbook)

1. **Write the golden set first.** Before you build anything, collect 20 to 50 real inputs your product has to handle, including the nasty edge cases. This is discovery, full stop.
2. **Define "good" explicitly.** Write a rubric a stranger could apply. If you can't get it onto the page, you don't yet know what you're building.
3. **Run offline and set a bar.** What pass rate ships? That's a product decision, not an engineering one, and it's yours to make.
4. **Instrument online.** Log traces, sample production, and watch the rate drift as the inputs evolve in the wild.
5. **Read the failures by hand, every week.** The aggregate number hides the insight. The individual trace is where you find it.

This connects straight back to a competency you already have. The discipline is the same one behind [[Experimentation and A-B Testing]] and [[Hypothesis-Driven Development]]: clear hypothesis, valid measurement, act on the result. You're just pointing it at model quality instead of feature impact.

## Evals as competitive moat

> [!note] The strategic angle
> Reforge's sharpest claim is that your eval framework can become your **product's competitive advantage.** Anyone can call the same model you call. What they can't copy is your accumulated, domain-specific definition of good. Your golden set and your rubrics encode a real understanding of your users' problem, and that understanding compounds the longer you run. The eval suite is proprietary judgment, and that is a genuine moat. Build it on purpose.

> [!warning] Don't fake it with vibes
> "We tried it and it seemed good" is not an eval. Spot-checking the demo case while ignoring the long tail is exactly how an AI feature sails through review and then embarrasses you in production. If there's no golden set and no rubric, you don't have an eval. You have hope, and hope is not a quality strategy.

## Continue Reading
- [[The PM's AI Literacy]] for how interviewing the model feeds the golden set.
- [[Experimentation and A-B Testing]] for the measurement discipline evals extend.
- [[Building AI Products]] for the eval-driven development loop in full.
- [[The 70% Problem]] for why edge cases dominate the eval set.
- [[Product Quality]] for the competency evals now operationalize.
- [[Designing for Trust and Probabilistic Systems]] for evals as a trust mechanism.
