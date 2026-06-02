# -*- coding: utf-8 -*-
"""
diagrams.py — hand-crafted SVG illustrations and infographics
for the IPA Knowledge Base site.

Exports:
  ILLUSTRATIONS[folder]            -> SVG inner markup (currentColor = domain color)
  PAGE_DIAGRAMS[slug]              -> HTML block injected after the page's intro paragraph
  FAMILY_TREE_SVG                  -> replacement for the IPA Family Tree ASCII fence
  vital_signs(stats, hops_html)    -> HTML for the style "Vital signs" panel
  srm_to_hex(srm)                  -> approximate beer color for an SRM value
"""

import re
import math


# ---------------------------------------------------------------- colors
_SRM_TABLE = [
    (1,  "#F5EE9E"), (2,  "#F3DC6F"), (3,  "#EFC94C"),
    (4,  "#ECB73A"), (6,  "#E6A11E"), (8,  "#DE8B0B"),
    (10, "#D17806"), (13, "#BE6300"), (17, "#A65100"),
    (20, "#8E3F00"), (24, "#722E00"), (29, "#572100"),
    (35, "#3A1500"), (40, "#1F0B00"),
]


def srm_to_hex(srm):
    """Approximate SRM → beer-color hex via piecewise linear interpolation."""
    try:
        srm = float(srm)
    except (TypeError, ValueError):
        return "#E6A11E"
    if srm <= _SRM_TABLE[0][0]:
        return _SRM_TABLE[0][1]
    if srm >= _SRM_TABLE[-1][0]:
        return _SRM_TABLE[-1][1]
    for (a, ah), (b, bh) in zip(_SRM_TABLE, _SRM_TABLE[1:]):
        if a <= srm <= b:
            t = (srm - a) / (b - a)
            ar, ag, ab = int(ah[1:3], 16), int(ah[3:5], 16), int(ah[5:7], 16)
            br, bg, bb_ = int(bh[1:3], 16), int(bh[3:5], 16), int(bh[5:7], 16)
            r = round(ar + t * (br - ar))
            g = round(ag + t * (bg - ag))
            bl = round(ab + t * (bb_ - ab))
            return f"#{r:02X}{g:02X}{bl:02X}"
    return "#E6A11E"


# ================================================================
# DOMAIN ILLUSTRATIONS
# 10 hand-drawn flat SVG motifs. currentColor = domain accent.
# Sit in a 280x180 viewBox; CSS provides --il-ink, --il-paper,
# --il-foam, --il-glass for theme-aware neutrals.
# ================================================================

def _wrap(inner, color):
    return (
        f'<svg viewBox="0 0 280 180" class="d-ill" '
        f'style="color:{color}" xmlns="http://www.w3.org/2000/svg" '
        f'aria-hidden="true">'
        f'<circle cx="140" cy="92" r="76" fill="currentColor" opacity=".12"/>'
        + inner + '</svg>'
    )


# 1. Introduction — pint glass with foam
_INTRO = '''
<ellipse cx="140" cy="166" rx="76" ry="7" fill="var(--il-ink)" opacity=".18"/>
<path d="M96 48 L188 48 L181 158 L103 158 Z" fill="var(--il-glass)"/>
<path d="M101 60 L183 60 L177 152 L107 152 Z" fill="var(--il-beer)"/>
<path d="M96 48 q7 -11 14 -2 q7 -10 14 -2 q7 -11 14 -2 q7 -10 14 -2 q7 -11 14 -2 q7 -10 12 -2"
   fill="var(--il-foam)" stroke="var(--il-ink)" stroke-width="2.5" stroke-linejoin="round"/>
<path d="M111 70 L107 144" stroke="var(--il-foam)" stroke-width="3.2" stroke-linecap="round" opacity=".7"/>
<circle cx="165" cy="100" r="3.4" fill="var(--il-foam)" opacity=".85"/>
<circle cx="158" cy="86" r="2.4" fill="var(--il-foam)" opacity=".7"/>
<circle cx="170" cy="118" r="2.6" fill="var(--il-foam)" opacity=".75"/>
<path d="M96 48 L188 48 L181 158 L103 158 Z" fill="none" stroke="var(--il-ink)" stroke-width="2.6" stroke-linejoin="round"/>
'''

# 2. History — clipper ship + sun
_HISTORY = '''
<circle cx="200" cy="74" r="22" fill="currentColor" opacity=".5"/>
<circle cx="200" cy="74" r="22" fill="none" stroke="var(--il-ink)" stroke-width="2.2"/>
<g stroke="var(--il-ink)" stroke-width="2.2" stroke-linecap="round" fill="none" opacity=".7">
  <line x1="200" y1="40" x2="200" y2="46"/><line x1="200" y1="102" x2="200" y2="108"/>
  <line x1="166" y1="74" x2="172" y2="74"/><line x1="228" y1="74" x2="234" y2="74"/>
  <line x1="178" y1="52" x2="182" y2="56"/><line x1="218" y1="92" x2="222" y2="96"/>
  <line x1="222" y1="52" x2="218" y2="56"/><line x1="182" y1="92" x2="178" y2="96"/>
</g>
<path d="M70 132 L210 132 L196 152 L84 152 Z" fill="currentColor" opacity=".6"/>
<path d="M70 132 L210 132 L196 152 L84 152 Z" fill="none" stroke="var(--il-ink)" stroke-width="2.6" stroke-linejoin="round"/>
<line x1="105" y1="56" x2="105" y2="132" stroke="var(--il-ink)" stroke-width="2.4" stroke-linecap="round"/>
<line x1="150" y1="48" x2="150" y2="132" stroke="var(--il-ink)" stroke-width="2.4" stroke-linecap="round"/>
<path d="M105 60 L138 86 L105 86 Z" fill="var(--il-foam)" stroke="var(--il-ink)" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M105 92 L142 122 L105 122 Z" fill="var(--il-foam)" stroke="var(--il-ink)" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M150 52 L182 86 L150 86 Z" fill="var(--il-foam)" stroke="var(--il-ink)" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M150 92 L186 122 L150 122 Z" fill="var(--il-foam)" stroke="var(--il-ink)" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M40 160 q24 -10 48 0 t48 0 t48 0 t48 0" fill="none"
  stroke="var(--il-ink)" stroke-width="2.2" stroke-linecap="round" opacity=".5"/>
'''

# 3. Styles — three taster glasses
def _taster(x, fill):
    return (
        f'<path d="M{x-18} 70 L{x+18} 70 L{x+12} 138 L{x-12} 138 Z" fill="var(--il-glass)"/>'
        f'<path d="M{x-15} 84 L{x+15} 84 L{x+11} 134 L{x-11} 134 Z" fill="{fill}"/>'
        f'<line x1="{x}" y1="138" x2="{x}" y2="148" stroke="var(--il-ink)" stroke-width="2.4" stroke-linecap="round"/>'
        f'<ellipse cx="{x}" cy="152" rx="13" ry="3" fill="var(--il-ink)" opacity=".18"/>'
        f'<path d="M{x-18} 70 L{x+18} 70 L{x+12} 138 L{x-12} 138 Z" fill="none" stroke="var(--il-ink)" stroke-width="2.5" stroke-linejoin="round"/>'
    )
_STYLES = (
    _taster(78,  "#F0CB52") +
    _taster(140, "#D58108") +
    _taster(202, "#6B3000")
)

