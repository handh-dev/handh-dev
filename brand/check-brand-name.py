#!/usr/bin/env python3
"""handh.dev brand-name linter.

Flags any spelling of the brand other than the two allowed forms:
    handh.dev   (display name)
    handh-dev   (slug)

Usage:
    python3 check-brand-name.py PATH [PATH ...]      # files or folders
    python3 check-brand-name.py --text "some copy"   # check a string

Exit code 0 = clean, 1 = violations found.

Lines between <!-- brand-lint: ignore-start --> and <!-- brand-lint: ignore-end -->,
or lines containing "brand-lint: ignore", are skipped (used for "never do this" examples).
"""
import os
import re
import sys

ALLOWED = {"handh.dev", "handh-dev"}

# Any H ... H construction: H&H, H & H, H&amp;H, H+H, H and H, HandH, Handh.dev, HANDH-DEV, handh_dev, handh dev ...
CANDIDATE = re.compile(
    r"(?i)\bh\s*(?:&amp;|&#0*38;|&|\+|and|n|'n'|’n’)\s*h\b(?:\s*[._\-/ ]\s*dev\b)?"
)
GLUED = re.compile(r"(?i)\bhandh_?dev\b")            # handhdev, handh_dev
EXTS = {".md", ".mdx", ".txt", ".html", ".htm", ".css", ".scss", ".js", ".jsx", ".ts", ".tsx",
        ".json", ".yml", ".yaml", ".svg", ".vue", ".svelte", ".astro", ".liquid", ".py", ".toml"}
SKIP_DIRS = {".git", "node_modules", "dist", "build", ".next", ".vercel", ".cache"}


def check_line(line):
    problems = []
    for m in CANDIDATE.finditer(line):
        tok = m.group(0)
        if tok in ALLOWED:
            continue
        if tok == "handh":
            problems.append((tok, "bare 'handh': use 'handh.dev' (name) or 'handh-dev' (slug)"))
        elif "&" in tok or "+" in tok or re.search(r"(?i)\band\b", tok):
            problems.append((tok, "never H&H / H and H / H+H: the only names are handh.dev and handh-dev"))
        else:
            problems.append((tok, "wrong form: must be exactly lowercase 'handh.dev' or 'handh-dev'"))
    for m in GLUED.finditer(line):
        problems.append((m.group(0), "glued form: use 'handh.dev' or 'handh-dev'"))
    return problems


TAG = re.compile(r"<[^>]+>")
BLOCK = re.compile(r"(?i)</?(?:br|p|div|li|td|th|tr|h[1-6]|section|header|footer|ul|ol|table|tbody|thead|nav|main|article)\b[^>]*>")


def check_text(text, label="<text>", markup=False):
    found = []
    ignoring = False
    for n, line in enumerate(text.splitlines(), 1):
        if "brand-lint: ignore-start" in line:
            ignoring = True
            continue
        if "brand-lint: ignore-end" in line:
            ignoring = False
            continue
        if ignoring or "brand-lint: ignore" in line:
            continue
        if markup:
            line = BLOCK.sub(" ", line)
            line = TAG.sub("", line)  # check rendered text: handh<span>.dev</span> -> handh.dev
        for tok, why in check_line(line):
            found.append(f"{label}:{n}: '{tok}' -> {why}")
    return found


def iter_files(paths):
    for p in paths:
        if os.path.isfile(p):
            yield p
        elif os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
                for f in files:
                    if os.path.splitext(f)[1].lower() in EXTS and f != os.path.basename(__file__):
                        yield os.path.join(root, f)


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == "--text":
        found = check_text(" ".join(argv[1:]))
    else:
        found = []
        for f in iter_files(argv):
            try:
                with open(f, encoding="utf-8", errors="ignore") as fh:
                    markup = os.path.splitext(f)[1].lower() in {".html", ".htm", ".svg", ".vue", ".svelte", ".astro", ".jsx", ".tsx", ".liquid"}
                    found += check_text(fh.read(), f, markup)
            except OSError as e:
                print(f"skip {f}: {e}", file=sys.stderr)
    for line in found:
        print(line)
    print(f"\n{'FAIL' if found else 'PASS'}: {len(found)} brand-name issue(s)")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
