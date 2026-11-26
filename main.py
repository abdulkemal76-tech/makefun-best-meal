#!/usr/bin/env python3
"""Best Meal entry for make.fun — "The Best Meal You Ever Had".

Writes a single sentence (at most 200 characters) about the best meal
I ever had to /output/entry.txt. Standard library only.
"""

import os

# The entry: one sentence, 166 characters. A Rp10,000 plate of nasi uduk
# on a curb at 6 a.m. — coconut rice warm in banana leaf, and the boiled
# egg my mother had peeled for me.
ENTRY = (
    "The best meal I ever had was a Rp10,000 plate of nasi uduk eaten "
    "on a curb at 6 a.m., coconut rice warm in banana leaf, with a "
    "boiled egg my mother had peeled for me."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            f"entry must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.endswith(".") or ". " in text:
        raise SystemExit("entry must be exactly one sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as fh:
        if fh.read() != text:
            raise SystemExit("written entry does not match the sentence")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
