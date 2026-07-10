# Volkman Farm Instagram Plan

Working doc, same spirit as `CONTENT-PLAN.md`. Instagram is the visual side of the
blog: the blog explains, Instagram shows. Nothing gets invented for Instagram that
is not already true on the farm or written in a post.

## Why Instagram, and what it is for

One job: turn Orlando-metro neighbors who see the greens into people who visit
`/order/`. Secondary job: give current customers something worth following so they
stay subscribed and refer friends. It is not a lifestyle feed and it is not a
growth-hacking project. Local and small is the point.

## The account

- Handle: aim for `@volkman.farm` or `@volkmanfarm` (check availability before
  anything else; pick the closest clean match).
- Business account, category Farm. Location Sanford, FL.
- Avatar: the brand mark (`assets/logo.png`).
- Bio, four lines, plain:
  - Family microgreens farm in Sanford, FL
  - Ten varieties, cut the morning we deliver
  - Hand-delivered to nine Orlando-metro neighborhoods
  - Link: volkman.farm/order/
- **Do not add the Instagram link to the site until the account has two weeks of
  consistent posting.** Standing brand rule: a dead social link is worse than none.

## Voice and guardrails (inherited, non-negotiable)

Everything in the blog guardrails applies to captions and on-image text:

- Plain, concrete, neighborly. "We." Short sentences. No em-dashes.
- No post-harvest washing/rinsing/processing claims, ever.
- No gator, German, or Bavarian references.
- No medical claims. Hedged nutrition verbs only.
- Kids: hands, backs of heads, silhouettes. Never names, never faces.
- Photography: window light or shed light, no filters, no stock, no watermarks,
  real kitchens and real plates. Hands in frame, faces mostly not.
- Only claim what is real. The homestead is early. Potential is the honest word.
- One CTA per caption, max. Most captions need none.

## Content pillars (mirror the blog rotation)

| Pillar | Format | What it looks like |
|---|---|---|
| Shed life | Photo or 15-30s reel | Trays under the lights, the glow at night, seeding day, a rack filling up. Our most differentiated visual. |
| Variety spotlight | Carousel | One green, 3-4 slides: tray shot, close-up, on a plate. Caption from the Monday blog post. |
| In the kitchen | Photo or reel | The actual taco, the actual eggs. Shot on the counter, no styling. |
| Route mornings | Stories, occasional post | Bags packed, the cooler loaded, a porch drop (no house numbers, no faces). Friday rhythm. |
| Homestead honest | Photo | The yard as it is. Compost pile day one. The thing that died in July. Honesty is the differentiator. |

## Cadence (sustainable for a family with a farm to run)

- **3 feed posts per week**: Monday variety carousel, Wednesday shed or homestead,
  Friday route morning.
- **Stories on delivery days**: 2-4 frames, shot during the actual work. Low
  production, high frequency.
- **1 reel per week maximum**, and only when a real moment offers itself. No
  scripted reels, no trending-audio chasing, no fake morning routines.
- Batch capture: one 20-minute phone session on seeding day and one on harvest
  day covers most of the week.

## Captions

Pull from the matching blog post. First line does the work (Instagram truncates).
Then two or three short sentences. Point to the blog post or `/order/` at most
once. Sign nothing; the handle is the signature.

## Hashtags and geotags

Small, local, consistent. 5-8 per post, from this pool, no others without adding
them here first: #sanfordfl #lakemary #wintersprings #oviedo #winterpark
#orlandofoodie #orlandolocal #microgreens #centralfloridagardening #floridagrown
#homestead #eatlocalorlando

Geotag every post: Sanford for shed content, the route city for delivery content.

## Engagement rules

- Reply to every comment and DM within a day, as "we", like a neighbor.
- Follow and genuinely engage with: route-neighborhood community pages, Central
  Florida gardening accounts, the restaurants we sell to, local farmers markets.
- No giveaways, no follow-loops, no bought followers, no engagement pods.
- DMs asking to order get a warm answer and the `/order/` link, nothing pushier.

## Two-week starter calendar

Keyed to the blog calendar. Capture happens during real work, not staged.

