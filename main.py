#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't.

Writes one line — the weather forecast for the invented city of
Kettlebury — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

LINE = (
    "Kettlebury: heavy rain, 11\u00b0C, expect localized flooding of the "
    "library and a 100% chance the ducks know why."
)


def main() -> None:
    # The gate allows 1 to 120 characters; refuse to write an over-long line.
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
