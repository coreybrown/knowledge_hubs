---
tags: [frameworks, moscow, prioritization, scoping, stakeholders]
aliases: [MoSCoW Prioritization, MoSCoW, Must Should Could Wont, MoSCoW Method]
domain: The Frameworks Toolkit
---

# MoSCoW Prioritization

MoSCoW is the framework I reach for when I'm **scoping a release** or negotiating with stakeholders about what makes the cut — not when I'm ranking a whole backlog. It sorts work into four commitment buckets: **Must have, Should have, Could have, Won't have** (the two o's are just there to make it pronounceable). Dai Clegg created it at Oracle in the 1990s, and it lives at the heart of agile/DSDM scoping.

Its strength is that it's **plain language anyone can use.** You don't need to explain a scoring formula to a sales lead or an exec — "is this a Must or a Should for the March release?" is a question any stakeholder can answer and argue about productively. That shared vocabulary is the whole value.

> [!note] The four buckets
> **Must have:** Non-negotiable for *this* release. If it slips, the release has failed or shouldn't ship. Test: would you delay launch for it? If no, it's not a Must.
> **Should have:** Important and painful to omit, but the release survives without it. There's a workaround, even an ugly one.
> **Could have:** Nice to have. First to be cut when time runs short. The buffer.
> **Won't have (this time):** Explicitly *out of scope* — and naming it is the most underrated move in the method. A documented "not now" kills the scope creep that comes from things drifting in unsaid.

## The discipline is the timebox

> [!tip] Cap your Musts — roughly 60% of effort
> The DSDM convention is that **Musts should be no more than ~60% of the release's effort**, leaving headroom in Shoulds and Coulds to absorb the inevitable overruns. This is the part that makes MoSCoW actually work and the part everyone skips. Without an effort cap, the method degrades instantly — see the warning below. MoSCoW only delivers when it's tied to a fixed timebox: *given this release window, what's Must versus Should?* Untethered from a deadline, the buckets are meaningless.

## When it fits and when it doesn't

MoSCoW is for **release scoping and stakeholder negotiation** — carving a fixed time window into commitment tiers. It is genuinely good at that and good at managing expectations: stakeholders feel heard because their item is a "Should," and you've still protected the launch. Pair it with [[The Impact-Likelihood Matrix|Impact-Likelihood]] (to triage the portfolio *before* scoping a release) and with [[The 10-50-90 Execution Framework|10/50/90]] (the scope you commit to at each confidence checkpoint).

It is *not* a ranking tool. It won't tell you the order of work *within* the Musts, and it has no notion of impact magnitude or effort beyond the bucket. For ranking, use [[RICE and Scoring Models|RICE]]; for *what kind* of value, [[The Kano Model|Kano]] (note the rough rhyme: Kano basics tend to be Musts, delighters tend to be Coulds).

> [!warning] The "everything is a Must" death spiral
> The universal failure mode: stakeholders, sensing that "Must" is the only bucket that guarantees their thing ships, push everything into it. Soon 90% of the release is Musts, the method is dead, and you're back to no prioritization at all. The cure is the **effort cap** above, plus a hard rule I enforce: a Must requires a *named consequence* of omission. "Important" isn't a Must. "Launch is illegal / unusable / pointless without it" is. Force the justification and the list shrinks fast.

## Continue Reading
- [[Prioritization Frameworks]] — where MoSCoW sits among the methods and the altitude it fits.
- [[The Kano Model]] — Kano basics ≈ Musts, delighters ≈ Coulds; complementary lenses.
- [[The 10-50-90 Execution Framework]] — the scope you commit to at each confidence checkpoint.
- [[Building and Managing a Roadmap]] — release scoping in the context of the broader roadmap.
- [[The Frameworks Toolkit]] — the full index of tools and when each earns its place.
