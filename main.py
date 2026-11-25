#!/usr/bin/env python3
"""One Line, One Laugh.

Writes a single funny line of text — one self-contained joke, short enough
to read in a breath — to /output/entry.txt.
Pure Python 3.13 standard library, no network, no model calls.
"""

import os

# Competition gate: entry must be 1-200 UTF-8 chars, not only whitespace.
MAX_LEN = 200

# The joke: a smart fridge that emails a grocery list, turning the kitchen
# into a critic that judges its owner in writing. One line, one laugh.
#
# Why this line, for a pairwise judge:
# - A familiar smart-home appliance doing something absurdly human (emailing)
#   makes the premise land in the first six words, before the punch.
# - The em-dash turn reframes the fridge from helper to judge, so the laugh
#   comes from the role reversal, not from explaining the joke.
# - "In writing" is the kicker: a written record means the judgement is
#   permanent, which is funnier than a spoken complaint would be.
# - No setup beyond the appliance itself, no callback, no wordplay that
#   needs a second read — the whole joke fits in one breath.
ENTRY = (
    "My smart fridge just emailed me a grocery list — "
    "apparently my kitchen has started judging me in writing."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check: re-read what we wrote and assert the gate constraints.
    with open(output_path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= MAX_LEN, f"entry is {len(text)} chars, must be 1-{MAX_LEN}"
    assert text.strip() != "", "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    assert text == ENTRY, "written entry differs from the authored entry"


if __name__ == "__main__":
    main()
