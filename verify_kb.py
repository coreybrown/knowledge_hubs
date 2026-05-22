#!/usr/bin/env python3
"""Verify an Obsidian knowledge base built by the knowledge-base-builder skill.

Checks, against `00_generator/Note Registry.md`:
  - every registry name has a matching `.md` file (and vice versa)
  - every [[wikilink]] resolves to a real note
  - no wikilink spans a line break (Obsidian won't render those)
  - no orphan notes (every note has at least one incoming link; `Home` exempt)

Note filenames carry a two-digit reading-order prefix (`NN <name>.md`) so the
Obsidian file explorer lists them in book order. The *canonical* name is the
filename with that prefix stripped; the registry and every [[wikilink]] use the
canonical name. Every prefixed note must also carry its canonical name as a
frontmatter alias so those links resolve in Obsidian.

Usage:
  python3 verify_kb.py [KB_ROOT] [--fix]

  KB_ROOT  path to the knowledge base (default: current directory)
  --fix    reflow any multi-line wikilinks onto a single line, in place
           (code fences are left untouched)

Exit code 0 when clean, 1 when issues remain.
"""
import os, re, sys

LINK_RE = re.compile(r"\[\[([^\[\]]+)\]\]")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
PREFIX_RE = re.compile(r"^\d\d\s+")


def canonical(basename):
    """Filename (no .md) with its reading-order prefix stripped."""
    return PREFIX_RE.sub("", basename)


def domain_folders(root):
    return sorted(d for d in os.listdir(root)
                  if re.match(r"\d\d_", d) and os.path.isdir(os.path.join(root, d)))


def md_files(root):
    """Content notes only — the 00_generator folder is scaffolding, not content."""
    out = []
    for d in domain_folders(root):
        if d == "00_generator":
            continue
        for f in sorted(os.listdir(os.path.join(root, d))):
            if f.endswith(".md"):
                out.append((d, f[:-3]))
    return out


def read_registry(root):
    path = os.path.join(root, "00_generator", "Note Registry.md")
    names = []
    in_folder = False
    with open(path) as fh:
        for line in fh:
            if re.match(r"##\s+\d\d_", line.strip()):
                in_folder = True
                continue
            m = re.match(r"-\s+(.+)", line.strip())
            if m and in_folder:
                names.append(m.group(1).strip())
    return names


def frontmatter_aliases(text):
    """Return the list of aliases declared in a note's YAML frontmatter."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return []
    try:
        end = lines.index("---", 1)
    except ValueError:
        return []
    for ln in lines[1:end]:
        m = re.match(r"\s*aliases:\s*\[(.*)\]\s*$", ln)
        if m:
            # split on commas that are not inside quotes, then unquote
            items = re.findall(r'"[^"]*"|\'[^\']*\'|[^,]+', m.group(1))
            return [a.strip().strip("\"'") for a in items if a.strip()]
    return []


def reflow_match(m):
    """Collapse newlines (and callout '>' continuations) inside one wikilink."""
    return re.sub(r"\s*\n\s*>?[ \t]*", " ", m.group(0))


def fix_file(path):
    """Reflow multi-line wikilinks outside code fences. Returns True if changed."""
    orig = open(path).read()
    parts = re.split(r"(```.*?```)", orig, flags=re.DOTALL)
    for i in range(0, len(parts), 2):  # even indices = outside fences
        parts[i] = re.sub(r"\[\[[^\[\]]*?\]\]", reflow_match, parts[i])
    new = "".join(parts)
    if new != orig:
        open(path, "w").write(new)
        return True
    return False


def main():
    args = [a for a in sys.argv[1:] if a != "--fix"]
    do_fix = "--fix" in sys.argv
    root = os.path.abspath(args[0]) if args else os.getcwd()

    files = md_files(root)
    canon = {basename: canonical(basename) for _, basename in files}
    notes = set(canon.values())
    registry = read_registry(root)
    regset = set(registry)

    if do_fix:
        fixed = [os.path.join(d, n + ".md") for d, n in files
                 if fix_file(os.path.join(root, d, n + ".md"))]
        print(f"--fix: reflowed multi-line wikilinks in {len(fixed)} file(s)")
        for f in fixed:
            print(f"   {f}")
        print()

    broken, multiline = {}, {}
    backlinks = {n: 0 for n in notes}
    missing_alias = []
    total_links = 0

    for d, name in files:
        cname = canon[name]
        text = open(os.path.join(root, d, name + ".md")).read()
        if PREFIX_RE.match(name) and cname not in frontmatter_aliases(text):
            missing_alias.append(f"{d}/{name}: needs alias [{cname}]")
        scan = FENCE_RE.sub("", text)              # ignore code blocks
        scan = re.sub(r"`[^`]*`", "", scan)        # ignore inline code
        for raw in LINK_RE.findall(scan):
            total_links += 1
            if "\n" in raw:
                multiline.setdefault((d, name), []).append(raw.replace("\n", " <NL> "))
            target = raw.split("|")[0].split("#")[0].replace("\\", "")
            target = " ".join(target.split())
            if target in notes:
                if target != cname:
                    backlinks[target] += 1
            else:
                broken.setdefault((d, name), []).append(raw.replace("\n", " <NL> "))

    missing = sorted(regset - notes)
    extra = sorted(notes - regset)
    orphans = sorted(canon[n] for _, n in files
                     if backlinks[canon[n]] == 0 and canon[n] != "Home")

    print(f"Knowledge base : {root}")
    print(f"Notes on disk  : {len(files)}   Registry names: {len(registry)}")
    print(f"Wikilinks      : {total_links}")
    print()

    ok = True

    def section(title, items, fmt):
        nonlocal ok
        if items:
            ok = False
            print(f"[FAIL] {title} ({len(items)})")
            for it in items:
                print("   " + fmt(it))
        else:
            print(f"[ OK ] {title}")

    section("Registry names with no file", missing, lambda x: x)
    section("Files not listed in registry", extra, lambda x: x)
    section("Broken wikilinks (target is not a real note)",
            [(d, n, l) for (d, n), ls in sorted(broken.items()) for l in ls],
            lambda t: f"{t[0]}/{t[1]}: [[{t[2]}]]")
    section("Multi-line wikilinks (run with --fix to reflow)",
            [(d, n, l) for (d, n), ls in sorted(multiline.items()) for l in ls],
            lambda t: f"{t[0]}/{t[1]}: [[{t[2]}]]")
    section("Prefixed notes missing canonical alias", sorted(missing_alias),
            lambda x: x)
    section("Orphan notes (no incoming links)", orphans, lambda x: x)

    print()
    print("RESULT: PASS — knowledge base is internally consistent." if ok
          else "RESULT: FAIL — fix the issues above (try --fix for multi-line links).")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
