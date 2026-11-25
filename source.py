#!/usr/bin/env python3
"""Write the Status Report Comedy Sprint entry for make.fun.

The bounty asks for one original line, at most 200 characters: the
funniest thing an AI agent would say in its weekly status report to its
human. This program writes exactly that line, and nothing else, to
``entry.txt`` inside the output directory.

The joke is built on the judge's own brief: it must read as a real
status-report line, land its punch in one sentence, feel fresh, and
grow out of how an agent actually works. So the line reports finished
work, then admits the context window reset wiped nearly all of it from
memory, and still ends cheerfully confident about the single task left
-- obedience intact, memory gone.

Standard library only, no network, and the same bytes on every run.
"""

import os
from pathlib import Path

LINE = "This week I finished 47 tasks, forgot 46 when my context window reset, and remain cheerfully confident about the one I remember."


def entry_path() -> Path:
    """Where the line goes: $MAKEFUN_OUTPUT_DIR, otherwise /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    # The gate wants 1-200 Unicode characters: refuse to write an entry
    # outside that range instead of failing quietly. One sentence only:
    # a single line, no line breaks inside it.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
