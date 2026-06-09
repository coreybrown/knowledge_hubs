---
tags: [customer-insight, discovery, torres, framework, opportunity-solution-tree]
aliases: [The Opportunity Solution Tree, Opportunity Solution Tree, OST]
domain: Customer Insight
---

# The Opportunity Solution Tree

The **Opportunity Solution Tree (OST)** is **Teresa Torres'** answer to the most common discovery failure I see: a team that does customer research, collects a pile of insights and feature ideas, and then has no structured way to decide which to pursue, so they default to whoever argued loudest or shipped fastest. The OST is a visual map that forces every solution to earn its place by tracing back to a customer opportunity, and every opportunity back to a business outcome.

## The four levels

It's a tree read top-down, and the structure is the argument:

```
            OUTCOME            (the one business result we're driving)
               │
        ┌──────┼──────┐
   OPPORTUNITY  OPPORTUNITY  OPPORTUNITY   (customer needs / pains / desires)
        │
   ┌────┼────┐
 SOLUTION SOLUTION SOLUTION   (ideas that address an opportunity)
        │
   ┌────┴────┐
  TEST     TEST              (assumption tests that de-risk a solution)
```

1. **Outcome** (root) is a single business or product outcome you are trying to move, for example "increase week-1 retention". Not a feature, not an output, but an [[Outcomes Over Outputs|outcome]]. The tree has *one* root on purpose.
2. **Opportunities** (branches) are customer **needs, pain points, and desires** surfaced through research, framed as opportunities to improve the outcome. Crucially these are framed in the *customer's* terms, not as solutions. "Users can't tell which bets are live" is an opportunity. "Add a filter" is not.
3. **Solutions** (sub-branches) are ideas that might address a *specific* opportunity. By hanging each solution off an opportunity, the tree quietly kills the orphan feature that serves no real need.
4. **Assumption tests** (leaves) are the small experiments that de-risk a solution before you commit to building it. This is where the tree connects to [[Experimentation and A-B Testing]] and rapid prototyping.

## Why I find it powerful

> [!tip] It makes "no" a structural act, not a political one
> The OST's real gift is turning prioritization from a personality contest into a visible map. When someone pitches a pet feature, you do not argue about the feature. You ask "which opportunity does this serve, and is that the opportunity we've decided is highest-leverage for this outcome?" If it does not hang on the tree, it does not get built. Saying no stops being political and becomes structural ([[Prioritization Frameworks]]).

Three things it does well:

- **It keeps discovery anchored.** This is the companion to [[Continuous Discovery]], the "in pursuit of a desired outcome" clause of Torres' definition made visible. Weekly touchpoints fill in the opportunity space, and the tree keeps them from wandering.
- **It separates the problem space from the solution space.** Opportunities are problems and solutions are answers. Most teams collapse the two and jump straight to features. The tree forces you to map the problem space *first* and pick the biggest opportunity *before* brainstorming solutions.
- **It compares opportunities, not features.** This is Torres' key move: prioritize at the *opportunity* level. Comparing "ship feature A vs feature B" is apples to oranges. Comparing "which customer problem matters most for this outcome" is a decision you can actually reason about.

## How it differs from a roadmap or a backlog

A roadmap is a time-ordered list of *what* you will ship, and a backlog is an undifferentiated pile of solutions. The OST is neither. It is a *reasoning structure* that shows **why** a solution connects to a need connects to a goal. You can generate a roadmap *from* a tree, but the tree shows the logic a roadmap hides. This pairs naturally with [[The Opportunity Solution Tree|OST]]-driven discovery feeding [[Building and Managing a Roadmap|roadmap]] decisions.

## Where I'm careful with it

I have watched OSTs become beautiful, sprawling diagrams that nobody updates and no decision ever flows from, discovery theater in tree form. The tree is a *thinking* tool, not a deliverable to be admired. Keep it small, keep it tied to one live outcome, and let it die when the outcome changes. A tidy tree that does not change what you build is worth nothing.

## How AI is changing it

AI can speed up the population of the tree: clustering interview transcripts and support tickets into candidate opportunities, and generating a spread of solution ideas for any branch far faster than a brainstorm. That is genuinely useful for the breadth. But the judgment the tree exists to support stays human. *Which* opportunity is highest-leverage, and whether a machine-generated cluster is a real need or just an artifact of how you phrased the query, is your call. AI fills the branches. You still decide which branch to climb. See [[AI in Discovery and Research]].

## Continue Reading
- [[Continuous Discovery]] for the cadence the tree organizes; both are Teresa Torres' work.
- [[Outcomes Over Outputs]] for the outcome that sits at the root of every tree.
- [[Prioritization Frameworks]] for how to choose between opportunities once they are mapped.
- [[Experimentation and A-B Testing]] for the assumption tests that form the leaves.
- [[Jobs To Be Done]] for another lens on framing the opportunity space.
