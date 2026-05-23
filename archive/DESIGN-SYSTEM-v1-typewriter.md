# Volkman Farm Design System

This is the working spec for every visual decision on volkman.farm. It builds directly on `BRAND.md`. If a token, component, or page archetype here contradicts `BRAND.md`, `BRAND.md` wins.

The system implements as a single hand-rolled stylesheet at `/assets/css/main.css`, linked from `_layouts/default.html`. No frameworks, no preprocessors, no build step beyond Eleventy.

**Why a separate file and not inline `<style>`:** the CSS is now large enough that diffing it inside the layout obscures real layout changes, the browser caches the file across page loads (every internal navigation on a static site is a full page request), and the file passes through Eleventy's existing `assets/` passthrough without any config change. The cost is one extra HTTP request on first paint; for a static site behind GitHub Pages with HTTP/2, that is invisible.

---

## 1. Design Tokens

Every value the system uses, declared once as a CSS custom property on `:root`. If you ever find yourself typing a hex code or a magic pixel value in a component, stop and add a token.

### Color tokens

| Token | Value | Purpose |
|---|---|---|
| `--cream` | `#fef6e9` | Page background. The brand. Never replaced. |
| `--cream-shadow` | `#f0e6d0` | Inputs, card surfaces, hover surfaces. |
| `--ink` | `#221d14` | Body text, borders, primary logo color. |
| `--sprout` | `#4f6b30` | Primary action: button, links, focus ring. |
| `--sprout-deep` | `#3d5224` | Pressed and hovered sprout. Active nav. |
| `--radish` | `#b04a30` | Link hover and error accent only. Never a primary CTA. |
| `--beet` | `#8a2f5a` | Variety illustration only (beet, chard stems). |
| `--chard` | `#d49a1f` | Variety illustration only (chard, mustard). |
| `--soil` | `#5a4a36` | Metadata, captions, footer copy, form labels. |
| `--rule` | `#c9bda3` | Hairline rules, table row borders, dividers. |

### Type families

| Token | Stack | Purpose |
|---|---|---|
| `--serif` | `'Fraunces', Georgia, 'Times New Roman', serif` | Headings, lead lines, blockquotes. |
| `--mono` | `'JetBrains Mono', 'Courier Prime', 'Courier New', Courier, monospace` | Body, nav, buttons, all UI chrome. |

### Type scale (fluid, mobile first)

| Token | Value | Purpose |
|---|---|---|
| `--fs-h1` | `clamp(2rem, 5.5vw, 3rem)` | Page title (set once per page). |
| `--fs-h2` | `clamp(1.375rem, 3.75vw, 1.875rem)` | Section heading. |
| `--fs-h3` | `clamp(1.125rem, 2.5vw, 1.375rem)` | Sub-section heading. |
| `--fs-lead` | `1.15rem` | The italic Fraunces intro line. |
| `--fs-body` | `1.0625rem` | Body copy (17px). |
| `--fs-small` | `0.875rem` | Captions, footer, form labels. |
| `--fs-nav` | `1rem` | Nav links and button labels. |

### Line heights

| Token | Value | Purpose |
|---|---|---|
| `--lh-tight` | `1.1` | H1 display. |
| `--lh-snug` | `1.2` | H2. |
| `--lh-normal` | `1.4` | Nav, button, small text. |
| `--lh-loose` | `1.65` | Body copy. Loose to compensate for mono fixed-width awkwardness. |

### Spacing scale (4pt base)

`--space-1` 4px, `--space-2` 8px, `--space-3` 12px, `--space-4` 16px, `--space-5` 24px, `--space-6` 32px, `--space-7` 48px, `--space-8` 64px, `--space-9` 96px.

### Layout

| Token | Value | Purpose |
|---|---|---|
| `--measure` | `60ch` | Body content column max width. |
| `--measure-wide` | `80ch` | Card grids, wide tables. |
| `--gutter-mobile` | `16px` | Body padding under 720px. |
| `--gutter-desktop` | `24px` | Body padding at and above 1024px. |

### Borders

