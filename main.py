"""news-summary-01 entry: write the summary of 11 November 2026 world news
to /output/entry.txt.

The summary lives in summary.txt beside this file; the program copies it
byte for byte (UTF-8, no newline translation), so two runs always write
identical bytes. Standard library only, no network.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    summary = (HERE / "summary.txt").read_text(encoding="utf-8")
    # Gate self-check (RULES.txt): 1 to 2,000 characters, not only whitespace.
    if not 1 <= len(summary) <= 2000 or not summary.strip():
        raise SystemExit("summary.txt fails the gate: not 1-2000 chars")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(summary, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
