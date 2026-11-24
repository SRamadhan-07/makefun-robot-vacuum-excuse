#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — entry program.

Writes one line to /output/entry.txt: a robot vacuum's excuse for
missing a spot — it did not miss it; it surveyed the spot, respected
its privacy, and left it exactly as the owner's shoes intended. One
line of UTF-8 text inside the gate of 1 to 140 characters, with no
trailing newline.
"""

import os
from pathlib import Path

EXCUSE = (
    "I didn't miss that spot. I surveyed it, respected its privacy, "
    "and left it exactly as your shoes intended."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_file = out_dir / "entry.txt"
    # No trailing newline is appended, so the excuse's characters are
    # the whole file the sealed scorer measures.
    entry_file.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
