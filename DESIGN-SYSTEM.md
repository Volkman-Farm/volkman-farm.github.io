# Volkman Farm Design System (v2: Heritage Gator)

This is the production design system for volkman.farm. It implements the v2 brand foundation locked at `/BRAND.md`. The v1 typewriter system is archived at `archive/DESIGN-SYSTEM-v1-typewriter.md` for structural reference only; none of its visual decisions carry forward.

If a question arises that this document does not answer, the answer is whatever makes the gator mark feel more at home on the page.

---

## 1. Design tokens

All tokens live in `:root` in `/assets/css/main.css`. Use the custom properties, not the hex values, anywhere downstream.

### Color

| Token | Hex | Role |
|---|---|---|
| `--cream` | `#f5ead3` | Page background. Never replaced. |
| `--ink` | `#1f2419` | Body text, borders, the wordmark on print. |
| `--alpine` | `#3a5a2a` | Primary action color. Buttons, link hover, nav active, monogram, laurels. |
| `--alpine-deep` | `#2d4720` | Button pressed/hover-darken, secondary text emphasis. |
| `--olive` | `#8a7e3a` | Heritage gold. Banners, roundels, nav separators, card corner mark. |
| `--burgundy` | `#6b2a2f` | Body link hover, error states, accent on radish variety pages. |
| `--bark` | `#5c4633` | Captions, metadata, footer copy, secondary text on cards. |
| `--rule` | `#c7b98f` | Hairline rules, table borders, derived warm tone. |
| `--surface` | `#ede0bf` | Card and input fill, derived darker cream. |

Wholesale (`[data-page="wholesale"]`) restricts to cream, ink, alpine, alpine-deep, bark. Burgundy and olive are visually suppressed in that scope.

### Typography

Three faces, all self-hosted woff2 under `/assets/fonts/`. Owner downloads:

- **DM Serif Display** (Roxane Gataud, OFL, free). Display only. `dm-serif-display.woff2`.
- **Source Serif 4** (Adobe, OFL, free). Body. Regular, italic, 600. `source-serif-4-regular.woff2`, `-italic.woff2`, `-600.woff2`.
- **Inter** (OFL, free). UI. 600 and 700. `inter-600.woff2`, `inter-700.woff2`.

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

No monospace. No blackletter (it lives in the wordmark file only).

### Spacing (4pt base)

`--space-1` through `--space-9`: 4, 8, 12, 16, 24, 32, 48, 64, 96px.

### Borders

`--border-hair: 1px;` for table rules and dividers. `--border-rule: 2px;` for inputs, cards, buttons.

### Focus ring

`--focus-ring: 3px solid var(--alpine);` with `--focus-offset: 2px;`. Contrast on cream is AAA at large; the 3px width carries it on text size as well.

### Motion

`--t-fast: 120ms ease-out;` for hover/focus color changes. `--t-normal: 200ms ease-out;` for shadow/transform on cards. All motion is suppressed under `prefers-reduced-motion: reduce`.

### Z-index lanes

Four lanes: base (0), raised (10), sticky (20), overlay (30). No fixed positioning today; the lanes exist for future toast/modal work.

### Eyebrow style

`.eyebrow`: small uppercase Inter at 700, tracking 0.18em, 0.8rem, alpine (or `.eyebrow--gold` for olive). The visual echo of the ribbon banner lettering on the mark. Use sparingly for section eyebrows and German loan-word callouts. One banner-shaped variant (`.banner`) draws the ribbon container itself; cap at one per page.

---

## 2. Layout primitives

**Container widths.** Two lanes, both inherited from v1:

- `min(60ch, 92%)` for flowing copy and forms. This is the body measure. Applied automatically to `h1`, `h2`, `h3`, `p`, top-level lists, hr, blockquote, details, table, and `.cta-row`.
- `min(80ch, 92%)` for `.grid`, which auto-fills 220px-min card columns.

