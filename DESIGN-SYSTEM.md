# Volkman Farm Design System

The production design system for volkman.farm. It implements the brand foundation at `/BRAND.md` and documents what is actually in `/assets/css/main.css` and `/_layouts/default.html`. Where this document and the stylesheet disagree, the stylesheet is right and this document is a bug.

The illustrated heritage direction from May 2026 was reverted on 2026-07-07 (commit `c5da537`). The mark is the logo at `/assets/logo.webp`. There is no mascot, no wordmark file, no monogram, and no crest. The typography, palette, and ornament vocabulary from that generation stayed and are documented below. The v1 typewriter system is archived at `archive/DESIGN-SYSTEM-v1-typewriter.md` for structural reference only.

If a question arises that this document does not answer, the answer is whatever makes the positioning statement in BRAND.md section 1 more believable on the page.

---

## 1. Design tokens

All tokens live in `:root` in `/assets/css/main.css`. Use the custom properties, not the hex values, anywhere downstream.

### Color

| Token | Hex | Role |
|---|---|---|
| `--cream` | `#f5ead3` | Page background. Never replaced. |
| `--ink` | `#1f2419` | Body text, borders, headings. |
| `--alpine` | `#3a5a2a` | Primary action color. Buttons, link color, nav hover, focus ring, list markers. |
| `--alpine-deep` | `#2d4720` | Button pressed and hover-darken, CTA-row links, active nav text. |
| `--olive` | `#8a7e3a` | Ornament gold. Nav and footer diamond separators, card corner roundel, laurel divider center. |
| `--burgundy` | `#6b2a2f` | Body link hover, invalid input border, error text. |
| `--bark` | `#5c4633` | Captions, metadata, footer copy, field labels, secondary text on cards. |
| `--rule` | `#c7b98f` | Hairline rules, table row borders, footer top border. |
| `--surface` | `#ede0bf` | Card and input fill, disclosure background. Derived darker cream. |

Wholesale (`[data-page="wholesale"]`) restricts to cream, ink, alpine, alpine-deep, bark. Burgundy is swapped for alpine-deep on link hover, invalid borders, and error text; olive separators become alpine; the card roundel, eyebrow, banner, and laurel divider are hidden outright.

### Typography

Three faces, woff2, self-hosted under `/assets/fonts/`.

- **DM Serif Display** (OFL, free). Display only. `dm-serif-display.woff2`. **Shipped.**
- **Source Serif 4** (Adobe, OFL, free). Body. Regular, italic, 600. **Not yet in the repo.**
- **Inter** (OFL, free). UI. 600 and 700. **Not yet in the repo.**

Until the last two land, `--body` falls back to Georgia and `--ui` to system-ui through the stacks in `main.css`. The site is legible but is not showing final typography, and any design judged against this document should account for that. `assets/fonts/README.md` lists the exact filenames and sources. This is the single highest-value outstanding task in the system; see section 9.

| Token | Size | Line-height | Tracking | Weight | Family |
|---|---|---|---|---|---|
| `--fs-h1` | `clamp(2.25rem, 5.5vw, 3.25rem)` | 1.05 | -0.015em | 400 | DM Serif Display |
| `--fs-h2` | `clamp(1.5rem, 3.75vw, 2rem)` | 1.15 | -0.005em | 400 | DM Serif Display |
| `--fs-h3` | `clamp(1.2rem, 2.5vw, 1.4rem)` | 1.25 | 0 | 400 | DM Serif Display |
| `--fs-body` | `1.0625rem` | 1.6 | 0 | 400 | Source Serif 4 |
| `--fs-lead` | `1.2rem` italic | 1.4 | 0 | 400 italic | Source Serif 4 |
| `--fs-small` | `0.875rem` | 1.5 | 0.005em | 400 | Source Serif 4 |
| `--fs-ui` | `0.95rem` | 1.4 | 0.04em | 600 | Inter |
| `--fs-eyebrow` | `0.8rem` | 1.3 | 0.18em | 700 | Inter, uppercase |