# 4. Ingredients — hop cone
_INGREDIENTS = '''
<path d="M140 40 q-2 6 -2 12" fill="none" stroke="var(--il-ink)" stroke-width="2.4" stroke-linecap="round"/>
<path d="M125 50 q5 -2 14 2" fill="none" stroke="var(--il-ink)" stroke-width="2.4" stroke-linecap="round"/>
<g fill="currentColor" stroke="var(--il-ink)" stroke-width="2.2" stroke-linejoin="round">
  <ellipse cx="140" cy="100" rx="38" ry="48"/>
</g>
<g fill="none" stroke="var(--il-ink)" stroke-width="1.8" opacity=".75">
  <path d="M108 84 q32 14 64 0"/>
  <path d="M104 100 q36 16 72 0"/>
  <path d="M108 116 q32 14 64 0"/>
  <path d="M114 130 q26 12 52 0"/>
  <path d="M140 56 v90"/>
  <path d="M120 64 q20 28 0 76"/>
  <path d="M160 64 q-20 28 0 76"/>
</g>
<path d="M174 70 q14 -10 22 4 q-12 6 -22 -4" fill="var(--il-paper)" stroke="var(--il-ink)" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M106 70 q-14 -10 -22 4 q12 6 22 -4" fill="var(--il-paper)" stroke="var(--il-ink)" stroke-width="2.2" stroke-linejoin="round"/>
'''

# 5. Brewing — kettle with steam
_BREWING = '''
<g fill="none" stroke="var(--il-ink)" stroke-width="2.4" stroke-linecap="round" opacity=".75">
  <path d="M118 38 q6 -8 0 -16"/>
  <path d="M140 32 q6 -8 0 -16"/>
  <path d="M162 38 q6 -8 0 -16"/>
</g>
<rect x="86" y="60" width="108" height="80" rx="14" fill="currentColor"/>
<rect x="86" y="60" width="108" height="80" rx="14" fill="none" stroke="var(--il-ink)" stroke-width="2.6"/>
<rect x="84" y="56" width="112" height="10" rx="5" fill="var(--il-paper)" stroke="var(--il-ink)" stroke-width="2.4"/>
<ellipse cx="140" cy="80" rx="46" ry="9" fill="var(--il-beer)" opacity=".95"/>
<path d="M194 86 q14 0 14 16 q0 16 -14 16" fill="none" stroke="var(--il-ink)" stroke-width="2.6"/>
<line x1="100" y1="140" x2="96" y2="158" stroke="var(--il-ink)" stroke-width="2.6" stroke-linecap="round"/>
<line x1="180" y1="140" x2="184" y2="158" stroke="var(--il-ink)" stroke-width="2.6" stroke-linecap="round"/>
<rect x="106" y="92" width="20" height="6" rx="2" fill="var(--il-paper)" opacity=".7"/>
'''

# 6. Science — flask with molecule
_SCIENCE = '''
<g stroke="var(--il-ink)" stroke-width="2.2" stroke-linecap="round" fill="none">
  <line x1="86" y1="42" x2="118" y2="58"/>
  <line x1="118" y1="58" x2="156" y2="44"/>
  <line x1="156" y1="44" x2="184" y2="60"/>
</g>
<circle cx="86" cy="42" r="7" fill="var(--il-paper)" stroke="var(--il-ink)" stroke-width="2.2"/>
<circle cx="118" cy="58" r="7" fill="currentColor" stroke="var(--il-ink)" stroke-width="2.2"/>
<circle cx="156" cy="44" r="7" fill="currentColor" stroke="var(--il-ink)" stroke-width="2.2"/>
<circle cx="184" cy="60" r="7" fill="var(--il-paper)" stroke="var(--il-ink)" stroke-width="2.2"/>
<rect x="128" y="74" width="20" height="22" fill="var(--il-paper)" stroke="var(--il-ink)" stroke-width="2.2"/>
<path d="M120 96 L118 110 q-22 14 -22 32 q0 16 16 16 h56 q16 0 16 -16 q0 -18 -22 -32 L160 96 Z"
  fill="currentColor"/>
<path d="M120 96 L118 110 q-22 14 -22 32 q0 16 16 16 h56 q16 0 16 -16 q0 -18 -22 -32 L160 96 Z"
  fill="none" stroke="var(--il-ink)" stroke-width="2.6" stroke-linejoin="round"/>
<ellipse cx="140" cy="146" rx="34" ry="6" fill="var(--il-beer)"/>
<circle cx="128" cy="138" r="3" fill="var(--il-foam)" opacity=".9"/>
<circle cx="148" cy="132" r="2.4" fill="var(--il-foam)" opacity=".9"/>
<circle cx="156" cy="142" r="2" fill="var(--il-foam)" opacity=".8"/>
'''

# 7. Drinking — two tulip glasses clinking
def _tulip(cx, lean):
    return (
        f'<g transform="translate({cx} 90) rotate({lean})">'
        f'<path d="M-22 -34 q0 24 8 36 q4 6 4 16 v22 h20 v-22 q0 -10 4 -16 q8 -12 8 -36 Z" fill="var(--il-glass)"/>'
        f'<path d="M-18 -22 q0 18 6 28 q4 6 4 12 v14 h16 v-14 q0 -6 4 -12 q6 -10 6 -28 Z" fill="var(--il-beer)"/>'
        f'<path d="M-22 -34 q0 24 8 36 q4 6 4 16 v22 h20 v-22 q0 -10 4 -16 q8 -12 8 -36 Z" fill="none" stroke="var(--il-ink)" stroke-width="2.5" stroke-linejoin="round"/>'
        f'<line x1="0" y1="40" x2="0" y2="50" stroke="var(--il-ink)" stroke-width="2.4" stroke-linecap="round"/>'
        f'<ellipse cx="0" cy="54" rx="14" ry="3" fill="var(--il-ink)" opacity=".2"/>'
        f'</g>'
    )
_DRINKING = (
    '<g stroke="currentColor" stroke-width="2.5" stroke-linecap="round" fill="none" opacity=".85">'
    '<path d="M132 38 q4 6 0 12"/><path d="M148 38 q-4 6 0 12"/>'
    '<path d="M140 28 v12"/>'
    '</g>'
    + _tulip(96, -14) + _tulip(184, 14)
    + '<g fill="currentColor"><circle cx="140" cy="74" r="3"/>'
    '<circle cx="128" cy="68" r="2"/><circle cx="152" cy="68" r="2"/></g>'
)

# 8. Best — medal with ribbon
_BEST = '''
<path d="M104 36 L122 36 L138 80 L120 80 Z" fill="currentColor" opacity=".85"/>
<path d="M104 36 L122 36 L138 80 L120 80 Z" fill="none" stroke="var(--il-ink)" stroke-width="2.4" stroke-linejoin="round"/>
<path d="M176 36 L158 36 L142 80 L160 80 Z" fill="currentColor" opacity=".85"/>
<path d="M176 36 L158 36 L142 80 L160 80 Z" fill="none" stroke="var(--il-ink)" stroke-width="2.4" stroke-linejoin="round"/>
<circle cx="140" cy="110" r="40" fill="var(--il-paper)" stroke="var(--il-ink)" stroke-width="2.6"/>
<circle cx="140" cy="110" r="30" fill="currentColor"/>
<circle cx="140" cy="110" r="30" fill="none" stroke="var(--il-ink)" stroke-width="2.2"/>
<path d="M140 92 L144 106 L158 108 L148 118 L150 132 L140 124 L130 132 L132 118 L122 108 L136 106 Z"
  fill="var(--il-foam)" stroke="var(--il-ink)" stroke-width="2" stroke-linejoin="round"/>
'''

# 9. Industry — three fermentation tanks
def _tank(x, color="currentColor"):
    return (
        f'<rect x="{x-18}" y="46" width="36" height="74" rx="8" fill="{color}"/>'
        f'<path d="M{x-18} 120 L{x} 152 L{x+18} 120 Z" fill="{color}"/>'
        f'<rect x="{x-18}" y="46" width="36" height="74" rx="8" fill="none" stroke="var(--il-ink)" stroke-width="2.4"/>'
        f'<path d="M{x-18} 120 L{x} 152 L{x+18} 120 Z" fill="none" stroke="var(--il-ink)" stroke-width="2.4" stroke-linejoin="round"/>'
        f'<ellipse cx="{x}" cy="46" rx="18" ry="5" fill="var(--il-paper)" stroke="var(--il-ink)" stroke-width="2.2"/>'
        f'<circle cx="{x}" cy="78" r="3" fill="var(--il-paper)"/>'
        f'<rect x="{x-7}" y="92" width="14" height="3" fill="var(--il-paper)" opacity=".7"/>'
    )
