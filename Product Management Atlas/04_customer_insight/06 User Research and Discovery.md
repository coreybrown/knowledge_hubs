---
tags: [customer-insight, research, discovery, methods, qualitative]
aliases: [User Research and Discovery, User Research, Discovery Methods]
domain: Customer Insight
---

# User Research and Discovery

The question I get most from junior PMs is "which research method should I use?" — and it's the wrong first question. The right one is **"what decision am I trying to make, and what's the cheapest way to be less wrong about it?"** Method follows from that. Research is not a box you check before building; it's risk reduction, and you buy exactly as much as the decision warrants. A reversible $5k decision deserves a hallway conversation; a one-way $5M decision deserves real study.

## Qualitative vs quantitative — the core split

Everything sorts onto one axis first: are you learning **why** or **how many**?

| | Qualitative | Quantitative |
|---|---|---|
| **Answers** | Why, how, what's the mental model | How many, how much, how often |
| **Sample** | Small (5–8 often enough) | Large (statistical) |
| **Output** | Hypotheses, needs, "aha"s | Confirmation, sizing, significance |
| **Methods** | Interviews, usability tests, field studies | Surveys (at scale), analytics, A/B tests |
| **Risk if alone** | Compelling but unrepresentative | Precise but can't explain itself |

The whole game is the loop between them: qual *generates* the hypothesis, quant *tests* whether it generalizes. A PM who only does one is the failure mode I described in [[Customer Insight]] — the qual-only PM ships heartfelt features nobody uses; the quant-only PM optimizes a dashboard into a local maximum.

## The methods, and when to reach for each

**User interviews** — your default for understanding *why*. One person, open questions, lots of "tell me about the last time you…". The mistake everyone makes is pitching their solution and fishing for a yes; the discipline is to ask about **past behavior**, not future intentions, because people are honest historians and terrible fortune-tellers.

**Usability tests** — for "can a user actually *do* this?" Put a person in front of a design or prototype and a task, then shut up and watch. Five users will surface the overwhelming majority of usability problems (Nielsen's well-worn finding), which is why you don't need a big sample to de-risk usability ([[The Four Big Product Risks]]). This is the cheapest insurance against shipping a confusing interface.

**Surveys** — for "how many / how widespread?" once you already know *what* to ask. Surveys are quantitative at scale and a trap when used to *discover* — you can only ask about what you already thought of, and you can't ask "why" follow-ups. I use them to *size* a problem qual already found, not to find it.

**Analytics** — passive, behavioral, always-on. The funnels and cohorts of [[Product Analytics and Metrics]]. Best at telling you *where* to point the other methods.

**A/B tests** — causal proof at scale, covered in [[Experimentation and A-B Testing]]. The most rigorous, and the most demanding of traffic and a clean metric.

> [!tip] Behavior beats opinion, every time
> If I had to compress every research lesson into one line: **what people do beats what people say.** Watch a usability test before you trust an interview; trust an interview before you trust a survey; treat "would you use this?" as worthless noise. Stated intent is the weakest signal in research, and the one PMs lean on most because it's easy to collect and always says yes.

## Avoiding the classic biases

Three traps poison research faster than anything: **leading questions** ("don't you find the old checkout slow?" — ask "walk me through your last checkout" instead); **confirmation bias** (going in to prove you're right — pre-commit to what would *change your mind*, like a good [[Hypothesis-Driven Development|hypothesis]]); and **survivorship bias** (only talking to happy current users, when the people who churned or never signed up hold your most important insights).

One more reframe that's now consensus: research isn't a *phase* before building — it's a habit that runs *alongside* it. Marty Cagan's rule never to split discovery from delivery and Teresa Torres' case for weekly customer contact say the same thing. I treat the methods above as the toolkit and [[Continuous Discovery]] as the cadence that keeps you using them.

## How AI is changing it

AI compresses the slowest parts of research — transcribing and coding interviews, clustering open-text survey responses, drafting synthesis with citations back to the source — so a solo PM can now process a volume of qualitative data that used to need a research team. The durable human work moves to *designing* the study (the right question, the right participants, an unbiased guide) and *interpreting* with judgment — and to resisting the urge to let a model average away the one uncomfortable interview that should have changed the plan. See [[AI in Discovery and Research]].

## Continue Reading
- [[Voice of the Customer]] — the competency this toolkit serves.
- [[Continuous Discovery]] — turning these methods into a weekly team cadence.
- [[The Four Big Product Risks]] — what research is actually de-risking: value and usability.
- [[Jobs To Be Done]] — a lens for what to listen *for* in an interview.
- [[Experimentation and A-B Testing]] — the quantitative method for proving causation.
