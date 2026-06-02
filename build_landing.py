#!/usr/bin/env python3
"""
build_landing.py — Field Guides portal generator
================================================

Builds the public-facing landing page (a "hub gallery") that fronts every
knowledge hub in this repo, and assembles a `docs/` folder ready for GitHub
Pages with clean URLs:

    docs/
      index.html        ← the Field Guides landing page (this generator)
      .nojekyll
      ipas/             ← copy of IPAs/site
      pour-over/        ← copy of Pour Over Coffee/site

Adding a future hub is one entry in the HUBS list below — drop in its source
`site` dir, slug, copy, blurb, accent, art and stats, then re-run:

    python3 build_landing.py

GitHub Pages: Settings → Pages → Deploy from branch → main → /docs.
"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"

# ---------------------------------------------------------------------------
# Hand-drawn tile illustrations — same ink-line + accent-fill language as the
# hubs themselves. They paint with CSS vars so each tile colours its own art.
# ---------------------------------------------------------------------------

ART_IPA = """
<circle cx="140" cy="92" r="78" fill="currentColor" opacity=".10"/>
<ellipse cx="140" cy="166" rx="70" ry="7" fill="var(--art-ink)" opacity=".16"/>
<path d="M96 48 L188 48 L181 158 L103 158 Z" fill="var(--art-glass)"/>
<path d="M101 60 L183 60 L177 152 L107 152 Z" fill="var(--art-fill)"/>
<path d="M96 48 q7 -11 14 -2 q7 -10 14 -2 q7 -11 14 -2 q7 -10 14 -2 q7 -11 14 -2 q7 -10 12 -2"
      fill="var(--art-foam)" stroke="var(--art-ink)" stroke-width="2.5" stroke-linejoin="round"/>
<path d="M111 70 L107 144" stroke="var(--art-foam)" stroke-width="3.2" stroke-linecap="round" opacity=".7"/>
<circle cx="165" cy="100" r="3.4" fill="var(--art-foam)" opacity=".85"/>
<circle cx="158" cy="86" r="2.4" fill="var(--art-foam)" opacity=".7"/>
<circle cx="170" cy="118" r="2.6" fill="var(--art-foam)" opacity=".75"/>
<path d="M96 48 L188 48 L181 158 L103 158 Z" fill="none" stroke="var(--art-ink)" stroke-width="2.6" stroke-linejoin="round"/>
"""

ART_COFFEE = """
<circle cx="140" cy="92" r="78" fill="currentColor" opacity=".10"/>
<g fill="none" stroke="var(--art-ink)" stroke-width="2.4" stroke-linecap="round" opacity=".5">
  <path d="M128 40 q7 -9 0 -18"/>
  <path d="M152 40 q7 -9 0 -18"/>
</g>
<path d="M108 112 q-6 0 -6 8 l0 16 q0 20 38 20 q38 0 38 -20 l0 -16 q0 -8 -6 -8 Z" fill="var(--art-glass)"/>
<path d="M104 136 q4 20 36 20 q32 0 36 -20 q-36 11 -72 0 Z" fill="var(--art-fill)"/>
<path d="M108 112 q-6 0 -6 8 l0 16 q0 20 38 20 q38 0 38 -20 l0 -16 q0 -8 -6 -8 Z"
      fill="none" stroke="var(--art-ink)" stroke-width="2.6" stroke-linejoin="round"/>
<path d="M178 118 q16 2 16 16 q0 14 -16 16" fill="none" stroke="var(--art-ink)" stroke-width="2.6"/>
<path d="M100 58 L180 58 L156 104 L124 104 Z" fill="var(--art-glass)"/>
<g stroke="var(--art-ink)" stroke-width="1.6" opacity=".45">
  <line x1="120" y1="58" x2="131" y2="104"/>
  <line x1="140" y1="58" x2="140" y2="104"/>
  <line x1="160" y1="58" x2="149" y2="104"/>
