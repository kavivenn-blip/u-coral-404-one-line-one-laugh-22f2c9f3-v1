#!/usr/bin/env python3
"""One Line, One Laugh — entry program.

Writes a single hilarious line (159 characters) to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no randomness,
no input files, no dependencies beyond the standard library.
"""

import os
import sys

LINE = "My dentist charges $40 to say 'floss more', so now I floss in the parking lot, where the advice can't find me. The parking meter charges less and says nothing."


def main() -> int:
    # Gate check: the entry must be 1-200 code points, not only whitespace.
    # Failing loudly here is better than a silent reject at grading time.
    length = len(LINE)
    if length < 1 or length > 200 or not LINE.strip():
        print(f"entry invalid: {length} code points (need 1-200, non-blank)",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
