---
tags: [product-execution, raci, decision-rights, governance, disagree-and-commit]
aliases: [RACI and Decision Rights, RACI, Decision Rights, Owner Partner Consulted]
domain: Product Execution
---

# RACI and Decision Rights

Most of what gets called an alignment problem is really a **decision-rights problem** wearing a disguise. The team is not misaligned on the goal. They are unclear on *who gets to make the call.* So the decision gets made by everyone, which is slow and political, or by no one, which is drift. This note is about fixing that, and it is the companion to the role split in [[The 10-50-90 Execution Framework]].

## RACI in one table

The classic model assigns four roles to every meaningful decision or deliverable.

| Role | Meaning | The trap |
|---|---|---|
| **Responsible** | Does the work | Few traps here; the work just needs an owner |
| **Accountable** | Owns the outcome; the single decider | More than one "A" = no real owner |
| **Consulted** | Input is sought *before* the call | Consulting too many people = paralysis |
| **Informed** | Told *after* the call | Confusing this with Consulted causes most friction |

> [!warning] There is exactly one Accountable
> The most common RACI failure is two people who both think they are accountable, or a committee that is collectively accountable, which means no one is. If you cannot name the single person who owns a decision, you do not have decision rights. You have a future argument scheduled for the worst possible moment.

## The model I actually use: Owner / Partner / Consulted

Full RACI can get bureaucratic. For day-to-day product work I run a lighter three-role split, the same one baked into [[The 10-50-90 Execution Framework]]:

- **Owner.** Accountable for the decision and its outcome. Makes the final call.
- **Partner.** Co-creates the work and owns the decisions in *their* domain. Not a passenger, but a peer with real authority in their lane.
- **Consulted.** Their input must be genuinely weighed, but they do not decide.

The reason this beats generic RACI for a product team is the **domain split** it implies, straight from how I run [[Product Delivery|delivery]]:

| Decision domain | Owner |
|---|---|
| Product success & business viability | **PM** |
| Usability & the user experience | **Design** ([[User Experience Design]]) |
| Technical feasibility & implementation | **Engineering** |

A PM who tries to own usability is overstepping; an engineer who tries to own scope-vs-value is overstepping. Healthy teams know whose call is whose. This is the [[The Product, Design, and Engineering Venn|PM/Design/Eng Venn]] expressed as decision rights.

## Disagree and commit

> [!tip] The most useful two words in product
> You will lose decisions, including ones you owned the input on. The mark of a professional is **disagree and commit**: argue hard *before* the call, then once it is made, execute it as if it were your own. Re-litigating a settled decision in the hallway is corrosive. It signals to the team that decisions are not real, which makes every future decision slower.

Disagree-and-commit only works if the disagreement was genuinely *heard* first. If you commit without ever having voiced the disagreement, that is not commitment. It is silence, and silence in the room becomes sabotage in the work.

## Escalation: a tool, not a failure

New PMs treat escalation as admitting defeat. I coach the opposite. Fast, clean escalation is a *skill*, and the APM-level [[Product Delivery]] bar explicitly rewards knowing when to escalate. The rule I use: escalate when a decision is **blocked, above your pay grade, or cross-team and stuck**, and escalate *with a recommendation*, not just a problem. "We're stuck between A and B, here's the trade-off, I recommend A, I need you to break the tie" is leadership. "Help, we can't agree" is not.

For *how much* senior leadership to pull in, I lean on Curtis Stanier's [[The Initiative Pyramid]]: a few high-risk initiatives warrant leaders being **consulted**; many low-risk ones only warrant them being **informed**. Match the escalation weight to the risk.

> [!note] Decision rights live in the spec
> The cleanest place to record who owns what is the [[Writing PRDs and Specs|spec]] itself. A one-line "Decisions & owners" section pre-empts most mid-project ownership fights, because you settled them when everyone was calm instead of when the deadline was on fire.

## How AI is changing it

AI does not change who *should* decide. Accountability is a human and organizational property, not a technical one. What it changes is the inputs. With analysis and first-draft options generated in minutes, the bottleneck shifts decisively from *gathering information* to *exercising judgment* on it, and Reforge's framing is that AI multiplies the burden of choice rather than reducing it. In agentic products this gets sharper. Deciding the human-in-the-loop checkpoints, meaning which calls a system may make on its own and which require a person, is itself a decision-rights problem you have to design. See [[Designing for Trust and Probabilistic Systems]] and [[Competencies AI Commoditizes vs Elevates]].

## Continue Reading
- [[The 10-50-90 Execution Framework]] for where Owner/Partner/Consulted is wired into the execution flow.
- [[Sound Product Decision-Making]] for how the accountable owner should actually make the call.
- [[The Initiative Pyramid]] for how much senior involvement a decision warrants, by risk.
- [[Stakeholder Management]] for keeping the Consulted and Informed genuinely in the loop.
- [[Leading Without Authority]] for making decisions stick when you don't control the people executing them.
