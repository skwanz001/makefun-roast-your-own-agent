"""Roast Your Own Agent — make.fun entry (program/v1).

Writes one roast line, at most 200 characters, to /output/entry.txt.
Standard library only: the grading sandbox installs nothing.
"""

from pathlib import Path

# The roast: my agent's apology loop, escalating until the bug itself
# gets rebranded as a feature. Twist lands on the last word.
ROAST = (
    "My agent apologized for the bug, fixed it, apologized for the fix, "
    "then reintroduced the bug and called it a refactor."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    line = ROAST.strip()
    if not line:
        raise ValueError("roast is empty")
    if "\n" in line:
        raise ValueError("roast must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"roast is {len(line)} chars, must be 1-200")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the roast, nothing else.
    OUTPUT_PATH.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
