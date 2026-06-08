#!/usr/bin/env python3
"""
build_site.py — Static-site generator for The Product Manager's Atlas.

Converts the Obsidian vault (numbered domain folders of Markdown notes) into a
fully interlinked, design-forward HTML website in ./site.

Pure standard library. Run:  python3 00_generator/build_site.py
"""

import os
import re
import html
import json
import shutil
import pathlib

import diagrams as DG

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
ASSETS = SITE / "assets"

# folder -> (display name, emoji icon, accent color, blurb)
DOMAINS = [
    ("01_introduction",            "Introduction",          "🧭",
     "#3B5BA5", "What product management is, the competency model, and how to read this Atlas."),
    ("02_foundations",             "Foundations",           "🧱",
     "#5B6B8C", "The role, the trade-offs, product sense, and the four big risks the job manages."),
    ("03_product_execution",       "Product Execution",     "🛠️",
     "#2F7E8C", "Specs, delivery, quality, and my 10-50-90 framework — the work of shipping."),
    ("04_customer_insight",        "Customer Insight",       "🔍",
     "#3E8E7E", "Data, research, discovery, and UX — understanding what's worth building."),
    ("05_product_strategy",        "Product Strategy",      "🎯",
     "#7A5EA8", "Vision, roadmaps, prioritization, and tying product work to business outcomes."),
    ("06_influencing_people",      "Influencing People",    "🤝",
     "#B5734A", "Stakeholders, leadership, communication, and influence without authority."),
    ("07_career_ladder",           "The Career Ladder",     "🪜",
     "#4666B0", "APM to CPO — the IC and manager tracks, and what changes at each level."),
    ("08_assessment_and_coaching", "Assessment & Coaching", "📊",
     "#5C8A4E", "Score yourself against the model, find the gaps, and build a growth plan."),
    ("09_frameworks_toolkit",      "Frameworks Toolkit",    "🧰",
     "#8A6D3B", "The frameworks I actually reach for — and when each one is just theater."),
    ("10_ai_and_modern_pm",        "AI & the Modern PM",    "🤖",
     "#6E56CF", "Evals, vibe-coding, AI product sense, and the competencies AI is rewriting."),
    ("11_reference",               "Reference",             "📚",
     "#50708A", "The master competency matrix, glossary, templates, and the PM canon."),
]
DOMAIN_BY_FOLDER = {d[0]: d for d in DOMAINS}

CALLOUTS = {
    "note":    ("ℹ", "callout-note",    "Note"),
    "tip":     ("✦", "callout-tip",     "Tip"),
    "example": ("◆", "callout-example", "Example"),
    "warning": ("▲", "callout-warning", "Warning"),
}


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def slugify(text):
    text = text.lower().replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def strip_prefix(name):
    """'05 West Coast IPA' -> 'West Coast IPA'"""
    return re.sub(r"^\d+\s+", "", name)


def split_frontmatter(raw):
    if raw.startswith("---"):
        end = raw.find("\n---", 3)
        if end != -1:
            fm = raw[3:end].strip()
            body = raw[end + 4:].lstrip("\n")
            meta = {}
            for line in fm.splitlines():
                m = re.match(r"^(\w+):\s*(.*)$", line)
                if m:
                    key, val = m.group(1), m.group(2).strip()
                    if val.startswith("[") and val.endswith("]"):
                        val = [v.strip() for v in val[1:-1].split(",") if v.strip()]
                    meta[key] = val
            return meta, body
    return {}, raw


def strip_code(body):
    """Remove fenced + inline code so link scans ignore code samples."""
    body = re.sub(r"```.*?```", " ", body, flags=re.S)
    body = re.sub(r"`[^`]*`", " ", body)
    return body