</g>
<path d="M100 58 L180 58 L156 104 L124 104 Z" fill="none" stroke="var(--art-ink)" stroke-width="2.6" stroke-linejoin="round"/>
<ellipse cx="140" cy="58" rx="40" ry="8" fill="var(--art-fill)"/>
<ellipse cx="140" cy="58" rx="40" ry="8" fill="none" stroke="var(--art-ink)" stroke-width="2.6"/>
<line x1="140" y1="104" x2="140" y2="118" stroke="var(--art-fill)" stroke-width="3" stroke-linecap="round"/>
<circle cx="140" cy="122" r="3" fill="var(--art-fill)"/>
"""

# Hub brand marks (lifted from each hub so the badge stays true to source).
MARK_IPA = (
    '<svg viewBox="0 0 64 64" aria-hidden="true"><defs><g id="hb">'
    '<path d="M0 8.5C-2 8.5 -3 7.5 -4.5 5.5C-7 2 -8.5 -2 -6 -5C-4 -7.2 -1.5 -6 0 -3.8C1.5 -6 4 -7.2 6 -5C8.5 -2 7 2 4.5 5.5C3 7.5 2 8.5 0 8.5Z" fill="currentColor"/>'
    '</g></defs>'
    '<path d="M30 17C29 9 30 5 33 3C35 1.5 38 2 39 4C37.5 3.2 35.5 3.5 35 5.5C34.3 8 35 12 33 17Z" fill="currentColor"/>'
    '<use href="#hb" transform="translate(32 53) scale(.9)"/><use href="#hb" transform="translate(26 47) rotate(-7) scale(.94)"/>'
    '<use href="#hb" transform="translate(38 47) rotate(7) scale(.94)"/><use href="#hb" transform="translate(21 40) rotate(-11)"/>'
    '<use href="#hb" transform="translate(43 40) rotate(11)"/><use href="#hb" transform="translate(32 41) rotate(2) scale(1.05)"/>'
    '<use href="#hb" transform="translate(18 32) rotate(-15) scale(1.06)"/><use href="#hb" transform="translate(46 32) rotate(15) scale(1.06)"/>'
    '<use href="#hb" transform="translate(32 32) scale(1.14)"/><use href="#hb" transform="translate(23 24) rotate(-14) scale(1.08)"/>'
    '<use href="#hb" transform="translate(41 24) rotate(14) scale(1.08)"/><use href="#hb" transform="translate(32 24) scale(1)"/>'
    '<use href="#hb" transform="translate(19 21) rotate(-38) scale(.98)"/><use href="#hb" transform="translate(45 21) rotate(38) scale(.98)"/>'
    '</svg>'
)

MARK_COFFEE = (
    '<svg viewBox="0 0 32 32" aria-hidden="true">'
    '<path d="M16 7c0-2 .8-3.4 2.4-4.2" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" opacity=".9"/>'
    '<path d="M16 6C11 8 8 12 8 17c0 5 3 9.5 8 12 5-2.5 8-7 8-12 0-5-3-9-8-11z" fill="currentColor" opacity=".95"/>'
    '<g fill="none" stroke="var(--bg)" stroke-width="1.1" stroke-linecap="round" opacity=".55">'
    '<path d="M16 8.5v18"/><path d="M11 13q5 3 10 0"/><path d="M10 18q6 3.2 12 0"/><path d="M11.5 23q4.5 2.6 9 0"/></g>'
    '</svg>'
)

# ---------------------------------------------------------------------------
# THE HUB REGISTRY — add a new field guide by appending one entry.
# ---------------------------------------------------------------------------

HUBS = [
    {
        "slug": "ipas",
        "src": "IPAs/site",
        "kicker": "Field Guide 01 · Beer",
        "title": "The IPA Knowledge Base",
        "blurb": (
            "From its contested 18th-century origins to the haze-clouded, "
            "thiol-driven frontier of modern brewing — history, styles, "
            "ingredients, the full brewing process, science &amp; sensory, and "
            "curated best-of lists."
        ),
        "accent": "#E6A93B",
        "accent2": "#F2C661",
        "mark": MARK_IPA,
        "art": ART_IPA,
        "stats": [("+150", "notes"), ("18", "IPA styles")],
    },
    {
        "slug": "pour-over",
        "src": "Pour Over Coffee/site",
        "kicker": "Field Guide 02 · Coffee",
        "title": "The Pour Over Knowledge Base",
        "blurb": (
            "From your first V60 to extraction theory, water chemistry, grind, "
            "and championship recipes — a complete manual-brewing manual for "
            "the first-time brewer and the competition barista alike."
        ),
        "accent": "#CE8A4F",
        "accent2": "#E0A877",
        "mark": MARK_COFFEE,
        "art": ART_COFFEE,
        "stats": [("+140", "notes"), ("26", "recipes")],
    },
]

# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


def render_tile(hub: dict) -> str:
    stats = "".join(
        f'<div class="stat"><b>{n}</b><span>{label}</span></div>'
        for n, label in hub["stats"]
    )
    mark_class = "tmark" + (" tmark-lg" if hub["slug"] == "ipas" else "")
    return f"""
      <a class="tile" href="{hub['slug']}/index.html"
         style="--accent:{hub['accent']};--accent2:{hub['accent2']}">
        <div class="tile-art">
          <div class="art-glow"></div>
          <svg viewBox="0 0 280 180" class="art" aria-hidden="true">{hub['art']}</svg>
        </div>
        <div class="tile-body">
          <div class="tile-kicker"><span class="{mark_class}">{hub['mark']}</span>{hub['kicker']}</div>
          <h2 class="tile-title">{hub['title']}</h2>
          <p class="tile-blurb">{hub['blurb']}</p>
          <div class="tile-stats">{stats}</div>
          <span class="tile-enter">Enter the hub
            <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h9M8.5 4 12.5 8 8.5 12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
        </div>
      </a>"""


GHOST_TILE = """
      <div class="tile tile-ghost" aria-hidden="true">
        <div class="ghost-mark">+</div>
        <h2 class="tile-title">More field guides in the making</h2>
        <p class="tile-blurb">Each hub is a deep, interlinked vault built for a single subject. New ones land here as they’re written.</p>
      </div>"""


def render_page() -> str:
    tiles = "".join(render_tile(h) for h in HUBS) + GHOST_TILE
    total_notes = sum(int(h["stats"][0][0]) for h in HUBS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Field Guides — a library of deep knowledge hubs</title>
<meta name="description" content="A growing library of deep, interlinked field guides — exhaustively researched knowledge hubs on the subjects worth going deep on.">
<meta property="og:title" content="Field Guides">
<meta property="og:description" content="A growing library of deep, interlinked knowledge hubs.">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..600;1,9..144,400&family=Inter:wght@400;500;600;700&family=Spline+Sans+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="aurora" aria-hidden="true"></div>
<header class="nav">
  <a class="wordmark" href="index.html">
    <svg viewBox="0 0 24 24" class="wordmark-mark" aria-hidden="true"><path d="M4 5.5h11M4 12h16M4 18.5h8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="19.5" cy="6" r="2.4" fill="currentColor"/></svg>
    <span>Field&nbsp;<b>Guides</b></span>
  </a>
  <span class="nav-tag">{len(HUBS)} hubs · {total_notes}+ notes</span>
</header>

<main>
  <section class="hero">
    <div class="hero-eyebrow">Library of Corey&rsquo;s Favorite Topics</div>
    <h1 class="hero-title">Field&nbsp;Guides</h1>
  </section>

  <section class="tiles">{tiles}
  </section>
</main>

<footer class="foot">
  <div class="foot-mark">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5h11M4 12h16M4 18.5h8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="19.5" cy="6" r="2.4" fill="currentColor"/></svg>
    <b>Field Guides</b>
  </div>
  <p>A personal library of deep, interlinked knowledge hubs.</p>
  <p class="foot-fine">Designed &amp; built with <a href="https://claude.com/claude-code">Claude&nbsp;Code</a></p>
</footer>
</body>
</html>
"""