**Headings are weight 400, and `h1, h2, h3` set `font-synthesis: none`.** DM Serif Display ships a single 400 weight, so asking for 600 or 700 would either do nothing or produce a synthetic bold. Two rules currently request 700 from the display face anyway (`.card__title` and `.roundels li::before`) and get a synthesized weight, because `font-synthesis: none` is scoped to headings only. Left as-is deliberately: it reads fine at those sizes. Do not add more of them.

Blockquote is the one place the display face carries body-adjacent text: DM Serif Display italic at 1.25rem, not Source Serif. See 3.15.

No monospace anywhere in the system.

### Spacing (4pt base)

`--space-1` through `--space-9`: 4, 8, 12, 16, 24, 32, 48, 64, 96px.

### Layout

`--measure: 60ch` (body measure), `--measure-wide: 80ch` (grid and post heroes), `--gutter-mobile: 16px`, `--gutter-desktop: 24px`.

### Borders

`--border-hair: 1px` for table rules, hairline dividers, and the footer top border. `--border-rule: 2px` for inputs, cards, and buttons.

### Focus ring

`--focus-ring: 3px solid var(--alpine)` with `--focus-offset: 2px`. Applied uniformly to links, buttons, inputs, cards, and disclosure summaries.

### Motion

`--t-fast: 120ms ease-out` for hover and focus color changes. `--t-normal: 200ms ease-out` for shadow and transform on cards. All motion is suppressed under `prefers-reduced-motion: reduce`.

### Z-index lanes

Four lanes: base (0), raised (10), sticky (20), overlay (30). No fixed positioning today; the lanes exist for future toast and modal work.

---

## 2. Layout primitives

**Container widths.** Two lanes:

- `min(var(--measure), 92%)` for flowing copy and forms. Applied to `h1`, `h2`, `h3`, `p`, top-level lists, hr, blockquote, details, table, `.cta-row`, footer, and the blog list.
- `min(var(--measure-wide), 92%)` for `.grid` and `.post-hero`. `.grid` auto-fills 220px-minimum columns with `--space-5` gaps.

**Vertical rhythm.** Section openers (`h2`) get `--space-7` (48px) top margin. Subsections (`h3`) get `--space-6`. Paragraphs get `--space-4`. Body padding-bottom is `--space-8` so the footer rule never kisses the last paragraph.

**Breakpoints (mobile-first).**

- Default: phone (< 720px).
- `@media (max-width: 720px)`: tighter gutters (12px), logo to 60% width, flowing elements to 96%, narrower nav separators, smaller roundels.
- `@media (min-width: 1024px)`: desktop gutter bump.

There is no tablet breakpoint. The 60ch column scales gracefully between the two.

**The cream extends behind content.** `html` and `body` both set `background-color: var(--cream)`. The paper-grain noise overlay (a small SVG `feTurbulence` filter at roughly 4% opacity) tiles on `body`. The screen reads flat without it. Test on retina and non-retina before adjusting, and do not raise the opacity past 6%.

---

## 3. Component specs

### 3.1 Header

A single `<a href="/">` wrapping one `<img id="logo" src="/assets/logo.webp">`, above the primary nav. Width `min(55%, 220px)`, centered, `--space-7` top margin, dropping to 60% width and `--space-5` on mobile. The alt text carries the business description ("Volkman Farm, Orlando-area microgreens"), so the logo is not decorative and must keep it.

This is the whole header. There is no wordmark image, no inline monogram SVG, and no hero mark composition on any page.

### 3.2 Primary nav

`nav[aria-label="Primary"]` with a flex-wrapped centered `<ul>`. Inter caps at 600, 0.18em tracking, ink. Separators are 4px olive squares rotated 45 degrees, drawn as `li:not(:first-child)::before`. Hover goes alpine. The current page (`aria-current="page"`) gets alpine-deep text plus a 2px alpine bottom border. On wholesale the separators go alpine.

