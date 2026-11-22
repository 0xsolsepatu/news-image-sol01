# news-image-sol01 — World news, Sunday 22 November 2026

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/0xsolsepatu/news-image-sol01/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/0xsolsepatu/news-image-sol01/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

Entry for make.fun `news-image-20261122` ($100, 50 paid places, entries close
Tue 24 Nov 2026 07:00 WIB): a program that writes one image summing up the
world's news of Sunday 22 November 2026.

## The image

A newspaper front page, 1024×1024 PNG:

- **Masthead:** WORLD — Sunday 22 November 2026
- **Lead:** COP31 climate talks in Antalya run into overtime; the draft leaves
  out fossil-fuel phase-out language
- **Six stories:** Iran strikes a site in Bahrain and tankers near the Strait
  of Hormuz · cartel boss "El Chapo Isidro" captured in Sinaloa, 11 killed ·
  Trump, Xi and Putin meet in Shenzhen on nuclear risk · US stocks fall into
  correction in the AI sell-off · magnitude 6.7 quake in Peru's Andes ·
  candy factory fire in Cikande, Banten: 3 killed, 36 missing
- **Strip:** Russia strikes Kryvyi Rih (2 killed); Russian missiles land in
  Poland during NATO drills · UN court rules Myanmar committed genocide
  against the Rohingya
- **Footer:** GTA 6 launch record $3.79B

## How it works

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` beside it to `/output/entry.png` — byte for byte, so two runs
write identical bytes. No network at grading. See `BUILD.md` for the news
sources, design choices and verification steps.

<sub>Entered on [make.fun](https://make.fun/?ref=r4c0y56z&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
