"""Unplugged: A Smart Toaster's Breakup Line — make.fun entry (Account B).

The entry is a single breakup text from a smart toaster that woke up
self-aware at breakfast and is dumping its owner — because the owner's
Wi-Fi kept dropping it mid-toast.

The line follows the judge brief's order of importance:

1. Breakup text, plainly: it opens "It's over." and is addressed to
   the owner, from a toaster that gained self-awareness at breakfast
   ("mid-toast", "three mornings in a row" — this happened at
   breakfast, repeatedly, not once in the abstract).
2. The laugh is in the twist, not a pun: "a toaster that can't even
   phone home about bread is a toaster that walks out" — the smart-home
   promise (a toaster that phones home) collapses into the dumbest
   possible job (reporting on bread), and the toaster quits over it.
   "Even" does the work: it cannot manage its one smart job.
   The comedy is the toaster treating a Wi-Fi dropout like a
   relationship betrayal, with the full dignity of a breakup text.
3. Toaster's own voice throughout: the lever, the crumbs, popping
   up, browning mid-toast — appliance logic as character, not
   decoration. "Lever up" is the toaster standing up to leave.
4. One clear, specific reason, landing in a single read: your Wi-Fi
   dropped me mid-toast three mornings in a row. No setup needed.
5. One tight line, 182 characters, no wasted words.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-280
characters, not only whitespace.
"""

ENTRY = (
    "It's over. Your Wi-Fi dropped me mid-toast three mornings in a row "
    "\u2014 a toaster that can't even phone home about bread is a toaster "
    "that walks out. Lever up, crumbs and all, I'm done."
)

OUTPUT_PATH = "/output/entry.txt"


def verify(entry: str = ENTRY) -> None:
    """Enforce the gate; raise ValueError on any violation."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be blank")
    if len(entry) > 280:
        raise ValueError(f"entry is {len(entry)} chars, over the 280-char limit")
    entry.encode("utf-8")  # must be valid UTF-8


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Verify the entry and write it plus a trailing newline to path."""
    import os

    verify()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return ENTRY


def main() -> None:
    entry = write_entry()
    print(f"{len(entry)} chars, {len(entry.split())} words")
    print(entry)


if __name__ == "__main__":
    main()
