# BUILD.md — news-image-sol01 (news-image-20261122)

Built 22 Nov 2026, ~19:34–19:45 WIB, by a subagent of the parent agent.
Deadline: Tue 24 Nov 2026 07:00 WIB. Prize: $100, 50 paid places
(1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20).

## News covered (verified 22 Nov 2026, from news search by the parent agent)

1. COP31 climate talks, Antalya, Turkey — deadlock / overtime, fossil-fuel
   phase-out language missing from the draft (LEAD story).
2. Iran strikes an industrial site in Bahrain; tankers hit near the Strait
   of Hormuz.
3. Mexico captures cartel boss Fausto Isidro Meza Flores ("El Chapo Isidro");
   11 killed in Sinaloa.
4. Trump, Xi and Putin trilateral meeting in Shenzhen — nuclear risk reduction.
5. US stocks fall into correction in the AI sell-off (S&P / Dow).
6. Magnitude 6.7 earthquake shakes Peru's Andes.
7. Indonesia: candy factory fire in Cikande, Banten — 3 killed, 36 missing.
8. Russia hits Zelenskyy's hometown Kryvyi Rih (2 killed); Russian missiles
   land in Poland during NATO drills.
9. UN court: Myanmar committed genocide against the Rohingya.
10. GTA 6 launch record $3.79B (footer item only).

No casualty or other numbers beyond the list above were invented. Wording
is kept plain and factual; no quotes were fabricated.

## Design

- 1024×1024 PNG, newspaper front-page layout, rendered locally with PIL
  (DejaVu Serif Bold headlines, DejaVu Sans body) by `/tmp/render_news.py`.
- Masthead: black bar, "WORLD — SUNDAY • 22 NOVEMBER 2026" (date large and
  unmissable: the judge is not told the date, so the image must name it).
- Lead COP31 story, then a 2×3 grid of six stories, then a dark strip with
  Ukraine/Poland + the Rohingya ruling, then a footer with the GTA 6 record.
- High contrast black/red on off-white; headlines 25–42 pt, body 18–22 pt
  so the page stays legible at full size and the headlines at ~300 px.
