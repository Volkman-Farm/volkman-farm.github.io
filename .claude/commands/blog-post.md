---
description: Scaffold the next blog post from CONTENT-PLAN.md, mark it done, and show the draft for review.
---

Scaffold the next blog post for volkman.farm. Follow these steps exactly:

1. Read `CONTENT-PLAN.md`. Re-read the **Voice and guardrails** section every time; it is
   the contract for every word you write.
2. Find the target topic:
   - If `$ARGUMENTS` names a topic, date, or title, use that row.
   - Otherwise take the first row in the calendar whose status is `[ ]`.
   - If today's date is past the row's date, still write it (we backfill in order).
3. **Fact check before drafting.** If the angle touches anything on the homestead that
   might not exist yet (animals, structures, plantings, results), ask Albert what is
   actually true before writing. Never invent specifics.
4. Draft the post at `posts/<slug>.md` where `<slug>` is a short kebab-case version of
   the title (no date prefix). Frontmatter:

   ```yaml
   ---
   title: <final title, sentence case>
   description: <140-160 char meta description>
   date: <row date>T09:00:00-04:00
   pillar: <pillar name from the row>
   ---
   ```

   Body requirements:
   - 500-800 words, plain neighborly voice, first person plural
   - No em-dashes anywhere
   - No post-harvest washing/rinsing/processing claims
   - No gator, German, or Bavarian references
   - Nutrition claims hedged ("carries", "is high in", "research suggests")
   - At least one internal link (variety, city, /order/, /subscribe/, or /restaurants/)
   - At most one CTA
   - H2 subheads every 150-250 words; no H1 (the layout renders the title)
5. Build: `npx @11ty/eleventy`. Fix any errors before proceeding.
6. Verify the post appears at `/blog/<slug>/` and on the `/blog/` index in `_site/`.
7. Update the row in `CONTENT-PLAN.md`: `[ ]` becomes `[x] posts/<slug>.md`.
8. Show me the full draft and wait for review. Do not commit until I approve.
9. On approval: commit as `feat(blog): add post <slug>` (stage the post file and
   CONTENT-PLAN.md only), then ask before pushing.

To automate this daily, pair with the `/schedule` skill or a cron-triggered
`claude -p "/blog-post"` run.

$ARGUMENTS