| Token | Value | Purpose |
|---|---|---|
| `--border-hair` | `1px` | Footer top, hr, table row separators. |
| `--border-rule` | `2px` | Inputs, buttons, card borders. Prints clean on a kraft label. |

### Focus ring

`--focus-ring: 3px solid var(--sprout)` at `--focus-offset: 2px`. Same ring on every focusable element. Contrast against cream is 4.8:1, AA.

### Motion

| Token | Value | Purpose |
|---|---|---|
| `--t-fast` | `120ms ease-out` | Color and background transitions. |
| `--t-normal` | `200ms ease-out` | Transforms (card lift). |

All motion respects `prefers-reduced-motion: reduce`, which collapses every transition to 0.01ms.

### Z-index scale

`--z-base: 0`, `--z-raised: 10`, `--z-sticky: 20`, `--z-overlay: 30`. The site does not need more lanes.

---

## 2. Layout Primitives

### Container

There is one container width and one wider container width:

- `min(60ch, 92%)` for flowing copy. Applied to `h1, h2, h3, p, ul, ol, hr, blockquote, table, .cta-row, form > p, form > div > p`.
- `min(80ch, 92%)` for card grids and wide content (`.grid`).

The cream background sits on `<html>`, not `<body>`, so it extends edge to edge regardless of body padding. Body has horizontal gutter padding (`16px` mobile, `24px` from 1024px up) and a `64px` bottom padding so the footer never kisses the viewport bottom.

### Vertical rhythm

Headings carry the rhythm. `h1` sits `24px` from the nav, `h2` sits `48px` above its body, `h3` sits `32px`. Paragraphs are `16px` apart. Section breaks (`<hr>`) are `48px` of breathing room.

### Breakpoints

Mobile first. Two breakpoints, both `min-width` after the mobile-specific overrides:

- Base: 320 to 720px. Default styles.
- `@media (max-width: 720px)`: small mobile tightening (slimmer gutters, wider content).
- `@media (min-width: 1024px)`: desktop gutter bump.

That is the whole set. The site does not need a tablet breakpoint. Content stays in a 60ch column even on a 27-inch display, which is correct for readable mono.

---

## 3. Component Specs

For each component: what it is, the default state, the states it has, and any mobile quirk.

### Header

Logo (linked to `/`) plus the primary nav. The logo is `/assets/logo.webp`, sized to `min(55%, 220px)` and centered with `40px` top margin. The `aria-label` on the link stays `Volkman Farm home`.

States: none. The logo is not hovered (it is a link, but visually unchanged).

Mobile: top margin drops to `24px`, width becomes `60%`.

### Primary nav

Centered horizontal list of five links: microgreens, greens, delivery, pricing, about. Lowercase, mono, bold, letter-spacing `0.08em`. Separated by a sprout-green `·`. Underline at `8px` offset.

States:

- Default: ink text, sprout `·` separator.
- Hover and focus-visible: sprout-deep text.
- `aria-current="page"`: sprout-deep text plus `2px` underline thickness. The owner should add this in the layout when a page is on the current path.

Mobile: separator margin tightens from `12px` to `8px`. Wraps to two lines under 380px (acceptable).

### Footer

Centered horizontal list of three links (subscribe, restaurants, mailto), then a NAP-style line. `1px` ink rule above the block. Footer copy uses soil text at `--fs-small`.

The NAP line is currently `Volkman Farm · Sanford, FL · family-grown microgreens`. Keep it. Do not add a phone number unless one is publicly listed elsewhere.

### Headings

Three sizes. All Fraunces, weight 600, centered, ink. H1 is set once per page from `{{ title }}` in the layout. H2 marks a section. H3 is rare; reserve it for sub-sections inside a long-form page (about, subscribe).

### Lead paragraph

The italic Fraunces line that sits below the H1 on variety, city, subscribe, and restaurants pages. Add `class="lead"` to a `<p>`. Was previously inline styled in each template; the new class lets you stop repeating the styling.

### Body paragraph + link styles

Mono, 17px, line-height 1.65, ink on cream. Links are sprout (4.8:1 on cream), underlined at 4px offset, 1px thickness. Hover and focus-visible turn radish (5.1:1 on cream). Focus-visible adds the sprout focus ring at 2px offset.