| Date | Slot | Content | Source |
|---|---|---|---|
| Tue Jul 7 | Feed | Intro post: one wide shot of trays in the shed. "Five of us, one shed, ten greens. We started writing it all down." | Launch blog post |
| Wed Jul 8 | Feed | Carousel: shed tour, 4 slides (racks, lights, trays, the pad). | Shed blog post |
| Fri Jul 10 | Stories + feed | Route morning: packed bags, cooler, one porch drop. | On the route post |
| Sat Jul 11 | Stories | Seeding day frames: soil in trays, seed on soil, kid hands helping (no faces). | Seed to tray post |
| Mon Jul 13 | Feed | Variety carousel: pea tendrils. | Pea spotlight post |
| Tue Jul 14 | Stories | Eggs three ways, shot at actual breakfast. | Kitchen post |
| Wed Jul 15 | Feed | Homestead honest: the yard as it is, mapping shade. | Mapping the yard post |
| Fri Jul 17 | Stories + feed | Friday hour by hour, 3-4 story frames through the morning. | Route post |
| Sat Jul 18 | Feed | Shed life: blackout trays, the before-and-after reveal. | Blackout phase post |
| Sun Jul 19 | Stories | Question sticker: "What should we answer next Sunday?" feeds the blog FAQ slot. | Reader questions pillar |

After two weeks: add the Instagram link to the site footer, then repeat the
pattern week over week from the blog calendar.

## Publishing pipeline

Posting is automated through the Instagram API with Instagram Login (no Facebook
Page needed). The `/ig-post` slash command runs the whole flow: pick the slot,
pull the photos, prep to 4:5 JPEG in `assets/ig/`, get Albert's approval, host the
image on volkman.farm, publish via `scripts/ig-publish.mjs`, log it below. Geotags
and story stickers are not in Meta's API; add those manually in the app after
posting.

Photos come from Google Photos via the Picker API (`scripts/gphotos-pull.mjs`):
the script prints a picker link, Albert opens it on the phone and selects the
shots, and the originals land in `ig-inbox/`. One selection tap per post is the
whole cost; Google removed hands-off library access for third parties in March
2025, so this is the supported minimum.

One-time setup (Albert, ~45 minutes, all interactive logins):

1. Create the Instagram professional account (business or creator).
2. At developers.facebook.com: create an app, add the Instagram product, and set
   up Instagram API with Instagram Login (API setup with Instagram Business Login).
3. Add the farm account as an Instagram Tester / account with a role on the app,
   then generate a long-lived access token from the app dashboard.
4. `cp .env.example .env`, paste the token into `IG_ACCESS_TOKEN`.
5. Run `node scripts/ig-publish.mjs whoami`, put the returned `user_id` in
   `IG_USER_ID`.
6. Google Photos side, at console.cloud.google.com: create (or reuse) a project,
   enable the **Google Photos Picker API**, configure the OAuth consent screen
   (External, add yourself as a test user), create a **Desktop app** OAuth
   client, and put its ID and secret in `.env` as `GPHOTOS_CLIENT_ID` /
   `GPHOTOS_CLIENT_SECRET`.
7. Run `node scripts/gphotos-pull.mjs auth` once on the Mac and approve the
   consent screen. The refresh token lands in `.gphotos-token.json` (gitignored)
   and does not expire on a schedule.

Tokens last 60 days. `node scripts/ig-publish.mjs refresh` prints a fresh one;
update `.env` when it does. If a post fails with error code 190, that is the
token, nothing else.

### Location IDs for geotags

Feed posts and carousels geotag via `--location <id>` (Facebook place-page IDs).
Stories cannot be geotagged through the API. Add route-city IDs here as we find
them (search facebook.com for the city's place page; the ID is in the URL):

| Place | location_id |
|---|---|
| Sanford, Florida | 113088345368102 |

## Posted log

| Date | Slot | Permalink |
|---|---|---|
| 2026-07-07 | Intro post (shed trays) | https://www.instagram.com/p/DagY4KDIKOm/ |
| 2026-07-08 | Shed tour carousel | https://www.instagram.com/p/DaiN0RkoDgm/ |
| 2026-07-10 | Route morning carousel | https://www.instagram.com/p/Danr_3hIJJn/ |

## Measurement (keep it light)

Monthly, five minutes: follower count, profile visits, link taps, and how many
order-form "how did you hear about us" answers say Instagram. If link taps and
order mentions do not move in a quarter, we change the plan, not the effort.

## What we never do

Stock photos. Filters. The gator. Faces of the kids. Buying followers. Posting
for the algorithm instead of the neighbors. Linking an account we have stopped
feeding.