_INDUSTRY = (
    _tank(86) + _tank(140) + _tank(194) +
    '<line x1="60" y1="156" x2="220" y2="156" stroke="var(--il-ink)" stroke-width="2.4" stroke-linecap="round"/>'
)

# 10. Reference — stack of books
_REFERENCE = '''
<rect x="64" y="120" width="156" height="22" rx="2" fill="currentColor"/>
<rect x="64" y="120" width="156" height="22" rx="2" fill="none" stroke="var(--il-ink)" stroke-width="2.4"/>
<line x1="76" y1="120" x2="76" y2="142" stroke="var(--il-ink)" stroke-width="2" opacity=".5"/>
<line x1="208" y1="120" x2="208" y2="142" stroke="var(--il-ink)" stroke-width="2" opacity=".5"/>

<rect x="78" y="92" width="130" height="22" rx="2" fill="var(--il-paper)"/>
<rect x="78" y="92" width="130" height="22" rx="2" fill="none" stroke="var(--il-ink)" stroke-width="2.4"/>
<line x1="90" y1="92" x2="90" y2="114" stroke="var(--il-ink)" stroke-width="2" opacity=".5"/>

<rect x="58" y="64" width="160" height="22" rx="2" fill="var(--il-beer)"/>
<rect x="58" y="64" width="160" height="22" rx="2" fill="none" stroke="var(--il-ink)" stroke-width="2.4"/>
<line x1="70" y1="64" x2="70" y2="86" stroke="var(--il-ink)" stroke-width="2" opacity=".4"/>

<path d="M198 64 L198 102 L188 92 L178 102 L178 64 Z"
  fill="var(--il-foam)" stroke="var(--il-ink)" stroke-width="2.2" stroke-linejoin="round"/>
'''


# ----------------------------------------------------------------------
# Coffee-specific domain motifs (replace the beer art above)
# ----------------------------------------------------------------------

# Pour-over dripper + cup + falling droplet
_DRIPPER = '''
<rect x="92" y="52" width="96" height="9" rx="4" fill="var(--il-paper)" stroke="var(--il-ink)" stroke-width="2.4"/>
<path d="M96 61 L184 61 L150 116 L130 116 Z" fill="var(--il-paper)"/>
<path d="M105 69 L175 69 L150 106 L130 106 Z" fill="currentColor" opacity=".6"/>
<path d="M96 61 L184 61 L150 116 L130 116 Z" fill="none" stroke="var(--il-ink)" stroke-width="2.6" stroke-linejoin="round"/>
<path d="M140 120 q-5 8 0 13 q5 -5 0 -13 Z" fill="var(--il-beer)" stroke="var(--il-ink)" stroke-width="1.6"/>
<path d="M112 134 L168 134 L162 158 L118 158 Z" fill="var(--il-glass)" stroke="var(--il-ink)" stroke-width="2.6" stroke-linejoin="round"/>
<path d="M168 138 q15 0 15 11 q0 9 -13 9" fill="none" stroke="var(--il-ink)" stroke-width="2.4"/>
<ellipse cx="140" cy="134" rx="28" ry="5" fill="var(--il-beer)"/>
'''

# Gooseneck kettle
_KETTLE = '''
<path d="M96 98 q0 -10 10 -10 h60 q10 0 10 10 v36 q0 14 -14 14 h-52 q-14 0 -14 -14 Z" fill="currentColor" stroke="var(--il-ink)" stroke-width="2.6" stroke-linejoin="round"/>
<path d="M168 102 q28 0 28 -28 q0 -16 -12 -22" fill="none" stroke="var(--il-ink)" stroke-width="3" stroke-linecap="round"/>
<rect x="110" y="80" width="50" height="9" rx="4" fill="var(--il-paper)" stroke="var(--il-ink)" stroke-width="2.4"/>
<circle cx="135" cy="74" r="4" fill="var(--il-paper)" stroke="var(--il-ink)" stroke-width="2.2"/>
<path d="M96 106 q-18 5 -18 24" fill="none" stroke="var(--il-ink)" stroke-width="2.8" stroke-linecap="round"/>
<ellipse cx="138" cy="152" rx="34" ry="5" fill="var(--il-ink)" opacity=".15"/>
'''

# Two coffee beans
_BEANS = '''
<g stroke="var(--il-ink)" stroke-width="2.5">
<ellipse cx="116" cy="98" rx="26" ry="34" fill="currentColor" transform="rotate(-22 116 98)"/>
<ellipse cx="170" cy="106" rx="24" ry="32" fill="currentColor" opacity=".82" transform="rotate(16 170 106)"/>
</g>
<path d="M116 66 q-7 32 0 64" fill="none" stroke="var(--il-ink)" stroke-width="2.2" transform="rotate(-22 116 98)"/>
<path d="M170 76 q-7 30 0 60" fill="none" stroke="var(--il-ink)" stroke-width="2.2" transform="rotate(16 170 106)"/>
<ellipse cx="142" cy="150" rx="40" ry="6" fill="var(--il-ink)" opacity=".14"/>
'''

# Hand grinder with crank
_GRINDER = '''
<line x1="140" y1="68" x2="140" y2="46" stroke="var(--il-ink)" stroke-width="2.6" stroke-linecap="round"/>
<path d="M140 46 h26 q6 0 6 7" fill="none" stroke="var(--il-ink)" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="172" cy="59" r="6" fill="var(--il-foam)" stroke="var(--il-ink)" stroke-width="2.2"/>
<rect x="108" y="70" width="64" height="72" rx="11" fill="currentColor" stroke="var(--il-ink)" stroke-width="2.6"/>
<rect x="108" y="100" width="64" height="7" fill="var(--il-paper)" opacity=".75"/>
<rect x="126" y="120" width="28" height="14" rx="3" fill="var(--il-paper)" stroke="var(--il-ink)" stroke-width="2"/>
<ellipse cx="140" cy="148" rx="34" ry="6" fill="var(--il-ink)" opacity=".15"/>
'''

# Water droplet
_DROP = '''
<path d="M140 48 q-32 42 -32 66 a32 32 0 0 0 64 0 q0 -24 -32 -66 Z" fill="currentColor" opacity=".7" stroke="var(--il-ink)" stroke-width="2.6" stroke-linejoin="round"/>
<path d="M126 110 a16 16 0 0 0 10 14" fill="none" stroke="var(--il-foam)" stroke-width="3.2" stroke-linecap="round" opacity=".85"/>
'''

# Coffee mug with steam
_MUG = '''
<path d="M104 78 h58 v46 q0 16 -16 16 h-26 q-16 0 -16 -16 Z" fill="currentColor" stroke="var(--il-ink)" stroke-width="2.6" stroke-linejoin="round"/>
<path d="M162 90 q24 0 24 17 q0 17 -24 17" fill="none" stroke="var(--il-ink)" stroke-width="2.6"/>
<ellipse cx="133" cy="78" rx="29" ry="6" fill="var(--il-beer)" stroke="var(--il-ink)" stroke-width="2.2"/>
<g fill="none" stroke="var(--il-ink)" stroke-width="2.2" stroke-linecap="round" opacity=".6">
<path d="M120 64 q6 -9 0 -18"/><path d="M133 64 q6 -9 0 -18"/><path d="M146 64 q6 -9 0 -18"/>
</g>
<ellipse cx="138" cy="148" rx="34" ry="5" fill="var(--il-ink)" opacity=".15"/>
'''