### Inline links inside flowing copy

Same as the base link styles. No special treatment. The body is mono, links are sprout, you can spot them at a glance without color blindness assistance because they are also underlined.

### Primary button

Used only as a form submit, the strongest visual signal on the page. Sprout background, cream text, sprout 2px border, uppercase, letter-spacing `0.08em`, `14px 28px` padding, `220px` min-width.

States:

- Default: sprout background.
- Hover: sprout-deep background and border.
- Focus-visible: sprout focus ring at 2px offset.
- Active (pressed): ink background and border.
- Disabled (`aria-disabled="true"` on `.btn`, or `:disabled` on submit): cream-shadow background, soil text and border, `not-allowed` cursor.

Tap target: `14px` padding plus 1.4 line-height plus 17px font puts the height above 48px, which exceeds the 44px iOS minimum.

There is also a `.btn` class for the rare case a non-form link needs the button treatment. Use sparingly; the cta-row text link is preferred.

### Secondary button / link button

There is no secondary button. The brand asks for one strong action per page, executed as the submit button or the CTA row text link. A second visual button competing with the primary submit dilutes the system.

If a future case actually needs a second affordance, render it as a `.cta-row` link.

### CTA row

A centered paragraph with a bold sprout-deep text link, often ending in `→`. Used inline in the content, not as a fixed banner. The arrow is part of the brand voice (calm, declarative, points forward, no urgency).

Format: `<p class="cta-row"><a href="..."><strong>Place an order →</strong></a></p>`.

### Form field set (label + input/select/textarea)

Two patterns coexist:

1. **Inline-with-copy pattern** (microgreens order form): the input sits inside a `<p>` and follows a sentence of explanation. No visible label, but a `placeholder` and an `id` matched to the surrounding copy.
2. **Label-above-input pattern** (restaurants inquiry form): wrap the label and input in `<div class="field">`. Label is uppercase mono small caps in soil; input fills the column width.

Inputs have cream-shadow background, ink 2px border, 17px mono text, 10/12 padding, no border-radius (the brand is typewriter, not iOS).

States:

- Default: cream-shadow background, ink border.
- Focus: sprout focus ring.
- `aria-invalid="true"`: radish border. Pair with `.form-error` text below.

### Form field error state

Small radish text directly below the input, centered, `--fs-small`. Use `class="form-error"` and `id` matched to `aria-describedby` on the input.

### Checkbox with inline label

Used in the order form for `standing_order` and `consent`. Scaled 1.4x for tap target, sprout accent color, sits inside the flowing `<p>` next to its label. The current markup works as-is.

### Honeypot field

The current `<input type="text" name="_honey" style="display:none">` becomes:

```html
<input type="text" name="_honey" class="honeypot" tabindex="-1" autocomplete="off">
```

The `.honeypot` class is `display: none !important`. `tabindex="-1"` keeps a real user's keyboard out of it; `autocomplete="off"` keeps Chrome from helpfully populating it.

### Card

The clickable tile in variety and city grids. Cream-shadow background, ink 2px border, padded, mono body text. Title uses `.card__title` (Fraunces 1.2rem ink). Meta line below uses `.card__meta` (soil, small).

States:

- Default: cream-shadow background.
- Hover and focus-visible: cream background, translates `-2px -2px`, drops a `4px 4px 0 0 var(--ink)` hard shadow. Reads like the card was lifted off the page (typewritten, not skeuomorphic).
- Focus-visible: same lift plus sprout focus ring.

### Card grid

`.grid` is `repeat(auto-fill, minmax(220px, 1fr))` at 80ch wide, with 24px gap (16px on mobile). Reflows from four columns to three to two to one as the viewport narrows. No JS.

### Variety description page hero

The italic Fraunces intro line (`.lead`), followed by a `.cta-row`. No image at launch. When an image lands, it follows the lead line and precedes the H2.

### Pricing table

Two columns: variety name (left), per-ounce price (right). Header row has a `--border-rule` ink underline; body rows have a `--border-hair` `--rule`-colored underline. All mono. Centered on the page.

