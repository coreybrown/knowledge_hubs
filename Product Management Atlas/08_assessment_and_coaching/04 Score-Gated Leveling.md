---
tags: [assessment, leveling, promotion, scoring, governance]
aliases: [Score-Gated Leveling, Numeric Leveling, The Score-Gated Model]
domain: Assessment and Coaching
---

# Score-Gated Leveling

One of the leveling systems I built took a different bet from the behavioral matrix. Instead of holistic judgment, it gated every level on a number. You score across a fixed set of skills, sum it, and the total, plus a few floor rules and a tenure clock, decides which level you qualify for. I have strong, mixed feelings about this approach, and this note is both the mechanics and my honest verdict.

## The mechanics

The system scores two skill groups on the [[The Proficiency Scale\|1-5 scale]] (here labeled Need-to-improve, Minimum, Good, Advanced, Master):

- **Hard skills**: strategic thinking & planning, delivering against goals/KPIs, team management & accountability, reporting & stakeholder management, user science & empathy, data analysis & experimentation, process implementation, requirement & documentation building, market/competitor grasp, innovation & community building, leadership fundamentals.
- **Soft skills**: teamwork & respect, communication, problem solving, efficiency & accuracy, attitude, initiative, time management.

Sum it all into a single number, then apply three kinds of gate.

> [!example] The gating logic
> | Level | Score band | Floor rule | Tenure |
> |---|---|---|---|
> | **APM** | 43-54 | none | none |
> | **PM** | 55-67 | no category below 2 | 1 yr as APM |
> | **SPM** | 68-80 | no category below 3, no required soft skill below 3.5 | 2 yrs as PM |
> | **LPM** | 81+ | no required skill below 4 | 2 yrs as SPM |

Three forces stack. The band is the primary gate: raw total competence. The floor rules tighten as you climb, so at PM you just can't be failing a whole category, and by LPM you can't be merely "Good" at anything that matters. Tenure is additive on top of both, because even a high scorer waits when some judgment only comes from reps.

## Why the floors tighten, and why the tenure gate exists

This is the part of the design I am proudest of. A pure sum lets a PM buy their way up by being spectacular at two things and absent on five. The rising floor closes that loophole. Seniority is not just more skill, it is the elimination of holes. A Senior PM with a glaring gap is a liability precisely because the org now relies on them where they are weak. The tenure clock guards against the other failure mode, the fast learner who scores high before they have seen enough go wrong to have real [[Product Sense and Judgment|judgment]]. You can't cram experience.

## My verdict: numeric gating is a great floor and a terrible ceiling

> [!tip] What numeric gating gets right
> - **Transparency.** Everyone sees the bar. "Why didn't I get promoted" has a concrete, defensible answer instead of a shrug. That kills a huge class of fairness complaints.
> - **Calibration anchor.** A summed score is harder to fudge than a vibe, which dampens [[Common Assessment Pitfalls|halo bias and median-grading]].
> - **Self-service growth.** A PM can see exactly which skills gate their next level and aim at them ([[Identifying Growth Areas]]).

> [!warning] What numeric gating gets wrong
> - **It implies skills are additive and fungible. They aren't.** A 4 in stakeholder management does not offset a 1 in delivery, and yet the score says it does.
> - **It invents precision.** The gap between a 64 and a 66 is noise, but the band makes it a verdict. See [[The Proficiency Scale]] on false precision.
> - **It can become the goal.** The moment people optimize the score instead of the craft, you have built a [[Outcomes Over Outputs|feature factory for performance reviews]], activity dressed up as growth.
> - **It struggles with spiky talent.** The brilliant, lopsided PM the [[The T-Shaped PM and Knowing Your Shape|shape model]] says you want is exactly who the floor rules punish hardest.

So I use the number as a floor and a conversation-starter, never the final call. It is excellent for answering "is this person clearly not ready" and for forcing an honest, transparent bar. It is dangerous as the thing that actually grants a promotion, because that decision belongs to calibrated human judgment ([[Calibration and Promotion]]), with the score as one input. The behavioral [[The Master Competency Matrix|matrix]] and its [[The Proficiency Scale\|0-2 rubric]] carry the nuance the number can't.

> [!note] Pairs with the ladder, not instead of it
> Score bands are a mechanism. They don't define what each level means. That is the job of [[The Product Career Ladder]] and [[What Changes at Each Level]]. The score tells you whether someone clears APM to PM; the ladder tells you what being a PM actually is.

## Continue Reading
- [[Calibration and Promotion]] for why the human call has to sit on top of the number.
- [[The Proficiency Scale]] for the 1-5 scale the score is built from, and its limits.
- [[Common Assessment Pitfalls]] for the biases numeric gating dampens, and the ones it creates.
- [[The Product Career Ladder]] for what the levels the score gates actually mean.
- [[Running a Performance Review]] for where a score becomes a leveling decision in practice.