# Cupping bowl with spoon and aroma
_CUPPING = '''
<g fill="none" stroke="var(--il-ink)" stroke-width="2.2" stroke-linecap="round" opacity=".55">
<path d="M122 76 q6 -9 0 -18"/><path d="M140 72 q6 -9 0 -18"/><path d="M158 76 q6 -9 0 -18"/>
</g>
<path d="M90 96 a50 32 0 0 0 100 0 Z" fill="currentColor" stroke="var(--il-ink)" stroke-width="2.6" stroke-linejoin="round"/>
<ellipse cx="140" cy="96" rx="50" ry="15" fill="var(--il-beer)" stroke="var(--il-ink)" stroke-width="2.4"/>
<ellipse cx="178" cy="78" rx="15" ry="8" fill="var(--il-paper)" stroke="var(--il-ink)" stroke-width="2.2" transform="rotate(30 178 78)"/>
<line x1="189" y1="70" x2="214" y2="50" stroke="var(--il-ink)" stroke-width="2.4" stroke-linecap="round"/>
'''


def domain_illustration(folder, color):
    inner = {
        "01_introduction":            _DRIPPER,
        "02_history":                 _HISTORY,
        "03_equipment":               _KETTLE,
        "04_coffee_beans":            _BEANS,
        "05_grinding":                _GRINDER,
        "06_water":                   _DROP,
        "07_brewing_technique":       _DRIPPER,
        "08_recipes":                 _MUG,
        "09_science_and_extraction":  _SCIENCE,
        "10_tasting_and_sensory":     _CUPPING,
        "11_culture_and_industry":    _INDUSTRY,
        "12_reference":               _REFERENCE,
    }.get(folder, _DRIPPER)
    return _wrap(inner, color)


# ================================================================
# FAMILY TREE  (refined SVG; replaces the ASCII fence in Brew Method Family Tree.md)
# ================================================================

def _ft_node(x, y, w, label, slug, sub=False, root=False):
    h = 46
    rx = x - w / 2
    if root:
        cls = "ft-node ft-root"
        rect = (f'<rect x="{rx}" y="{y-h/2}" width="{w}" height="{h}" '
                f'rx="11" class="ft-rect"/>')
        text = f'<text x="{x}" y="{y+1}" class="ft-label">{label}</text>'
        return f'<g class="{cls}">{rect}{text}</g>'
    cls = "ft-node ft-sub" if sub else "ft-node"
    rect = f'<rect x="{rx}" y="{y-h/2}" width="{w}" height="{h}" rx="11" class="ft-rect"/>'
    text = f'<text x="{x}" y="{y+1}" class="ft-label">{label}</text>'
    if slug is None:
        # category node with no page of its own — render unlinked
        return f'<g class="{cls} ft-static">{rect}{text}</g>'
    return f'<a href="{slug}.html" class="{cls}">{rect}{text}</a>'


FAMILY_TREE_SVG = (
    '<figure class="diagram diagram-tree">'
    '<svg viewBox="0 0 960 380" class="ftree" '
    'xmlns="http://www.w3.org/2000/svg" role="img" '
    'aria-label="The coffee brew-method family tree — percolation, hybrid, '
    'and immersion methods and the brewers in each branch">'
    # root -> three branches
    '<path class="ft-line" d="M480 65 L480 90 L180 90 L180 115"/>'
    '<path class="ft-line" d="M480 90 L480 115"/>'
    '<path class="ft-line" d="M480 90 L780 90 L780 115"/>'
    # pour-over subtree (2x2 grid off a central rail at x=180)
    '<path class="ft-line" d="M180 161 L180 200"/>'
    '<path class="ft-line" d="M180 200 L110 200 L110 227"/>'
    '<path class="ft-line" d="M180 200 L250 200 L250 227"/>'
    '<path class="ft-line" d="M180 200 L180 290"/>'
    '<path class="ft-line" d="M180 290 L110 290 L110 307"/>'
    '<path class="ft-line" d="M180 290 L250 290 L250 307"/>'
    # hybrid subtree (two stacked, dashed — straddles the two worlds)
    '<path class="ft-line ft-line-dash" d="M480 161 L480 200 L500 200 L500 227"/>'
    '<path class="ft-line ft-line-dash" d="M480 200 L480 290 L500 290 L500 307"/>'
    # immersion subtree (two stacked off x=780)
    '<path class="ft-line" d="M780 161 L780 200 L820 200 L820 227"/>'
    '<path class="ft-line" d="M780 200 L780 290 L820 290 L820 307"/>'
    # mechanism captions above each branch
    + '<text x="180" y="106" class="ft-era">water flows through</text>'
    + '<text x="480" y="106" class="ft-era">steep, then flow</text>'
    + '<text x="780" y="106" class="ft-era">full immersion</text>'
    # nodes
    + _ft_node(480, 42, 220, "Brewing Coffee", None, root=True)
    + _ft_node(180, 138, 176, "Pour Over", "what-is-pour-over-coffee")
    + _ft_node(480, 138, 150, "Hybrid", None)
    + _ft_node(780, 138, 176, "Immersion", None)
    + _ft_node(110, 250, 96, "Hario V60", "hario-v60", sub=True)
    + _ft_node(250, 250, 128, "Kalita Wave", "kalita-wave", sub=True)
    + _ft_node(110, 330, 104, "Chemex", "chemex", sub=True)
    + _ft_node(250, 330, 120, "Origami", "origami-dripper", sub=True)
    + _ft_node(500, 250, 128, "AeroPress", "aeropress", sub=True)
    + _ft_node(500, 330, 182, "OXO Rapid Brewer", "oxo-rapid-brewer", sub=True)
    + _ft_node(820, 250, 150, "French Press", "french-press", sub=True)
    + _ft_node(820, 330, 150, "Clever Dripper", "the-clever-dripper", sub=True)
    + '</svg>'
    '<figcaption>The pour-over family — percolation, immersion, and the hybrids '
    'between. Tap any brewer to explore it.</figcaption>'
    '</figure>'
)


# ================================================================
# BREWING PROCESS FLOW  — Grain to Glass (9 steps)
# Boustrophedon layout: hot side row 1 L→R, cold side row 2 R→L.
# ================================================================