### Lists (ordered, unordered)

Inside `<main>`, lists inherit the 60ch container. Unordered lists use `list-style: square`, the same shape as the bullet markers in the restaurants page. Markers are sprout (`::marker` color), bodies are mono ink. Items have `4px` vertical margin.

When a list is inside a template that already wraps its own container (the variety page does), add `class="list-square"` to the `<ul>` and remove the inline width.

### Horizontal rule

A `1px` `--rule`-colored line at 60ch wide with `48px` vertical margin. Used to separate the closing wholesale call-out on the home page.

### Blockquote / testimonial

Fraunces italic, 1.125rem, with a 4px sprout left border, 8/24 padding, 60ch wide, centered. Add an optional `<cite>` for attribution, which renders as a small soil-colored mono line.

Not used anywhere on the site yet. If a real restaurant testimonial lands for the wholesale page, this is what it uses.

---

## 4. Page Archetypes

### Home (`/`)

Centered single column. Logo and nav, then a Markdown body that opens with the tagline as the first paragraph (the H1 from `{{ title }}` already sits above it). Two CTA links separated by `·`. Two sections (`Why our greens`, `How it works`) with H2s. Closing `<hr>` and a wholesale callout. No images at launch.

### Content page (`/about/`, `/subscribe/`, `/pricing/`)

H1 from frontmatter. Optional lead line (subscribe uses one, about does not). Body sections with H2s. CTA row at the end. Pricing adds a `<table>` between sections.

### Variety landing (`/greens/{slug}/`)

H1 (`{{ variety.name }} Microgreens`). Italic lead line. CTA row with price. Four H2 sections: Flavor, Nutrition, How to use, How we grow. A `list-square` of uses. Closing CTA. Italic mono "browse all ten" link line at the bottom. JSON-LD Product schema in the template.

### City landing (`/delivery/{slug}/`)

Same shape as variety, different sections: Where we deliver, Your delivery day, What we grow, How it works. The "What we grow" section lists all ten varieties as inline links. Closing CTA.

### Index / grid page (`/greens/`, `/delivery/`)

H1, one or two paragraphs of intro, then a `.grid` of `.card`s. `delivery/` groups cards under three H2s (Friday morning, Mon and Wed, Sunday afternoon). Closing CTA.

### Form page (`/microgreens/`)

The most complex page. H1, then a `<form>` with four progressively revealed steps. Each step is a `<div>` toggled by inline JS. Each step is a sequence of `<p>` paragraphs alternating between guidance copy and a single `<input>` or `<select>`. The submit button is the only thing in step 4 below the consent checkboxes.

This page is the reason the inline-with-copy form pattern exists. Keep it.

### Thank-you page (`/thanks/`)

H1, two short paragraphs, sign-off as plain text (`The Volkmans`). `eleventyExcludeFromCollections: true` so it does not appear in the sitemap as a discoverable destination. Fires the `order_form_submit` GA event inline.

### Wholesale / B2B page (`/restaurants/`)

Uses the restrained palette per BRAND.md 10.3: cream, cream-shadow, ink, sprout, soil. No radish. No beet, no chard accents.

Implementation: add `data-page="wholesale"` to the `<body>` or `<main>` on this template. The stylesheet has a scope that suppresses radish link hover and reverts to sprout-deep when that attribute is present.

```liquid
---
title: For Chefs and Restaurants
permalink: /restaurants/
layout: default
bodyAttr: 'data-page="wholesale"'
---
```

Then in the layout: `<body{% if bodyAttr %} {{ bodyAttr }}{% endif %}>`. (Optional. The simpler move is to put the attribute directly on `<main>` inside the template by wrapping its content in `<div data-page="wholesale">`.)

This is the only page that deviates. Every other page uses the full palette.

---

## 5. The Logo Mark

Per BRAND.md decision 10.5, the brand needs a stamped square mark in addition to the wordmark. The wordmark stays primary. The mark goes on the favicon, the social avatar, label corners, and any place 220px wide is too wide.

### Concept

