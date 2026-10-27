"""Check that every relative link and #anchor in the handbook's Markdown resolves.

Usage: python3 tools/check_links.py   (from the repository root; exits 1 on problems)
"""
import glob
import os
import re
import sys

FENCE = re.compile(r"```.*?```", re.S)
HEADING = re.compile(r"^#{1,6} (.+)$", re.M)
LINK = re.compile(r"\]\(([^)\s]+)\)")


def slug(heading):
    """GitHub's anchor for a heading: lower case, punctuation dropped, spaces to hyphens."""
    return re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")


def text(path):
    with open(path, encoding="utf-8") as handle:
        return FENCE.sub("", handle.read())


def main():
    files = sorted(set(glob.glob("**/*.md", recursive=True) + glob.glob(".github/**/*.md", recursive=True)))
    anchors = {os.path.normpath(f): {slug(h) for h in HEADING.findall(text(f))} for f in files}
    problems = []
    for f in files:
        for url in LINK.findall(text(f)):
            if url.startswith(("http://", "https://", "mailto:")):
                continue
            path, _, anchor = url.partition("#")
            target = os.path.normpath(os.path.join(os.path.dirname(f), path)) if path else os.path.normpath(f)
            if not os.path.exists(target):
                problems.append(f"{f}: missing target {url}")
            elif anchor and anchor not in anchors.get(target, set()):
                problems.append(f"{f}: no heading for #{anchor} in {target}")
    for problem in problems:
        print(problem)
    print(f"checked {len(files)} files, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
