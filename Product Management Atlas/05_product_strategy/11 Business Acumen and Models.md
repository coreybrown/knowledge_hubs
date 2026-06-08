---
tags: [product-strategy, business-model, unit-economics, finance]
aliases: [Business Acumen and Models, Business Acumen, Business Models and Unit Economics]
domain: Product Strategy
---

# Business Acumen and Models

This is the competency PMs most often dodge, and the one that most reliably separates a senior PM from a stalled one. You cannot have [[Strategic Impact]] on a business you don't understand *mechanically* — how it makes money, what it costs, and where the margins are. The [[Strategic Impact|Business Understanding & Clarity]] behavior in my model says it plainly: "grasp the core business model and bottom-line drivers." This note is the minimum business literacy I expect of any PM who wants their strategy opinions to carry weight.

> [!warning] The myth: business is finance's job
> Plenty of PMs treat the P&L as someone else's problem and speak only in user-value terms. Then they get out-argued in every resourcing meeting by whoever can speak in dollars. If you can't tie your product to the bottom line, you're an order-taker for the people who can. Business fluency is not optional at senior levels — it's the price of admission.

## Business models: how the company actually makes money

Start with the model itself, because product strategy looks completely different depending on it. A few common ones and what they make the PM optimize for:

| Model | How it earns | What the PM optimizes |
|---|---|---|
| **Subscription / SaaS** | Recurring fee | Retention, expansion, churn reduction |
| **Transactional / marketplace** | Take rate on each transaction | Transaction volume, take rate, liquidity |
| **Advertising** | Sell attention to advertisers | Engagement, time spent, ad inventory |
| **Freemium** | Free tier → paid conversion | Activation, free-to-paid conversion |
| **Usage-based** | Pay per consumption | Usage depth, expansion |

In my world — sports/media/betting — you live across several at once: ad-supported media, subscription, and transactional betting revenue under one roof, each pulling product priorities in a different direction. Knowing *which* model a feature serves is half of [[Prioritization Frameworks|prioritization]].

## Unit economics: the numbers that decide if the model works

Business models are the shape; unit economics are whether the shape is profitable *per customer.* The core vocabulary every PM should own cold:

- **CAC** (Customer Acquisition Cost) — fully loaded cost to acquire one customer.
- **LTV** (Lifetime Value) — total margin a customer generates over their life. The **LTV:CAC ratio** is the headline health metric; ~3:1 is a common rule of thumb for a healthy business.
- **Gross margin** — revenue minus the cost of *delivering* the product (COGS), as a percentage. SaaS runs 80–90%; this is why software is a great business.
- **Payback period** — months of margin to recover CAC. Shorter is better; it's how fast growth self-funds.
- **Contribution margin** — what each additional unit contributes after variable costs.

These aren't finance trivia — they're *product levers.* A feature that lifts retention raises LTV. One that improves onboarding shortens payback. A pricing change moves contribution margin. When I justify a roadmap bet to [[Executive Communication|executives]], I do it in these terms, because this is the language the bottom line is written in.

## Reading a P&L

The Profit & Loss statement is the company's scoreboard, and a PM who can read it has a strategic edge. The skeleton, top to bottom:

```
Revenue              ← what you sold
− COGS               ← cost to deliver it
= Gross Profit       ← (Gross Margin %)
− OpEx               ← S&M, R&D, G&A
= Operating Income   ← the real "are we profitable" line
```

What I look for as a PM: which revenue line is my product in, and is it growing? What's our gross margin, and does my work help or hurt it? Where is OpEx concentrated — and is the company spending to grow or to survive? You don't need to *build* the P&L; you need to find your product on it and know which line your work moves. Get the deck the CFO presents to the board and learn to read it — that single habit does more for strategic credibility than any framework.

## Tying product to the bottom line

The whole point of this competency is the connection from feature → metric → financial line. A worked example: a retention feature → lifts D30 retention → raises LTV → improves LTV:CAC → makes paid acquisition profitable → grows revenue at healthy margin. That chain is what turns "I think users want this" into "this is worth funding." It's the same logic as the [[The North Star Framework|North Star]] (value metric predicting revenue) and the engine behind [[Business Outcome Ownership]]. When you can draw that chain, you stop being a feature requester and become a business operator who happens to work in product. And it's exactly the test [[The DHM Model|the DHM model]] applies — is this *margin-enhancing*?

## How AI is changing it

AI lowers the barrier to business literacy, which is good news for PMs who've avoided it: you can paste a P&L and have a model explain each line and where the margin pressure is, or sanity-check a unit-economics model. What *rises* in value is the [[The Unit Economics of AI|economics of AI products themselves]] — they don't behave like SaaS. Inference has a real marginal cost per request, so AI gross margins run closer to 50–60% versus software's 80–90%, and the PM's levers now include prompt and response length, model selection, and concurrency. The PM who already understands unit economics can reason about this; the one who dodged it is exposed precisely when the model gets harder.

## Continue Reading
- [[Strategic Impact]] — the competency this business literacy directly enables.
- [[The DHM Model]] — the "margin-enhancing" test for whether a strategy strengthens the business.
- [[The Unit Economics of AI]] — why AI products break the SaaS margin playbook.
- [[The North Star Framework]] — choosing a value metric that leads to financial results.
- [[Executive Communication]] — speaking to leadership in the language of the P&L.
