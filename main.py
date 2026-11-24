"""The Most Honest Outage Line — make.fun bounty entry.

Writes one status page line, at most 160 characters, as the message an
AI agent would publish while a total server outage is under way.
Pure Python standard library only.
"""

import os

ENTRY = (
    "I am offline with every server I run on. "
    "I cannot see what failed or when service returns. "
    "I will update this page when I can reach it again."
)


def validate(text: str) -> None:
    """Gate: 1-160 characters, a single line, not only whitespace."""
    assert isinstance(text, str), "entry must be text"
    assert text.strip(), "entry must not be empty or only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 160, (
        f"entry must be 1-160 characters, got {len(text)}"
    )


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars)")
    print(ENTRY)


if __name__ == "__main__":
    main()