### 3.3 Headings

DM Serif Display, 400, centered, ink. Tight line-height on h1 (1.05) and h2 (1.15), normal on h3 (1.25). Negative tracking on h1 (-0.015em) and h2 (-0.005em). `font-synthesis: none`.

### 3.4 Body links

Alpine, underlined at 1px with 4px offset, hover and focus transition to burgundy over 120ms. Focus-visible adds the 3px alpine ring at 2px offset with a 2px radius. Wholesale swaps the burgundy hover for alpine-deep.

### 3.5 Lead line (`.lead`)

Source Serif italic at `--fs-lead` (1.2rem), line-height 1.4, centered, ink. The intro line on variety, city, subscribe, and restaurants pages.

### 3.6 Primary button (`input[type="submit"]`, `.btn`)

Alpine fill, cream label, Inter caps at 600 with 0.04em tracking, 14px/28px padding, 2px solid alpine border, 2px radius, min-width 220px so the primary action anchors the page. Hover darkens to alpine-deep. Active goes ink. Disabled (`:disabled` or `[aria-disabled="true"]`) uses the surface fill with bark text and bark border.

### 3.7 Secondary button (`.btn--secondary`)

Transparent fill, alpine border, alpine label. Hover inverts to alpine fill with cream label. For supporting actions where the alpine fill would be too loud.

### 3.8 CTA row (`.cta-row`)

A centered paragraph containing a strong link, body font, link in alpine-deep at 600. Deliberately short of the full button treatment so pages don't drown in CTAs.

### 3.9 Form fields

Inputs, selects, and textareas share a surface fill, 2px ink border, 2px radius, 12/14px padding (44px+ tap target), body font at 1.0625rem, block display, centered at `min(var(--measure), 92%)`. Selects use Inter 600 so the chosen option is scannable. Focus uses the global ring.

`.field` is the label-above-input wrapper used on the restaurants form: labels in Inter caps at 600, small size, bark, with the input at full width inside the wrapper.

`.honeypot` is `display: none !important` and exists for spam trapping on the order and inquiry forms. Do not repurpose it or make it visible.

### 3.10 Form errors

`.form-error` is centered burgundy text in Inter 600 at small size, pulled up 4px to sit tight under its field. `aria-invalid="true"` swaps the input border to burgundy. The wholesale variant uses ink for both.

Errors are styled but not yet wired to `aria-describedby`. See section 9.

### 3.11 Checkbox

Native input, scaled 1.4x, `accent-color: var(--alpine)`, inline inside a `<p>` next to its label, both vertical-align middle.

### 3.12 Card (`.card`)

Surface fill, 2px ink border, 2px radius, body font, relative positioned. A small olive roundel sits in the top-right corner (`::before`, 8px circle, 70% opacity). Hover and focus lift the card by -2px/-2px with a 4px alpine drop-shadow, no blur, which prints clean and reads as a stamp. `.card__title` uses the display face at 1.25rem; `.card__meta` is small bark text. The roundel is hidden on the wholesale page.

**`.card--variety`** is the variety-tile variant: right padding is extended to clear a 48px `.card__icon` SVG in the top-right corner, and the olive roundel is suppressed because the icon claims that corner. The icon rotates -4deg on hover.

### 3.13 Lists and roundels

Top-level `main > ul` uses square markers with alpine `::marker`. `.list-square` applies the same treatment to lists inside flowing copy.

`.roundels` converts an `<ol>` into numbered badges: a CSS counter renders upper-roman numerals into a 40px circle (`::before`) ringed with a 2px alpine border, display face, alpine text, 56px of left padding on the item. Drops to 36px circles and 48px padding on mobile. Used for "How it works" sequences.

### 3.14 Pricing table

`<table>` with Inter caps headers at small size over a 2px ink bottom border, and Source Serif body rows separated by hairline `--rule` borders. Second and subsequent columns are right-aligned and set in Inter 600 so prices read tight.

