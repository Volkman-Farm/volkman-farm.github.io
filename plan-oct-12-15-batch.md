# Plan: Oct 12 - Oct 15, four posts

Written 2026-10-15. All four are backfills. Slate proposed by Claude and approved by Albert
2026-10-15 ("good"). Oct 7-11 drafts are backdated to their calendar dates (Albert's call
2026-10-15). The next-quarter planning session is still owed.

## Interview results (2026-10-15)

| Question | Albert |
|---|---|
| The 2 birds | **Reintegrated without issue** |
| Chicks | **Plan still in progress** |
| Cover crop, food forest | **No changes** |
| Order form | **Nobody has used it yet. It emails Albert, then he reaches out to the person** |

## The four

| Date | Pillar | Post | Words | Facts |
|---|---|---|---|---|
| Mon Oct 12 | In the kitchen | Stir-fry and fried rice: in at the very end | ~400 | Off-heat finishing, wash and dry first (customer's step). Available varieties only |
| Tue Oct 13 | Homestead journal | A quiet week in the run | ~250 | Interview only. Short on purpose |
| Wed Oct 14 | Permaculture | Small and slow solutions | ~650 | Holmgren principle 9 against published facts: 5 weeks in the brooder, one rack in the shed, front field mowed with no next step, trees unpicked |
| Thu Oct 15 | On the route | What happens after you hit send | ~380 | The form fields as built; it emails Albert; he reaches out to confirm the first delivery day and total (the site's own promise). No payment method, no response time, no usage claims |

## Hard lines for this batch

- **No usage claims for the order form** either way: never say people use it, and don't
  publish that nobody has (buyer counts are commercially sensitive).
- **No payment method** and no "within a day" promise in post copy.
- **Anniversary and the trip** stay out. "We just got back today" is Oct 15, so it can't
  appear in an Oct 13 post anyway.
- **The birds:** "without issue" only. No pecking-order detail, no flock count, no laying claim.
- **Chicks:** still a plan, nothing ordered.
- Radish, kohlrabi, chard never named as available.
- Same rules as every batch: no em-dashes, washing as the customer's step, nutrition hedged,
  kids by birth order and role, at most one CTA, at least one internal link, VOICE.md
  banned-mannerism grep before commit.

## Found along the way, not in this batch

`pages/order.liquid`: lists kohlrabi; meta description names radish; "Up to 40x the
sulforaphane" unhedged; mustard "Aids digestion"; "Most neighbors start with" implies a
customer base. `pages/thanks.md` promises a text "within a day". Albert to decide.

## Build and verify

Heroes as SVG plus 1200x630 PNG via headless Chrome, read back (Sonnet agent). Build must
pass; all dates are past so no fake clock needed. Open all nine (Oct 7-15) on the running
8083 server. Mark the rows in CONTENT-PLAN.md, commit after review, stop. No push.
