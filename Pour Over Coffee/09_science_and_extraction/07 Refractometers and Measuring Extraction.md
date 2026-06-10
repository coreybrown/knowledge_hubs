---
tags: [science, extraction, measurement, tools]
aliases: [Refractometers and Measuring Extraction, Refractometer, Measuring extraction]
domain: Science & Extraction
---

# 🔭 Refractometers and Measuring Extraction

A **refractometer** is the instrument that turns brewing from intuition into measurement. It reads the **[[Total Dissolved Solids (TDS)|TDS]]** of your cup, and from TDS plus a little arithmetic you can calculate the **[[Extraction Yield and Strength|extraction yield]]**: the two coordinates that place your brew on the [[The Coffee Brewing Control Chart|control chart]]. For anyone chasing repeatability, it is the difference between "I think that was better" and "that was 21.2%, half a point higher than yesterday." 📐

## How It Works 💡

Dissolved solids change how much light **bends** (refracts) as it passes through a liquid: more solids, more bending. A refractometer shines an LED through a small drop of brew and measures the **refractive index**, which it reports as a percentage of TDS (or as **°Brix**, a sugar-scale reading it converts internally). Coffee refractometers like the well-known **VST** units pair the optics with software calibrated specifically to brewed coffee, since coffee solids refract slightly differently from pure sugar.

> [!warning] Brix is not TDS
> A cheap winemaker's Brix refractometer reads sugar, not coffee solids. The conversion factor differs, so generic Brix readings overstate coffee TDS unless corrected. Coffee-specific tools (or apps) apply the right factor.

## Measuring Cleanly

Garbage in, garbage out. Small errors swing the result:

1. **Filter the sample.** Undissolved fines scatter light and inflate the reading; draw your drop through a small syringe filter.
2. **Cool it down.** Temperature shifts refractive index; let the sample reach near room temperature or use a temperature-compensating unit.
3. **Wipe and zero.** Calibrate to distilled water, and clean the lens between reads.
4. **Sample representatively.** Stir the brew first; the first drops from the [[The Drawdown|drawdown]] differ from the average cup.

## Calculating Extraction Yield 🧮

> [!example] The formula
> **EY% = (Beverage Mass × TDS%) ÷ Dry Coffee Dose**
> Example: 250 g of brewed coffee at 1.40% TDS from a 15 g dose →
> (250 × 0.014) ÷ 15 = **3.5 g dissolved ÷ 15 g = 23.3% extraction yield.**

| You need | How to get it |
|---|---|
| Beverage mass | Weigh the brewed liquid in the cup/server |
| TDS% | Read from the refractometer |
| Dose | Weigh dry coffee before grinding on your [[Scales, Timers, and Servers\|scale]] |

Note **beverage mass**, not water poured: some water is retained by the wet grounds and never reaches the cup, so using the poured weight inflates EY.

## Is It Worth It? 🤔

> [!tip] A tool for repeatability, not a flavor judge
> A refractometer can't tell you a cup is *delicious*, only *where* it is on the map. Its value is letting you reproduce a great brew and reason about adjustments precisely. Many superb brewers never own one; many dialed-in [[Dialing In Grind Size|grind routines]] go faster with one.

## Continue Reading

- [[Total Dissolved Solids (TDS)]]: the value the device reads
- [[Extraction Yield and Strength]]: the value you calculate from it
- [[The Coffee Brewing Control Chart]]: where your measurement lands
- [[Scales, Timers, and Servers]]: the weighing gear it depends on
- [[Science and Extraction]]: back to the domain hub