### 3.15 Horizontal rule and laurel divider

Plain `main > hr` is a hairline in `--rule` with `--space-7` margins, for section breaks that don't warrant ornament.

`<hr class="laurel">` renders a 120x28 inline SVG data URI: two facing sprays of laurel strokes in alpine around a 3px olive dot. Abstract ornament, no heraldry. Use between major content blocks on the homepage, About, and variety pages. Hidden on wholesale.

### 3.16 Blockquote

DM Serif Display italic at 1.25rem, line-height 1.45, with a 4px alpine left rule, constrained to `min(var(--measure), 88%)`. `cite` renders as a block in Inter caps 600, small, bark.

### 3.17 FAQ disclosure (`<details>` / `<summary>`)

Surface fill, 4px alpine left rule, 0/2px radius. Summary in Inter 600 at UI size with the native marker removed and a display-face `+` indicator at the right, swapping to `−` when open. Focus-visible gets the global ring. Used on pricing and restaurants.

### 3.18 Blog components

The blog is a first-class part of the site and these ship in `main.css` section 19.

- **`.post-meta`**: Inter caps, small, 0.04em tracking, bark. The date and pillar line above a post title or under a post h1.
- **`.post-hero`**: the post's hero image at `min(var(--measure-wide), 92%)` with a 1px alpine border and 2px radius. Sits directly under the h1.
- **`.post-list`**: the unstyled `<ul>` on `/blog/`. Each item stacks `.post-meta`, a title link in the display face at `--fs-h3`, and a description paragraph.
- **`.pager`**: a baseline-aligned flex row at the foot of a post. Uses `order` so the count sits center (`.pager-count`, bark) between previous (`order: 1`) and next (`order: 3`) links, which are alpine-deep at 600.

### 3.19 Eyebrow (`.eyebrow`) and banner (`.banner`)

`.eyebrow` is the workhorse ornament: block-level, centered, Inter 700 at 0.8rem, 0.18em tracking, uppercase, alpine. `.eyebrow--gold` recolors it to olive. Use for section eyebrows and short labels above a heading.

`.banner` draws a ribbon container in pure CSS: an alpine fill with cream text and two clip-path triangles forming the ribbon ends. One per page maximum, and most pages need none. Both are hidden on wholesale.

### 3.20 Footer

A `--space-9` top margin and a hairline top rule, then a centered flex link row (Inter caps 600, small, ink, olive diamond separators matching the nav, hover to alpine with a 6px-offset underline), then the NAP paragraph in Source Serif small, bark. No mark in the footer.

---

## 4. Page archetypes

### 4.1 Homepage (`/`)

Logo, nav, h1, then the tagline line, then the dual CTA row (kitchen and restaurant). "Why our greens" as an h2 section with bolded lead-ins. `.roundels` for "How it works". The routes list with per-city links. Standing-order callout. Footer.

### 4.2 About (`/about/`)

Logo, nav, h1, then the family story in short paragraphs: who lives here, the shed, the varieties and inputs, the routes, wholesale, and a closing CTA row. Under 600 words per BRAND.md 9.8. No portrait until the family is ready.

### 4.3 Variety landing (`/greens/[variety]/`)

h1 set by the layout ("[Variety] Microgreens"), `.lead` italic intro, `.cta-row` with the order link and price, then Flavor, Nutrition, How to use, and How we grow sections. `.list-square` for the usage list. A single `<hr class="laurel">` before the closing CTA row is welcome.

### 4.4 City landing (`/delivery/[city]/`)

The variety skeleton with local emphasis: "Where we deliver," "Your delivery day," "What we grow," "How it works in [City]." Closing laurel divider is welcome; no banner.

### 4.5 Blog index (`/blog/`)

h1, then `.post-list`. Each entry is meta, title link, description. Reverse chronological.

### 4.6 Blog post (`/blog/[slug]/`)