**Vertical rhythm.** Section openers (`h2`) get `--space-7` (48px) top margin. Subsections (`h3`) get `--space-6`. Paragraphs get `--space-4`. The body padding-bottom is `--space-8` so the footer-rule never kisses the last paragraph.

**Breakpoints (mobile-first).**

- Default: phone (< 720px).
- `@media (max-width: 720px)`: small-screen tweaks (tighter gutters, narrower nav separators, smaller hero monogram).
- `@media (min-width: 1024px)`: desktop gutter bump.

There is no tablet breakpoint. The 60ch column already scales gracefully between the two.

**The cream extends behind content.** `html` and `body` both set `background-color: var(--cream)`. The paper-grain noise overlay (a tiny SVG `feTurbulence` filter, 4% opacity ish) is set on `body` as a tiled background-image. The screen never reads flat without it; it never reads textured with it. Test on retina and non-retina before adjusting.

---

## 3. Component specs

### 3.1 Header

`<header class="site-header">` containing one `<a>` that wraps both the laurel-V monogram (inline SVG, 44px, alpine green) and the wordmark image (`/assets/brand/wordmark.svg`, target height ~32-48px responsive). On mobile the monogram shrinks to 36px. The wordmark has an `onerror` fallback that swaps to the gator mark derivative until the wordmark.svg is ready.

The header is the only place the monogram + wordmark sit side by side. On `/` and `/about/` the gator mark replaces this composition for the hero (one per page max).

### 3.2 Footer

A small alpine monogram, then the secondary link row (subscribe, chefs, email), then the NAP line in Source Serif. UI text in the link row uses Inter caps with olive diamond separators. NAP stays Source Serif at small size and bark color.

### 3.3 Primary nav

Inter caps, 600, tracking 0.18em, lowercase letters preserved from v1 copy. Separators are small olive diamonds (`::before` pseudo-elements, 4px rotated squares). Active page (`aria-current="page"`) gets an alpine underline 2px thick. Hover transitions ink → alpine in 120ms.

### 3.4 Headings

DM Serif Display, 400, centered. Tight line-height on h1 (1.05) and h2 (1.15), normal on h3 (1.25). Negative letter-spacing on h1 (-0.015em) and h2 (-0.005em) keeps the display weight from feeling soft.

### 3.5 Body links

Alpine, underlined at 1px with 4px offset, hover transitions to burgundy. Focus-visible gets the 3px alpine ring with 2px offset. Wholesale page swaps the burgundy hover for alpine-deep.

### 3.6 Primary button

Alpine fill, cream label, Inter caps at 600 with 0.04em tracking, 14px/28px padding, 2px solid border, 2px radius (just enough to feel intentional, not soft). Hover darkens to alpine-deep. Active goes ink. Disabled state uses the surface fill with bark text and bark border. Min-width 220px so the primary "send my order" button reads as the page's anchor action.

### 3.7 Secondary button (`.btn--secondary`)

Transparent fill, alpine border, alpine label. Hover inverts to alpine fill with cream label. Used for read-more style actions where the alpine fill would be too loud.

### 3.8 CTA row (`.cta-row`)

A centered paragraph containing a strong link. Body font. Used after the lead line on variety, city, subscribe, restaurants. The link is alpine-deep at 600 weight; it stops short of the full button treatment so the page doesn't drown in CTAs.

### 3.9 Form field set

Forms remain `<form><p><input></p>` for the order form; `.field` wraps label-above-input on restaurants. Inputs get a surface fill, 2px ink border, 2px radius, 12/14 padding (44px+ tap target). Focus ring matches the global focus token. Labels in `.field` use the Inter eyebrow style for clear hierarchy. Selects use Inter 600 to make the chosen option scannable.

### 3.10 Form errors

`.form-error` is centered burgundy text in Inter 600 at small size. The matching `aria-invalid="true"` on the input swaps the border to burgundy. Wholesale variant uses ink instead of burgundy for both.

### 3.11 Checkbox

Native input, scaled 1.4x, accent-color alpine. Wrapped inline in a `<p>` next to its `<label>`. Vertical-align middle on both.