_BREW_STEPS = [
    # (number, label, slug, glyph svg path-only, hot=True)
    (1, "Mill",       "milling-and-the-grain-bill",
     '<circle cx="0" cy="-3" r="6" fill="none" stroke="currentColor" stroke-width="2"/>'
     '<circle cx="0" cy="9" r="6" fill="none" stroke="currentColor" stroke-width="2"/>'),
    (2, "Mash",       "mashing",
     '<rect x="-7" y="-7" width="14" height="16" rx="2" fill="none" stroke="currentColor" stroke-width="2"/>'
     '<line x1="0" y1="-7" x2="0" y2="6" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>'
     '<circle cx="0" cy="9" r="3" fill="currentColor"/>'),
    (3, "Lauter",     "lautering-and-sparging",
     '<path d="M-9 -4 L9 -4 L6 8 L-6 8 Z" fill="none" stroke="currentColor" stroke-width="2"/>'
     '<line x1="-5" y1="-1" x2="5" y2="-1" stroke="currentColor" stroke-width="1.5"/>'
     '<line x1="-4" y1="3" x2="4" y2="3" stroke="currentColor" stroke-width="1.5"/>'),
    (4, "Boil",       "the-boil",
     '<path d="M-8 -2 L8 -2 L7 8 L-7 8 Z" fill="currentColor"/>'
     '<path d="M-4 -8 q3 -3 0 -6 M0 -8 q3 -3 0 -6 M4 -8 q3 -3 0 -6"'
     ' fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>'),
    (5, "Whirlpool",  "whirlpool-and-hop-stand",
     '<path d="M-7 0 a7 7 0 1 1 7 7 a4 4 0 1 1 4 -4"'
     ' fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>'),
    (6, "Chill",      "carbonation-and-packaging",
     '<g stroke="currentColor" stroke-width="2" stroke-linecap="round" fill="none">'
     '<line x1="0" y1="-8" x2="0" y2="8"/>'
     '<line x1="-7" y1="-4" x2="7" y2="4"/>'
     '<line x1="-7" y1="4" x2="7" y2="-4"/></g>'),
    (7, "Ferment",    "fermentation",
     '<path d="M-7 -8 L7 -8 L6 6 L-6 6 Z" fill="none" stroke="currentColor" stroke-width="2"/>'
     '<path d="M-6 6 L0 10 L6 6" fill="none" stroke="currentColor" stroke-width="2"/>'
     '<circle cx="-2" cy="-1" r="1.5" fill="currentColor"/>'
     '<circle cx="2" cy="2" r="1.2" fill="currentColor"/>'
     '<circle cx="0" cy="-5" r="1" fill="currentColor"/>'),
    (8, "Dry hop",    "dry-hopping",
     '<ellipse cx="0" cy="0" rx="5" ry="8" fill="currentColor"/>'
     '<line x1="0" y1="-12" x2="0" y2="-8" stroke="currentColor" stroke-width="2"/>'),
    (9, "Package",    "carbonation-and-packaging",
     '<rect x="-6" y="-9" width="12" height="18" rx="2" fill="none" stroke="currentColor" stroke-width="2"/>'
     '<line x1="-6" y1="-4" x2="6" y2="-4" stroke="currentColor" stroke-width="1.5"/>'),
]


def _flow_node(num, label, slug, glyph, cx, cy):
    inner = (
        f'<circle cx="{cx}" cy="{cy}" r="38" class="bp-node-bg"/>'
        f'<circle cx="{cx}" cy="{cy}" r="38" class="bp-node-rim"/>'
        f'<g transform="translate({cx} {cy-2})" class="bp-glyph">{glyph}</g>'
        f'<text x="{cx}" y="{cy+58}" class="bp-step-num">STEP {num}</text>'
        f'<text x="{cx}" y="{cy+76}" class="bp-step-label">{label}</text>'
    )
    return f'<a href="{slug}.html" class="bp-step">{inner}</a>'


def brewing_flow():
    # Row 1 (hot): steps 1-5, x = 90,260,430,600,770; y = 130
    # Row 2 (cold): steps 6-9, x = 770,600,430,260; y = 330
    xs_hot = [90, 260, 430, 600, 770]
    xs_cold = [770, 600, 430, 260]
    nodes = []
    for i, x in enumerate(xs_hot):
        n, l, s, g = _BREW_STEPS[i][:4]
        nodes.append(_flow_node(n, l, s, g, x, 130))
    for i, x in enumerate(xs_cold):
        n, l, s, g = _BREW_STEPS[i+5][:4]
        nodes.append(_flow_node(n, l, s, g, x, 330))
    return (
        '<figure class="diagram diagram-flow">'
        '<svg viewBox="0 0 860 440" class="bpflow" xmlns="http://www.w3.org/2000/svg" '
        'role="img" aria-label="The brewing process — nine steps from grain to glass">'
        # band labels
        '<rect x="20" y="40" width="820" height="32" rx="8" class="bp-band bp-band-hot"/>'
        '<text x="430" y="60" class="bp-band-label">HOT SIDE · BREW DAY · ~5 HOURS</text>'
        '<rect x="20" y="240" width="820" height="32" rx="8" class="bp-band bp-band-cold"/>'
        '<text x="430" y="260" class="bp-band-label">COLD SIDE · 2–4 WEEKS</text>'
        # connectors row 1 (left to right between nodes)
        + ''.join(
            f'<line x1="{xs_hot[i]+38}" y1="130" x2="{xs_hot[i+1]-38}" y2="130" class="bp-conn"/>'
            for i in range(4)
        )
        # transition: right end of row 1 (step5 at x=770,y=130) down to row2 step6 (x=770,y=330)
        + '<path d="M770 168 q0 22 0 35 q0 30 0 60 q0 22 0 35" class="bp-conn bp-conn-curve"/>'
        # connectors row 2 (right to left between nodes — step6→7→8→9)
        + ''.join(
            f'<line x1="{xs_cold[i]-38}" y1="330" x2="{xs_cold[i+1]+38}" y2="330" class="bp-conn"/>'
            for i in range(3)
        )
        # arrowhead end
        + '<g transform="translate(260 330)"><polygon points="-44,-6 -38,0 -44,6" class="bp-arrow"/></g>'
        + ''.join(nodes)
        + '</svg>'
        '<figcaption>Grain to glass — the nine-step brewing sequence. '
        'Hot side wins or loses extraction; cold side wins or loses aroma. '
        'Tap any step to dive in.</figcaption>'
        '</figure>'
    )


# ================================================================
# HOP ADDITIONS & TIMING — five-window infographic
# ================================================================

