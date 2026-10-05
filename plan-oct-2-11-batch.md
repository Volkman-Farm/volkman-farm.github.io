# Plan: Oct 2 - Oct 11, ten posts

Written 2026-10-05. Oct 2-4 are backfills; Oct 5 is today. The calendar ended at Oct 3, so
Oct 4-11 are new rows, proposed by Claude and approved by Albert 2026-10-05 ("I propose a
slate"). The next-quarter planning session is still owed; the Oct 3 post collects reader
topics for it.

## Interview results (2026-10-05)

| Question | Albert |
|---|---|
| The shed in October | **A/C runs less, humidity is lower, grow times are longer** |
| How readers send topics | **Email** (site address: micros@volkman.farm) |
| Radish, kohlrabi, chard back? | **No, and no plan to order until someone requests them** |
| Homestead now | **The 2 hurt birds moved in with the rest of the flock yesterday (Sun Oct 4). Next week is Albert's wedding anniversary; a plan for new chicks comes after that. Cover crop mowed again last week. No solid next plans; ask readers for thoughts** |
| Edges | Use the parcel GIS |
| Root hairs vs mold | **Yes, he's had to tell them apart; generally by smell and appearance** |

## Rows changed from the proposal, and why

- **Thu Oct 8 "Why each route runs on the day it does"** is spent: the family-calendar
  reasons are published in 7 posts. Replaced by the 64 oz clamshell being a volume and the
  price being a weight, which no post covers.
- **Sun Oct 4 and Oct 11** run as non-spotlight variety posts (the Sep 13 and Sep 27
  precedent). Only the 7 available varieties are named.
- **Fri Oct 9 root hairs** repeats one paragraph of the Aug 8 home-growing post. Kept as a
  short dedicated post because Albert has done the check himself; it links back and adds
  his first-hand smell-and-look test, no new mechanism.

## The ten

| Date | Pillar | Post | Words | Facts |
|---|---|---|---|---|
| Fri Oct 2 | Growing notes | The shed in October | 380 | Interview. No temperatures, no day counts, no because for longer grow times |
| Sat Oct 3 | Reader questions | What should we write about next? | 260 | Email micros@volkman.farm. No CTA beyond the email |
| Sun Oct 4 | Variety spotlight | Four families on one shelf | 520 | Mustard family: arugula, broccoli, kale, mustard. Beet (amaranth family), cilantro (carrot family), pea (legume) |
| Mon Oct 5 | In the kitchen | Pesto, and other things you blend at home | 470 | Raw use, wash before using as the customer's step; no "we made" |
| Tue Oct 6 | Homestead journal | Back with the flock | 700 | Interview. Ends asking readers for ideas by email |
| Wed Oct 7 | Permaculture | The edges we keep | 850 | GIS: parcel edge ~1,230 ft; front field ~830 ft of edge; old run ~150 ft of fence vs 300 ft outer + 290 ft inner netting now; oldest daughter's first bed on the lowest point |
| Thu Oct 8 | On the route | A 64 oz clamshell, sold by the ounce | 400 | 64 oz clamshell is a volume; $3.50/oz is a weight; every tray is weighed (Sep 18), into the clamshell and onto the scale (Sep 25). No fill weight given |
| Fri Oct 9 | Growing notes | Root hairs or mold? | 330 | Interview plus the Aug 8 paragraph |
| Sat Oct 10 | Reader questions | Are microgreens more nutritious than the grown-up plant? | 450 | Research pass (subagent), hedged verbs only |
| Sun Oct 11 | Variety spotlight | Seven greens, seven clocks | 480 | Day ranges from `_data/varieties.js`, framed as summer clocks after Oct 2 |

## Hard lines for this batch

- **The 2 birds:** they're out of the brooder and with the flock as of Sun Oct 4. No
  prognosis beyond that, no flock count, no species for the attacker.
- **Chicks:** still a plan. The order comes after next week, not "as soon as the brooder
  empties" any more. The Sep 30 post said that, so Oct 6 corrects it forward.
- **Anniversary:** flagged for review; cut if Albert doesn't want it in print.
- **Cover crop:** "mowed again", not the chop-and-drop cut and not a termination. The 8-way
  species inventory is still owed; don't discharge it.
- **No reasons invented** for longer October grow times or the lower A/C load.
- **Radish, kohlrabi, chard** are never named as available.
- Same rules as every batch: no em-dashes, washing as the customer's step only, nutrition
  hedged, kids by birth order and role, one CTA max, at least one internal link, the VOICE.md
  banned-mannerism grep against the diff before commit.

## Build and verify

Heroes as SVG plus 1200x630 PNG via headless Chrome, read back (delegated to a Sonnet agent
with existing heroes as references). `npx @11ty/eleventy` must pass. Oct 6-11 won't build
until their date, so verify them with a fake-clock build. Then `eleventy --serve` and open
Oct 2-5 in Albert's browser (one-time approval, 2026-10-05). Mark the rows in CONTENT-PLAN.md,
commit after review, stop. No push.
