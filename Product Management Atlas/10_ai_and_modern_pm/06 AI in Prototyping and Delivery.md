---
tags: [ai, modern-pm, prototyping, vibe-coding, delivery]
aliases: [AI in Prototyping and Delivery, Vibe Coding for PMs, AI Prototyping]
domain: AI and the Modern PM
---

# AI in Prototyping and Delivery

This is the change that surprised me most, because it ran the opposite direction from the consensus. For a decade the PM job moved away from building. We wrote docs, others built. AI reversed it. Atlassian caught the shift in a single line, that AI turns product managers back into builders, and I think it is the most exciting change in the whole domain. I stopped writing documents about prototypes and started shipping the prototypes.

## Vibe coding and the tool stack

"Vibe coding," describing what you want in natural language and letting an AI build it, went from a meme to a daily PM workflow in about a year. The tools are good enough now that a PM with taste and no formal CS background can produce a working, clickable, sometimes shippable artifact. Here is how I think about the stack:

| Tool | Best for | Where it fits |
|---|---|---|
| **v0** | React/UI generation from a prompt | Fast interface mockups |
| **Lovable** | Full-stack MVPs; PM/designer-friendly | Clickable end-to-end concept |
| **Bolt / Replit** | Browser-based full apps | Build-and-host without local setup |
| **Cursor** | Graduating a prototype into a real repo | When eng needs to take it forward |

The progression is real: rough it in v0 or Lovable, validate the concept, then move to Cursor when it is worth making real. You do not need all of them. You need one you are fluent in.

> [!tip] Prototyping is a skill, not a party trick
> Aakash Gupta is right that vibe coding is a skill with technique, not random prompting until something works. The technique is the same product muscle as always: clear intent, tight scope, knowing what you are testing. A bad prompter produces a bad prototype the same way a bad spec produces a bad feature. AI raised the ceiling. It did not remove the craft.

## Why this matters more than it sounds

A prototype is the highest-bandwidth spec ever invented. Showing a working thing collapses an entire cycle of "did you mean it like *this*?" Engineers, designers, and executives align on a clickable artifact in minutes where a document would take a week of back-and-forth. This is [[Feature Specification]] reaching its logical endpoint: the deliverable was always *shared understanding*, and nothing creates shared understanding like a thing you can touch.

It also attacks the [[The Four Big Product Risks|value and usability risks]] directly, because you can put a real artifact in front of a user during discovery instead of describing it. Prototype-first is becoming the default in AI-native teams. Anthropic's product org, per Cat Wu, leans on demos over status meetings (more in [[Building AI Products]]).

## Spec-driven development

The flip side of "PMs build" is a tightening of how intent flows to code. **Spec-driven development**, where GitHub's Spec Kit (Sept 2025) is the visible example, treats intent as the source of truth. You write a precise spec, the AI generates code *from* it, and the spec, not the code, is the artifact you maintain. Addy Osmani has written on what makes a spec good enough to drive this. It is the same competency I have always pushed, with higher stakes on precision: vague intent now produces vague software automatically.

> [!warning] The prototype is not the product
> A vibe-coded prototype is a *learning tool*, not production software. It skips error handling, security, scale, and edge cases, which is exactly the territory of [[The 70% Problem]]. Treat it as a question you are asking, not an answer you are shipping. The danger is an executive seeing a slick demo and assuming it is two days from launch. It is not. Manage that expectation explicitly.

## Continue Reading
- [[The 70% Problem]] for why the prototype's last 30% is the hard part.
- [[Feature Specification]] for the competency prototyping extends and partly replaces.
- [[Building AI Products]] for prototype-first as a build philosophy.
- [[The Four Big Product Risks]] for the risks a prototype lets you test early.
- [[The PM Tool Landscape]] for where these tools fit the broader kit.
- [[Build-Measure-Learn and the MVP]] for the loop prototyping accelerates.