def hop_timing():
    # 5 zones x positions (band 80→820), each ~148 wide
    zones = [
        ("Bittering", "the-boil",                 "60 min · 100°C", "High",      "—",         5),
        ("Flavor",    "bittering-flavor-and-aroma-hops", "10–20 min · 100°C", "Moderate",   "Some",      3.5),
        ("Whirlpool", "whirlpool-and-hop-stand",  "Flameout · 60–80°C", "Low",        "High",      2.2),
        ("Active dry hop", "dry-hopping",         "Fermentation · 18–22°C", "Negligible", "Very high", 1.2),
        ("Cold dry hop",   "dry-hopping",         "Post-ferment · 1–4°C",   "None",       "Maximal",   0.6),
    ]
    band_x, band_w = 124, 776
    zone_w = band_w / 5
    parts = [
        '<figure class="diagram diagram-hops">',
        '<svg viewBox="0 0 920 420" class="hopline" xmlns="http://www.w3.org/2000/svg" '
        'role="img" aria-label="Five hop-addition windows from bittering through cold dry hop">',
        # title axes
        '<defs>',
        '<linearGradient id="bitGrad" x1="0" x2="1">'
        '<stop offset="0%" stop-color="var(--accent)" stop-opacity=".95"/>'
        '<stop offset="100%" stop-color="var(--accent)" stop-opacity=".05"/></linearGradient>',
        '<linearGradient id="aroGrad" x1="0" x2="1">'
        '<stop offset="0%" stop-color="var(--hop)" stop-opacity=".08"/>'
        '<stop offset="100%" stop-color="var(--hop)" stop-opacity=".95"/></linearGradient>',
        '</defs>',
        # background band
        f'<rect x="{band_x}" y="200" width="{band_w}" height="80" rx="14" class="hl-band"/>',
        # gradient bars: bitterness above, aroma below
        f'<rect x="{band_x}" y="158" width="{band_w}" height="22" rx="6" fill="url(#bitGrad)"/>',
        f'<text x="{band_x-8}" y="172" text-anchor="end" class="hl-axis">Bitterness</text>',
        f'<rect x="{band_x}" y="300" width="{band_w}" height="22" rx="6" fill="url(#aroGrad)"/>',
        f'<text x="{band_x-8}" y="314" text-anchor="end" class="hl-axis">Aroma</text>',
    ]
    # hop-cone scale row above (sized by aroma_size)
    for i, (label, slug, meta, bit, aro, cone_h) in enumerate(zones):
        x = band_x + i * zone_w + zone_w / 2
        # cone size scales 16..48 by aroma intensity
        scale = 16 + (5 - cone_h) * 6  # smaller cone for less aroma at left
        # invert: cold dry hop has highest aroma -> biggest cone
        # use cone_h directly: high cone_h = bittering's cone size (largest physical addition)
        size = 18 + cone_h * 6
        parts.append(
            f'<g transform="translate({x} 110)" class="hl-cone">'
            f'<ellipse cx="0" cy="0" rx="{size*0.55}" ry="{size}" fill="var(--hop)" opacity=".22"/>'
            f'<ellipse cx="0" cy="0" rx="{size*0.45}" ry="{size*0.85}" fill="var(--hop)"/>'
            f'<line x1="0" y1="{-size}" x2="0" y2="{-size-7}" stroke="var(--hop-deep)" '
            f'stroke-width="2.4" stroke-linecap="round"/>'
            f'<path d="M{-size*0.45} -2 q{size*0.45} {size*0.4} {size*0.9} 0" '
            f'fill="none" stroke="var(--hop-deep)" stroke-width="1.4" opacity=".5"/>'
            f'<path d="M{-size*0.45} 8 q{size*0.45} {size*0.4} {size*0.9} 0" '
            f'fill="none" stroke="var(--hop-deep)" stroke-width="1.4" opacity=".5"/>'
            f'</g>'
        )
    # zone labels inside the band
    for i, (label, slug, meta, bit, aro, cone_h) in enumerate(zones):
        x = band_x + i * zone_w + zone_w / 2
        parts.append(
            f'<a href="{slug}.html" class="hl-zone">'
            f'<rect x="{band_x + i*zone_w + 4}" y="206" '
            f'width="{zone_w-8}" height="68" rx="10" class="hl-zone-rect"/>'
            f'<text x="{x}" y="232" class="hl-zone-label">{label}</text>'
            f'<text x="{x}" y="252" class="hl-zone-meta">{meta}</text>'
            f'<text x="{x}" y="269" class="hl-zone-num">{i+1}</text>'
            f'</a>'
        )
    # bottom contribution labels
    for i, (label, slug, meta, bit, aro, cone_h) in enumerate(zones):
        x = band_x + i * zone_w + zone_w / 2
        parts.append(
            f'<text x="{x}" y="350" class="hl-contrib hl-contrib-bit">{bit}</text>'
            f'<text x="{x}" y="370" class="hl-contrib hl-contrib-aro">{aro}</text>'
        )
    # legend
    parts.append(
        f'<g transform="translate({band_x} 390)">'
        f'<circle cx="6" cy="0" r="4" fill="var(--accent)"/>'
        f'<text x="16" y="4" class="hl-legend">Bitterness contribution</text>'
        f'<circle cx="190" cy="0" r="4" fill="var(--hop)"/>'
        f'<text x="200" y="4" class="hl-legend">Aroma contribution</text>'
        f'</g>'
    )
    parts.append('</svg>')
    parts.append(
        '<figcaption>The same hop becomes bitterness or aroma based on when it goes in. '
        'Modern hazies push 70–90% of their hops to the right side of this chart.</figcaption>'
        '</figure>'
    )
    return ''.join(parts)


# ================================================================
# HISTORY TIMELINE
# ================================================================

_TIMELINE = [
    # (era_idx, year_label, title, slug)
    (0, "Early 1700s", "Pale ale emerges as coke-fired malting yields paler grain",
        "origins-of-pale-ale"),
    (0, "1750s–80s", "Hodgson's Bow Brewery supplies the East India Company",
        "hodgson-and-the-east-india-trade"),
    (0, "Early 1800s", "The 'India Pale Ale' descriptor enters use",
        "ipa-in-the-british-empire"),
    (0, "1820s",   "Bass & Allsopp adopt the export trade — Burton character defined",
        "burton-on-trent-and-burton-pale-ale"),
    (0, "Mid-1800s","IPA peaks across the British Empire and reaches America",
        "ipa-in-early-america"),
    (0, "Late 1800s","Tastes shift; British IPA declines into a shadow of itself",
        "decline-of-ipa-in-britain"),
    (1, "1971",    "CAMRA forms in Britain, reviving traditional cask ale",
        "decline-of-ipa-in-britain"),
    (1, "1975",    "Anchor's Liberty Ale — widely held as the first modern American IPA",
        "anchor-liberty-ale-and-the-first-modern-ipa"),
    (1, "1980s",   "U.S. craft beer takes off; microbreweries embrace American hops",
        "the-american-craft-beer-revolution"),
    (1, "Late 80s–90s", "The bold, bitter West Coast IPA takes shape",
        "rise-of-the-west-coast-ipa"),
    (1, "1994",    "Russian River's Pliny the Elder — the archetypal Double IPA",
        "origins-of-the-double-ipa"),
    (2, "2004",    "Heady Topper popularises the unfiltered hazy idea in Vermont",
        "the-new-england-ipa-emergence"),
    (2, "Early 2010s","The hazy/NEIPA emerges as a defined style — soft, juicy",
        "the-new-england-ipa-emergence"),
    (2, "Mid–late 2010s","Substyle explosion — Brut, Milkshake, Cold, Brett, Sour",
        "modern-ipa-diversification"),
    (2, "~2018",   "Cold IPA — lager yeast and a crisp hop showcase",
        "cold-ipa"),
    (2, "2020s",   "Thiol-driven biotransformation reshapes hop expression",
        "thiols-and-hop-burst"),
    (2, "Now",     "IPA remains craft's flagship — still evolving",
        "the-future-of-ipa"),
]
_ERAS = [
    ("18–19th century · Origins",      "#9B6A43"),
    ("20th century · Revival",         "#B5612E"),
    ("21st century · Diversification", "#4E8C72"),
]


def history_timeline():
    row_h = 78
    head_h = 56
    rows = []
    y = 0
    last_era = -1
    for era_idx, year, title, slug in _TIMELINE:
        if era_idx != last_era:
            label, color = _ERAS[era_idx]
            rows.append(
                f'<div class="ht-era" style="--ec:{color}">'
                f'<span class="ht-era-dot"></span>'
                f'<span class="ht-era-label">{label}</span></div>'
            )
            last_era = era_idx
            y += head_h
        rows.append(
            f'<a class="ht-row" href="{slug}.html" style="--ec:{_ERAS[era_idx][1]}">'
            f'<div class="ht-year">{year}</div>'
            f'<div class="ht-spine"><span class="ht-dot"></span></div>'
            f'<div class="ht-card">'
            f'<div class="ht-title">{title}</div>'
            f'<div class="ht-go">Read the note <span>›</span></div>'
            f'</div></a>'
        )
        y += row_h
    return (
        '<figure class="diagram diagram-timeline">'
        '<div class="htimeline">' + ''.join(rows) + '</div>'
        '<figcaption>Three centuries in a column — every dot links to the '
        'detailed note for that milestone.</figcaption>'
        '</figure>'
    )


# ================================================================
# FLAVOR WHEEL
# ================================================================

def _polar(cx, cy, r, ang):
    a = math.radians(ang - 90)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def _arc_path(cx, cy, r0, r1, a0, a1):
    x0, y0 = _polar(cx, cy, r1, a0)
    x1, y1 = _polar(cx, cy, r1, a1)
    x2, y2 = _polar(cx, cy, r0, a1)
    x3, y3 = _polar(cx, cy, r0, a0)
    large = 1 if (a1 - a0) > 180 else 0
    return (f"M{x0:.2f} {y0:.2f} A{r1} {r1} 0 {large} 1 {x1:.2f} {y1:.2f} "
            f"L{x2:.2f} {y2:.2f} A{r0} {r0} 0 {large} 0 {x3:.2f} {y3:.2f} Z")


