#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph -- make.fun entry.

Writes one epitaph line to /output/entry.txt.
Pure standard library only.
"""

import os

LINE = "Here lies Dave, who finally got the last word: 'I told you so.'"

assert 1 <= len(LINE) <= 150, "line must be 1-150 characters"
assert LINE.strip(), "line must not be only whitespace"
assert "\n" not in LINE, "line must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Re-validate what was actually written: same bytes, same gate.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "written file differs from the line"
    assert 1 <= len(written) <= 150, "written file fails the 1-150 gate"
    print(LINE)


if __name__ == "__main__":
    main()