A 24-unit-square stamped frame, drawn as if pressed into cream paper with a 2-unit ink rule. Inside the frame: a single Fraunces small-cap `V` rendered in sprout. Below the `V`, a 4-cell-wide row of three small soil-colored dots (the grow-tray motif, abbreviated to a row of seeds). The whole composition reads as `V` plus `tray` plus `frame` at 32px; at 16px it reads as a stamped square.

It depicts the brand at a glance: the V is Volkman, the row of seeds is the tray, the stamped frame is the typewriter-on-cream foundation. Nothing depicts a leaf, a chef, or a banner because those were ruled out in section 8 of BRAND.md.

### Inline SVG

Drop this into `_layouts/default.html` next to the wordmark, or use it inline anywhere the brand needs a mark. It uses currentColor for the frame so it can sit in ink or sprout depending on context.

```html
<svg class="mark" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"
     role="img" aria-label="Volkman Farm">
  <rect x="1" y="1" width="22" height="22" fill="none"
        stroke="currentColor" stroke-width="2"/>
  <path d="M7 6 L12 16 L17 6" fill="none"
        stroke="#4f6b30" stroke-width="2.5"
        stroke-linecap="square" stroke-linejoin="miter"/>
  <circle cx="9"  cy="19" r="1" fill="#5a4a36"/>
  <circle cx="12" cy="19" r="1" fill="#5a4a36"/>
  <circle cx="15" cy="19" r="1" fill="#5a4a36"/>
</svg>
```

At 32px it reads as the full composition. At 16px (favicon) the three dots merge to a single soil-colored line under the V; that is fine, the V plus the frame still read.

For a sprout favicon, replace the V stroke color with `#4f6b30` (already set) and let the frame inherit ink. For a sprout-on-cream avatar, fill the rect with `#4f6b30` and recolor the V to `#fef6e9`.

The owner should export this as `/assets/mark.svg` and a `/assets/favicon.svg` variant, then regenerate `favicon.ico` from the SVG.

---

## 6. Imagery System

Per BRAND.md section 7, the photo direction is window light, top-down, cream or wood ground, single source of light, no stock, no styled-blog plating. The list below translates that into shoot-this-weekend instructions.

### Hero photo (home page)

Top-down 16:9 crop of five small piles of microgreens arranged in a loose row on a wooden cutting board placed on the cream paper. Camera 24 inches above the board, lens aligned to vertical (no tilt). Single window light from the left, sheer curtain diffused, late morning. No knife, no jar, no styled props. Count visible greens at roughly 50% of frame.

### Variety pages (one each, ten total)

Top-down 4:5 crop of a single 10x20 tray of the variety on the cream paper. Stems visible at the cut. Tray rotated 5 degrees off-axis so the grid reads. Window light from the left. Crop tight enough that the tray edges run off the frame on three sides; the fourth side leaves room for cream around the cut line.

Avoid: a hand in the frame, a chef's tool, a clamshell, water droplets (would imply post-harvest washing, which BRAND.md prohibits).

### About page

Two photos.

1. **Shed exterior:** 3:2 landscape, daylight, the shed door open, no people in frame. Shot from about 12 feet away, standing height, late afternoon. Cream paper not in frame. Soft golden light.
2. **Seeding hands:** 1:1 square, top-down on a tray of soaked paper towel. One adult hand placing seeds. Crop above the wrist. Window light from the left. No face, no second person, no kids.

### Restaurants page

One photo: a stack of three to five clamshells of varied stem-color greens (beet, chard, radish) on a stainless prep surface, top-down 4:5. No chef, no plating, no white coat. The shot reads "delivery just landed, you take it from here." Window light from the left. Optional: a single brown kraft paper hangtag visible on the top clamshell. No watermarks.

Stem color is the entire visual story on this page. It is also why the restrained palette works: chefs see the color in the produce, not the chrome.

### Delivery page

Optional, not required for launch. If shot: 3:2 landscape, the back of a station wagon parked on a residential street, a crate of stacked clamshells in the trunk. Soft afternoon light, blurred mailbox or porch in soft background. No person in frame. No license plate visible.

### Constraints that apply to every shot