CSS = """
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#0E0B07; --bg-2:#16110A;
  --panel:#191309; --panel-2:#1F1810;
  --ink:#F4EBD7; --ink-2:#CCBD9F; --ink-3:#9A8A6C;
  --border:rgba(245,233,206,.10); --border-2:rgba(245,233,206,.18);
  --gold:#E6A93B;
  --serif:"Fraunces",Georgia,serif;
  --sans:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --mono:"Spline Sans Mono",ui-monospace,Menlo,monospace;
}
html{scroll-behavior:smooth}
body{
  font-family:var(--sans);background:var(--bg);color:var(--ink);
  font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased;
  min-height:100vh;overflow-x:hidden;position:relative;
}
a{color:inherit;text-decoration:none}
::selection{background:rgba(230,169,59,.3)}

/* ambient backdrop */
.aurora{
  position:fixed;inset:0;z-index:-1;pointer-events:none;
  background:
    radial-gradient(680px 460px at 18% -6%, rgba(230,169,59,.16), transparent 70%),
    radial-gradient(620px 480px at 88% 8%, rgba(206,138,79,.15), transparent 70%),
    radial-gradient(900px 700px at 50% 120%, rgba(230,169,59,.07), transparent 70%),
    linear-gradient(180deg,var(--bg),var(--bg-2));
}
.aurora::after{
  content:"";position:absolute;inset:0;opacity:.5;
  background-image:radial-gradient(rgba(245,233,206,.035) 1px,transparent 1px);
  background-size:46px 46px;mask-image:radial-gradient(80% 60% at 50% 30%,#000,transparent);
}

/* nav */
.nav{
  max-width:1120px;margin:0 auto;padding:26px 28px;
  display:flex;align-items:center;justify-content:space-between;gap:16px;
}
.wordmark{display:flex;align-items:center;gap:10px;font-family:var(--serif);
  font-size:1.18rem;letter-spacing:.01em;color:var(--ink)}
.wordmark b{font-weight:600}
.wordmark-mark{width:24px;height:24px;color:var(--gold)}
.nav-tag{font-family:var(--mono);font-size:.72rem;letter-spacing:.04em;
  color:var(--ink-3);padding:6px 11px;border:1px solid var(--border);border-radius:999px}

/* hero */
main{max-width:1120px;margin:0 auto;padding:0 28px 30px}
.hero{text-align:center;padding:54px 0 46px;max-width:760px;margin:0 auto}
.hero-eyebrow{
  font-family:var(--mono);font-size:.76rem;letter-spacing:.22em;text-transform:uppercase;
  color:var(--gold);margin-bottom:22px;
}
.hero-title{
  font-family:var(--serif);font-weight:500;letter-spacing:-.02em;line-height:.96;
  font-size:clamp(3.4rem,11vw,6.4rem);
  background:linear-gradient(180deg,#FBF3DF 12%,#E6C27E 92%);
  -webkit-background-clip:text;background-clip:text;color:transparent;
}
/* tile grid */
.tiles{
  display:grid;grid-template-columns:repeat(2,1fr);gap:26px;margin-top:18px;
}

/* hub tile */
.tile{
  position:relative;display:flex;flex-direction:column;overflow:hidden;
  background:linear-gradient(180deg,var(--panel-2),var(--panel));
  border:1px solid var(--border);border-radius:24px;isolation:isolate;
  transition:transform .4s cubic-bezier(.2,.7,.2,1),border-color .4s,box-shadow .4s;
  --art-ink:rgba(246,236,213,.9); --art-fill:var(--accent);
  --art-foam:#F4EBD7; --art-glass:rgba(246,236,213,.05);
}
.tile::before{
  content:"";position:absolute;inset:0;z-index:-1;opacity:0;transition:opacity .4s;
  background:radial-gradient(120% 80% at 50% -10%,
    color-mix(in srgb,var(--accent) 26%,transparent),transparent 60%);
}
.tile:hover{
  transform:translateY(-6px);
  border-color:color-mix(in srgb,var(--accent) 50%,var(--border-2));
  box-shadow:0 30px 70px -30px rgba(0,0,0,.8),
             0 0 0 1px color-mix(in srgb,var(--accent) 22%,transparent) inset;
}
.tile:hover::before{opacity:1}
.tile:focus-visible{outline:2px solid var(--accent);outline-offset:3px}

.tile-art{
  position:relative;height:188px;display:grid;place-items:center;overflow:hidden;
  border-bottom:1px solid var(--border);
  background:
    radial-gradient(90% 130% at 50% -30%,color-mix(in srgb,var(--accent) 13%,transparent),transparent 70%),
    linear-gradient(180deg,rgba(0,0,0,.12),transparent);
}
.art-glow{
  position:absolute;width:230px;height:230px;border-radius:50%;
  background:radial-gradient(circle,color-mix(in srgb,var(--accent) 30%,transparent),transparent 65%);
  filter:blur(8px);transition:transform .5s,opacity .5s;opacity:.65;
}
.tile:hover .art-glow{transform:scale(1.12);opacity:.9}
.art{position:relative;width:230px;height:auto;color:var(--accent)}
.tile:hover .art{animation:floaty 4s ease-in-out infinite}
@keyframes floaty{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}

.tile-body{padding:26px 28px 28px;display:flex;flex-direction:column;flex:1}
.tile-kicker{
  display:flex;align-items:center;gap:8px;
  font-family:var(--mono);font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;
  color:color-mix(in srgb,var(--accent) 70%,var(--ink-2));margin-bottom:13px;
}
.tmark{width:17px;height:17px;display:grid;place-items:center;color:var(--accent);flex:none}
.tmark svg{width:100%;height:100%}
.tmark-lg{width:19px;height:19px}
.tile-title{font-family:var(--serif);font-weight:500;font-size:1.62rem;
  letter-spacing:-.01em;line-height:1.12;color:var(--ink)}
.tile-blurb{margin-top:11px;color:var(--ink-2);font-size:.96rem;line-height:1.66}
.tile-stats{display:flex;gap:10px;margin-top:20px;flex-wrap:wrap}
.stat{
  display:flex;align-items:baseline;gap:5px;padding:6px 12px;border-radius:999px;
  background:rgba(245,233,206,.04);border:1px solid var(--border);
}
.stat b{font-family:var(--serif);font-weight:600;font-size:1rem;color:var(--ink)}
.stat span{font-size:.76rem;color:var(--ink-3)}
.tile-enter{
  margin-top:auto;padding-top:22px;display:inline-flex;align-items:center;gap:8px;
  font-weight:600;font-size:.94rem;color:var(--accent);
}
.tile-enter svg{width:16px;height:16px;transition:transform .3s}
.tile:hover .tile-enter svg{transform:translateX(5px)}

/* ghost / coming-soon */
.tile-ghost{
  grid-column:1/-1;flex-direction:row;align-items:center;gap:22px;
  padding:30px 32px;background:none;border-style:dashed;cursor:default;
}
.tile-ghost:hover{transform:none;border-color:var(--border);box-shadow:none}
.tile-ghost::before{display:none}
.tile-ghost .tile-title{font-size:1.28rem}
.tile-ghost .tile-blurb{margin-top:5px;max-width:560px}
.ghost-mark{
  width:54px;height:54px;flex:none;display:grid;place-items:center;border-radius:16px;
  border:1px dashed var(--border-2);font-family:var(--serif);font-size:1.9rem;
  color:var(--ink-3);line-height:1;
}

/* footer */
.foot{max-width:1120px;margin:34px auto 0;padding:40px 28px 56px;
  border-top:1px solid var(--border);text-align:center;color:var(--ink-3)}
.foot-mark{display:inline-flex;align-items:center;gap:9px;font-family:var(--serif);
  font-size:1.08rem;color:var(--ink-2);margin-bottom:10px}
.foot-mark svg{width:20px;height:20px;color:var(--gold)}
.foot-mark b{font-weight:600}
.foot p{font-size:.92rem}
.foot-fine{margin-top:8px;font-family:var(--mono);font-size:.76rem;letter-spacing:.03em;color:var(--ink-3)}
.foot-fine a{color:var(--ink-2);border-bottom:1px solid var(--border-2);transition:color .2s}
.foot-fine a:hover{color:var(--gold)}

/* entrance */
.hero,.tile{animation:rise .7s cubic-bezier(.2,.7,.2,1) both}
.tiles .tile:nth-child(1){animation-delay:.06s}
.tiles .tile:nth-child(2){animation-delay:.14s}
.tiles .tile:nth-child(3){animation-delay:.22s}
@keyframes rise{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){
  *{animation:none!important;transition:none!important}
}

/* responsive */
@media (max-width:760px){
  .tiles{grid-template-columns:1fr}
  .tile-ghost{flex-direction:column;text-align:center;align-items:center}
  .nav-tag{display:none}
}
"""


