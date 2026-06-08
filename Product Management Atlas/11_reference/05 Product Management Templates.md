---
tags: [reference, templates, prd, strategy, growth-plan]
aliases: [Product Management Templates, PM Templates, Templates, Copy-Paste Templates]
domain: Reference
---

# Product Management Templates

Copy-paste skeletons for the artifacts you'll write most. These are *formats*, not laws — the thinking matters more than the headings (see [[Feature Specification]] and [[Writing PRDs and Specs]]). Match the depth to the risk: a low-risk tweak gets a one-pager; a bet-the-quarter initiative gets the full strategy doc. Each template below is meant to be copied into your own doc and filled in.

> [!tip] Steal formats, not templates
> A template is a checklist; a format is a way of thinking. Learn a few, then bend them to the situation. The fastest way to ruin any of these is to fill in every field out of obligation when the work doesn't need it.

## 1. PRD / One-Pager

The one-pager is my default. If a feature can't be framed on a single page, the thinking usually isn't done yet.

```markdown
# [Feature / Initiative Name]
Author · Date · Status (Draft / In Review / Approved) · Stakeholders

## Problem
What user or business problem are we solving? For whom? Why now?
(Evidence: link the research, data, or insight — see Continuous Discovery.)

## Outcome / Success Metric
The ONE number we expect to move, and the target. State this BEFORE the solution.
Guardrail metrics we must not harm:

## Solution (the "what", not the "how")
Brief description of the approach. Link mocks/prototype.

## Scope
User stories + acceptance criteria:
- As a [user], I can [action], so that [value]. AC: ...
Out of scope (explicitly):

## Considerations
- UX:
- Technical / feasibility:
- Data & instrumentation (how we'll measure the outcome):
- Edge cases:
- Risks & mitigations (see Risk Identification and Mitigation):
- Go-to-market (see Shipping and Launch):

## Open Questions
```

## 2. Product Strategy Doc

For an area or product line. This is the "where are we going and why" artifact — see [[Product Strategy]] and [[The DHM Model]].

```markdown
# [Product / Area] Strategy — [Time Horizon]

## Vision
The compelling long-term picture. Where does this win in 3 years?
(see Crafting a Product Vision)

## Context & Insight
- Customer/market truth we're betting on:
- Competitive landscape (see Competitive Landscape Analysis):
- Where we are today (honest baseline):

## Strategy (the DHM test)
- Delight: how does this delight customers?
- Hard-to-copy: what's our durable advantage?
- Margin-enhancing: how does it improve the business model?

## Objectives & Key Results
Objective 1: ...
  KR1: ...  KR2: ...
(see OKRs and Goal-Setting; tie to The North Star Framework)

## Roadmap (outcome-focused, not a dated feature list)
- Now / Next / Later — and the outcome each bet targets.
(see Building and Managing a Roadmap)

## What we're explicitly NOT doing
The "no" list is the strategy. (see Prioritization Frameworks)

## Risks & Assumptions
```

## 3. Growth Plan (3 areas × 3 tasks)

My development-plan format, lifted directly from how I coach: pick the **three lowest competencies**, and give each three concrete, near-term tasks. Don't over-invest in your spikes. See [[Building a Growth Plan]] and [[Identifying Growth Areas]].

```markdown
# Growth Plan — [Name] — [Quarter]
Current level: ___   Target: ___   (assessed via The Competency Self-Assessment)

## Growth Area 1: [lowest competency]
Why this one: [the gap, in one line]
- Small Task 1:
- Small Task 2:
- Small Task 3:
Evidence of progress / how my manager will know it moved:

## Growth Area 2: [second-lowest competency]
Why this one:
- Small Task 1:
- Small Task 2:
- Small Task 3:
Evidence of progress:

## Growth Area 3: [third-lowest competency]
Why this one:
- Small Task 1:
- Small Task 2:
- Small Task 3:
Evidence of progress:
```

## 4. Competency Self-Assessment

A lightweight version of [[The Competency Self-Assessment]]. Score each competency, then look for your shape — not a flat profile. Use the [[The Proficiency Scale|proficiency scale]] (e.g., 1 Knows → 5 Teaches, or the 0–2 Needs Focus / On Track / Outperform rubric).

```markdown
# Self-Assessment — [Name] — [Date]
Scale: 1 Inadequate · 2 Knows (supervised) · 3 Does (unsupervised) · 4 Masters · 5 Teaches/Leads

## Product Execution
- Feature Specification:        __ / 5   Evidence:
- Product Delivery:             __ / 5   Evidence:
- Product Quality:              __ / 5   Evidence:

## Customer Insight
- Fluency with Data:            __ / 5   Evidence:
- Voice of the Customer:        __ / 5   Evidence:
- User Experience Design:       __ / 5   Evidence:

## Product Strategy
- Business Outcome Ownership:   __ / 5   Evidence:
- Strategic Impact:             __ / 5   Evidence:
- Product Vision & Roadmapping: __ / 5   Evidence:

## Influencing People
- Stakeholder Management:       __ / 5   Evidence:
- Team Leadership:              __ / 5   Evidence:
- Managing Up:                  __ / 5   Evidence:

My three spikes:
My three lowest (→ feed the Growth Plan):
```

> [!note] AI does the first draft now
> Tools like ChatPRD will scaffold any of these in seconds, and that's fine — the typing was never the bottleneck. What AI *can't* supply is the judgment in the fields that matter: the problem you chose, the metric you committed to, and the "no" list. Let it draft; you do the thinking. See [[Competencies AI Commoditizes vs Elevates]].

## Continue Reading
- [[Writing PRDs and Specs]] — the craft behind the PRD format, and the anti-patterns.
- [[Building a Growth Plan]] — the full method behind the growth-plan skeleton.
- [[The Competency Self-Assessment]] — the complete assessment, scored against the model.
- [[The Master Competency Matrix]] — what each score *means* at each level.
- [[The PM Tool Landscape]] — where to put these docs and the AI tools that draft them.
