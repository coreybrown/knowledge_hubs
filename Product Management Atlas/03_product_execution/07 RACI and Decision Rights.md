---
tags: [product-execution, raci, decision-rights, governance, disagree-and-commit]
aliases: [RACI and Decision Rights, RACI, Decision Rights, Owner Partner Consulted]
domain: Product Execution
---

# RACI and Decision Rights

Most "alignment problems" are actually **decision-rights problems** in disguise. The team isn't misaligned on the goal; they're unclear on *who gets to make the call.* So the decision either gets made by everyone (slow, political) or by no one (drift). This note is about fixing that, and it's the companion to the role split in [[The 10-50-90 Execution Framework]].

## RACI in one table

The classic model assigns four roles to every meaningful decision or deliverable.

| Role | Meaning | The trap |
|---|---|---|
| **Responsible** | Does the work | — |
| **Accountable** | Owns the outcome; the single decider | More than one "A" = no real owner |
| **Consulted** | Input is sought *before* the call | Consulting too many people = paralysis |
| **Informed** | Told *after* the call | Confusing this with Consulted causes most friction |

> [!warning] There is exactly one Accountable
> The most common RACI failure is two people who both think they're accountable, or a committee that's collectively accountable (which means no one is). If you can't name the single person who owns a decision, you don't have decision rights — you have a future argument scheduled for the worst possible moment.

## The model I actually use: Owner / Partner / Consulted

Full RACI can get bureaucratic. For day-to-day product work I run a lighter three-role split, the same one baked into [[The 10-50-90 Execution Framework]]:

- **Owner** — accountable for the decision and its outcome. Makes the final call.
- **Partner** — co-creates the work and owns *their* domain's decisions. Not a passenger; a peer with real authority in their lane.
- **Consulted** — input must be genuinely weighed, but they don't decide.

The reason this beats generic RACI for a product team is the **domain split** it implies, straight from how I run [[Product Delivery|delivery]]:

| Decision domain | Owner |
|---|---|
| Product success & business viability | **PM** |
| Usability & the user experience | **Design** ([[User Experience Design]]) |
| Technical feasibility & implementation | **Engineering** |

A PM who tries to own usability is overstepping; an engineer who tries to own scope-vs-value is overstepping. Healthy teams know whose call is whose. This is the [[The Product, Design, and Engineering Venn|PM/Design/Eng Venn]] expressed as decision rights.

## Disagree and commit

> [!tip] The most useful two words in product
> You will lose decisions — including ones you owned the input on. The mark of a professional is **disagree and commit**: argue hard *before* the call, then once it's made, execute it as if it were your own. Re-litigating a settled decision in the hallway is corrosive; it signals to the team that decisions aren't real, which makes every future decision slower.

Disagree-and-commit only works if disagreement was genuinely *heard* first. If you commit without ever having voiced the disagreement, that's not commitment — it's silence, and silence in the room becomes sabotage in the work.

## Escalation: a tool, not a failure

New PMs treat escalation as admitting defeat. I treat fast, clean escalation as a *skill* — the APM-level [[Product Delivery]] bar explicitly rewards "knowing when to escalate." The rule: escalate when a decision is **blocked, above your pay grade, or cross-team and stuck** — and escalate *with a recommendation*, not just a problem. "We're stuck between A and B, here's the trade-off, I recommend A, I need you to break the tie" is leadership. "Help, we can't agree" is not.

For *how much* senior leadership to pull in, I lean on Curtis Stanier's [[The Initiative Pyramid]]: a few high-risk initiatives warrant leaders being **consulted**; many low-risk ones only warrant them being **informed**. Match the escalation weight to the risk.

> [!note] Decision rights live in the spec
> The cleanest place to record who owns what is the [[Writing PRDs and Specs|spec]] itself. A one-line "Decisions & owners" section pre-empts most mid-project ownership fights — because you settled them when everyone was calm instead of when the deadline was on fire.

## How AI is changing it

AI doesn't change who *should* decide — accountability is a human and organizational property, not a technical one — but it changes the inputs. With analysis and first-draft options generated in minutes, the bottleneck shifts decisively from *gathering information* to *exercising judgment* on it; Reforge's framing is that AI multiplies the burden of choice rather than reducing it. In agentic products this gets sharper: deciding the human-in-the-loop checkpoints — which calls a system may make autonomously and which require a person — is itself a decision-rights design problem. See [[Designing for Trust and Probabilistic Systems]] and [[Competencies AI Commoditizes vs Elevates]].

## Continue Reading
- [[The 10-50-90 Execution Framework]] — where Owner/Partner/Consulted is wired into the execution flow.
- [[Sound Product Decision-Making]] — how the accountable owner should actually make the call.
- [[The Initiative Pyramid]] — how much senior involvement a decision warrants, by risk.
- [[Stakeholder Management]] — keeping the Consulted and Informed genuinely in the loop.
- [[Leading Without Authority]] — making decisions stick when you don't control the people executing them.