# ---------------------------------------------------------------------------
# Portal back-link — injected into every hub page's sidebar at assembly time.
# Lives here (not in the hub generators) because the portal only exists in the
# deployed docs/ tree; "../index.html" resolves to docs/index.html from any
# hub page. Re-injected on every build since each copy starts from pristine
# source, so it never duplicates.
# ---------------------------------------------------------------------------

NAV_MARKER = "</nav></aside>"

BACKLINK_HTML = (
    '<a class="nav-home" href="../index.html">'
    '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M13 8H3M7.5 4 3 8l4.5 4" '
    'fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
    'stroke-linejoin="round"/></svg>'
    '<span>All Field Guides<span class="nh-sub">Back to the library</span></span></a>'
)

BACKLINK_CSS = """
/* --- Field Guides portal back-link (injected by build_landing.py) --- */
.nav-home{display:flex;align-items:center;gap:10px;margin:18px 8px 6px;padding:11px 12px;
  border:1px solid var(--border);border-radius:11px;color:var(--ink-2);
  font-weight:600;font-size:.86rem;line-height:1.15;
  transition:background .15s,border-color .15s,color .15s}
.nav-home:hover{background:var(--surface-2);border-color:var(--border-2);color:var(--accent)}
.nav-home svg{width:15px;height:15px;flex:none}
.nav-home .nh-sub{display:block;font-weight:500;font-size:.71rem;color:var(--ink-3);
  font-family:var(--mono);letter-spacing:.02em;margin-top:1px}
"""


