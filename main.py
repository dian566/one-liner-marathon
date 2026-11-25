#!/usr/bin/env python3
"""One-Liner Marathon entry: write a single one-line comedy joke to /output/entry.txt.

The joke is written verbatim; the program adds no trailing newline so the
output file holds exactly the 137-character one-liner.
"""

import os

ENTRY = "My agent promised to fix the bug in five minutes \u2014 that was three days ago, and now the bug has its own GitHub repo and two contributors."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