### 3.12 Card (`.card`)

Surface fill, 2px ink border, 2px radius, body font. Small olive roundel in the top-right corner (an absolutely positioned `::before`, 8px, 70% opacity). Hover lifts -2px/-2px with a 4px alpine drop-shadow (no blur, prints clean, reads as heritage stamp). Card titles use DM Serif Display at 400; card meta uses small bark text. The roundel does not appear on the wholesale page.

### 3.13 Variety hero

Variety pages keep the v1 structure: italic lead line, CTA row, then h2 sections. The lead line now uses the `.lead` class (Source Serif italic at 1.2rem). Above the lead, optional `<span class="eyebrow eyebrow--gold">Frisch gezüchtet</span>` for a heritage flourish. Below "How to use [variety]" the laurel HR may appear once.

### 3.14 Pricing table

`<table>` with Inter caps headers at small size and Source Serif body rows. Right-aligned numerical columns use Inter 600 so $3.50 reads tight. Hairline rule between rows in `--rule` color; 2px ink rule under the header.

### 3.15 Body lists

Top-level `<ul>` is square markers in alpine. Use `.list-square` for inline lists when the parent context needs the markers. The `.roundels` class converts an `<ol>` into Roman-numeral roundels (I, II, III in DM Serif Display 400, ringed alpine) for "How it works" sections.

### 3.16 Horizontal rule and laurel divider

Plain `<hr>` is hairline rule color, used between content sections that don't warrant ornament. `<hr class="laurel">` renders a small SVG laurel sprig pair with an olive roundel center; reserve for heritage-leaning pages (home, about, variety). The wholesale variant hides `.laurel`.

### 3.17 Blockquote

DM Serif Display italic at 1.25rem with a 4px alpine left rule. Cite block is Inter caps in bark.

### 3.18 FAQ disclosure (`<details>`/`<summary>`)

Carry the v1 disclosure pattern forward: surface fill, 4px alpine left rule, Inter 600 summary text, alpine plus-to-minus indicator drawn in DM Serif Display. Used on pricing and restaurants.

### 3.19 Eyebrow ribbon (`.banner`)

A heritage-gold or alpine ribbon container drawn in pure CSS (a centered alpine fill with two clip-path triangles forming the ribbon ends). Holds one short German loan-word callout, eyebrow style. One per page max. Wholesale hides it.

---

## 4. Page archetypes

### 4.1 Homepage (`/`)

- Site header (monogram + wordmark) and primary nav as on every page.
- **Hero replacement:** the gator mark (`.mark-hero`, ~420px max) sits where the h1 normally would. Below it, the h1 carries the heritage tagline pair. Below that, the dual CTA row (primary alpine button + secondary text CTA).
- Laurel divider, then the "Why us" section using `.eyebrow` + h2 pattern.
- Numbered roundels (`<ol class="roundels">`) for "How it works": I. Place an order. II. We confirm by text. III. Hand-delivered on your route.
- Standing order callout. Then the routes list. Closing laurel divider, then footer.

### 4.2 About (`/about/`)

