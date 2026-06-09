---
tags: [frameworks, hypothesis-driven, experimentation, discovery, evidence]
aliases: [Hypothesis-Driven Development, HDD, Hypothesis Driven Development, HDD Framing]
domain: The Frameworks Toolkit
---

# Hypothesis-Driven Development

Hypothesis-driven development (HDD) is less a framework than a *posture*: you stop framing work as "build feature X" and start framing it as "we believe X will produce outcome Y, and here's how we'll know if we're wrong." It's a small change in sentence structure with an outsized effect on behavior, because the moment you commit to *how you'd know you're wrong*, you can no longer hide a failed bet behind a successful launch.

## The hypothesis format I use

> [!note] The structure
> **We believe** [building this / this change]
> **will result in** [this measurable outcome]
> **for** [this user segment].
> **We'll know we're right when** [this metric moves by this much, by this date].
> **We'll know we're wrong when** [the falsifying signal].

The last two lines are the ones that matter, and the ones people drop. A hypothesis you can't *falsify* isn't a hypothesis. It's a wish with a metric stapled to it. "Engagement will improve" is unfalsifiable hand-waving. "Day-7 retention rises from 22% to 27% within four weeks, or we revert" is a real bet with a real loser's condition. Stating the kill criterion *before* you ship is the entire discipline.

## Why the framing changes behavior

> [!tip] It reframes failure as information
> When a feature is a "deliverable," shipping it is success and removing it is admitting defeat, so dead features pile up forever (the [[Outcomes Over Outputs|output trap]]). When a feature is a *hypothesis*, a disproven one is a *successful experiment*: you spent a little, learned the bet was wrong, and freed the resource. HDD makes killing things emotionally and politically survivable, which is the only way teams actually do it. It also forces the [[Product Analytics and Metrics|instrumentation]] conversation up front, because you literally cannot write the hypothesis without naming the metric, so "we forgot to measure it" stops happening.

It also makes prioritization honest. A backlog of *hypotheses* ranked by *how much you'd learn* and *what's at stake* is a far better artifact than a backlog of features ranked by gut. And it exposes the assumptions hiding inside confident roadmaps, because every "obviously we should build X" is really an untested belief, and writing it as a hypothesis drags that belief into the light where it can be checked.

## How it connects

HDD is the connective tissue between several tools. It's the framing layer on top of [[Build-Measure-Learn and the MVP|Build-Measure-Learn]], since the hypothesis *is* the thing the MVP tests. It hands directly to [[Experimentation and A-B Testing|experimentation]], which is the rigorous machinery for *deciding* whether a hypothesis held (clear hypothesis → valid sample → stat-sig read → ship/iterate/sunset). And it's the day-to-day grammar of [[Continuous Discovery|continuous discovery]] and the [[The Opportunity Solution Tree|opportunity solution tree]], where each candidate solution is an assumption to be tested, not a commitment.

| Layer | Role |
|---|---|
| [[Hypothesis-Driven Development\|HDD]] | The *framing*: turn beliefs into falsifiable bets |
| [[Build-Measure-Learn and the MVP\|MVP]] | The *cheapest test* of the hypothesis |
| [[Experimentation and A-B Testing\|Experiment]] | The *rigorous read* on whether it held |

> [!warning] Don't dress up certainty as a hypothesis
> Two cautions. First, not every task deserves a hypothesis. A clear bug fix or a legal requirement isn't a "bet," and wrapping it in hypothesis theater wastes everyone's time. Second, beware the *retrofitted* hypothesis: writing the belief after results are in so the data always "confirms" it. The kill criterion must be set *before* you look. Pre-register the loser's condition or you're just telling yourself a story.

## Continue Reading
- [[Experimentation and A-B Testing]] for the rigorous machinery that decides whether a hypothesis held.
- [[Build-Measure-Learn and the MVP]] because the MVP is the cheapest test of a hypothesis.
- [[Continuous Discovery]] for where treating solutions as assumptions becomes a weekly habit.
- [[Outcomes Over Outputs]] for why hypothesis-framing is the cure for the feature-factory output trap.
- [[The Frameworks Toolkit]] for the full index of tools and when each earns its place.
