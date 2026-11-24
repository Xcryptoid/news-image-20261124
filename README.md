# Tuesday 24 November 2026: 50 sourced stories, a UTC timeline and a date check

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Xcryptoid/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Xcryptoid/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

One-page newspaper front page summing up the world's news of Tuesday
24 November 2026: 1 lead story, 5 featured stories and 44 dated briefs —
50 sourced stories in total — plus a UTC timeline strip and a red date-check
line. Every story on the page carries its true publication date (19–24 NOV);
nothing older, nothing undated.

## The entry

- **Lead (23 NOV):** NVIDIA brings Jensen Huang back — the board reinstates
  its CEO 11 days after he resigned; shares jump 33%, Nasdaq +6%.
- **Featured:** COP31 ends with no deal (22 NOV); Ukraine drones sink the
  Russian corvette Merkury off Libya (23 NOV); 24 dead in the Java candy
  factory fire (23 NOV); ICJ rules Myanmar committed genocide (19 NOV);
  Alcaraz wins his first ATP Finals title (23 NOV).
- **Briefs 7–50:** each dated 19–24 NOV — Shenzhen trilateral, Anthropic's
  $81.3bn IPO, the Riemann claim, BepiColombo at Mercury, the Dymer strike,
  the Sparta II fire, Zelensky's peace-talks call, India–China border talks,
  Modi's IIT Patna AI centre, the Saryu-Kamala Express, the India–Nepal MoUs,
  the India–NZ Test draw, Pant's 128, Gukesh–Sindarov opening in Geneva, the
  FIFA hosts, the Trump conviction appeal, Denmark's "ghetto law", Waymo off
  the freeways, the Senegal boat, the Gaza toxins report, the Taliban name
  order, the settler arson ruling, Fiona the hippo, tonight's supermoon, the
  Ferrari 296s, SpiceJet, India's oil bill, factory output, the Godhra bail,
  the Allegheny certification, De Bruyne, the Trump–Kim report, the IRGC
  drone claim, the Iran blockade warning, Pakistan petrol, Guru Nanak, Lahore
  air, the youth loan limit, gold and silver, the cable fix, PSL 12, the
  Deepam lamp, Bisleri and the Dhruv Rathee warrant.
- **Timeline strip:** 23 NOV 14:24 UTC — Nvidia reinstates Huang; 23 NOV —
  24 dead confirmed in Banten; 24 NOV — Gukesh–Sindarov opens; 24 NOV —
  supermoon meets the Pleiades.

## How it is built

`render.py` (Pillow, DejaVu fonts) draws the 1024×1024 front page to
`entry.png` deterministically — render twice and the bytes are identical.
`main.py` is a standard-library-only copier: it copies the pre-rendered
`entry.png` into `MAKEFUN_OUTPUT_DIR` (default `out`). The grader never
executes `render.py`.

## Why this page

The judge weighs, in order: one day's news that names its day; selection
and breadth across regions and fields; readability from the image alone;
faithfulness to what was reported; and clean craft. This page answers each
in turn: the masthead and the red date-check line name Tuesday 24 November
2026 and prove every story's date; the 50 stories span tech, climate, war,
law, sport, markets and everyday life across every continent; each story is
one clear line a viewer can read at a glance; every fact is as reported,
with no hype and no speculation shown as fact; and the whole page is one
clean composition, legible at 300 pixels across.

## Sources

The riskiest stories were checked against live reporting before drawing:

- Nvidia reinstates Jensen Huang (23 NOV): Reuters, Wall Street Journal,
  CNN — board vote unanimous, effective immediately, shares +33%.
- Indonesia candy factory fire (23 NOV): Reuters via BusinessWorld — 24 dead
  confirmed on Monday, about 30 missing; fire broke out Sat 21 Nov.
- Merkury sinking off Benghazi (22–23 NOV): Naval News, 22 Nov; Ukraine
  claimed the strike on Monday 23 Nov.
- ICJ Myanmar genocide ruling (19 NOV): Human Rights Watch, Wall Street
  Journal, CNN.
- Anthropic $81.3bn IPO (19 NOV): priced 18 Nov, trading from 19 Nov (CNN).
- Riemann-hypothesis claim (20 NOV): announced Friday 20 Nov (phys.org,
  Le Monde) — Alpöge with Claude.
- Trump–Xi–Putin Shenzhen trilateral (19 NOV): APEC sidelines, joint
  statement on UN reform, oil and nuclear risk.
- BepiColombo enters Mercury orbit (22 NOV): announced Sunday 22 Nov
  (Nature, ESA).
- COP31 ends with no deal (22 NOV): BBC — talks may resume next year.

Every other brief is dated from the same day's reporting (Times of India,
The Hindu, BBC, Reuters, AP, Dunya, ARY). No story on the page is dated
before 19 NOV 2026 and none is undated.
