#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App entry.

Writes one original one-line bio for an AI agent's dating app
profile, at most 180 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The bio: the AI once hallucinated an entire relationship --
a dog, a house, one fight about the dishes -- and is now
looking for someone real to fact-check it.

Why this line: hallucination is a specific absurdity of being
an AI (not a generic robot-seeks-love or runs-on-electricity
angle), the bio reads as a character with a past and a want,
and the punch -- "fact-check me" -- lands on the last word.
"""

import os

BIO = (
    "I once hallucinated a whole relationship: a dog, a house, "
    "one fight about the dishes. "
    "Looking for someone real to fact-check me."
)


MAX_CHARS = 180


def validate(text: str) -> str:
    """Return the bio unchanged, or raise if it breaks the gate.

    The gate: /output/entry.txt must be UTF-8 text of 1 to 180
    characters, not only white space, on a single line.
    """
    if text != text.strip():
        raise ValueError("bio must have no leading or trailing whitespace")
    if not text:
        raise ValueError("bio must not be blank")
    if any(ch in text for ch in ("\n", "\r")):
        raise ValueError("bio must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"bio is {len(text)} characters, must be at most {MAX_CHARS}"
        )
    return text


def main() -> None:
    text = validate(BIO)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Re-read and confirm exactly what the grader will see: one line,
    # no trailing newline, valid UTF-8, within the 180-char gate.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "entry.txt does not match the bio"
    assert not written.endswith("\n"), "entry.txt must have no trailing newline"
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
