---
tags: [foundations, cagan, four-risks, value, viability]
aliases: [The Four Big Product Risks, The Four Risks, Cagan's Four Risks]
domain: Foundations of the Craft
---

# The Four Big Product Risks

If you internalize one framework from this entire domain, make it this one. Marty Cagan's **four big product risks** are the cleanest model I know of *what a product team is actually managing* — and, crucially, *who owns what.* Every product that fails, fails on at least one of these four. Every product decision is a bet across all four. And the reason the PM job exists at all is that someone has to hold the two risks no one else is accountable for. Cagan's framing, my conviction.

## The four risks

> [!quote] Cagan's four big risks
> Before you build anything, you face four questions. Most teams answer one and ship — then discover the hard way which of the other three killed them.

| Risk | The question | Owner | Killed by |
|---|---|---|---|
| **Value** | Will customers *want* it — enough to buy, switch, or keep using it? | **PM** | Building something nobody needs |
| **Usability** | Can users figure out *how* to use it? | **Design** | A great idea no one can operate |
| **Feasibility** | Can we *build* it, with the time, skills, and tech we have? | **Engineering** (tech lead) | Overpromising what's buildable |
| **Viability** | Does it work for *our business* — margin, legal, brand, sales, partners? | **PM** | A product users love that the business can't sustain |

## Who owns what — and why it's the PM job

Look at the ownership column. **Usability is design's. Feasibility is engineering's. Value and viability are the PM's** — and that pairing *is* the product management job in one line. It's not arbitrary. Design has the craft to judge usability; engineering has the expertise to judge feasibility; you don't overrule either ([[The Product, Design, and Engineering Venn]]). But value and viability require someone with the *full context* — user insight, market, business model, GTM — and that's the only seat with all of it. So they fall to you.

> [!note] Value is the most-skipped risk
> In my experience, **value is the risk teams most reliably under-test.** It's the hardest to assess (you can't ask users if they'll want something they've never seen and trust the answer) and the most tempting to assume ("of course they'll want it"). [[Continuous Discovery]] exists almost entirely to attack value risk *before* you spend engineering's time on feasibility. Skipping value validation is how you build a beautifully engineered, perfectly usable product that nobody uses.

> [!note] Viability is the most-forgotten risk
> Viability is invisible until it bites: the feature that violates a regulation, torches your unit economics, confuses your brand, undercuts sales, or breaks a partner deal. A PM who only fights for the user and ignores viability isn't a user champion — they're half-doing the job. This is where [[Business Acumen and Models]] and the [[The DHM Model|DHM model]]'s "margin-enhancing" lens live. Loving the user *and* protecting the business is the trade-off only you can make.

## Test risks before you build, not after

The deepest point in Cagan's framing isn't the taxonomy — it's the *sequencing*. **Address these risks in discovery, before you commit to delivery.** The classic, expensive failure is treating all four as build-time problems: you spec it, build it, ship it, and only *then* learn it had no value or wasn't viable. By then you've spent your most expensive resource — engineering time — to learn what a prototype or a few interviews could have told you in a week. This is the whole logic behind separating discovery from delivery while keeping them on *one* team (see [[Product Teams vs Feature Teams]]).

> [!tip] How to use the four risks
> On any meaningful initiative, before building, ask all four out loud and assign each an owner and an evidence level: *do we know, or are we assuming?* The risk you're assuming hardest, with the least evidence, is where your discovery should go first. This turns a vague "let's de-risk it" into a specific, ownable plan — and it dovetails with [[Risk Identification and Mitigation]] for the execution-phase risks that come *after* these four.

## AI adds dimensions, not new risks

For AI products, the four risks still hold — value, usability, feasibility, viability are timeless — but feasibility and viability acquire sharp new edges: *can the model do this reliably?* (a feasibility question with a probabilistic answer) and *does the inference economics work?* (a viability question SaaS never had to ask). More in [[Building AI Products]].

## Continue Reading
- [[Understanding Trade-offs]] — making the call across the four axes when they conflict.
- [[Continuous Discovery]] — the practice built to attack value risk before delivery.
- [[Product Teams vs Feature Teams]] — why discovery and delivery must live on one team.
- [[The Product, Design, and Engineering Venn]] — the ownership split, in picture form.
- [[Business Acumen and Models]] — the business fluency that viability risk demands.