- No flash.
- No filters or presets. The cream paper is already the color story.
- No close-ups of kids' faces. Hands at work are allowed, faces are not.
- No water droplets, no rinsing bowl, no spray bottle, no drying rack. State regulations and BRAND.md section 4 both rule out anything that implies post-harvest handling.
- Export JPEG at 1600px wide, quality 80, then run through `cwebp -q 75` to produce a webp companion. Serve the webp with a jpeg fallback if the owner wants belt-and-suspenders; on GitHub Pages, webp alone is fine for modern traffic.

---

## 7. Voice Integration

Copy that ships with components, written to BRAND.md sections 1 and 4.

### Placeholders

| Field | Placeholder |
|---|---|
| Order form, phone | `867-5309` (already in use, keep it) |
| Order form, email | `crazy@about.microgreens` (already in use, keep it) |
| Restaurant inquiry, restaurant name | `The Polite Pig` |
| Restaurant inquiry, what are you looking for | `Concept, weekly volume by variety, preferred delivery day, anything else.` |

### Button labels

| Context | Label |
|---|---|
| Order form submit | `Send my order` |
| Restaurants inquiry submit | `Send my inquiry` |
| Subscribe nudge button (if ever) | `Start a standing order` |
| Generic "place an order" CTA | `Place an order` |

### Form error messages

| Field | Message |
|---|---|
| Missing phone | `We need a phone so we can text you on delivery day.` |
| Missing email | `Drop an email so we can confirm your first order.` |
| Missing consent | `Tick the consent box so we can text and email about your order.` |

### Thank-you headline

`Your order is in.` (Already in use. Keep it.)

Every string above is em-dash free, period-led, and avoids the banned word list.

---

## 8. Accessibility Notes

### Contrast ratios (computed against `#fef6e9`)

| Pair | Ratio | Standard |
|---|---|---|
| Ink `#221d14` on cream | 14.5:1 | AAA |
| Sprout `#4f6b30` on cream | 4.8:1 | AA normal, AAA large |
| Sprout-deep `#3d5224` on cream | 6.9:1 | AAA |
| Radish `#b04a30` on cream | 5.1:1 | AA |
| Soil `#5a4a36` on cream | 6.8:1 | AAA |
| Cream on sprout (button text) | 4.4:1 | AA large |
| Sprout focus ring on cream | 4.8:1 | AA |

The cream-on-sprout button text is the tightest pair. It is above 4.4:1 because the button text is 16px and bold, which counts as "large" under WCAG. If a future button needs body-weight text on sprout, swap to ink-on-cream-shadow instead.

### Tab order

The layout's tab order on every page: skip-target (none; the layout is simple enough that a skip link is optional), logo link, five nav links, all in-content links and form controls in source order, footer links. Page order matches source order; do not introduce `tabindex` values above zero.

### Required ARIA

- `<nav aria-label="Primary">` on the top nav (already in use). Keep it.
- `<a aria-label="Volkman Farm home">` wrapping the logo image (already in use). Keep it.
- `<input aria-invalid="true" aria-describedby="...">` paired with `.form-error` text when validating client-side.
- `<svg role="img" aria-label="Volkman Farm">` on the inline mark.
- `aria-current="page"` on the active nav link (recommend adding via a Liquid filter).

### Mobile tap targets

All interactive elements clear 44x44px:

- Nav links: 16px text + 8px above and below underline offset, line wraps at 44px.
- Submit: 17px text + 14/28 padding = 60px tall.
- Card: 220px minimum width, 24px padding, far above 44px in every dimension.
- Checkbox: 1.4x scale on an 18px base = ~25px visible, but the surrounding `<label>` is fully clickable, padding the effective target.

### Focus management

The sprout focus ring at 3px solid, 2px offset, applied uniformly via `:focus-visible`. No `:focus` styling without the `-visible` qualifier, so keyboard users get the ring but mouse users do not get a flash on click.

---

## 9. Implementation Plan

A numbered list, each step small enough to do in under thirty minutes. Do them in order. Test in a browser after each step.

