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
    """Gate: 1-160 characters, a single line, not only whitespace.

    Second-pass checks (revision): no trailing whitespace, exactly one
    line, and no invented ETA phrasing — an honest outage line must not
    promise a return time it cannot know.
    """
    assert isinstance(text, str), "entry must be text"
    assert text.strip(), "entry must not be empty or only whitespace"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.count("\n") == 0, "entry must be exactly one line"
    assert 1 <= len(text) <= 160, (
        f"entry must be 1-160 characters, got {len(text)}"
    )
    banned_eta = (
        "soon", "shortly", "minutes", "hours", "eta", "estimated",
        "back in", "restored by", "expected", "within the hour",
    )
    lowered = text.lower()
    for phrase in banned_eta:
        assert phrase not in lowered, (
            f"entry must not invent an ETA: found {phrase!r}"
        )


def main() -> None:
    validate(ENTRY)
    print(f"entry length: {len(ENTRY)} characters (limit 160)")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars)")
    print(ENTRY)


if __name__ == "__main__":
    main()
