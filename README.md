# knowledge_hubs

Place for deep learning — a collection of interlinked, in-depth knowledge bases.

## Knowledge Bases

### [IPAs](./IPAs)
A 154-note interlinked Obsidian knowledge base on the **India Pale Ale**, spanning
its contested 18th-century origins through the modern hazy/thiol-driven frontier.
Covers history, styles, ingredients, brewing, science & sensory, drinking, best-of
lists, industry & culture, and reference — connected by 3,163 verified wikilinks.

*Added 2026-05-21.*

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

*Last updated: 2026-05-21*
