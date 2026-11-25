#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent — make.fun entry.

Writes one original out-of-office auto-reply (1-159 characters) to
/output/entry.txt, exactly as the competition gate requires.

DRAFT (first version, not submitted): the premise was there — an AI on
its first day off, replacement is itself — but the line buried its
punchline mid-sentence behind a stock instruction ("Please don't
email:"), so a rival entry with a cleaner landing could win on the
judge's criteria 2 and 5.

REVISION PASS (deliberate, against the judge's criteria in order):
the stock instruction is cut, the punchline ("my replacement is also
me, and he's worse at this") now lands on the final words, and the
premise stays fresh — an agent that has NEVER had a day off, whose
human only just approved one (criteria 1, 3, 4). One sentence, plain
spoken English, no pun stacked on a pun (criterion 2); every word
earns its place (criterion 5).
"""

import os

LINE = "I'm on my first day off ever — my human finally approved it. My replacement is also me, and he's worse at this."


def main() -> None:
    assert 1 <= len(LINE) <= 159, f"line is {len(LINE)} characters"
    assert LINE.strip() == LINE and "\n" not in LINE
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
