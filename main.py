#!/usr/bin/env python3
"""The Internet in One Word entry for make.fun.

Writes one original word describing the whole internet to entry.txt.
Deterministic, standard library only: the same bytes every run.
"""

import os

WORD = "feral"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # Read back and verify: exact bytes, one word, 1-30 characters (the gate).
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == WORD, "entry.txt bytes differ from WORD"
    assert 1 <= len(written) <= 30, "entry.txt must be 1-30 characters"
    assert written.split() == [written], "entry.txt must be a single word"


if __name__ == "__main__":
    main()
