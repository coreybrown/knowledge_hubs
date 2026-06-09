---
tags: [ai, modern-pm, discovery, research]
aliases: [AI in Discovery and Research, AI in Discovery, AI for Research]
domain: AI and the Modern PM
---

# AI in Discovery and Research

Discovery is where AI delivers its most immediate, least controversial win for PMs. The grunt work of research (transcribing, tagging, theming, summarizing across hundreds of inputs) was always a time sink that crowded out the actual thinking. AI collapses it. What took a research team two weeks now takes an afternoon. That is not a marginal speedup. It changes how often you can afford to listen.

## What just got cheap

You can now synthesize interviews, support tickets, app-store reviews, sales-call notes, and survey responses in hours instead of weeks. **Dovetail**, the research repository most PM teams already use, shipped AI Docs in its Fall 2025 launch. It is Claude-powered, and it generates evidence-backed PRDs with citations back to the source clips. That citation-to-source link is the part I care about, because it gives you synthesis you can audit.

| Task | Before | With AI |
|---|---|---|
| Theme 40 interview transcripts | Days of manual tagging | Minutes, with quotes attached |
| Summarize a quarter of support tickets | A dedicated analysis project | A query |
| Draft an evidence-backed PRD | Manual synthesis, then writing | Generated from tagged research with citations |

## Faster insight changes the cadence

> [!tip] The real unlock
> The win is not "research is faster." It is that **you can listen continuously** without it being a project. Teresa Torres' case for [[Continuous Discovery]], small and frequent contact with customers, used to fight against the cost of synthesis. AI removes that cost. The discipline of weekly touchpoints feeding an [[The Opportunity Solution Tree|opportunity solution tree]] is now operationally cheap. Use that.

This extends straight into [[Voice of the Customer]]: the competency was always about turning feedback into decisions. AI handles the aggregation; you keep the judgment about which signal is real.

## The risks, and they are real

I am bullish on AI in discovery, but it has specific, dangerous failure modes. Name them so you can guard against them.

> [!warning] What AI synthesis gets wrong
> - **Smoothing over the outlier.** The single weird interview that contained the real insight gets averaged into a tidy theme. Discovery breakthroughs often live in the outlier, and summarization is designed to erase it.
> - **Confident hallucinated themes.** The model will name a pattern that is not there, in fluent prose, with no tell. Without source citations you cannot catch it.
> - **Confirmation bias, accelerated.** Ask a leading question and the model finds support for whatever you already believed, faster than you ever could manually.
> - **Losing the felt sense.** Reading a synthesized summary is not the same as watching a user struggle. The summary tells you *what*; sitting with the raw clip tells you *why it matters*.

The mitigations are not exotic. Insist on citations to source (which is exactly why the Dovetail approach matters), spot-check raw clips against every theme, and never let synthesis fully replace direct customer contact. AI is a research accelerant, not a research substitute. The PMs who get burned are the ones who stop watching the interviews.

## My take

Use AI to do the synthesis you would never have had time for, but keep your hands dirty. Watch a few raw sessions every week. The model can tell you what users said. It cannot tell you what they meant, and that gap is where [[Product Sense and Judgment|product judgment]] is made. See [[User Research and Discovery]] for the underlying craft this sits on top of.

## Continue Reading
- [[Continuous Discovery]] for the discipline AI now makes operationally cheap.
- [[Voice of the Customer]] for the competency AI accelerates.
- [[User Research and Discovery]] for the craft underneath the tooling.
- [[The Opportunity Solution Tree]] for where synthesized insight should land.
- [[The PM Tool Landscape]] for where Dovetail and friends sit.
- [[AI in Prototyping and Delivery]] for the next stage after discovery.
