#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence pitching a bizarre startup idea to /output/entry.txt.
Standard library only. Deterministic: the same sentence on every run.
"""

import os

# One sentence, 200 characters at most: a bizarre startup pitch that
# turns out to be a real business.
ENTRY = (
    "We rent strangers' dogs to nervous first-daters: a borrowed puppy "
    "makes anyone look trustworthy, dates last longer, and the dog's "
    "owner gets paid for the walk."
)


def main() -> None:
    # Gate check, done here so a bad sentence fails loudly instead of
    # silently submitting an invalid entry.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
