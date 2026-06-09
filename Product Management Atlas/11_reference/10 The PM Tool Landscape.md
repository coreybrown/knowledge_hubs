---
tags: [reference, tools, software, tooling, ai-tools]
aliases: [The PM Tool Landscape, PM Tools, The Tool Landscape, PM Tooling]
domain: Reference
---

# The PM Tool Landscape

The software a PM touches, by category, with the examples worth knowing. I'm deliberately brief on each, because tools are the **easy-to-teach** layer of the craft, the bottom of the [[Character, Competency, and Craft|character → competency → craft → tools]] hierarchy. You can learn Jira in a week; you can't learn judgment in a week. Pick a sensible default in each category, get fluent, and don't mistake tool mastery for the job.

> [!warning] The trap
> Knowing the tools is table stakes, not a differentiator. I've never hired anyone *because* they knew Amplitude, and I've never rejected anyone *because* they didn't. Tools change; the competency they serve doesn't. Optimize for the [[The PM Competency Model|competency]], then pick whatever tool the team already uses.

## Delivery and project tracking

Where work is planned, tracked, and shipped. Serves [[Product Delivery]] and [[Agile Delivery and Team Cadence]].

- **Jira**: the enterprise default; powerful, heavy, infinitely configurable.
- **Linear**: the fast, opinionated favorite of modern product teams.
- **Asana / Trello**: lighter project tracking, common at smaller orgs.

## Roadmapping and product management platforms

Where strategy and the roadmap live. Serves [[Building and Managing a Roadmap]] and [[Prioritization Frameworks]].

- **Productboard**: feedback-to-roadmap with prioritization (incl. [[RICE and Scoring Models|RICE]]).
- **Aha!**: roadmap- and strategy-heavy.
- **Notion / Confluence**: where many teams keep specs, strategy docs, and the [[Product Management Templates|templates]] from this Atlas.

## Analytics and metrics

Where you measure whether it worked. Serves [[Fluency with Data]] and [[Product Analytics and Metrics]].

- **Amplitude / Mixpanel**: the two leading product-analytics platforms (funnels, retention, [[Product Analytics and Metrics|cohorts]]).
- **Looker / Tableau**: BI and dashboards for broader business data.
- **SQL**: not a tool so much as a literacy; the PMs who can self-serve a query move faster.

## Experimentation

Where you run [[Experimentation and A-B Testing|A/B tests]] and feature flags. Serves [[Hypothesis-Driven Development]].

- **Optimizely / LaunchDarkly / Statsig**: feature flagging and experimentation at scale.

## Design and prototyping

Where the experience gets shaped. Serves [[User Experience Design]] and [[Design Sense and Critique]].

- **Figma**: the universal design and collaboration tool; PMs live in it for [[Feature Specification|specs]] and critique.
- **FigJam / Miro**: whiteboarding, [[User Personas and Journey Mapping|journey maps]], workshops.

## User research

Where insight gets captured and synthesized. Serves [[Voice of the Customer]] and [[User Research and Discovery]].

- **Dovetail**: research repository and synthesis; its AI Docs feature now produces evidence-backed, cited PRDs.
- **Maze / UserTesting**: usability testing and unmoderated research.
- **Typeform / SurveyMonkey**: surveys and quantitative feedback.

## AI prototyping ("vibe coding")

The newest category, and the one reshaping the job fastest, because PMs now ship working prototypes themselves. Serves [[AI in Prototyping and Delivery]].

- **v0**: generates React UI from prompts.
- **Lovable / Bolt / Replit**: full-stack MVPs in the browser, designer/PM-friendly.
- **Cursor**: the bridge to a real repo when a prototype graduates.

> [!note] AI prototyping is a skill with technique, not a magic button
> "Vibe coding" gets you to a credible prototype fast, and then the [[The 70% Problem|last 30%]] (edge cases, security, production hardening) is exactly as hard as it ever was. Prototype to *learn and align*, not to ship to production. See [[AI in Prototyping and Delivery]].

## AI spec and writing tools

Where the mechanical writing now gets a first draft. Serves [[Writing PRDs and Specs]].

- **ChatPRD**: the most popular PM-specific AI tool; drafts PRDs, strategy, and reviews.
- **Claude / ChatGPT**: general assistants for drafting, analysis, and summarizing.
- **GitHub Spec Kit**: spec-driven development, where "intent is the source of truth."

## Evals tooling (for AI products)

If you build AI features, this category is becoming non-negotiable. Serves [[Writing Evals for AI Products]].

- **Braintrust / LangSmith / OpenAI Evals**: datasets, scoring, traces, [[Writing Evals for AI Products|LLM-as-judge]].

## How to choose

> [!tip] My rule of thumb
> 1. **Use what the team already uses**: tool fragmentation costs more than any tool's marginal feature. 2. **Match the tool to the competency, not the trend.** 3. **Spend your learning budget on the AI-prototyping and evals categories**: that's where the leverage is shifting. 4. Stay swap-ready, especially on the AI layer; the landscape turns over fast (Cat Wu's "do the simple thing that works").

## Continue Reading
- [[Character, Competency, and Craft]] for why tools are the easy-to-teach layer, and what isn't.
- [[AI in Prototyping and Delivery]] for the vibe-coding category in depth.
- [[Writing Evals for AI Products]] for why evals tooling is the new must-have.
- [[The PM Competency Model]] for the competencies these tools actually serve.
- [[Product Management Templates]] for what to put *into* Notion, Figma, and ChatPRD.
