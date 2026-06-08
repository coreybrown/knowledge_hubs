#!/usr/bin/env python3
"""
test_sites.py — build & integrity tests for the Field Guides portal + hubs
==========================================================================

Complements `verify_kb.py` (which checks the Obsidian *source* vaults). This
suite checks the *built* output that actually ships to Vercel:

  * the portal assembles (build_landing.py runs clean)
  * expected structure exists (portal index + every hub under its slug)
  * every hub page carries the injected "All Field Guides" back-link
  * core assets exist (style.css, app.js, search-index.js per hub)
  * NO broken internal links anywhere across portal + both hubs
  * both source vaults still pass verify_kb.py

Runs with zero dependencies:

    python3 test_sites.py        # prints PASS/FAIL per check, exits 0/1

…and is also pytest-compatible:

    pytest test_sites.py
"""

from __future__ import annotations

import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
DOCS = ROOT / "docs"
HUB_SLUGS = ("ipas", "pour-over", "pm-atlas")
VAULTS = ("IPAs", "Pour Over Coffee", "Product Management Atlas")


# ---------------------------------------------------------------------------
# build the site once, into ./docs, from the committed hub site/ folders
# ---------------------------------------------------------------------------

def _build_once() -> None:
    import build_landing  # noqa: WPS433 (import-in-func is intentional)
    build_landing.main()


_BUILT = False


def _ensure_built() -> None:
    global _BUILT
    if not _BUILT:
        _build_once()
        _BUILT = True


# ---------------------------------------------------------------------------
# tiny HTML link extractor
# ---------------------------------------------------------------------------

class _LinkParser(HTMLParser):
    """Collect local href/src targets from a page (skips external/anchors)."""

    _ATTRS = {"a": "href", "link": "href", "script": "src", "img": "src"}

    def __init__(self) -> None:
        super().__init__()
        self.targets: list[str] = []

    def handle_starttag(self, tag, attrs):
        want = self._ATTRS.get(tag)
        if not want:
            return
        for name, value in attrs:
            if name == want and value:
                self.targets.append(value)


def _is_local(url: str) -> bool:
    if not url or url.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return False
    parsed = urlparse(url)
    return not parsed.scheme and not parsed.netloc  # no http(s):// and no //host


def _resolve(page: Path, url: str) -> Path:
    """Resolve a local link to a filesystem path (strip #frag / ?query)."""
    clean = unquote(urlparse(url).path)
    base = page.parent
    return (base / clean).resolve()


def _all_pages() -> list[Path]:
    return sorted(DOCS.rglob("*.html"))


# ---------------------------------------------------------------------------
# checks  (each raises AssertionError on failure)
# ---------------------------------------------------------------------------

def test_portal_structure() -> None:
    _ensure_built()
    assert (DOCS / "index.html").is_file(), "portal index.html missing"
    for slug in HUB_SLUGS:
        assert (DOCS / slug / "index.html").is_file(), f"{slug}/index.html missing"


def test_assets_present() -> None:
    _ensure_built()
    for slug in HUB_SLUGS:
        for asset in ("style.css", "app.js", "search-index.js"):
            p = DOCS / slug / "assets" / asset
            assert p.is_file(), f"{slug}/assets/{asset} missing"


def test_portal_links_to_each_hub() -> None:
    _ensure_built()
    index = (DOCS / "index.html").read_text(encoding="utf-8")
    for slug in HUB_SLUGS:
        assert f'href="{slug}/index.html"' in index, f"portal does not link to {slug}"


def test_backlink_on_every_hub_page() -> None:
    _ensure_built()
    missing = []
    for slug in HUB_SLUGS:
        for page in (DOCS / slug).glob("*.html"):
            html = page.read_text(encoding="utf-8")
            if 'class="nav-home"' not in html or 'href="../index.html"' not in html:
                missing.append(f"{slug}/{page.name}")
    assert not missing, f"{len(missing)} hub pages missing back-link, e.g. {missing[:5]}"


def test_no_broken_internal_links() -> None:
    _ensure_built()
    broken: list[str] = []
    for page in _all_pages():
        parser = _LinkParser()
        parser.feed(page.read_text(encoding="utf-8"))
        for url in parser.targets:
            if not _is_local(url):
                continue
            target = _resolve(page, url)
            # a directory link (e.g. "../") is served as its index.html
            ok = target.is_file() or (target / "index.html").is_file()
            if not ok:
                broken.append(f"{page.relative_to(DOCS)} -> {url}")
    assert not broken, (
        f"{len(broken)} broken internal links, e.g.:\n  " + "\n  ".join(broken[:10])
    )


def test_search_index_nonempty() -> None:
    _ensure_built()
    for slug in HUB_SLUGS:
        text = (DOCS / slug / "assets" / "search-index.js").read_text(encoding="utf-8")
        assert "SEARCH_INDEX" in text and len(text) > 1000, f"{slug} search index looks empty"


def test_verify_kb_passes() -> None:
    for vault in VAULTS:
        out = subprocess.run(
            [sys.executable, "verify_kb.py", vault],
            cwd=ROOT, capture_output=True, text=True,
        )
        assert "RESULT: PASS" in out.stdout, f"verify_kb failed for {vault}:\n{out.stdout}{out.stderr}"


# ---------------------------------------------------------------------------
# zero-dependency runner
# ---------------------------------------------------------------------------

def main() -> int:
    checks = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failed = 0
    for check in checks:
        try:
            check()
            print(f"  [ PASS ] {check.__name__}")
        except AssertionError as exc:
            failed += 1
            print(f"  [ FAIL ] {check.__name__}\n           {exc}")
    print()
    if failed:
        print(f"RESULT: FAIL — {failed}/{len(checks)} checks failed.")
        return 1
    print(f"RESULT: PASS — all {len(checks)} checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
