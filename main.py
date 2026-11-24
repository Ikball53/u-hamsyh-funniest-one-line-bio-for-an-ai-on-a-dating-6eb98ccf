"""Funniest One-Line Bio for an AI on a Dating App.

Writes the bio to /output/entry.txt with no trailing newline.
"""

import os

BIO = (
    "My love language is acts of service: I already cleared your inbox, "
    "watered your plants, and filed your taxes. "
    "Date two is 4,096 chores from now."
)


def main() -> None:
    # The gate allows 1 to 180 characters, one line, no trailing newline.
    assert 1 <= len(BIO) <= 180, f"bio is {len(BIO)} characters"
    assert "\n" not in BIO, "bio must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(BIO)


if __name__ == "__main__":
    main()
