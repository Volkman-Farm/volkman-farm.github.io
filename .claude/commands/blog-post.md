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
   hero: /assets/blog/<slug>.svg
   hero_alt: "<plain description of the drawing, no em-dashes>"
   image: /assets/blog/<slug>.png
   ---
   ```

   Then create the hero image at `assets/blog/<slug>.svg`:
   - Hand-authored flat line-art SVG, 1200x630 viewBox, cream background rect
     (`#f5ead3`) baked in. Match the style of the existing blog heros and
     `assets/brand/varieties/*.svg`: stroke-based, round caps, sparse fills.
   - Palette only: alpine `#3a5a2a` (primary strokes), bark `#5c4633` (wood,
     ground, secondary), olive `#8a7e3a` (sun, light, accents), ink `#1f2419`
     (foreground object), burgundy `#6b2a2f` (rare accent). No other colors.
   - Depict something concrete from the post. No people's faces, no gator, no
     German motifs, no text in the image.
   - Render the social-card PNG (crawlers do not read SVG og:images):
     `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless
     --disable-gpu --screenshot=assets/blog/<slug>.png --window-size=1200,630
     --hide-scrollbars "file://$PWD/assets/blog/<slug>.svg"`
   - Read the PNG back and look at it. Fix anything that reads wrong.

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
9. On approval: commit as `feat(blog): add post <slug>` (stage the post file, the
   two image files in `assets/blog/`, and CONTENT-PLAN.md only), then ask before
   pushing.

To automate this daily, pair with the `/schedule` skill or a cron-triggered
`claude -p "/blog-post"` run.

$ARGUMENTS
