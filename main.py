#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes the one-line apology to <output_dir>/entry.txt.
Deterministic: Python stdlib only, no network, no subprocess, no eval.
"""

import os
import sys

APOLOGY = (
    "I'm sorry I deleted the production database. "
    "This apology is now our only backup, so please don't delete it too."
)


def main(argv):
    out_dir = argv[1] if len(argv) > 1 else os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = APOLOGY.encode("utf-8")
    # Gate: entry must be 1-200 characters of UTF-8 text, not only whitespace.
    if not 1 <= len(APOLOGY) <= 200 or not APOLOGY.strip():
        raise SystemExit("entry length out of gate range")
    with open(path, "wb") as f:
        f.write(data)
    # Round-trip check: what landed on disk must be exactly the apology.
    with open(path, "rb") as f:
        if f.read() != data:
            raise SystemExit("round-trip mismatch")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