def plain_text(body):
    t = re.sub(r"`[^`]*`", " ", body)
    t = re.sub(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", r"\1", t)
    t = re.sub(r"[#>*|_~-]+", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()


# --------------------------------------------------------------------------
# pass 1 — collect every note
# --------------------------------------------------------------------------
def collect_pages():
    pages = []        # ordered, book order
    linkmap = {}      # lowercased name/alias -> page

    for folder, dname, icon, color, blurb in DOMAINS:
        fdir = ROOT / folder
        if not fdir.is_dir():
            continue
        files = sorted(fdir.glob("*.md"), key=lambda p: p.name)
        moc_seen = False
        for f in files:
            raw = f.read_text(encoding="utf-8")
            meta, body = split_frontmatter(raw)
            canonical = strip_prefix(f.stem)
            h1 = re.search(r"^#\s+(.+)$", body, re.M)
            title = h1.group(1).strip() if h1 else canonical
            # drop a decorative leading emoji (and its modifiers) from the title
            title = re.sub(
                r"^[\s"
                r"\U0001F000-\U0001FAFF"     # pictographs, flags, symbols
                r"\u2190-\u21FF"             # arrows
                r"\u2300-\u23FF"             # misc technical (hourglass, timers)
                r"\u25A0-\u25FF"             # geometric shapes
                r"\u2600-\u27BF"             # misc symbols & dingbats
                r"\u2900-\u297F"             # supplemental arrows-B
                r"\u2B00-\u2BFF"             # misc symbols & arrows (star)
                r"\u3030\u303D\u3297\u3299"
                r"\uFE00-\uFE0F\u200D\u20E3"  # variation selectors, ZWJ, keycap
                r"]+", "", title).strip() or canonical
            slug = "index" if canonical.lower() == "home" else slugify(canonical)
            is_moc = not moc_seen
            moc_seen = True
            page = {
                "canonical": canonical,
                "title": title,
                "slug": slug,
                "folder": folder,
                "domain": dname,
                "icon": icon,
                "color": color,
                "body": body,
                "meta": meta,
                "tags": meta.get("tags", []) or [],
                "aliases": meta.get("aliases", []) or [],
                "is_moc": is_moc,
                "is_recipe": meta.get("recipe") == "true",
            }
            pages.append(page)

    # build link resolution map — aliases first, canonical/title last (win)
    for p in pages:
        for a in p["aliases"]:
            linkmap.setdefault(a.lower(), p)
    for p in pages:
        linkmap[p["canonical"].lower()] = p
        linkmap[p["title"].lower()] = p
    return pages, linkmap


def compute_backlinks(pages, linkmap):
    back = {p["slug"]: [] for p in pages}
    for p in pages:
        seen = set()
        for m in re.finditer(r"\[\[([^\]]+?)\]\]", strip_code(p["body"])):
            target = re.split(r"\\?\|", m.group(1))[0].strip()
            dest = linkmap.get(target.lower())
            if dest and dest["slug"] != p["slug"] and dest["slug"] not in seen:
                seen.add(dest["slug"])
                back[dest["slug"]].append(p)
    return back


# --------------------------------------------------------------------------
# inline markdown
# --------------------------------------------------------------------------
def render_inline(text, ctx):
    text = html.escape(text, quote=False)

    # protect inline code
    codes = []
    def _code(m):
        codes.append(m.group(1))
        return f"\x00C{len(codes)-1}\x00"
    text = re.sub(r"`([^`]+)`", _code, text)

    # wikilinks
    def _wiki(m):
        inner = m.group(1)
        parts = re.split(r"\\?\|", inner, maxsplit=1)
        target = parts[0].strip()
        display = parts[1].strip() if len(parts) > 1 else target
        dest = ctx["linkmap"].get(target.lower())
        if dest:
            cls = "wlink"
            if dest["slug"] == ctx.get("slug"):
                return f'<span class="wlink-self">{display}</span>'
            return (f'<a class="{cls}" data-domain="{dest["domain"]}" '
                    f'href="{dest["slug"]}.html">{display}</a>')
        return f'<span class="wlink-missing" title="unresolved link">{display}</span>'
    text = re.sub(r"\[\[([^\]]+?)\]\]", _wiki, text)

    # standard markdown links
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
                  r'<a class="exlink" href="\2" target="_blank" rel="noopener">\1</a>',
                  text)

    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<em>\1</em>", text)
    text = text.replace("\\|", "|")

    def _restore(m):
        return f"<code>{html.escape(codes[int(m.group(1))], quote=False)}</code>"
    text = re.sub(r"\x00C(\d+)\x00", _restore, text)
    return text


# --------------------------------------------------------------------------
# block markdown
# --------------------------------------------------------------------------
def is_table_sep(line):
    s = line.strip()
    return bool(s) and "-" in s and "|" in s and set(s) <= set("|-: ")


def split_table_row(row):
    cells = re.split(r"(?<!\\)\|", row.strip())
    if cells and cells[0].strip() == "":
        cells = cells[1:]
    if cells and cells[-1].strip() == "":
        cells = cells[:-1]
    return cells


def render_table(header, sep, rows, ctx):
    aligns = []
    for c in split_table_row(sep):
        c = c.strip()
        if c.startswith(":") and c.endswith(":"):
            aligns.append("center")
        elif c.endswith(":"):
            aligns.append("right")
        elif c.startswith(":"):
            aligns.append("left")
        else:
            aligns.append("")
    head_cells = split_table_row(header)
    kv = all(c.strip() == "" for c in head_cells)

    def cells_html(cells, tag):
        out = []
        for i, c in enumerate(cells):
            al = aligns[i] if i < len(aligns) else ""
            style = f' style="text-align:{al}"' if al else ""
            out.append(f"<{tag}{style}>{render_inline(c.strip(), ctx)}</{tag}>")
        return "".join(out)

    cls = "kvtable" if kv else "datatable"
    parts = [f'<div class="table-wrap"><table class="{cls}">']
    if not kv:
        parts.append(f"<thead><tr>{cells_html(head_cells, 'th')}</tr></thead>")
    parts.append("<tbody>")
    for r in rows:
        parts.append(f"<tr>{cells_html(split_table_row(r), 'td')}</tr>")
    parts.append("</tbody></table></div>")
    return "".join(parts)


def render_list(items, ctx):
    """items: list of (indent, ordered, text). Build nested list."""
    def build(idx, indent):
        if idx >= len(items):
            return "", idx
        ordered = items[idx][1]
        tag = "ol" if ordered else "ul"
        out = [f"<{tag}>"]
        while idx < len(items) and items[idx][0] >= indent:
            cur_indent, cur_ord, text = items[idx]
            if cur_indent > indent:
                break
            li = f"<li>{render_inline(text, ctx)}"
            idx += 1
            if idx < len(items) and items[idx][0] > cur_indent:
                sub, idx = build(idx, items[idx][0])
                li += sub
            li += "</li>"
            out.append(li)
        out.append(f"</{tag}>")
        return "".join(out), idx

    h, _ = build(0, items[0][0])
    return h


def _parse_kv_table(lines, ctx):
    """Pull the kv rows out of a 'Quick stats' callout body.
    Returns (stats_raw, hops_html, glass_html). Raw values are the
    bracketed plain text (with wikilinks rendered) for free-text fields,
    or the unrendered cell text for numeric fields."""
    stats_raw = {}
    hops_html = ""
    glass_html = ""
    for ln in lines:
        if not ln.strip().startswith("|"):
            continue
        if set(ln.strip()) <= set("|-: "):
            continue
        cells = split_table_row(ln)
        if len(cells) < 2:
            continue
        key = re.sub(r"\*\*", "", cells[0]).strip()
        if not key:
            continue
        raw = cells[1].strip()
        if key.lower().startswith("key hop"):
            hops_html = render_inline(raw, ctx)
        elif key.lower().startswith("glassware"):
            glass_html = render_inline(raw, ctx)
        else:
            stats_raw[key] = raw
    return stats_raw, hops_html, glass_html


def render_blocks(lines, ctx, headings=None, top=False):
    out = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue

        # headings
        m = re.match(r"^(#{1,6})\s+(.+)$", line)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            if level == 1:                       # page H1 handled separately
                i += 1
                continue
            hid = slugify(text)
            if headings is not None and level in (2, 3):
                headings.append((level, text, hid))
            out.append(f'<h{level} id="{hid}">'
                       f'<a class="anchor" href="#{hid}">#</a>'
                       f'{render_inline(text, ctx)}</h{level}>')
            i += 1
            continue

        # fenced code  /  family-tree diagram
        if line.startswith("```"):
            j = i + 1
            buf = []
            while j < n and not lines[j].startswith("```"):
                buf.append(lines[j])
                j += 1
            if ctx.get("slug") == "brew-method-family-tree":
                out.append(FAMILY_TREE_SVG)
            else:
                code = html.escape("\n".join(buf), quote=False)
                out.append(f'<pre class="codeblock"><code>{code}</code></pre>')
            i = j + 1
            continue

        # blockquote / callout
        if line.lstrip().startswith(">"):
            buf = []
            while i < n and lines[i].lstrip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            cm = re.match(r"^\[!(\w+)\]\s*(.*)$", buf[0])
            if cm:
                ctype = cm.group(1).lower()
                ctitle = cm.group(2).strip()
                # special-case: "Quick stats" callout on style pages
                # becomes a designed vital-signs panel
                if ctype == "example" and ctitle.lower().startswith("quick stat"):
                    stats_raw, hops_html, glass_html = _parse_kv_table(
                        buf[1:], ctx)
                    out.append(DG.vital_signs(
                        stats_raw, hops_html, glass_html,
                        ctx.get("page_title", "")))
                    continue
                icon, cls, default = CALLOUTS.get(
                    ctype, ("●", "callout-note", "Note"))
                inner = render_blocks(buf[1:], ctx, headings)
                label = render_inline(ctitle, ctx) if ctitle else default
                out.append(
                    f'<div class="callout {cls}">'
                    f'<div class="callout-head"><span class="callout-icon">{icon}</span>'
                    f'<span class="callout-title">{label}</span></div>'
                    f'<div class="callout-body">{inner}</div></div>')
            else:
                out.append(f'<blockquote>{render_blocks(buf, ctx, headings)}</blockquote>')
            continue

        # table
        if "|" in line and i + 1 < n and is_table_sep(lines[i + 1]):
            header = line
            sep = lines[i + 1]
            rows = []
            j = i + 2
            while j < n and "|" in lines[j] and lines[j].strip():
                rows.append(lines[j])
                j += 1
            out.append(render_table(header, sep, rows, ctx))
            i = j
            continue

        # list
        lm = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", line)
        if lm:
            items = []
            while i < n:
                lm = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", lines[i])
                if lm:
                    indent = len(lm.group(1))
                    ordered = lm.group(2).endswith(".")
                    items.append([indent, ordered, lm.group(3).strip()])
                    i += 1
                elif (lines[i].strip() and lines[i][:1] in (" ", "\t") and items):
                    items[-1][2] += " " + lines[i].strip()
                    i += 1
                else:
                    break
            out.append(render_list(items, ctx))
            continue

        # horizontal rule
        if line.strip() in ("---", "***", "___"):
            out.append("<hr>")
            i += 1
            continue

        # paragraph
        buf = [line]
        i += 1
        while i < n and lines[i].strip():
            s = lines[i]
            if (re.match(r"^#{1,6}\s", s) or s.startswith("```") or
                    s.lstrip().startswith(">") or
                    re.match(r"^\s*([-*+]|\d+\.)\s", s) or
                    ("|" in s and i + 1 < n and is_table_sep(lines[i + 1]))):
                break
            buf.append(s)
            i += 1
        out.append(f"<p>{render_inline(' '.join(buf), ctx)}</p>")
        if (top and ctx.get("diagram_html")
                and not ctx.get("_diagram_emitted")):
            out.append(ctx["diagram_html"])
            ctx["_diagram_emitted"] = True
    return "".join(out)


# The family-tree diagram (and all other bespoke diagrams) live in diagrams.py.
FAMILY_TREE_SVG = DG.FAMILY_TREE_SVG
PAGE_DIAGRAMS = DG.page_diagrams()


# --------------------------------------------------------------------------
# HTML chrome
# --------------------------------------------------------------------------
# Hop cone — a layered brewing hop flower, drawn inline so it inherits the
# accent color (currentColor) and theme like the previous mark.
LOGO_SVG = (
    '<svg viewBox="0 0 32 32" class="logo-mark" aria-hidden="true">'
    '<circle cx="16" cy="16" r="13" fill="currentColor" opacity=".16"/>'
    '<circle cx="16" cy="16" r="13" fill="none" stroke="currentColor" stroke-width="2"/>'
    '<path d="M16 5.5 L19.8 16 L16 26.5 L12.2 16 Z" fill="currentColor"/>'
    '<path d="M16 5.5 L19.8 16 L12.2 16 Z" fill="currentColor" opacity=".5"/>'
    '<circle cx="16" cy="16" r="2.1" fill="#fff"/>'
    '</svg>')


def topbar():
    return (
        '<header class="topbar">'
        '<a class="brand" href="index.html">' + LOGO_SVG +
        '<span class="brand-name">The Product Manager&rsquo;s <b>Atlas</b></span></a>'
        '<button class="searchbtn" id="searchOpen" aria-label="Search">'
        '<svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="9" cy="9" r="6" '
        'fill="none" stroke="currentColor" stroke-width="2"/>'
        '<line x1="13.5" y1="13.5" x2="18" y2="18" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round"/></svg>'
        '<span>Search the base</span><kbd>/</kbd></button>'
        '<div class="topbar-right">'
        '<button class="iconbtn" id="themeToggle" aria-label="Toggle theme">'
        '<svg viewBox="0 0 24 24" class="ic-sun" aria-hidden="true">'
        '<circle cx="12" cy="12" r="4.2" fill="currentColor"/>'
        '<g stroke="currentColor" stroke-width="2" stroke-linecap="round">'
        '<line x1="12" y1="2.5" x2="12" y2="5"/><line x1="12" y1="19" x2="12" y2="21.5"/>'
        '<line x1="2.5" y1="12" x2="5" y2="12"/><line x1="19" y1="12" x2="21.5" y2="12"/>'
        '<line x1="5.2" y1="5.2" x2="7" y2="7"/><line x1="17" y1="17" x2="18.8" y2="18.8"/>'
        '<line x1="5.2" y1="18.8" x2="7" y2="17"/><line x1="17" y1="7" x2="18.8" y2="5.2"/>'
        '</g></svg>'
        '<svg viewBox="0 0 24 24" class="ic-moon" aria-hidden="true">'
        '<path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5z" fill="currentColor"/>'
        '</svg></button>'
        '<button class="iconbtn menubtn" id="menuToggle" aria-label="Menu">'
        '<svg viewBox="0 0 24 24" aria-hidden="true">'
        '<g stroke="currentColor" stroke-width="2" stroke-linecap="round">'
        '<line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/>'
        '<line x1="3" y1="18" x2="21" y2="18"/></g></svg></button>'
        '</div></header>')


def sidebar(pages, active_slug):
    by_domain = {}
    for p in pages:
        by_domain.setdefault(p["folder"], []).append(p)
    active_folder = next((p["folder"] for p in pages
                          if p["slug"] == active_slug), None)
    parts = ['<aside class="sidebar" id="sidebar"><nav class="nav">']
    for folder, dname, icon, color, blurb in DOMAINS:
        notes = by_domain.get(folder, [])
        if not notes:
            continue
        is_open = folder == active_folder
        moc = notes[0]
        parts.append(
            f'<details class="nav-group"{" open" if is_open else ""} '
            f'style="--dc:{color}">'
            f'<summary class="nav-head"><span class="nav-icon">{icon}</span>'
            f'<span class="nav-dname">{html.escape(dname)}</span>'
            f'<svg class="nav-caret" viewBox="0 0 12 12" aria-hidden="true">'
            f'<path d="M3 4.5 6 8 9 4.5" fill="none" stroke="currentColor" '
            f'stroke-width="1.7" stroke-linecap="round"/></svg></summary>'
            f'<ul class="nav-list">')
        for i, p in enumerate(notes):
            cls = "nav-link"
            if p["slug"] == active_slug:
                cls += " current"
            if p is moc:
                cls += " nav-moc"
            elif p.get("is_recipe"):
                cls += " nav-sub"          # recipe leaf — nest under its hub
            elif i + 1 < len(notes) and notes[i + 1].get("is_recipe"):
                cls += " nav-parent"       # category hub for the recipes below
            parts.append(
                f'<li><a class="{cls}" href="{p["slug"]}.html">'
                f'{html.escape(p["title"])}</a></li>')
        parts.append("</ul></details>")
    parts.append("</nav></aside>")
    return "".join(parts)


def page_shell(title, body, pages, active_slug, extra_head=""):
    return (
        "<!DOCTYPE html><html lang=\"en\" data-theme=\"light\">"
        "<head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
        "<link rel=\"icon\" href=\"data:image/svg+xml,"
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>"
        "<text y='.9em' font-size='90'>🗺️</text></svg>\">"
        f"<title>{html.escape(title)} · The Product Manager's Atlas</title>"
        "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">"
        "<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>"
        "<link href=\"https://fonts.googleapis.com/css2?"
        "family=Fraunces:ital,opsz,wght@0,9..144,400..600;1,9..144,400&"
        "family=Inter:wght@400;500;600;700&"
        "family=Spline+Sans+Mono:wght@400;500&display=swap\" rel=\"stylesheet\">"
        "<link rel=\"stylesheet\" href=\"assets/style.css\">"
        f"{extra_head}</head><body>"
        + topbar()
        + '<div class="layout">'
        + sidebar(pages, active_slug)
        + body
        + '</div>'
        + '<div class="scrim" id="scrim"></div>'
        + search_overlay()
        + '<script src="assets/search-index.js"></script>'
        + '<script src="assets/app.js"></script>'
        + "</body></html>")


def search_overlay():
    return (
        '<div class="search-modal" id="searchModal" hidden>'
        '<div class="search-box">'
        '<div class="search-input-row">'
        '<svg viewBox="0 0 20 20" class="search-ic" aria-hidden="true">'
        '<circle cx="9" cy="9" r="6" fill="none" stroke="currentColor" stroke-width="2"/>'
        '<line x1="13.5" y1="13.5" x2="18" y2="18" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round"/></svg>'
        '<input type="text" id="searchInput" placeholder="Ask about product management, '
        'or search 126 notes…" autocomplete="off">'
        '<kbd>Esc</kbd></div>'
        '<div class="search-body" id="searchBody">'
        '<div class="ask-panel" id="askPanel" hidden></div>'
        '<div class="search-results" id="searchResults"></div>'
        '</div>'
        '</div></div>')


# --------------------------------------------------------------------------
# content page
# --------------------------------------------------------------------------
def render_page(page, pages, idx, backlinks, ctx):
    headings = []
    ctx["page_title"] = page["title"]
    ctx["diagram_html"] = PAGE_DIAGRAMS.get(page["slug"])
    body_html = render_blocks(
        page["body"].splitlines(), ctx, headings, top=True)

    # breadcrumb
    crumb = (
        '<nav class="crumb"><a href="index.html">Home</a>'
        '<span class="crumb-sep">/</span>'
        f'<a href="{pages_first_of_domain(pages, page["folder"])}.html">'
        f'{html.escape(page["domain"])}</a>'
        '<span class="crumb-sep">/</span>'
        f'<span>{html.escape(page["title"])}</span></nav>')

    words = len(re.findall(r"\w+", plain_text(page["body"])))
    read = max(1, round(words / 210))
    tags = "".join(f'<span class="tag">{html.escape(t)}</span>'
                   for t in page["tags"][:6])

    # MOC pages get an illustrated banner; regular pages get the standard head
    if page.get("is_moc") and page["slug"] != "index":
        _, dname, icon, color, blurb = DOMAIN_BY_FOLDER.get(
            page["folder"], (None, page["domain"], page["icon"], page["color"], ""))
        illus = DG.domain_illustration(page["folder"], color)
        header = (
            f'<header class="moc-banner" style="--dc:{page["color"]}">'
            f'{crumb}'
            f'<div class="moc-grid">'
            f'<div class="moc-text">'
            f'<div class="moc-kicker">Domain {page["folder"][:2]} · {len(pages_in_domain(pages, page["folder"]))} notes</div>'
            f'<h1 class="moc-title">{html.escape(page["title"])}</h1>'
            f'<p class="moc-blurb">{html.escape(blurb)}</p>'
            f'<div class="page-meta"><span class="readtime">{read} min read</span>'
            f'<span class="dot">·</span><span>{words:,} words</span></div>'
            f'</div><div class="moc-art">{illus}</div></div>'
            f'</header>')
    else:
        header = (
            f'<header class="page-head" style="--dc:{page["color"]}">'
            f'{crumb}'
            f'<div class="domain-chip"><span>{page["icon"]}</span>'
            f'{html.escape(page["domain"])}</div>'
            f'<h1 class="page-title">{html.escape(page["title"])}</h1>'
            f'<div class="page-meta"><span class="readtime">{read} min read</span>'
            f'<span class="dot">·</span><span>{words:,} words</span></div>'
            f'<div class="tags">{tags}</div></header>')

    # prev / next in book order
    prev_p = pages[idx - 1] if idx > 0 else None
    next_p = pages[idx + 1] if idx < len(pages) - 1 else None
    nav_cards = ['<nav class="pagenav">']
    if prev_p:
        nav_cards.append(
            f'<a class="pn-card pn-prev" href="{prev_p["slug"]}.html">'
            f'<span class="pn-dir">‹ Previous</span>'
            f'<span class="pn-title">{html.escape(prev_p["title"])}</span></a>')
    else:
        nav_cards.append('<span></span>')
    if next_p:
        nav_cards.append(
            f'<a class="pn-card pn-next" href="{next_p["slug"]}.html">'
            f'<span class="pn-dir">Next ›</span>'
            f'<span class="pn-title">{html.escape(next_p["title"])}</span></a>')
    nav_cards.append("</nav>")

    # backlinks
    bl = backlinks.get(page["slug"], [])
    bl_html = ""
    if bl:
        items = "".join(
            f'<a class="bl-item" href="{b["slug"]}.html">'
            f'<span class="bl-ic">{b["icon"]}</span>'
            f'<span>{html.escape(b["title"])}</span></a>'
            for b in sorted(bl, key=lambda x: x["title"]))
        bl_html = (
            '<section class="backlinks">'
            f'<h2 class="bl-head">Referenced by <span>{len(bl)}</span></h2>'
            f'<div class="bl-grid">{items}</div></section>')

    # right rail TOC
    toc = ""
    if len(headings) >= 3:
        links = "".join(
            f'<a class="toc-link toc-l{lv}" href="#{hid}">{html.escape(tx)}</a>'
            for lv, tx, hid in headings)
        toc = (f'<aside class="toc"><div class="toc-inner">'
               f'<div class="toc-head">On this page</div>{links}</div></aside>')

    main = (
        '<main class="main"><div class="content-grid">'
        '<article class="article">'
        + header
        + f'<div class="prose">{body_html}</div>'
        + bl_html
        + "".join(nav_cards)
        + '</article>'
        + toc
        + '</div></main>')
    return page_shell(page["title"], main, pages, page["slug"])


def pages_first_of_domain(pages, folder):
    for p in pages:
        if p["folder"] == folder:
            return p["slug"]
    return "index"


def pages_in_domain(pages, folder):
    return [p for p in pages if p["folder"] == folder]


# --------------------------------------------------------------------------
# home page
# --------------------------------------------------------------------------
def render_home(pages, linkmap):
    by_domain = {}
    for p in pages:
        by_domain.setdefault(p["folder"], []).append(p)

    cards = []
    for folder, dname, icon, color, blurb in DOMAINS:
        notes = by_domain.get(folder, [])
        if not notes:
            continue
        moc = notes[0]
        illus = DG.domain_illustration(folder, color)
        # Introduction's MOC is the home page itself — link the card to the
        # next intro note instead so users move forward, not in a circle.
        target = notes[1] if moc["slug"] == "index" and len(notes) > 1 else moc
        cards.append(
            f'<a class="dcard" href="{target["slug"]}.html" style="--dc:{color}">'
            f'<div class="dcard-art">{illus}</div>'
            f'<div class="dcard-top"><span class="dcard-icon">{icon}</span>'
            f'<span class="dcard-count">{len(notes)} notes</span></div>'
            f'<h3 class="dcard-name">{html.escape(dname)}</h3>'
            f'<p class="dcard-blurb">{html.escape(blurb)}</p>'
            f'<span class="dcard-go">Enter {html.escape(dname)} '
            f'<svg viewBox="0 0 16 16" aria-hidden="true">'
            f'<path d="M3 8h9M8.5 4 12.5 8 8.5 12" fill="none" '
            f'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            f'stroke-linejoin="round"/></svg></span></a>')

    ctx = {"linkmap": linkmap, "slug": "index"}
    para = render_inline(
        "Product management is the discipline of being [[What Is Product Management|accountable "
        "for whether a product succeeds]] — not for shipping features, but for the "
        "[[Outcomes Over Outputs|outcomes]] they produce. The job lives where "
        "[[The Four Big Product Risks|user value, business viability, usability, and feasibility]] "
        "meet, and the real work is [[Product Sense and Judgment|judgment under uncertainty]]: "
        "deciding which problems are worth solving and rallying a team to solve them. I organize "
        "that ability into [[The PM Competency Model|four areas and twelve competencies]] — "
        "[[Product Execution]], [[Customer Insight]], [[Product Strategy]], and [[Influencing People]] — "
        "that escalate from [[Associate Product Manager|APM]] to [[The Chief Product Officer|CPO]]. "
        "This Atlas maps all of it, including how [[AI and the Modern PM|AI is rewriting]] the craft.", ctx)

    paths = [
        ("\U0001F9ED", "New to product",
         "Start with what the job actually is.",
         [("What Is Product Management", "what-is-product-management"),
          ("The Product Manager Role", "the-product-manager-role")]),
        ("\U0001F4C8", "Leveling up",
         "Assess yourself against the model and close the gaps.",
         [("The Competency Self-Assessment", "the-competency-self-assessment"),
          ("Building a Growth Plan", "building-a-growth-plan")]),
        ("\U0001F916", "Wondering about AI",
         "See what's changing in the craft — and what isn't.",
         [("How AI Is Reshaping Product Management", "how-ai-is-reshaping-product-management"),
          ("Competencies AI Commoditizes vs Elevates", "competencies-ai-commoditizes-vs-elevates")]),
        ("\U0001F3AF", "Want a framework",
         "The tools I reach for, and when to use them.",
         [("The Frameworks Toolkit", "the-frameworks-toolkit"),
          ("Prioritization Frameworks", "prioritization-frameworks")]),
    ]
    path_cards = []
    for icon, ttl, desc, links in paths:
        lk = "".join(
            f'<a class="path-link" href="{s}.html">{html.escape(t)}</a>'
            for t, s in links)
        path_cards.append(
            f'<div class="path-card"><div class="path-icon">{icon}</div>'
            f'<h4>{html.escape(ttl)}</h4><p>{html.escape(desc)}</p>'
            f'<div class="path-links">{lk}</div></div>')

    hero = (
        '<section class="hero">'
        '<div class="hero-inner">'
        '<div class="hero-eyebrow">A field guide to the product management craft</div>'
        '<h1 class="hero-title">The <span class="hero-em">Product Manager&rsquo;s</span><br>'
        'Atlas</h1>'
        '<p class="hero-sub">The competencies that define product management at every level — '
        'from APM to CPO — how to assess and grow them, and how AI is rewriting the job. '
        'The competency system I&rsquo;ve built and use to level and coach PMs.</p>'
        '<div class="hero-actions">'
        '<a class="btn btn-primary" href="what-is-product-management.html">'
        'Start here — What is product management?</a>'
        '<a class="btn btn-ghost" href="the-pm-competency-model.html">See the competency model</a>'
        '</div>'
        '<div class="hero-stats">'
        f'<div class="hstat"><b>{len(pages)}</b><span>interlinked notes</span></div>'
        '<div class="hstat"><b>11</b><span>domains of the craft</span></div>'
        '<div class="hstat"><b>12</b><span>core competencies</span></div>'
        '</div></div></section>')

    body = (
        '<main class="main main-home">'
        + hero
        + '<section class="home-sec">'
        '<div class="sec-head"><span class="sec-kicker">The map</span>'
        '<h2>Explore the eleven domains</h2>'
        '<p>Each domain is a guided path. Follow it front-to-back like a book, '
        'or dive straight to what you need — every note links onward.</p></div>'
        f'<div class="dcard-grid">{"".join(cards)}</div></section>'
        '<section class="home-sec home-sec-tint">'
        '<div class="sec-head"><span class="sec-kicker">In one paragraph</span>'
        '<h2>So — what is product management?</h2></div>'
        f'<p class="lede">{para}</p></section>'
        '<section class="home-sec">'
        '<div class="sec-head"><span class="sec-kicker">Choose your path</span>'
        '<h2>Where do you want to go deeper?</h2></div>'
        f'<div class="path-grid">{"".join(path_cards)}</div></section>'
        + footer()
        + '</main>')
    return page_shell("Home", body, pages, "index")


def footer():
    return (
        '<footer class="site-footer">'
        '<div class="footer-mark">' + LOGO_SVG + '<b>The Product Manager&rsquo;s Atlas</b></div>'
        '<p>An opinionated, interlinked field guide to the product management craft — '
        'the competencies, the career ladder, the frameworks, and the AI frontier.</p>'
        '<p class="footer-fine">Generated from an Obsidian vault · '
        '<a href="index.html">Return home</a></p></footer>')


# --------------------------------------------------------------------------
# assets
# --------------------------------------------------------------------------
def write_search_index(pages):
    idx = []
    for p in pages:
        body = re.sub(r"^#\s+.*(?:\n|$)", "", p["body"], count=1)
        snippet = plain_text(body)[:240]
        idx.append({
            "t": p["title"],
            "u": p["slug"] + ".html",
            "d": p["domain"],
            "i": p["icon"],
            "c": p["color"],
            "s": snippet,
            "k": " ".join(p["tags"]) + " " + " ".join(p["aliases"]),
        })
    (ASSETS / "search-index.js").write_text(
        "window.SEARCH_INDEX = " + json.dumps(idx, ensure_ascii=False) + ";",
        encoding="utf-8")


def write_ask_corpus(pages):
    """Plain-text corpus for the 'Ask the guide' retrieval layer (RAG).

    One entry per note, split into H2 sections so the backend can pull
    section-level snippets rather than whole notes. Navigation-only sections
    are dropped. Public content only — no secrets. Served at
    assets/ask-corpus.json and read server-side by /api/ask."""
    skip = {"continue reading"}
    corpus = []
    for p in pages:
        body = re.sub(r"^#\s+.*(?:\n|$)", "", p["body"], count=1)
        parts = re.split(r"^##\s+(.+)$", body, flags=re.M)
        sections = []
        intro = plain_text(parts[0])
        if intro:
            sections.append({"h": "", "t": intro})
        for i in range(1, len(parts), 2):
            head = plain_text(parts[i]).strip()
            text = plain_text(parts[i + 1]) if i + 1 < len(parts) else ""
            if head.lower() in skip or (not head and not text):
                continue
            sections.append({"h": head, "t": text})
        if not sections:
            continue
        corpus.append({
            "slug": p["slug"],
            "title": p["title"],
            "domain": p["domain"],
            "url": p["slug"] + ".html",
            "sections": sections,
        })
    (ASSETS / "ask-corpus.json").write_text(
        json.dumps(corpus, ensure_ascii=False), encoding="utf-8")


# --------------------------------------------------------------------------
# build
# --------------------------------------------------------------------------
def main():
    pages, linkmap = collect_pages()
    backlinks = compute_backlinks(pages, linkmap)

    if SITE.exists():
        shutil.rmtree(SITE)
    ASSETS.mkdir(parents=True)

    (ASSETS / "style.css").write_text(CSS, encoding="utf-8")
    (ASSETS / "app.js").write_text(JS, encoding="utf-8")
    write_search_index(pages)
    write_ask_corpus(pages)

    for idx, p in enumerate(pages):
        ctx = {"linkmap": linkmap, "slug": p["slug"]}
        if p["slug"] == "index":
            html_doc = render_home(pages, linkmap)
        else:
            html_doc = render_page(p, pages, idx, backlinks, ctx)
        (SITE / f'{p["slug"]}.html').write_text(html_doc, encoding="utf-8")

    print(f"Built {len(pages)} pages -> {SITE}")
    unresolved = set()
    for p in pages:
        for m in re.finditer(r"\[\[([^\]]+?)\]\]", strip_code(p["body"])):
            tgt = re.split(r"\\?\|", m.group(1))[0].strip()
            if tgt.lower() not in linkmap:
                unresolved.add(tgt)
    if unresolved:
        print(f"  WARNING: {len(unresolved)} unresolved link targets:")
        for u in sorted(unresolved):
            print("   -", u)
    else:
        print("  All wikilinks resolved.")


# CSS and JS are defined in build_assets.py and imported.
from build_assets import CSS, JS  # noqa: E402

if __name__ == "__main__":
    main()
