# knowledge_hubs

Place for deep learning — a collection of interlinked, in-depth knowledge bases.

## Knowledge Bases

### [IPAs](./IPAs)
A 154-note interlinked Obsidian knowledge base on the **India Pale Ale**, spanning
its contested 18th-century origins through the modern hazy/thiol-driven frontier.
Covers history, styles, ingredients, brewing, science & sensory, drinking, best-of
lists, industry & culture, and reference — connected by 3,163 verified wikilinks.

*Added 2026-05-21.*

### [Pour Over Coffee](./Pour%20Over%20Coffee)
A 144-note interlinked Obsidian knowledge base on **pour over coffee** — manual
filter brewing — with immersion methods (AeroPress, Clever, French press, OXO Rapid
Brewer) covered as adjacent techniques. Spans history & origins, equipment & drippers,
beans & roast, grinding, water, brewing technique, a deep recipes domain (26 official,
competition, and community recipes with machine-readable specs), science & extraction,
tasting & sensory, culture & industry, and reference — connected by 2,855 verified
wikilinks. Ships with a generated static website in `site/`.

*Added 2026-06-02.*

## Tooling

### `verify_kb.py`
Consistency checker for any knowledge base in this repo. Validates that every note
matches the `Note Registry`, every `[[wikilink]]` resolves, no link spans a line
break, and no note is orphaned.

```
python3 verify_kb.py <KB folder>        # report
python3 verify_kb.py <KB folder> --fix  # also reflow multi-line wikilinks
```

New knowledge bases are generated with the `knowledge-base-builder` Claude Code
skill, which builds, verifies, and publishes a KB here for any topic.

---

*Last updated: 2026-06-02*
