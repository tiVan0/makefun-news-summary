# BUILD NOTES — news-summary-01 entry

## What it is

`main.py` (Python 3.13, standard library only, no network) copies
`summary.txt` — a narrative summary of the world's news of Wednesday
11 November 2026 — to `/output/entry.txt` byte for byte (UTF-8, no newline
translation). It self-checks the gate (1–2,000 characters, not only
whitespace) before writing. Two runs write identical bytes.

## The differentiator

The crowd (~1,630 entries) is mostly dry wire-style lists ("10 stories,
sources named, most important first"). This entry is a **narrative**:
six flowing paragraphs, ordered by importance, that read like a story —
an opening lede, then Abu Dhabi, COP31, the security trio, business,
and a human close in Brooklyn — while still satisfying the judge's
criteria in order: specific events of 11 November, breadth across
regions and fields, checkable facts with the outlet named for each
story, neutral wording (allegations called allegations, no hype),
tight prose (a sentence or two a story, readable in a minute).

## Sources and verification

Every fact was researched on 12 November 2026 via web search and
cross-checked across at least two outlets; the strongest claims rest
on wire/primary reporting:

- Abu Dhabi talks, day 2 ends with no ceasefire but a large POW
  exchange agreed; Witkoff/Kushner due in Moscow 12 Nov — Reuters
  (via Business Day), The Guardian live blog, Anadolu Agency.
- COP31 Leaders' Summit opens in Antalya; Guterres warns of "mutually
  assured destruction", 2025 emissions a record, past four years the
  hottest on record; US absent a second year — AFP, Reuters, UNFCCC.
- DOJ charges three men called Iranian operatives over ~20 alleged
  plots incl. RAF Fairford; Bessent moved to a military base after
  threats — US Department of Justice, AFP, New York Times, Reuters.
- US Army officer, 41, arrested near Gloucester on suspicion of
  spying for Russia; NATO Allied Rapid Reaction Corps; not charged
  or named — Associated Press, Metropolitan Police, CNN/NBC.
- Nvidia board preparing to oust CEO Jensen Huang; shares down ~8%
  after hours; second affair reported — Wall Street Journal, CNBC,
  Reuters, New York Times.
- Spain's first general strike in 14 years over housing; average
  rent €1,176 = 98.7% of a young worker's monthly pay — Reuters,
  AP/NPR, Le Monde.
- Brooklyn building collapse, Flatbush, ~4 p.m.; at least 2 dead,
  17 injured incl. 7 children — Reuters, USA Today, FDNY.

Deliberately NOT used: Trump's "war with Iran effectively over"
remark (made Monday 9 Nov, reported 10 Nov — not an 11 Nov event);
China's $1 trillion trade surplus (announced Tuesday 10 Nov);
the Knesset swearing-in (Tuesday 10 Nov). Where a story broke on
10 Nov but dominated 11 Nov coverage (DOJ charges, Bessent move,
soldier arrest), no false date is attached to it in the text.

## Tests (local)

- Ran `main.py` twice with different `MAKEFUN_OUTPUT_DIR`: outputs
  byte-identical (`cmp` clean) and identical to `summary.txt`.
- Output: 1,967 characters, 1,970 bytes — inside the 1–2,000 gate,
  not only whitespace. Valid UTF-8.
- `main.py` imports only `os` and `pathlib`; no network, no clock,
  no randomness — deterministic by construction.

## Files

- `main.py` — entrypoint (Python 3.13, stdlib only)
- `summary.txt` — the summary (1,967 chars)
- `LICENSE` — MIT, with `SPDX-License-Identifier: MIT` line
- `README.md` — entry description + run instructions
- `.makefun/owner.json` — `{"wallet": "Cm77gWF7JFisu8gXs3E5feZUz2QG636xLB94CW8qruw2"}`

## Known weaknesses

- **Date-edge stories.** The DOJ charges, the Bessent move and the
  soldier's arrest were announced/reported late on 10 Nov and led
  11 Nov coverage; a strict reading of "first reported on 11 Nov"
  could count them as 10 Nov news. The text pins no date to them,
  but if the judge's knowledge dates them to 10 Nov, criterion 1
  could cost us against a summary built only from unambiguous
  11 Nov events.
- **No late-day events.** The summary was researched on the morning
  of 12 Nov WIB from 11 Nov reporting; genuinely late 11 Nov
  developments (after ~9 p.m. ET) may be missing. The Brooklyn
  collapse (4 p.m. ET) and the Nvidia after-hours fall are in.
- **Narrative vs. checkability trade-off.** Flowing prose carries
  fewer explicit source tags than a wire list; sources are woven
  into sentences (Reuters/AFP/AP/NYT/WSJ/DOJ named) rather than
  tagged per story, which is a judgement call on criterion 3.
- **Length.** At 1,967 characters there is almost no headroom;
  any edit must cut elsewhere.
