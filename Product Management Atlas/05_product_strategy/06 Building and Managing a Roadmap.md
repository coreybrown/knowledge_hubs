---
tags: [product-strategy, roadmap, prioritization, communication]
aliases: [Building and Managing a Roadmap, Roadmapping, Product Roadmap]
domain: Product Strategy
---

# Building and Managing a Roadmap

A roadmap is the most over-promised, under-delivered artifact in product. Built well, it's the strategy made visible — a living statement of what matters and in what order. Built badly, it's a Gantt chart of dated feature promises that turns the PM into a project manager forever defending slipped dates. This note is the version I actually run.

## The roadmap is not a release schedule

The single most important reframe: a roadmap communicates **intent and priority**, not delivery dates. The moment a roadmap becomes a list of features-by-date, three bad things happen — every estimate hardens into a commitment, learning gets punished as "missing the plan," and the conversation moves from *what's worth building* to *why is this late.* This is the [[Product Vision and Roadmapping]] behavior in practice: translate strategy into an **outcome-focused** roadmap, not a schedule.

> [!warning] The myth: a roadmap is a contract
> Stakeholders want dates and will pressure you for them. Giving precise dates for work you haven't started is the fastest way to lose credibility — because you'll miss them, and you'll have taught everyone that your roadmap is a promise you break. A roadmap is a statement of priority that gets *more* certain as work gets closer, not a contract signed in ink a year out.

## Now / Next / Later — the format I default to

I organize roadmaps by **time horizon and confidence**, not by calendar quarter. Three buckets:

| Bucket | Confidence | What it contains | Granularity |
|---|---|---|---|
| **Now** | High | Committed, in flight | Specific features, near-dates OK |
| **Next** | Medium | Strongly likely, sequenced | Initiatives, no hard dates |
| **Later** | Low / directional | Bets we believe in | Themes and outcomes, no dates |

The genius of Now/Next/Later is that it makes the *uncertainty honest.* Nobody is surprised when a "Later" item shifts — it was always directional. And it tells the truth about how product actually works: near-term work is concrete, far-term work is a bet. The further out, the more it should be expressed as an **outcome** ("grow activated users") rather than a feature ("ship onboarding v3"), because you shouldn't pre-commit to a solution for a problem you haven't fully discovered yet ([[Continuous Discovery]]).

## Communicating to execs vs teams — two different roadmaps

The same underlying roadmap needs two presentations, and conflating them is a common failure. The [[Product Vision and Roadmapping]] behavior calls this "tailor communication to the audience," and here's what that means concretely:

- **For executives** ([[Executive Communication]]): lead with **outcomes and bets**. Which numbers move, which strategic problems get solved, where the risk sits. They don't want the feature list; they want to know the resources are pointed at the right business problems. Frame it in terms tied to KPIs and the [[Business Acumen and Models|business model]].
- **For the team** ([[Cross-Functional Collaboration]]): lead with **the next two horizons of work** — what we're building now, what's coming next, and the *why* behind the sequence so engineers and designers can make good local trade-offs.

Same priorities, two altitudes. An exec roadmap full of feature names signals you're operating below your level; a team roadmap that's all themes and no concrete work signals you haven't done the [[Feature Specification|specification]].

## Saying no to dates (without saying "no")

You can't refuse to give stakeholders *any* sense of timing — that reads as evasive. What I do instead: give **ranges that widen with distance** and tie them to confidence. "This quarter" for Now, "next quarter, roughly" for Next, "we believe this is a 2027 bet" for Later. And I always pair a date question with the trade-off: *"I can commit to X by then if we drop Y — which do you want?"* That converts a date demand into a [[Understanding Trade-offs|prioritization]] conversation, which is where it belongs. The discipline of [[Prioritization Frameworks|saying no]] is what protects the roadmap from becoming everyone's wish list.

## Managing it: a roadmap is a verb

The "Management" in the title is the part that gets neglected. A roadmap is reviewed and adjusted continuously while *preserving intent* — same idea as evolving a vision. I revisit it on a regular cadence ([[Agile Delivery and Team Cadence]]), move items between horizons as confidence changes, and re-communicate when something material shifts. The thing I guard against is whiplash: changing direction every time a loud stakeholder appears teaches the team the roadmap is meaningless. Change it for *evidence*, not for volume.

## How AI is changing it

The mechanical parts of roadmapping — formatting, generating the exec-vs-team versions, drafting the rationale, summarizing changes for stakeholders — are increasingly one-prompt jobs, and that's a genuine time win. What AI doesn't touch is the *sequencing judgment* and the *political work* of holding a controversial roadmap. A model can render a Now/Next/Later board; it can't decide that you'll starve a popular feature to fund a risky bet, or absorb the heat from the stakeholder whose pet project landed in "Later." Use AI to kill the busywork of maintaining the artifact so you spend your time on the choices and the conversations — the parts that were always the actual job.

## Continue Reading
- [[Crafting a Product Vision]] — the layer above the roadmap; where its direction comes from.
- [[Prioritization Frameworks]] — how to decide what lands in Now vs Next vs Later.
- [[Outcomes Over Outputs]] — why far-horizon roadmap items should be outcomes, not features.
- [[Executive Communication]] — presenting the roadmap upward in business terms.
- [[The Initiative Pyramid]] — matching senior-leadership involvement to the risk of each bet on the roadmap.