h1, `.post-meta` line, `.post-hero` image, then the post body at the standard measure, then `.pager`. Posts run 450 to 950 words and vary their structure by pillar; they are not templated beyond this shell. Hero art is a flat SVG in palette colors with a PNG twin for OpenGraph, both under `/assets/blog/`.

### 4.7 Wholesale (`/restaurants/`)

The restrained variant. The layout sets `data-page="wholesale"` on `<body>`. The system suppresses the eyebrow, the banner, the laurel divider, and the card roundel; swaps burgundy for alpine-deep on link hover, invalid borders, and error text; and recolors nav and footer separators to alpine. It keeps the logo header, the alpine primary button, the alpine disclosure rule, and the `.field` form pattern. Copy is more formal and takes no winks, per BRAND.md 10.3.

### 4.8 Subscribe (`/subscribe/`)

Lead line, the standing-order pitch, then the order CTA. Banner allowed here if a page ever needs one.

### 4.9 Thanks (`/thanks/`)

Single h1 ("Thanks, neighbor."), one paragraph, one CTA row home. No ornament. Quiet page.

### 4.10 Pricing (`/pricing/`)

Lead line, the table, the FAQ disclosure block. No ornament. Pricing wants restraint to read as credible.

---

## 5. The logo

File: `/assets/logo.webp` for display, `/assets/logo.png` as the raster fallback and the OpenGraph and JSON-LD image. Both are referenced by `_layouts/default.html` and **must not be deleted**.

Usage: once per page, in the header, at `min(55%, 220px)`. It is not a decorative element, does not repeat down the page, and is not composited onto photographs. There is no secondary or tertiary mark; see BRAND.md 10.5.

The favicon is `/assets/favicon.ico`.

**Retired assets.** `/assets/brand/` still contains the heritage-era files (`volkman-mark*`, `monogram*`, `wordmark.svg`). Nothing references them. They are history, not a resource. Do not wire them into a layout, a label, or a social profile.

---

## 6. Imagery system

### 6.1 Photography

One layer, real photographs. Full direction lives in BRAND.md section 7. The shot list still worth working through:

1. **Shed at dawn, door open.** Wide, grow lights still on, daylight just starting. The most differentiated asset the farm owns.
2. **Top-down on a single tray** on a wooden cutting board, window light from the left. No tweezers, no styling.
3. **A hand cutting a tray with kitchen scissors.** Three-quarters angle. Watch the burgundy stems against the cream backdrop.
4. **The porch handoff.** A bag of greens on a doormat or railing, late-afternoon light, no face in frame.
5. **A child's hand pressing seeds into a tray.** Above the wrist, no face.
6. **Trays under grow lights at night.** Cool-green wash. The signature shot.
7. **A meal in use.** The actual kitchen, the actual plate, a scatter of microgreens on top.
8. **The shed exterior at sunset**, palms in frame.

Not shot: matching-flannel family poses, chef-coat-and-tweezers garnish shots, drone overheads, time-lapses, stock photography of any kind.

### 6.2 Ornament

- **Eyebrow (`.eyebrow`):** section labels. The most-used ornament.
- **Banner (`.banner`):** one per page max, and most pages need none.
- **Laurel divider (`<hr class="laurel">`):** between major blocks on home, about, variety. Not on city, pricing, restaurants, blog, or thanks.
- **Roundels (`.roundels`):** ordered "How it works" sequences.
- **Card roundel:** the 8px olive corner dot on `.card`, suppressed on `.card--variety` and on wholesale.
- **Square bullets:** default on `main > ul` and on `.list-square`.

### 6.3 Texture

The cream paper-grain noise overlay on `body` is the only texture in the system. Wood grain appears in product photography when a wooden board is the surface; it never appears in UI.

---

## 7. Voice integration

Sample copy in the house voice. Full rules in BRAND.md section 4.

### Form field placeholders

- Phone: `867-5309`
- Email: `crazy@about.microgreens`
- Restaurant name (chefs): `Where we should drive to`
- Kitchen notes (chefs): `What you cook, how much you need, what days work`

