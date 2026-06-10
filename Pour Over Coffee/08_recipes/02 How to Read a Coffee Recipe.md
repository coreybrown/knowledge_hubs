---
tags: [recipes, schema, reference]
aliases: [How to Read a Coffee Recipe, Recipe schema, Recipe card schema]
domain: Recipes & Methods
---

# 📖 How to Read a Coffee Recipe

Every recipe in this knowledge base follows the same structure, deliberately, so that a human can scan it in five seconds and a machine can parse it without guessing. This note is the **contract**: it defines each field you'll see in the frontmatter and in the Recipe Card callout near the top of every recipe note. Once you know the schema, every recipe reads the same way. 🧩

## The Recipe Card

Near the top of each recipe you'll find a `> [!example] ☕ Recipe Card` callout, a key/value table that mirrors the structured frontmatter and adds a plain-language **Resulting cup** row. It's the at-a-glance spec sheet. The same numbers live in the YAML frontmatter above the H1, which is what an app actually reads.

## The Structured Fields

> [!note] The recipe contract
> | Field | Meaning |
> |---|---|
> | `recipe` | Always `true` for an actual recipe note (false/absent on index notes). |
> | `category` | `official`, `competition`, `community`, or `soup` (the unpressurized-espresso method). |
> | `brewer` | The device, e.g. `Hario V60`, `Kalita Wave`, `AeroPress`. |
> | `dose_g` | Grams of dry coffee. |
> | `water_g` | Total grams of brew water (including bloom). |
> | `ratio` | Coffee-to-water as `1:NN`; see [[The Brew Ratio]]. |
> | `temp_c` | Brew temperature in Celsius; a range like `92-94` is allowed. |
> | `grind` | Relative size plus a reference point, e.g. medium-fine. See [[Grind Size for Pour Over]]. |
> | `bloom_g` | Grams of water used in the [[The Bloom\|bloom]]. |
> | `bloom_time_s` | Bloom duration in seconds. |
> | `brew_time` | Target total time as `m:ss`; see [[Brew Time and Total Contact Time]]. |
> | `roast` | The [[Roast Levels for Pour Over\|roast level]] the recipe flatters. |
> | `source` | Originating person or brand, plus year. |

## How the Fields Relate

The numbers are not independent. `dose_g` and `water_g` together imply the `ratio`; a 15 g dose with 250 g water is a 1:16.7 ratio. The `bloom_g` is conventionally **two to three times the dose**. See [[CO2, Degassing, and the Bloom Science]] for why. The `grind`, `temp_c`, and `brew_time` form an extraction triangle: finer grind, hotter water, and longer time each push [[Extraction Yield and Strength|extraction]] up, so recipes balance them. Change one and you usually compensate elsewhere, which is the whole subject of [[Recipe Variables and Cup Outcomes]].

## Reading the Pour Schedule

Below the card, each recipe lists a **numbered, timed pour schedule**. Every step gives three things: the **clock time** (from when the bloom water hits), the **cumulative water in grams** your scale should read at that moment, and the **action** (pour, swirl, wait, drain). Cumulative weight (not per-pour) is used because that's what you watch on the [[Scales, Timers, and Servers|scale]] as you brew. Hit each number on time and the recipe reproduces.

> [!tip] A recipe is a starting point, not a law
> Treat published numbers as a calibrated baseline. Your [[Coffee Beans and Roast|beans]], [[Grinding|grinder]], [[Water for Coffee|water]], and [[Dripper Materials and Heat Retention|dripper]] all differ from the originator's, so expect to dial in. The [[Pour Over Troubleshooting Guide]] tells you which way to nudge.

## Continue Reading

- [[Recipe Variables and Cup Outcomes]]: what happens when you change each field
- [[The Brew Ratio]]: the math behind `dose_g`, `water_g`, and `ratio`
- [[The Bloom]]: what `bloom_g` and `bloom_time_s` are for
- [[Recipes and Methods]]: back to the recipe hub
- [[Dialing In Grind Size]]: turning a recipe into *your* recipe