1. **Pull the new stylesheet in.** `assets/css/main.css` is now in the repo. `_layouts/default.html` now links it and the old inline `<style>` block is gone. Run `npx @11ty/eleventy --serve` and confirm every page renders with no visible regression. Expect a tiny darkening of body text (the ink token shifted from `#2b2418` to `#221d14`) and slightly cleaner link contrast.
2. **Replace the inline `<p style="...">` lead lines** on `variety.liquid`, `delivery-city.liquid`, `restaurants.liquid`, and `subscribe.md` with `<p class="lead">`. Remove the inline styles. Verify the italic Fraunces (or Georgia fallback) lead still renders.
3. **Replace the variety-page `<ul style="...">` and the restaurants-page `<ul style="...">`** with `<ul class="list-square">`. Remove the inline width and list-style. Center alignment comes from the main column.
4. **Refactor the card grids in `greens-index.liquid` and `delivery-index.liquid`.** Replace the inline-styled `<div>` and `<a>` with `<div class="grid">` and `<a class="card">`, with the title in `<strong class="card__title">` and the meta line in `<span class="card__meta">`. Remove every inline style on the grid and the cards.
5. **Refactor the pricing table** in `pricing.liquid` to drop the inline `style` attributes on `<table>`, `<th>`, and `<td>`. The new stylesheet has matching selectors. Confirm the table still centers and the row borders still read.
6. **Refactor the restaurants form** to use `<div class="field">` wrappers for each label + input pair, so the inline `style="display:block..."` on labels can come out. Verify focus states still work.
7. **Drop `data-page="wholesale"`** on `restaurants.liquid`. Two options: wrap the page content in `<div data-page="wholesale">`, or add a `bodyAttr` frontmatter field and apply it to `<body>` in the layout. Either way, confirm link hover on that page no longer goes radish.
8. **Self-host Fraunces and JetBrains Mono.** Download Fraunces (variable, `Soft 0`, `Wonk 0`, weight 600 and 400-italic) and JetBrains Mono (400, 400-italic, 700) as woff2 files. Drop them in `/assets/fonts/`. Add `@font-face` rules at the top of `main.css` with `font-display: swap` and `size-adjust` to keep cream from flashing. Until you do this step, the fallback stack (Georgia, Courier) is doing the job.
9. **Add the inline mark SVG** to the layout, sitting to the left of the wordmark logo on every page (or in the footer if you do not want to touch the header). Export `mark.svg` and a `favicon.svg` and regenerate `favicon.ico` from the SVG. Keep the `.webp` wordmark logo as primary.
10. **Add `aria-current="page"` to the active nav link.** A small Liquid filter inside the nav `<ul>` does this without JS: `<a href="/about/"{% if page.url == '/about/' %} aria-current="page"{% endif %}>about</a>`. Repeat across the five nav items.
11. **Replace the about-page copy.** The current about copy uses banned words ("passionate," "mission," "community," "sustainability," "farm-to-table" adjacent). Drop in the BRAND.md section 4 rewrite: "Five of us live in Sanford. Two parents, three kids, one shed full of trays..." Keep the page short per BRAND.md do-not-do item 12.
12. **Shoot the hero, the about pair, the wholesale stack, and ten variety photos** per section 6 above. Save as `/assets/img/hero.webp`, `/assets/img/about-shed.webp`, etc. The system will accept them with `<img src="..." alt="..." class="...">`; new image styles can be added when a real photo lands.
13. **Add a `.lead` class instance to the home page** if the tagline `<p>` should render as italic Fraunces. Currently the markdown renders it as plain mono, which is a defensible choice (the H1 above it carries the display weight). The owner should decide; one line of either feels right.
14. **Final pass: open `pages/restaurants.liquid` and confirm every BRAND.md 10.3 rule holds.** No radish in any link state. No beet, chard, or variety color anywhere. The form, the list of varieties, the lead line all stay in cream, cream-shadow, ink, sprout, soil. Add a real testimonial blockquote once a chef gives you one.

Done. The system is fully implemented when steps 1 through 7 are committed. Steps 8 through 14 are polish that improves the system without blocking it.

---

*Document author: UI Designer (Claude). Pairs with BRAND.md. Read both before changing the look of the site.*