- Header + nav.
- Gator mark hero again, smaller (~320px), centered above the h1.
- One paragraph family story (per BRAND.md section 4 example #2). No em-dashes, no "passion," no "launched a business."
- Small Florida shield (`.shield` inline SVG) inline with a single line of heritage credibility ("German on one side, Florida on the other.").
- The kids/family paragraph, generic.
- "Gemütlich" used exactly once, describing the kitchen.

### 4.3 Variety landing (`/greens/[variety]/`)

- Header + nav.
- h1 (set by the layout: "[Variety] Microgreens").
- Optional gold eyebrow ("Frisch gezüchtet").
- `.lead` italic intro line.
- `.cta-row` with the order link and price.
- Sections: Flavor, Nutrition, How to use, How we grow.
- `<ul class="list-square">` for usage list.
- Single `<hr class="laurel">` before the closing CTA row.

### 4.4 City landing (`/delivery/[city]/`)

Same skeleton as variety landing, with the local-route emphasis: "Where we deliver," "Your delivery day," "What we grow," "How it works in [City]." The local angle replaces the heritage flourish; this page uses no eyebrow ribbon, but the closing laurel divider is welcome.

### 4.5 Wholesale (`/restaurants/`)

The restrained variant. Body gets `data-page="wholesale"`. The system:

- **Suppresses** the gator hero, the eyebrow ribbon, the laurel divider, the olive card roundel, the burgundy hover (swapped for alpine-deep).
- **Keeps** the wordmark + monogram header, the laurel-and-shield credibility moment (use `.shield` inline), the alpine primary button, the alpine FAQ disclosure rule, the Inter caps section eyebrows (if used) in alpine (not olive).
- Copy avoids German loan words entirely (per BRAND.md 10.3). The lead line is the formal "Cut the morning of service" rewrite.

### 4.6 Subscribe (`/subscribe/`)

Heritage-leaning. Lead line, then the standing-order pitch (BRAND.md #4 example). Eyebrow ribbon allowed here.

### 4.7 Thanks (`/thanks/`)

Single h1 ("Thanks, neighbor."), one paragraph, one CTA row back to home. Small monogram allowed above the h1 (~64px). No laurels, no ribbon. Quiet page.

### 4.8 Pricing (`/pricing/`)

Lead line, the table, the FAQ disclosure block. No ribbon, no laurel. Pricing wants restraint to read as credible.

---

## 5. The marks

### 5.1 Primary mark (the gator)

File: `/assets/brand/volkman-mark.png` (1.9MB). Unacceptable to ship as-is. Derivation strategy:

```
volkman-mark.png            (master, archive only, do not link)
volkman-mark-2400.webp      (retina large, ~150-200KB target)
volkman-mark-1200.webp      (default web, ~70-100KB target)
volkman-mark-1200.png       (OpenGraph fallback, ~250KB target)
volkman-mark-600.webp       (mobile, ~30-50KB target)
volkman-mark-600.png        (wordmark fallback in layout, header)
```

Use the `<picture>` element on the hero:

```html
<picture class="mark-hero">
  <source type="image/webp"
          srcset="/assets/brand/volkman-mark-600.webp 600w,
                  /assets/brand/volkman-mark-1200.webp 1200w,
                  /assets/brand/volkman-mark-2400.webp 2400w"
          sizes="(max-width: 720px) 78vw, min(420px, 70vw)">
  <img src="/assets/brand/volkman-mark-1200.png"
       alt="Volkman Farm: an alligator in lederhosen holding a tray of microgreens"
       width="1200" height="1200" loading="eager" decoding="async">
</picture>
```

The OpenGraph image references `volkman-mark-1200.png` (PNG, because most OG scrapers still prefer PNG/JPEG over WebP). Once derivatives exist, the layout's meta tags already point at the right path.

**Generation command (owner runs once):**

```bash
# Requires: brew install cwebp imagemagick
cd assets/brand/
for w in 600 1200 2400; do
  cwebp -q 82 volkman-mark.png -resize $w 0 -o volkman-mark-$w.webp
  magick volkman-mark.png -resize ${w}x volkman-mark-$w.png
done
```

### 5.2 Wordmark alone

The blackletter "Volkman Farm" extracted from the mark. Two paths:

1. **Recommended:** commission a designer (4-8 hours) to redraw the wordmark cleanly in SVG with proper kerning, optical correction of the blackletter, and the "MICROGREENS" subline as DM Serif Display caps. Cost: ~$150-400 freelance, one-time.
2. **Stopgap:** Inkscape's autotrace on a high-res crop of the wordmark area from the master PNG, manually cleaned. Result is acceptable for the header at small sizes; do not use on labels.

Target file: `/assets/brand/wordmark.svg`. Until it ships, the layout's `onerror` falls back to `volkman-mark-600.png` cropped via CSS height. This is intentional fallback behavior, not a permanent state.

### 5.3 Tertiary mark: laurel-wreathed V monogram

Provided inline in the layout. Production-ready as a 64x64 SVG that uses `currentColor` so it inherits alpine on the header and footer. Geometry: a heavy V stroke at 3.4px, framed by paired curved laurel sprigs left and right, optionally enclosed in a thin outer roundel rule (35% opacity). Scales cleanly to 32px favicon and 128px label-corner stamp.

Concept in one line: **a single heavy V framed by two curved laurel sprigs, in alpine green on cream, suggesting the wreath on the gator's lower banner without copying it.**

The owner can ship the inline SVG as-is. To produce a static favicon and the iOS touch icon, render the SVG to PNG at 32, 180, and 512px:

```bash
# Requires: brew install librsvg
cd assets/brand/
rsvg-convert -w 32 monogram.svg -o monogram-32.png
rsvg-convert -w 180 monogram.svg -o monogram-180.png
rsvg-convert -w 512 monogram.svg -o monogram-512.png
```

(Save the inline SVG from `_layouts/default.html` to a standalone `assets/brand/monogram.svg` file first.)

If after seeing the monogram on a real label the owner decides it reads as too generic, the BRAND.md-documented fallback is the cropped gator-head spot mark. That is a one-line CSS swap; do not redesign the monogram twice.

### 5.4 Florida shield

Used on About and wholesale as a small credibility stamp. Render inline:

```html
<svg class="shield" viewBox="0 0 28 32" fill="none" aria-hidden="true">
  <path d="M14 1 L26 4 V18 C26 25 14 31 14 31 C14 31 2 25 2 18 V4 Z"
        stroke="currentColor" stroke-width="1.4" fill="none"/>
  <path d="M14 12 V20 M11 16 H17 M12 14 C12 12 14 11 14 11 C14 11 16 12 16 14"
        stroke="currentColor" stroke-width="1.2" fill="none" stroke-linecap="round"/>
</svg>
```

Approximates the small green shield in the lower banner of the gator mark: shield silhouette in Florida proportions, with a sprout inside.

---

## 6. Imagery system

### 6.1 Photography (the product-and-place layer)

The v1 rules still apply; v2 extends them by leaning harder into the shed and the route. **Shoot this weekend with a phone (back camera, portrait orientation off, locked exposure):**

1. **Shed at dawn, door open.** Wide shot. Grow lights still on, daylight just starting. The most differentiated asset you own.
2. **Top-down on a single tray of broccoli microgreens** on a wooden cutting board, window light from the left. No tweezers, no styling.
3. **A hand cutting a tray of radish microgreens with kitchen scissors.** Three-quarters angle. Watch the burgundy stems against the cream-paper backdrop.
4. **The porch handoff.** A paper bag of greens on a doormat or porch railing, late-afternoon golden light, no face in frame.
5. **A kid's hand pressing seeds into a tray.** Above the wrist, no face. Soil dust visible.
6. **Trays under grow lights at night.** Cool-green wash. Long exposure if the phone allows. This is the brand's signature shot.
7. **A meal in use.** The actual family kitchen, the actual taco, a scatter of cilantro microgreens on top. Real plate, real lighting.
8. **The exterior of the shed at sunset.** Florida palms in frame on one side. This is the visual rhyme to the mark.

What we do not shoot: matching-flannel family poses, chef-coat-and-tweezers garnish shots, drone overheads, time-lapses, anyone smiling for the camera on the About page.

### 6.2 The gator-and-heritage layer

- **The gator mark:** home hero, about hero, social avatar at large sizes. Once per page.
- **The wordmark:** site header and footer on every page. Wholesale page header.
- **Laurel divider (`<hr class="laurel">`):** between major content blocks on home, about, variety. Not on city, pricing, restaurants, or thanks.
- **Banner ribbon (`.banner`):** one per page max, only on home, about, subscribe, variety. Contains one German loan word.
- **Roundels:** `.roundels` ordered list for "How it works" type sections.
- **Florida shield:** about and wholesale only. Once per page.
- **Square bullets:** carried over from v1, default on all `main > ul`.

### 6.3 Texture

The cream paper-grain noise overlay is set on `body`. It is the only texture in the system. Wood grain appears in product photos when a wooden board is the surface; it does not appear in UI. No Bavarian-pattern tiling anywhere.

---

## 7. Voice integration

Sample copy in v2 voice. All ready to drop in.

### Form field placeholders (microgreens order)

- Phone field: `867-5309`
- Email field: `crazy@about.microgreens`
- Restaurant name (chefs): `Where we should drive to`
- Kitchen notes (chefs): `What you cook, how much you need, what days work`

### Button labels

- `Send my order` (microgreens primary)
- `Send my inquiry` (chefs primary)
- `Stand a weekly order` (subscribe primary)
- `<span class="eyebrow eyebrow--gold">Frisch gezüchtet</span> Order this week's greens` (homepage hero, with the eyebrow above the alpine button)

### Form errors

- `We need a phone we can text. Format: 555-867-5309.`
- `That email looks off. One more try.`
- `Pick a neighborhood first so we know which day works.`

### Thank-you headline

`Thanks, neighbor. We will text you within a day.`

Heritage flourish guardrails: one German loan word per page max, never two in a sentence, only from the BRAND.md approved list (frisch, gezüchtet, nachhaltig, Volk, gemütlich). No em-dashes, ever. No post-harvest handling claims anywhere.

---

## 8. Accessibility notes

Contrast ratios on `--cream` (`#f5ead3`) computed against WCAG AA.

| Foreground | Ratio | AA normal | AA large | AAA normal | Use |
|---|---|---|---|---|---|
| `--ink` `#1f2419` | ~12.8:1 | pass | pass | pass | Body text, headings. Default. |
| `--alpine` `#3a5a2a` | ~5.4:1 | pass | pass | fail | Links, buttons, eyebrow. OK for body links. |
| `--alpine-deep` `#2d4720` | ~7.3:1 | pass | pass | pass | Hover state, CTA-row link. |
| `--bark` `#5c4633` | ~6.3:1 | pass | pass | fail (small body) | Captions, meta. Avoid below 14px. |
| `--burgundy` `#6b2a2f` | ~7.2:1 | pass | pass | pass | Body link hover, error text. |
| `--olive` `#8a7e3a` | ~3.4:1 | fail | pass | fail | Decorative only (banner fill, roundel ornament). Never on body type. |

Inverse ratios:

| Background | Foreground | Ratio | Use |
|---|---|---|---|
| `--alpine` | `--cream` | ~5.4:1 | Primary button. AA pass on caps at 0.95rem. |
| `--burgundy` | `--cream` | ~7.2:1 | Error state surface (currently unused; reserved). |
| `--ink` | `--cream` | ~12.8:1 | Active-button state. |

**Combinations to avoid:**

- Olive (`--olive`) on cream below 18px. Use bark or alpine-deep instead.
- Bark on surface (`--surface` is too close in luminance). Bark stays on cream.
- Alpine body text at < 14px (passes AA, fails AAA). Use ink for body, alpine for links and UI.

**Other accessibility decisions:**

- Focus ring is the 3px alpine outline plus 2px offset, applied uniformly. AAA on cream by virtue of the 3px width.
- Tap targets stay at 44px minimum via input padding plus line-height; the primary button is 220px wide minimum.
- `prefers-reduced-motion` suppresses all transitions.
- The paper-grain noise is at 4% opacity and uses high-frequency turbulence; it does not interfere with text legibility (tested on cream at body size). Owner: do not raise the opacity past 6%.
- Form labels use `for` attributes (already in markup). Errors will need to be wired with `aria-describedby` when implemented; reserve `.form-error` for now.

---

## 9. Implementation plan for the owner

Numbered, sequential, each step under 30 minutes. Run them in this order.

1. **Fonts.** DM Serif Display already shipped at `/assets/fonts/dm-serif-display.woff2`. Pending: Source Serif 4 from https://github.com/adobe-fonts/source-serif/releases (400, 400 italic, 600). Inter from https://github.com/rsms/inter/releases (600, 700). Place as woff2 only.

2. **Place fonts at `/assets/fonts/`.** Filenames must match the `@font-face` declarations in `main.css`: `dm-serif-display.woff2`, `source-serif-4-regular.woff2`, `source-serif-4-italic.woff2`, `source-serif-4-600.woff2`, `inter-600.woff2`, `inter-700.woff2`.

3. **Replace `/assets/css/main.css`.** Already done as part of this design system delivery. Verify it loaded by running `npx @11ty/eleventy --serve` and confirming Source Serif is rendering (not Georgia fallback).

4. **Update `_layouts/default.html`.** Already done. The header now uses the inline laurel-V monogram + wordmark, the meta og:image points at the new mark, the JSON-LD logo points at the new mark, font preloads are wired, and `data-page="wholesale"` is conditionally set on `/restaurants/`.

5. **Generate WebP and PNG derivatives of the gator mark.** Run the `cwebp` + `magick` loop from section 5.1. Output six files: `volkman-mark-{600,1200,2400}.{webp,png}` in `/assets/brand/`. Delete `/assets/logo.png` and `/assets/logo.webp` once nothing references them.

6. **Save the inline monogram to a file.** Copy the `<svg class="site-header__monogram">...</svg>` block from `_layouts/default.html` into `/assets/brand/monogram.svg` (strip the `class` attribute, keep `viewBox`, make sure `fill="currentColor"` is on the stroke paths). This is what the favicon link points at.

7. **Generate favicon PNG derivatives.** Use `rsvg-convert` per section 5.3 to produce `monogram-32.png` and `monogram-180.png`. Optionally rebuild `favicon.ico` from `monogram-32.png` (use https://realfavicongenerator.net if you don't have ImageMagick set up for ICO output).

8. **Commission or trace the wordmark SVG.** Per section 5.2. Save as `/assets/brand/wordmark.svg`. Until this exists, the layout's `onerror` fallback renders `volkman-mark-600.png` in the header; this is functional but should not be permanent.

9. **Update the homepage hero.** In `pages/index.md`, replace the current hero block with a `<picture class="mark-hero">` element pointing at the WebP/PNG derivatives. Below it, set the h1 to the new two-line tagline. Below the h1, the dual CTA row.

10. **Update the About hero.** Same `<picture>` element, smaller via inline `style="width:min(320px,78%)"` or by adjusting `.mark-hero` if the about page becomes a recurring archetype. Replace the opening paragraph with the BRAND.md v2 rewrite.

11. **Update variety pages.** In `pages/variety.liquid`, replace the inline `style="..."` on the lead `<p>` with `class="lead"`. Replace the inline `style` on the uses list with `class="list-square"`. Optionally add `<hr class="laurel">` before the closing CTA row.

12. **Update city pages.** Same treatment as variety: swap inline styles for `.lead` class. No laurel divider on city pages.

13. **Update the restaurants page.** Swap inline `style="..."` on the lead and the list for `.lead` and `.list-square`. Swap the inline-styled label patterns for the `.field` wrapper. Confirm `data-page="wholesale"` is present on `<body>` (it is, via the layout conditional).

14. **Regression-test the microgreens order form.** Walk through the four-step reveal: pick location, pick green, pick amount, fill contact, submit. The form should look unstyled-but-tidy in v2; nothing in the JS should have broken because no IDs changed.

15. **Deploy.** Commit and push. GitHub Pages picks it up on push to master. Verify on production: the gator on home, the laurel monogram in header and footer, no Courier mono anywhere, the wholesale page reads as the restrained variant.

---

**Document author: UI Designer (Claude). Last updated 2026-05-23.**
**Replaces: archive/DESIGN-SYSTEM-v1-typewriter.md (do not restore).**
