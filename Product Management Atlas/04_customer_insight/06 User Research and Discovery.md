---
tags: [customer-insight, research, discovery, methods, qualitative]
aliases: [User Research and Discovery, User Research, Discovery Methods]
domain: Customer Insight
---

# User Research and Discovery

The question I get most from junior PMs is "which research method should I use?", and it is the wrong first question. The right one is "what decision am I trying to make, and what is the cheapest way to be less wrong about it?" Method follows from that. Research is not a box you check before building. It is risk reduction, and you buy exactly as much as the decision warrants. A reversible $5k decision deserves a hallway conversation. A one-way $5M decision deserves real study.

## Qualitative vs quantitative, the core split

Everything sorts onto one axis first: are you learning **why** or **how many**?

| | Qualitative | Quantitative |
|---|---|---|
| **Answers** | Why, how, what's the mental model | How many, how much, how often |
| **Sample** | Small (5 to 8 often enough) | Large (statistical) |
| **Output** | Hypotheses, needs, "aha"s | Confirmation, sizing, significance |
| **Methods** | Interviews, usability tests, field studies | Surveys (at scale), analytics, A/B tests |
| **Risk if alone** | Compelling but unrepresentative | Precise but can't explain itself |

The whole game is the loop between them. Qual *generates* the hypothesis, quant *tests* whether it generalizes. A PM who only does one is the failure mode I described in [[Customer Insight]]: the qual-only PM ships heartfelt features nobody uses, and the quant-only PM optimizes a dashboard into a local maximum.

## The methods, and when to reach for each

**User interviews** are your default for understanding *why*. One person, open questions, lots of "tell me about the last time you…". The mistake everyone makes is pitching their solution and fishing for a yes. The discipline is to ask about **past behavior**, not future intentions, because people are honest historians and terrible fortune-tellers.

**Usability tests** answer "can a user actually *do* this?" Put a person in front of a design or prototype and a task, then shut up and watch. Five users will surface the overwhelming majority of usability problems, which is Nielsen's well-worn finding, and it is why you do not need a big sample to de-risk usability ([[The Four Big Product Risks]]). This is the cheapest insurance you can buy against shipping a confusing interface.

**Surveys** answer "how many, how widespread?" once you already know *what* to ask. They are quantitative at scale and a trap when you use them to *discover*, because you can only ask about what you already thought of, and you cannot ask a "why" follow-up. I use them to *size* a problem qual already found, not to find it.

**Analytics** are passive, behavioral, and always on. These are the funnels and cohorts of [[Product Analytics and Metrics]], and they are best at telling you *where* to point the other methods.

**A/B tests** are causal proof at scale, covered in [[Experimentation and A-B Testing]]. They are the most rigorous method and the most demanding of traffic and a clean metric.

> [!tip] Behavior beats opinion, every time
> If I had to compress every research lesson into one line, it is this: **what people do beats what people say.** Watch a usability test before you trust an interview, trust an interview before you trust a survey, and treat "would you use this?" as worthless noise. Stated intent is the weakest signal in research, and it is the one PMs lean on most, because it is easy to collect and it always says yes.

## Avoiding the classic biases

Three traps poison research faster than anything else. **Leading questions** ("don't you find the old checkout slow?", when you should ask "walk me through your last checkout"). **Confirmation bias** (going in to prove you are right, when you should pre-commit to what would *change your mind*, like a good [[Hypothesis-Driven Development|hypothesis]]). And **survivorship bias** (only talking to happy current users, when the people who churned or never signed up hold your most important insights).

One more reframe that is now broadly consensus: research is not a *phase* before building, it is a habit that runs *alongside* it. Marty Cagan's rule never to split discovery from delivery and Teresa Torres' case for weekly customer contact are saying the same thing. I treat the methods above as the toolkit and [[Continuous Discovery]] as the cadence that keeps you using them.

## How AI is changing it

AI compresses the slowest parts of research: transcribing and coding interviews, clustering open-text survey responses, and drafting synthesis with citations back to the source. A solo PM can now process a volume of qualitative data that used to need a whole research team. So the durable human work moves to *designing* the study (the right question, the right participants, a guide that does not lead the witness) and *interpreting* it with judgment. It also moves to resisting the urge to let a model average away the one uncomfortable interview that should have changed the plan. See [[AI in Discovery and Research]].

## Continue Reading
- [[Voice of the Customer]] for the competency this toolkit serves.
- [[Continuous Discovery]] for turning these methods into a weekly team cadence.
- [[The Four Big Product Risks]] for what research is actually de-risking: value and usability.
- [[Jobs To Be Done]] for a lens on what to listen *for* in an interview.
- [[Experimentation and A-B Testing]] for the quantitative method that proves causation.
