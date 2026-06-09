---
tags: [frameworks, prioritization, impact-likelihood, original, portfolio]
aliases: [The Impact-Likelihood Matrix, Impact-Likelihood Matrix, Impact x Likelihood, Impact Likelihood 2x2]
domain: The Frameworks Toolkit
---

# The Impact-Likelihood Matrix

This is my go-to for fast portfolio triage, and it is the one I sketch on a whiteboard more than any other. It is a 2×2: **impact for the company** on one axis, **likelihood of success** on the other, both high or low. Four quadrants, four very different decisions. I built it because most teams either rank everything in a flat list (no shape) or argue endlessly about a single "priority" score that smuggles two distinct questions into one number. Splitting impact from likelihood forces both questions into the open.

The honesty this buys you is the point. A feature can be enormously valuable *and* a long shot. Another can be a near-certain win that barely moves the needle. A flat priority list flattens those into the same bucket. The matrix keeps them apart so you can deliberately balance your portfolio across them.

## The four quadrants

| | High likelihood | Low likelihood |
|---|---|---|
| **High impact** | **Home Runs** | **Strategic Initiatives** |
| **Low impact** | **Housekeeping** | **Stuff You Shouldn't Be Doing** |

> [!note] What each quadrant means, and what to do
> **Home Runs (high impact / high likelihood):** Do these now. Big payoff, and you are confident you can land them. If your roadmap has obvious Home Runs you are not building, stop reading and go fix that.
> **Strategic Initiatives (high impact / low likelihood):** The big bets. High value but uncertain: new markets, hard tech, behavior change. You need some of these or you are just maintaining. Fund them deliberately and de-risk them with [[Build-Measure-Learn and the MVP|cheap experiments]] before betting the quarter.
> **Housekeeping (low impact / high likelihood):** Easy, safe, low value. Bug fixes, small debts, table-stakes upkeep. Necessary in moderation, but a roadmap that is *all* Housekeeping is a [[Product Teams vs Feature Teams|feature factory]] slowly dying.
> **Stuff You Shouldn't Be Doing (low impact / low likelihood):** Unlikely *and* not worth much. The name is the instruction. The fact that someone asked for it is not a reason.

## How I actually use it

> [!tip] Triage first, then go deeper
> This matrix is a **coarse filter**, deliberately. Its job is to separate the big bets from the busywork in five minutes, kill the bottom-right, and show whether your portfolio is dangerously lopsided. It is not precise enough to rank items *within* a quadrant. For that, drop into [[RICE and Scoring Models|RICE]] or [[The Initiative Pyramid]]. I triage with this 2×2, then score the survivors.

The likelihood axis is where it earns its keep over a plain impact/effort grid. Effort is *cost*; likelihood is *risk of failure*, which is a different and often more important question. A low-effort feature that probably will not work is still a bad bet. This maps directly onto how I classify [[Risk Identification and Mitigation|risk]]: impact × likelihood is the same lens, just pointed at opportunities instead of threats.

> [!warning] The dishonest-likelihood trap
> The failure mode is optimism. Everyone rates their pet project "high likelihood" because they want to build it. Likelihood has to be a *cold* estimate grounded in evidence: past results, [[Continuous Discovery|discovery]] signal, technical knowns, not enthusiasm. If every item lands in Home Runs, you are not estimating, you are cheerleading. The empty quadrants are the tell that you are being honest.

One more thing: do not confuse this with the [[The Eisenhower Matrix|Eisenhower matrix]]. That one is urgency × importance for *task* triage. This is impact × likelihood for *portfolio* triage. Same shape, different axes, different job.

## Continue Reading
- [[Prioritization Frameworks]] for where this 2×2 sits among the methods and when to reach for it.
- [[The Initiative Pyramid]] for the next level down: organizing the surviving bets by risk and escalation.
- [[Risk Identification and Mitigation]] for the same impact × likelihood lens applied to threats.
- [[RICE and Scoring Models]] for ranking items *within* a quadrant once triage is done.
- [[The Frameworks Toolkit]] for the full index of tools and when each earns its place.
