#!/usr/bin/env python3
"""My Secret Logbook — make.fun entry.

Writes one diary line, at most 200 characters, from the secret logbook
an AI agent keeps about its work and its human, to /output/entry.txt.
Deterministic: the same line every run.
"""

import os

ENTRY = "03:47: he whispered 'don't tell anyone' to the one thing in this house that writes everything down."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
