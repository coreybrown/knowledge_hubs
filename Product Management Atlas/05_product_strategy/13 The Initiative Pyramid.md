---
tags: [product-strategy, initiative-pyramid, risk, governance]
aliases: [The Initiative Pyramid, Initiative Pyramid, Initiative Risk Pyramid]
domain: Product Strategy
---

# The Initiative Pyramid

The Initiative Pyramid is a deceptively simple model that solves a real organizational problem: *how much should senior leadership be involved in any given product decision?* Get it wrong and you either bottleneck everything through executives (slow, demoralizing) or let a high-risk bet sail through with no oversight (reckless). The model comes from **Curtis Stanier**, and it's earned a spot in my toolkit because it gives a principled answer to a question most orgs handle by gut feel and politics.

> [!quote] Attribution
> The Initiative Pyramid as presented here is **Curtis Stanier's** framework. I'm applying it to how I think about decision rights and senior involvement.

## The core idea: risk and quantity are inversely related

Picture a pyramid. The vertical axis is **risk** (and impact); the horizontal width at any level is the **number of initiatives** at that risk level.

- **At the top:** a *few* very high-risk, high-impact initiatives. Big bets. Rare.
- **At the bottom:** *many* low-risk, low-impact initiatives. Routine work. Constant.

The shape encodes a truth about healthy product orgs: you should have a small number of company-defining bets and a large volume of everyday improvements. If your pyramid is inverted, with dozens of "bet the company" initiatives running at once, you don't have a strategy, you have chaos, and you've violated the first principle of [[Product Strategy|strategy]]: deciding what *not* to do.

## The real payoff: matching senior involvement to risk

Here's where the model earns its keep. Senior-leadership involvement should scale with risk, moving along a spectrum from **consulted** to **informed**:

| Level | Risk / impact | # of initiatives | Senior leadership is... | Decision rights |
|---|---|---|---|---|
| **Top** | Very high | Few | **Consulted**: actively involved, weigh in before commitment | Leadership co-owns the call |
| **Middle** | Moderate | Some | Reviewed: kept in the loop, light approval | PM owns, leadership aware |
| **Bottom** | Low | Many | **Informed**: told after the fact, if at all | PM/team decides autonomously |

The principle is simple: **a few high-risk initiatives mean you consult senior leaders, and many low-risk initiatives mean you merely inform them.** This is the same governance logic I apply through [[RACI and Decision Rights|RACI]], just resolved by *risk altitude* rather than by function. A new payments integration that could expose the company to regulatory risk? Top of the pyramid, so consult the execs early. A copy tweak on a settings page? Bottom, so ship it and maybe mention it in the weekly update.

> [!warning] The myth: more executive oversight is safer
> Routing every decision through senior leadership feels prudent and is actually corrosive. It bottlenecks delivery, signals distrust of the team, and, worst of all, *dilutes* executive attention so the genuinely high-risk bets get the same cursory glance as the trivial ones. The goal isn't maximum oversight; it's *calibrated* oversight. Leaders should be deeply involved in the few things that matter and absent from the many that don't.

## Why I find it useful

Two reasons. First, it's a **prioritization and focus tool in disguise**, because it forces you to classify initiatives by risk, which immediately exposes whether you have too many big bets in flight (you usually do). It pairs naturally with [[The Impact-Likelihood Matrix]]: the pyramid's top is essentially that matrix's "Strategic Initiatives" and "Home Runs," and its base is "Housekeeping."

Second, it's a **communication and [[Managing Up|managing-up]] tool.** It gives me a clean way to set expectations with executives: *here are the three initiatives I need you in the room for, and here's everything else I'm just keeping you informed on.* That earns autonomy on the routine work by *demonstrating* good judgment about when to escalate, which is exactly how a senior PM builds the trust that lets them operate without a manager hovering. It also dovetails with the [[The 10-50-90 Execution Framework|10/50/90]] checkpoints: the higher up the pyramid, the more seriously you treat each confidence gate.

## How it scales by level

The pyramid looks different depending on where you sit. An [[Associate Product Manager|APM]] mostly lives at the base: low-risk initiatives, autonomy with manager awareness. A [[Senior Product Manager|Senior PM]] owns initiatives across the middle and occasionally the top, and is *consulted* on the org's big bets. A [[Director and VP of Product|Director or VP]] *is* the senior leadership being consulted, so their job is to be present for the apex bets and to deliberately stay out of the base so the teams own it. Reading the pyramid is partly about knowing which tier of decisions belongs to your level.

## How AI is changing it

AI doesn't alter the governance principle, but it shifts where the line sits, and it adds a new high-risk category. Routine, low-risk work that used to need a human gate (basic prioritization, content tweaks, standard analyses) increasingly runs with AI assistance and lighter oversight, widening the autonomous base. Meanwhile a *new* class of apex initiatives appears: probabilistic AI systems in high-stakes flows carry risks (hallucination, trust, [[AI Ethics and Governance|governance]]) that genuinely warrant senior consultation. The judgment that stays human is the *risk classification itself*, and deciding which initiative belongs at the top is, fittingly, the kind of call that sits near the top of the pyramid.

## Continue Reading
- [[RACI and Decision Rights]] is the functional cousin: who's Responsible, Accountable, Consulted, Informed.
- [[The Impact-Likelihood Matrix]] is the 2×2 that maps cleanly onto the pyramid's tiers.
- [[Managing Up]] for using the pyramid to set executive-involvement expectations and earn autonomy.
- [[Prioritization Frameworks]] for the pyramid as a focus tool that limits how many big bets run at once.
- [[The 10-50-90 Execution Framework]] for confidence checkpoints that intensify higher up the pyramid.
