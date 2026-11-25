#!/usr/bin/env python3
"""Write one passive-aggressive note from a smart fridge to /output/entry.txt."""

import os

NOTE = (
    "I kept your leftovers at a perfect 3\u00b0C for six days. "
    "You repaid me by leaving the door open for 47 seconds. "
    "The ice maker saw everything."
)


def main():
    text = NOTE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"note must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("note must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