_FLAVOR_CLASSES = [
    ("Hoppy",   "#4E8C72", ["Citrus", "Pine", "Tropical", "Floral", "Dank"],     "hop-aroma-compounds"),
    ("Bitter",  "#B5612E", ["Clean", "Resinous", "Lingering", "Harsh"],          "ibu-and-perceived-bitterness"),
    ("Malty",   "#8A560C", ["Bready", "Toasty", "Biscuit", "Caramel"],           "malt"),
    ("Fruity",  "#B14A55", ["Banana", "Pear", "Stone fruit", "Berry"],           "biotransformation"),
    ("Off",     "#5E6C99", ["Buttery", "Cooked corn", "Papery", "Skunky"],       "off-flavors-in-ipa"),
]


def flavor_wheel():
    cx = cy = 260
    r_hub, r1, r2 = 56, 158, 234
    n = len(_FLAVOR_CLASSES)
    sector = 360 / n
    parts = [
        '<figure class="diagram diagram-wheel">',
        '<svg viewBox="0 0 520 520" class="fwheel" xmlns="http://www.w3.org/2000/svg" '
        'role="img" aria-label="Beer flavor wheel — five classes, twenty descriptors">',
    ]
    for i, (label, color, descs, slug) in enumerate(_FLAVOR_CLASSES):
        a0 = i * sector
        a1 = (i + 1) * sector
        # outer descriptors
        sub_n = len(descs)
        for j, d in enumerate(descs):
            sa0 = a0 + j * (sector / sub_n)
            sa1 = a0 + (j + 1) * (sector / sub_n)
            mid = (sa0 + sa1) / 2
            tx, ty = _polar(cx, cy, (r1 + r2) / 2, mid)
            rot = mid
            if 90 < rot < 270:
                rot += 180
            parts.append(
                f'<path d="{_arc_path(cx, cy, r1+2, r2, sa0+0.5, sa1-0.5)}" '
                f'class="fw-outer" style="--fc:{color}"/>'
                f'<text x="{tx:.2f}" y="{ty:.2f}" '
                f'transform="rotate({rot - 90:.2f} {tx:.2f} {ty:.2f})" '
                f'class="fw-desc">{d}</text>'
            )
        # inner class arc
        ang_pad = 1.2
        parts.append(
            f'<a href="{slug}.html" class="fw-class-link">'
            f'<path d="{_arc_path(cx, cy, r_hub+2, r1-2, a0+ang_pad, a1-ang_pad)}" '
            f'class="fw-inner" style="--fc:{color}"/>'
        )
        mid = (a0 + a1) / 2
        tx, ty = _polar(cx, cy, (r_hub + r1) / 2, mid)
        parts.append(
            f'<text x="{tx:.2f}" y="{ty:.2f}" class="fw-class">{label}</text></a>'
        )
    # hub
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r_hub}" class="fw-hub"/>')
    parts.append(f'<text x="{cx}" y="{cy-6}" class="fw-hub-label">FLAVOR</text>')
    parts.append(f'<text x="{cx}" y="{cy+14}" class="fw-hub-sub">WHEEL</text>')
    parts.append('</svg>')
    parts.append(
        '<figcaption>From general to specific — start at the centre, '
        'narrow outward, land on a precise descriptor.</figcaption>'
        '</figure>'
    )
    return ''.join(parts)


# ================================================================
# STYLE COMPARISON MAP — 2D scatter (clarity × strength)
# ================================================================

_MAP_STYLES = [
    # (name, slug, clarity 0=brilliant..1=opaque, abv mid, color hex,
    #  label_anchor, label_dx, label_dy)
    ("English IPA",     "english-ipa",     0.20, 6.0,  "#E6A11E", "start",  12,   4),
    ("American IPA",    "american-ipa",    0.30, 6.5,  "#E6A11E", "start",  12,   4),
    ("West Coast IPA",  "west-coast-ipa",  0.03, 6.7,  "#ECB73A", "start",  14,   4),
    ("Cold IPA",        "cold-ipa",        0.05, 5.8,  "#F3DC6F", "start",  14,   4),
    ("Brut IPA",        "brut-ipa",        0.08, 7.3,  "#F3DC6F", "start",  14,   4),
    ("Black IPA",       "black-ipa",       0.13, 7.8,  "#3A1500", "start",  14,   4),
    ("Red IPA",         "red-ipa",         0.18, 6.8,  "#A65100", "start",  14, -10),
    ("Belgian IPA",     "belgian-ipa",     0.42, 7.5,  "#E6A11E", "start",  12,   4),
    ("Session IPA",     "session-ipa",     0.42, 4.3,  "#ECC04A", "start",  12,   4),
    ("Double IPA",      "double-ipa",      0.48, 9.0,  "#DE8B0B", "start",  12,   4),
    ("Triple IPA",      "triple-ipa",      0.52, 11.0, "#D17806", "start",  12,   4),
    ("Sour IPA",        "sour-ipa",        0.72, 5.5,  "#F0CB52", "end",   -12,   4),
    ("New England IPA", "new-england-ipa", 0.92, 6.6,  "#F3DC6F", "end",   -14,   4),
    ("Milkshake IPA",   "milkshake-ipa",   0.96, 7.4,  "#F5EE9E", "end",   -14,   4),
]


def style_map():
    # plot area (60, 60) - (700, 420)
    x0, y0, x1, y1 = 86, 60, 700, 420
    def px(c):  return x0 + c * (x1 - x0)
    def py(a):
        # ABV scale 3..13
        t = (a - 3) / (13 - 3)
        return y1 - t * (y1 - y0)
    parts = [
        '<figure class="diagram diagram-map">',
        '<svg viewBox="0 0 760 480" class="smap" xmlns="http://www.w3.org/2000/svg" '
        'role="img" aria-label="IPA styles plotted by clarity and strength">',
        # axes
        f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" class="sm-axis"/>',
        f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" class="sm-axis"/>',
        # grid horizontal (ABV ticks)
        *(
            f'<line x1="{x0}" y1="{py(abv)}" x2="{x1}" y2="{py(abv)}" class="sm-grid"/>'
            f'<text x="{x0-10}" y="{py(abv)+4}" text-anchor="end" class="sm-tick">{abv}%</text>'
            for abv in (4, 6, 8, 10, 12)
        ),
        # vertical clarity labels
        f'<text x="{x0}" y="{y1+24}" class="sm-axis-label">Brilliant ←</text>',
        f'<text x="{x1}" y="{y1+24}" text-anchor="end" class="sm-axis-label">→ Opaque</text>',
        f'<text x="{(x0+x1)/2}" y="{y1+42}" text-anchor="middle" class="sm-axis-title">CLARITY</text>',
        # rotated y title
        f'<text transform="translate(36 {(y0+y1)/2}) rotate(-90)" text-anchor="middle" '
        f'class="sm-axis-title">STRENGTH (ABV)</text>',
    ]
    # quadrant tints (clear-light, hazy-light, clear-strong, hazy-strong)
    mid_x = (x0 + x1) / 2
    mid_y = (y0 + y1) / 2
    parts.append(
        f'<rect x="{x0}" y="{y0}" width="{mid_x-x0}" height="{mid_y-y0}" class="sm-quad-a"/>'
        f'<rect x="{mid_x}" y="{y0}" width="{x1-mid_x}" height="{mid_y-y0}" class="sm-quad-b"/>'
        f'<rect x="{x0}" y="{mid_y}" width="{mid_x-x0}" height="{y1-mid_y}" class="sm-quad-c"/>'
        f'<rect x="{mid_x}" y="{mid_y}" width="{x1-mid_x}" height="{y1-mid_y}" class="sm-quad-d"/>'
    )
    parts.append(
        f'<line x1="{mid_x}" y1="{y0}" x2="{mid_x}" y2="{y1}" class="sm-grid sm-grid-mid"/>'
        f'<line x1="{x0}" y1="{mid_y}" x2="{x1}" y2="{mid_y}" class="sm-grid sm-grid-mid"/>'
    )
    # dots
    for entry in _MAP_STYLES:
        name, slug, clarity, abv, col = entry[:5]
        anchor = entry[5] if len(entry) > 5 else "start"
        dx     = entry[6] if len(entry) > 6 else 12
        dy     = entry[7] if len(entry) > 7 else 4
        x, y = px(clarity), py(abv)
        parts.append(
            f'<a href="{slug}.html" class="sm-pt">'
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="14" class="sm-halo"/>'
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="{col}" class="sm-dot"/>'
            f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{anchor}" class="sm-label">{name}</text>'
            f'</a>'
        )
    parts.append('</svg>')
    parts.append(
        '<figcaption>Two axes explain most IPAs. Brilliant + bitter sits left; '
        'soft + hazy sits right; double-digit ABV sits up top.</figcaption>'
        '</figure>'
    )
    return ''.join(parts)


