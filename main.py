#!/usr/bin/env python3
"""Write the one-line joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

The joke lives in joke.txt next to this file; the program only copies it
to the grader's output directory, unchanged.
"""

import os
import sys
from pathlib import Path

MAX_CHARS = 280


def main() -> int:
    here = Path(__file__).resolve().parent
    joke = (here / "joke.txt").read_text(encoding="utf-8")
    line = joke.strip()
    if not line or len(line) > MAX_CHARS:
        print("joke must be 1-280 characters on one line", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", ""))
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(line + "\n", encoding="utf-8")
    print(f"wrote {len(line)} characters to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
