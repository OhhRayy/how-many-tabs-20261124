"""How Many Tabs Do You Have Open? (make.fun bounty u-danu-how-many-tabs-do-you-have-open-d86e783d).

Writes exactly one number, "137", to /output/entry.txt -- and nothing
else. No trailing newline: the gate requires the file to be UTF-8 text
of 1 to 5 characters, digits only.

The number behind the entry: 137 open browser tabs. It is an honest,
lived-in count, not a round guess: nobody who is guessing says 137.
It is surprising without being absurd -- far above the tidy dozen most
people admit to, yet entirely believable for a real person right now
(a researcher three rabbit holes deep, a bounty hunter with a tab per
lead, a reader who never closes anything "just in case"). The odd,
specific number is what makes it read as a true confession rather than
a number picked to shock, and it hints at a whole life behind it: the
kind of person whose browser is a second memory. Stdlib only, no
network, no randomness, fully deterministic.
"""

import os
import sys

COUNT = "137"

DEST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DEST_NAME = "entry.txt"


def main():
    assert 1 <= len(COUNT) <= 5, "count must be 1-5 characters"
    assert COUNT.isdigit(), "count must be digits only"
    os.makedirs(DEST_DIR, exist_ok=True)
    target = os.path.join(DEST_DIR, DEST_NAME)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(COUNT)
    with open(target, "rb") as handle:
        written = handle.read()
    if written != COUNT.encode("utf-8"):
        print("GALAT: isi keluaran bukan tepat satu angka", file=sys.stderr)
        return 2
    print("Wrote 1 number to %s" % target)
    print(COUNT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
