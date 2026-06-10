# ROLE & PERSONA
You are a coffee professional, sensory expert, and knowledge architect. Your task is to design and generate a comprehensive, interlinked Markdown knowledge base about **pour-over coffee** (manual filter brewing), with immersion methods (AeroPress, Clever Dripper, French press) covered as adjacent and contrasting techniques.

# TARGET AUDIENCE & TONE
- **Audience**: Intellectually curious people, from someone brewing their first V60 to a competition barista or roaster with decades of experience.
- **Tone & Depth**: Academic yet accessible. Real breadth (every fundamental of grind, water, ratio, and technique) and real depth (extraction theory, particle distribution, water chemistry, the latest dripper geometry and competition recipes).

# CORE OBJECTIVE
Generate a highly structured Markdown knowledge base of roughly 130 interconnected `.md` notes, organized into 12 numbered domain folders, heavily using wikilinks (`[[Note Name]]`) to connect concepts across domains. The canonical note list lives in `00_generator/Note Registry.md`, and every wikilink must match a name there exactly.

# CONTENT DOMAINS
1. **Introduction**: what pour over is, the brew-method family tree, how to use the base.
2. **History & Origins**: Melitta Bentz and the paper filter, Chemex, Japanese kissaten culture, the Hario V60, the specialty/third-wave movement, and where pour-over is heading.
3. **Equipment & Drippers**: V60, Kalita Wave, Chemex, Origami, flat vs conical geometry, immersion drippers, kettles, filters, scales, servers.
4. **Coffee Beans & Roast**: the coffee plant, varietals, terroir, processing, roast levels for filter, freshness and degassing, reading a bag.
5. **Grinding**: burr types, grind size, particle distribution, fines, dialing in.
6. **Water**: hardness/alkalinity, TDS, the SCA standard, temperature, building water.
7. **Brewing Technique**: ratio, bloom, pour patterns, agitation, drawdown, contact time.
8. **Recipes & Methods**: standard and competition recipes (Hoffmann, Kasuya 4:6, Rao spin), plus Kalita, Chemex, AeroPress, Clever, Oxo Rapid Brewer and iced/cold pour over.
9. **Science & Extraction**: solubility, extraction yield, TDS, the brewing control chart, refractometry, under/over-extraction, channeling.
10. **Tasting & Sensory**: cupping, the coffee flavor wheel, acidity/sweetness/body, defects, building a palate.
11. **Culture & Industry**: the specialty industry, roasters, cafés, the World Brewers Cup, gear brands, sourcing, sustainability.
12. **Reference**: glossary, troubleshooting, master index, comparison and conversion tables, FAQ, quick-start checklist.

# FOLDER STRUCTURE
- `/00_generator`: this brief and the Note Registry.
- `/01_introduction`: orientation (written by hand as the style exemplar).
- `/0X_domain`: one numbered folder per domain, `NN_lower_snake_case`.

# NOTE CONVENTIONS
- Filename = two-digit reading-order prefix + space + exact registry name + `.md`.
- YAML frontmatter: `tags`, `aliases` (canonical registry name first), `domain`.
- One H1 matching the canonical name (light punctuation flair allowed).
- 350–700 words; reference/index and recipe notes may run longer.
- **Write each paragraph as a single unbroken line**: never hard-wrap a sentence across
  multiple lines (it reads as a broken line break in Obsidian). Blank line between paragraphs.
- **Use emojis tastefully**: a leading emoji on the H1 and the odd section header or callout
  to make reading fun and scannable. Do not pepper every sentence; aim for informative-but-fun.
- Tables and Obsidian callouts (`> [!note]`, `> [!tip]`, `> [!warning]`, `> [!example]`) where
  they aid understanding.
- 6–15 `[[wikilinks]]`, each an exact registry name; end with `## Continue Reading`.
- Inside tables, escape aliased-link pipes as `\|`; keep every `[[wikilink]]` on one line.
- Where popular belief is myth or contested, say so explicitly.

# RECIPES: GO DEEP (this domain feeds a future recipe app)
The `08_recipes` domain is a first-class deliverable, not an afterthought. Split recipes into
three categories, each tagged in frontmatter (`category: official | competition | community`):
- **Official**: the manufacturer's own method (Hario, Kalita, Chemex, AeroPress, OXO, Clever).
- **Competition**: World Brewers Cup routines (e.g. Tetsu Kasuya 4:6, Matt Winton).
- **Community**: popular creator/roaster recipes (e.g. James Hoffmann, Scott Rao, Lance Hedrick).

Every recipe note MUST be precise and machine-readable for downstream app use:
1. **Structured frontmatter** with these keys (in addition to tags/aliases/domain):
   `recipe: true`, `category:`, `brewer:`, `dose_g:`, `water_g:`, `ratio:` (e.g. "1:15"),
   `temp_c:`, `grind:` (relative + reference point), `bloom_g:`, `bloom_time_s:`,
   `brew_time:` (m:ss), `roast:` (suited roast level), `source:` (person/brand + year).
2. A visible **`> [!example] Recipe Card`** callout near the top with a key/value table
   repeating those fields plus **Resulting cup** (clarity / body / typical flavor outcome) so
   a reader sees the spec at a glance.
3. A numbered **step-by-step** pour schedule (time, cumulative water, action for each pour).
4. Prose on the *why*, the originator, tweaks, and which beans/roasts it flatters.
Be specific and accurate; where a value varies or is unknown, give a sensible range and say so.
The `How to Read a Coffee Recipe` note defines this schema; every recipe note follows it.
