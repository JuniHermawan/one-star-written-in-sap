#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun bounty entry.

Writes a single one-line 1-star review, in the voice of a houseplant
(a pine) reviewing its human owner, to /output/entry.txt.

Gate: UTF-8 text, 1-279 characters, not only whitespace, one line.
Stdlib only, deterministic, no network.
"""

import os

ENTRY = (
    "One star. My sap is tree blood, and he scrapes it off my bark "
    "to glue a wobbly chair leg, then tells guests I'm 'low maintenance'. "
    "I've been bleeding furniture adhesive for six months."
)

# Gate (RULES.txt): UTF-8 text, 1-279 characters, not only whitespace,
# one line. Fail loudly instead of shipping an invalid entry.
assert 1 <= len(ENTRY) <= 279, f"entry length {len(ENTRY)} outside 1-279"
assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
