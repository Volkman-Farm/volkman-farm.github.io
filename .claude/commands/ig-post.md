---
description: Prep and publish today's Instagram post from INSTAGRAM-PLAN.md. Shows the image and caption for approval before anything goes live.
---

Publish an Instagram post for Volkman Farm. Follow these steps exactly:

1. Read `INSTAGRAM-PLAN.md`. Re-read **Voice and guardrails** every time. Determine
   today's slot from the calendar and pillars, or use `$ARGUMENTS` if it names one.
2. Get the photo(s). In order of preference:
   - A local path Albert gives in `$ARGUMENTS`, or fresh files already in `ig-inbox/`.
   - Google Photos, the primary source: run
     `node scripts/gphotos-pull.mjs pull` in the background, grab the picker
     link it prints, and send it to Albert (via the Apple Messages MCP if
     available, otherwise show it in chat). He selects the shots on his phone;
     the script downloads the originals into `ig-inbox/` (gitignored). If it
     reports the OAuth setup is missing, walk him through the setup in
     INSTAGRAM-PLAN.md first.
   - If there are no photos to be had, give him a shot list for the slot (see
     the pillar table) and stop. Never publish a placeholder or a stock image.
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
5. **Show Albert the final image(s) and caption and wait for explicit approval.**
   Always open the prepped image(s) in Preview so he can eyeball them full-size:
   `open -a Preview assets/ig/<file>.jpg` (one command, all files). Publishing is
   public and irreversible; never skip this gate.
6. On approval, host the image: commit the `assets/ig/` files
   (`chore(ig): add media for <date> post`), push, then poll
   `https://volkman.farm/assets/ig/<file>.jpg` until it returns 200 (GitHub Pages
   deploys take a minute or two).
7. Publish, geotagging with `--location <id>` from the Location IDs table in
   `INSTAGRAM-PLAN.md` (Sanford for shed/homestead content, the route city for
   delivery content; if the city is not in the table yet, find its Facebook
   place-page ID, add the row, then use it):
   - Single: `node scripts/ig-publish.mjs image <url> --location <id> "<caption>"`
   - Carousel: `node scripts/ig-publish.mjs carousel <url1,url2,...> --location <id> "<caption>"`
   - Story: `node scripts/ig-publish.mjs story <url>` (no location support)
   If the token is expired (error code 190), run `node scripts/ig-publish.mjs refresh`,
   have Albert update `.env`, and retry.
8. After publishing, verify the geotag shows on the post. Remind Albert of what
   the API cannot do: story stickers, and story geotags, are manual in the app.
9. Log it: add a row to the **Posted log** table in `INSTAGRAM-PLAN.md` (date, slot,
   permalink), commit as `docs(social): log <date> post`, push.

$ARGUMENTS