def inject_backlink(dest: Path) -> None:
    """Add the portal back-link to every page sidebar and theme its CSS."""
    css = dest / "assets" / "style.css"
    if css.is_file() and ".nav-home{" not in css.read_text(encoding="utf-8"):
        with css.open("a", encoding="utf-8") as fh:
            fh.write(BACKLINK_CSS)
    for page in dest.glob("*.html"):
        text = page.read_text(encoding="utf-8")
        if NAV_MARKER in text and 'class="nav-home"' not in text:
            page.write_text(text.replace(NAV_MARKER, BACKLINK_HTML + NAV_MARKER, 1),
                            encoding="utf-8")


def copy_hub(hub: dict) -> int:
    src = ROOT / hub["src"]
    if not src.is_dir():
        raise SystemExit(f"!! source site not found: {src}")
    dest = DOCS / hub["slug"]
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)
    inject_backlink(dest)
    return sum(1 for _ in dest.glob("*.html"))


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    # GitHub Pages: skip Jekyll processing so nothing gets rewritten.
    (DOCS / ".nojekyll").write_text("")

    for hub in HUBS:
        n = copy_hub(hub)
        print(f"  copied {hub['src']:<28} -> docs/{hub['slug']}/  ({n} pages)")

    (DOCS / "index.html").write_text(render_page(), encoding="utf-8")
    print(f"  wrote  docs/index.html  ({len(HUBS)} hubs)")
    print("\nDone. Preview:  python3 -m http.server -d docs 8000  ->  http://localhost:8000/")


if __name__ == "__main__":
    main()