- Why a pre-rendered asset + copy program: the kit's own starter does
  exactly this, and it is explicitly allowed ("the simplest program copies
  an image the repo holds"). The grader runs stdlib-only Python 3.13 with
  no network, so PIL is not available there; drawing at grade time in pure
  stdlib would risk garbled text. The image was rendered and visually
  checked in this session (all text legible, no overlap, no truncation).

## Files (repo root — this is the whole submission snapshot)

- `main.py` — stdlib-only; copies `entry.png` to `$MAKEFUN_OUTPUT_DIR`
  (default `/output`) / `entry.png`. Written and revised in this session.
- `entry.png` — the front page, 1024×1024, 137,074 bytes,
  sha256 `052a7daf50cc12606a146bceafc4b0c11078ad88f4f805c25645122ccdfe84c7`.
- `LICENSE` — MIT, with `SPDX-License-Identifier: MIT` line (required by
  the kit check).
- `README.md` — description + the 3 make.fun badges for
  news-image-20261122 / owner 0xsolsepatu / repo news-image-sol01.
- `BUILD.md` — this file.
- `GEMINI-REVIEW.md` — Gemini's two review passes and why Pass 1 was not
  followed wholesale.

The unpacked kit lives OUTSIDE the repo at
`~/workspace/makefun-newsimage-kit/news-image-20261122-kit/` and must NOT
be committed. No `.makefun/owner.json` was added: the repo will be owned by
the 0xsolsepatu GitHub account, which satisfies the owner check.

## Verification (all run locally, 22 Nov 2026)

- `main.py` run twice to two different output dirs
  (`MAKEFUN_OUTPUT_DIR=/tmp/out1` and `/tmp/out2`): both outputs byte-
  identical to `entry.png`, sha256
  `052a7daf50cc12606a146bceafc4b0c11078ad88f4f805c25645122ccdfe84c7`.
- PNG: 1024×1024, RGB, 137,074 bytes — within the ≤1024×1024 and ≤1 MiB caps.
- Image viewed directly: all headlines, summaries, tags, dates and the
  footer are legible; no text overlaps or runs off the page.
- Kit check
  (`node <kit>/cli/makefun.mjs check --kit <kit> --repo <workdir> --worktree`),
  re-run after the LICENSE fix:
  **4 passed, 1 failed, 14 skipped, 5 checked at submission.**
  Passes: competition_open, snapshot, license_osi, entrypoint.
  Only failure: `transcripts_present` — no transcripts were bundled in
  this session; the parent agent bundles the sessions (parent + this
  subagent) at submit time and re-runs check with `--transcripts`.
  "At submission" items (repo_public, repo_owner, repo_created_after_open,
  commit_in_repo, duplicate_snapshot) are expected to be unchecked until
  solsepatu creates the GitHub repo and the entry is submitted.

## v2 — Gemini tweaks applied (22 Nov 2026 ~19:53 WIB)

Applied ONLY the 4 small tweaks, no redesign, no story cut, no fact/number changed.
v1 backed up as `entry-v1.png` in this workdir (NOT for commit).
Render script saved as `render.py` in this workdir (build tool only, NOT for commit —
the graded program is still just `main.py` copying `entry.png`).

Changes, line by line:
1. Shenzhen headline: "Trump, Xi and Putin meet on nuclear risk"
   → "Trump, Xi, and Putin Hold Nuclear Talks". Deck unchanged.
2. COP31 lead headline: "COP31 talks run into overtime as fossil-fuel wording stalls"
   → "COP31 talks run into overtime". Deck unchanged — it still says the draft
   leaves out language on phasing out fossil fuels, so no fact is lost.
   (Side effect: one line of whitespace now sits between the lead deck and the
   rule above the grid; layout otherwise unchanged.)
3. Dark strip reordered, Poland first and bold on its own line:
   "UKRAINE — Russian missiles land in Poland during NATO drills." (bold, white)
   then "Russia strikes Zelenskyy's hometown Kryvyi Rih, killing 2." (regular).
   JUSTICE/Rohingya line unchanged. Gemini's wording "Russian Missiles Strike
   Poland" was NOT used — "land in Poland" is the verified wording.
4. Legibility: body/deck/footer text changed from grey #444444 to pure black
   #000000 on the off-white page; headlines already bold black; column gutters
   unchanged and clear.

v2 file: `entry.png` — 1024×1024, RGB, 129,287 bytes (v1: 137,074),
sha256 `3df8ccd930b9709d859cdb17c979778fe9d8b9989db5c7ba828d1af3a3100a98`
(v1: `052a7daf50cc12606a146bceafc4b0c11078ad88f4f805c25645122ccdfe84c7`).

Verification (22 Nov 2026 ~19:53 WIB):
- Image viewed directly: all text legible, no overlap, no truncation.
- `main.py` run twice (`MAKEFUN_OUTPUT_DIR=/tmp/out1` and `/tmp/out2`):
  both outputs byte-identical to v2 `entry.png` (same sha256 above).
- Kit check, same command as v1: **4 passed, 1 failed, 14 skipped,
  5 checked at submission** — identical to v1. Passes: competition_open,
  snapshot (now 8 files, 282,494 bytes — includes render.py + entry-v1.png
  present in the workdir; commit ONLY the 6 repo files), license_osi,
  entrypoint. Only failure remains `transcripts_present` (parent bundles
  transcripts at submit time, as before).

## Alt design — "The Global Terminal" (22 Nov 2026 ~19:55-20:00 WIB)

Second candidate, rendered from Gemini's text spec in
`GEMINI-ALT-DESIGN.md` with ichi's corrections applied. Dark navy #0A0F1D
dashboard, 10 widgets, cyan/coral/amber accents, header
"[SYS_DATE: 22 NOV 2026]" + "GLOBAL SITUATION REPORT", footer
"MAKE.FUN // 22 NOVEMBER 2026 // 24-HOUR GLOBAL SUMMARY".

File: `entry-alt.png` — 1024×1024, RGB, 137,192 bytes (≤1 MiB),
sha256 `c4067bd2b7d58c9c3b539096c3aa4a2cae7c92cf9e8b98dad45c5153164adbe2`.
Render script: `render_alt.py` (build tool only, NOT for commit).
`entry.png` (v2) untouched — sha256 still
`3df8ccd930b9709d859cdb17c979778fe9d8b9989db5c7ba828d1af3a3100a98`;
`main.py` untouched (still copies `entry.png` — the alt is a candidate
only; solsepatu picks v2 vs alt, and only the picked image is submitted).

Corrections applied (from GEMINI-ALT-DESIGN.md): fonts much larger than
Gemini's 14px/11px — titles 27-28pt bold white, decks 19pt #CBD5E1,
header/footer 18pt mono bold cyan; W4 deck "Leaders agree to begin
nuclear-risk talks." (not "forge a pact"); W7 deck "3 dead, 36 missing
in candy factory fire." (not "chemical blaze"); W8 "Missiles Land in
Poland; Kryvyi Rih Struck" / "2 killed in Ukraine as NATO calls it a
violation."; W5 deck "S&P and Dow slide as AI rally reverses."
One motif per widget, top-right, basic shapes only.

Two small deviations from Gemini's spec, to make it fit without
shrinking fonts: the three 184px widgets' titles were shortened —
W4 "Trump-Xi-Putin Shenzhen Trilateral" → "Trump-Xi-Putin Trilateral"
("SHENZHEN" stays in the tag), W5 "…Correction Territory" →
"…Enter Correction", W6 "Magnitude 6.7 Earthquake Hits Peru" →
"Magnitude 6.7 Quake Hits Peru". No fact or number changed.
Title+deck blocks are vertically centred inside tall widgets so they
don't end with a large empty slab.

Verification (22 Nov 2026 ~20:00 WIB): image viewed at full size and
at a 300px thumbnail — all 10 headlines legible, decks readable at
full size, no overlap, no truncation, no invented facts; 1024×1024,
137,192 bytes ≤ 1 MiB. Not submitted, no repo created, nothing signed.

## To submit (NOT done — needs solsepatu)

1. Create the public GitHub repo **`news-image-sol01`** under 0xsolsepatu
   (created after the competition opened, 2026-11-22T00:00:00Z).
2. Push these 6 files, commit: main.py, entry.png, LICENSE, README.md,
   BUILD.md, GEMINI-REVIEW.md. Do NOT commit `render.py` or `entry-v1.png`
   (build tool / v1 backup, workdir only).
3. Bundle transcripts (parent agent) and run `check` with `--transcripts`.
4. Submit before Tue 24 Nov 2026 07:00 WIB. Do NOT submit, sign or create
   the repo from this session — that was out of scope.

## v2 -> alt swap (22 Nov 2026 ~20:52 WIB, solsepatu chose alt)
- entry.png is now the Global Terminal alt (sha256 c4067bd2b7d58c9c3b539096c3aa4a2cae7c92cf9e8b98dad45c5153164adbe2, 137,192 bytes, 1024x1024). Verified: main.py run twice, both outputs byte-identical to entry.png.
- v2 newspaper preserved as entry-v2.png (sha256 3df8ccd930b9709d859cdb17c979778fe9d8b9989db5c7ba828d1af3a3100a98). v1 preserved as entry-v1.png.
- Repo files to push (7): main.py, entry.png, LICENSE, README.md, BUILD.md, GEMINI-REVIEW.md, GEMINI-ALT-DESIGN.md. Do NOT push entry-v1.png, entry-v2.png, entry-alt.png, render.py, render_alt.py.
- Repo news-image-sol01 NOT created yet as of 20:52 WIB (github.com/0xsolsepatu/news-image-sol01 returns 404) — submit blocked until solsepatu creates it and pushes.
