---
description: Prep and publish today's Instagram post from INSTAGRAM-PLAN.md. Shows the image and caption for approval before anything goes live.
---

Publish an Instagram post for Volkman Farm. Follow these steps exactly:

1. Read `INSTAGRAM-PLAN.md`. Re-read **Voice and guardrails** every time. Determine
   today's slot from the calendar and pillars, or use `$ARGUMENTS` if it names one.
2. Get the photo(s). In order of preference:
   - A local path Albert gives in `$ARGUMENTS`.
   - The most recent images in the Google Drive folder he uses for farm photos
     (search Drive via MCP; confirm with him which files before using them).
   - If there are no photos, give him a shot list for the slot (see the pillar
     table) and stop. Never publish a placeholder or a stock image.
3. Prep each image into `assets/ig/` as `<yyyy-mm-dd>-<slug>[-n].jpg`:
   - Feed: 1080x1350 (4:5). Stories: 1080x1920 fits best.
   - `sips --resampleWidth 1080 in.jpg --out out.jpg` then
     `sips --cropToHeightWidth 1350 1080 out.jpg` (resample the short side first
     so the crop never upscales; crop is centered, so re-crop manually if the
     subject sits off-center).
   - JPEG only. Read the result back and look at it before proceeding.
4. Draft the caption from the plan and the matching blog post. First line carries
   the hook. No em-dashes, no adulteration claims, no medical claims, no gator or
   German references, one CTA max. Pick 5-8 hashtags from the approved pool.
5. **Show Albert the final image(s) and caption and wait for explicit approval.
   Publishing is public and irreversible; never skip this gate.**
6. On approval, host the image: commit the `assets/ig/` files
   (`chore(ig): add media for <date> post`), push, then poll
   `https://volkman.farm/assets/ig/<file>.jpg` until it returns 200 (GitHub Pages
   deploys take a minute or two).
7. Publish:
   - Single: `node scripts/ig-publish.mjs image <url> "<caption>"`
   - Carousel: `node scripts/ig-publish.mjs carousel <url1,url2,...> "<caption>"`
   - Story: `node scripts/ig-publish.mjs story <url>`
   If the token is expired (error code 190), run `node scripts/ig-publish.mjs refresh`,
   have Albert update `.env`, and retry.
8. Remind Albert of the manual finishers the API cannot do: geotag the post and
   add any story stickers from the Instagram app.
9. Log it: add a row to the **Posted log** table in `INSTAGRAM-PLAN.md` (date, slot,
   permalink), commit as `docs(social): log <date> post`, push.

$ARGUMENTS