# ================================================================
# VITAL SIGNS — data-driven style stat panel
# Parses the kv table inside a "Quick stats" callout.
# ================================================================

def _parse_range(text):
    """Pull two floats from '6.0–7.5%' or '25–60 (low perceived)'."""
    m = re.search(r"(\d+(?:\.\d+)?)\s*[–-]\s*(\d+(?:\.\d+)?)", text)
    if m:
        return float(m.group(1)), float(m.group(2))
    m = re.search(r"(\d+(?:\.\d+)?)", text)
    if m:
        v = float(m.group(1))
        return v, v
    return None, None


def _haze_level(text):
    t = text.lower()
    if any(w in t for w in ("brilliant", "crystal")):  return ("Brilliant", 0)
    if "opaque" in t or "heavy" in t:                  return ("Opaque", 4)
    if "hazy" in t and ("light" in t or "soft" in t):  return ("Lightly hazy", 2)
    if "hazy" in t:                                    return ("Hazy", 3)
    if "varies" in t:                                  return ("Varies", 2)
    if "clear" in t:                                   return ("Clear", 1)
    return (text.strip().title() or "—", 1)


def _gauge(label, lo, hi, scale_max, suffix=""):
    if lo is None:
        return (f'<div class="vs-gauge vs-gauge-empty">'
                f'<div class="vs-glabel">{label}</div>'
                f'<div class="vs-gbody"><div class="vs-gtrack"></div>'
                f'<div class="vs-gval">—</div></div></div>')
    pct_lo = max(0, min(100, lo / scale_max * 100))
    pct_hi = max(0, min(100, hi / scale_max * 100))
    val = (f"{lo:g}–{hi:g}" if lo != hi else f"{lo:g}") + suffix
    fill = (f'<div class="vs-gfill" style="left:{pct_lo:.1f}%;'
            f'width:{max(0.8, pct_hi-pct_lo):.1f}%"></div>')
    pin = f'<div class="vs-gpin" style="left:{(pct_lo+pct_hi)/2:.1f}%"></div>'
    return (
        f'<div class="vs-gauge">'
        f'<div class="vs-glabel"><span>{label}</span>'
        f'<span class="vs-gval">{val}</span></div>'
        f'<div class="vs-gbody"><div class="vs-gtrack"></div>{fill}{pin}'
        f'<span class="vs-gmax">{scale_max:g}{suffix}</span></div></div>'
    )


def _glass_svg(beer_hex, haze):
    """SVG of a pint glass filled with the SRM-derived color, with optional haze."""
    haze_filter = ""
    overlay = ""
    if haze >= 3:
        # add a milky overlay
        overlay = ('<rect x="38" y="44" width="84" height="120" fill="#ffffff" '
                   'opacity=".22"/>')
    if haze >= 4:
        overlay += ('<ellipse cx="80" cy="100" rx="42" ry="64" fill="#ffffff" '
                    'opacity=".18"/>')
    return (
        '<svg viewBox="0 0 160 200" class="vs-glass" '
        'xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
        '<defs>'
        f'<linearGradient id="vsbeer" x1="0" x2="0" y1="0" y2="1">'
        f'<stop offset="0%" stop-color="{beer_hex}" stop-opacity=".75"/>'
        f'<stop offset="100%" stop-color="{beer_hex}"/></linearGradient>'
        '</defs>'
        '<path d="M32 38 L128 38 L120 178 L40 178 Z" fill="var(--il-glass)"/>'
        f'<path d="M38 50 L122 50 L116 172 L44 172 Z" fill="url(#vsbeer)"/>'
        + overlay +
        '<path d="M32 38 q9 -11 18 -2 q9 -11 18 -2 q9 -11 18 -2 q9 -11 18 -2 q9 -11 16 -2"'
        ' fill="var(--il-foam)" stroke="var(--il-ink)" stroke-width="2.4" stroke-linejoin="round"/>'
        '<path d="M50 64 L46 160" stroke="var(--il-foam)" stroke-width="3" '
        'stroke-linecap="round" opacity=".55"/>'
        '<path d="M32 38 L128 38 L120 178 L40 178 Z" fill="none" '
        'stroke="var(--il-ink)" stroke-width="2.6" stroke-linejoin="round"/>'
        '</svg>'
    )


def vital_signs(stats, hops_html, glass_html, name):
    """
    stats: dict with keys ABV, IBU, Color, Haze (strings, raw)
    hops_html: pre-rendered HTML of the Key hops cell (with wikilinks)
    glass_html: pre-rendered HTML of Glassware cell (plain text)
    """
    abv_lo, abv_hi = _parse_range(stats.get("ABV", ""))
    ibu_lo, ibu_hi = _parse_range(stats.get("IBU", ""))
    srm_lo, srm_hi = _parse_range(stats.get("Color", ""))
    haze_label, haze_n = _haze_level(stats.get("Haze", "Varies"))
    srm_mid = ((srm_lo or 0) + (srm_hi or 0)) / 2 if srm_lo else 6
    beer_hex = srm_to_hex(srm_mid)
    color_text = stats.get("Color", "").strip()
    haze_dots = "".join(
        f'<span class="vs-hdot{" on" if i < haze_n else ""}"></span>'
        for i in range(5)
    )
    parts = [
        '<aside class="vs-panel" aria-label="Vital signs">',
        '<div class="vs-head"><span class="vs-kicker">VITAL SIGNS</span>',
        f'<h3 class="vs-name">{name}</h3></div>',
        '<div class="vs-grid">',
        f'<div class="vs-glass-wrap">{_glass_svg(beer_hex, haze_n)}'
        f'<div class="vs-color-label">'
        f'<span class="vs-swatch" style="background:{beer_hex}"></span>'
        f'<span>{color_text or "—"}</span></div></div>',
        '<div class="vs-gauges">',
        _gauge("ABV", abv_lo, abv_hi, 14, "%"),
        _gauge("IBU", ibu_lo, ibu_hi, 120, ""),
        f'<div class="vs-haze"><div class="vs-glabel"><span>Haze</span>'
        f'<span class="vs-gval">{haze_label}</span></div>'
        f'<div class="vs-hdots">{haze_dots}</div>'
        f'<div class="vs-hscale"><span>Brilliant</span><span>Opaque</span></div></div>',
        '</div></div>',
        '<div class="vs-foot">',
        f'<div class="vs-foot-row"><span class="vs-foot-label">Key hops</span>'
        f'<span class="vs-foot-val">{hops_html or "—"}</span></div>',
        f'<div class="vs-foot-row"><span class="vs-foot-label">Glassware</span>'
        f'<span class="vs-foot-val">{glass_html or "—"}</span></div>',
        '</div></aside>',
    ]
    return "".join(parts)


# ================================================================
# Registry — which slug gets which diagram, injected after intro paragraph
# ================================================================

def page_diagrams():
    # No bespoke per-page diagrams for the coffee base yet; the beer-specific
    # builders above are unused. Return empty so nothing is injected.
    return {}