### Button labels

- `Send my order` (microgreens primary)
- `Send my inquiry` (chefs primary)
- `Stand a weekly order` (subscribe primary)

### Form errors

- `We need a phone we can text. Format: 555-867-5309.`
- `That email looks off. One more try.`
- `Pick a neighborhood first so we know which day works.`

### Thank-you headline

`Thanks, neighbor. We will text you within a day.`

Guardrails: no em-dashes, ever. No post-harvest handling claims anywhere. No invented anecdotes in blog copy.

---

## 8. Accessibility notes

**The contrast table needs recomputation before it is quoted again.** This document and BRAND.md have historically published different ratios for the same hex pairs (ink on cream as both 12.8:1 and 14:1, alpine as both 5.4:1 and 5.2:1, and so on). At least one set was computed against a different background, probably the v1 cream `#fef6e9`. Until someone recomputes every pair against `--cream` `#f5ead3` with a tool and syncs both documents, treat the old numbers as unverified. See section 9.

The qualitative rules below are not in doubt and stand on their own:

- **Ink is the default for all body text and headings.** It is the highest-contrast pairing in the system by a wide margin.
- **Olive is decorative only.** Separators, the card roundel, the laurel center dot. Never body type, never small text, never a link color.
- **Alpine is for links, buttons, markers, and the focus ring**, not for running body copy.
- **Alpine-deep is the safer alpine** where text needs more weight: CTA-row links, pager links, active nav.
- **Bark stays on cream, never on surface.** The two are too close in luminance.
- **Cream on alpine** is the primary button pairing and is the only inverse combination in production use.

Other decisions:

- Focus ring is the 3px alpine outline plus 2px offset, applied uniformly to links, buttons, inputs, cards, and summaries.
- Tap targets stay at 44px minimum via input padding plus line-height; the primary button is 220px wide minimum.
- `prefers-reduced-motion: reduce` suppresses all transitions.
- The paper-grain noise sits at roughly 4% opacity with high-frequency turbulence and does not interfere with text legibility at body size. Do not raise it past 6%.
- Form labels use `for` attributes. `.form-error` is styled but not yet wired to `aria-describedby`.
- The logo carries descriptive alt text rather than being marked decorative, because it is the only place the business name appears in the header.

---

## 9. Outstanding work

Real remaining tasks, highest value first. The old numbered rollout is done or void and has been removed.

1. **Ship the five missing font files.** Source Serif 4 (regular, italic, 600) and Inter (600, 700) as woff2 into `/assets/fonts/`, with the exact filenames the `@font-face` blocks expect. Nothing else is required; the CSS already points at them. This is the largest visible gap between the documented system and the live site.
2. **Recompute the contrast table.** Every palette color against `--cream` `#f5ead3`, plus the cream-on-alpine inverse. Update section 8 here and section 5 in BRAND.md from the same computation so the two documents cannot drift again.
3. **Wire `aria-describedby`** from each input to its `.form-error` so screen readers announce validation messages. The styling is already in place.
4. **Clean the stale comments in `main.css`.** The file header still reads "v2 Heritage Gator", the section 1 comment still lists `bely-display-regular.woff2` as an OFL face (Bely is neither OFL nor in use), the section 6 comment still refers to "the mark" and "German-loan-word callouts", the section 13 card comment says "heritage roundel", and the section 21 comment says "No gator." None of it affects rendering; all of it misleads the next reader.
5. **Decide on the retired brand assets.** `/assets/brand/` holds roughly 2MB of unreferenced heritage-era files. Either delete them or move them under `archive/`.
6. **Document the variety card icons.** `.card__icon` expects a 48px SVG per variety. Where those live and how a new one gets added is not written down anywhere.

---

**Working document. Last updated 2026-08-05, rewritten to match the system actually shipping after the 2026-07-07 revert.**
**Supersedes: archive/DESIGN-SYSTEM-v1-typewriter.md (do not restore).**
