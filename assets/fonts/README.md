# Font files (place woff2 here)

The v2 design system expects these self-hosted woff2 files in this directory. Until they exist, the CSS falls back to Georgia (for serif text) and system-ui (for UI text), which works but is not the final visual. The site keeps building and rendering.

## Required files

- `bely-display.woff2` — Bely Display (variable, weight 400-700)
- `source-serif-4-regular.woff2` — Source Serif 4, weight 400, normal
- `source-serif-4-italic.woff2` — Source Serif 4, weight 400, italic
- `source-serif-4-600.woff2` — Source Serif 4, weight 600
- `inter-600.woff2` — Inter, weight 600
- `inter-700.woff2` — Inter, weight 700

## Where to get them

**Bely Display** (Roxane Gataud, OFL): https://www.behance.net/gallery/61040881/Bely-Typeface or via Google Fonts mirror searches. Place the variable-weight woff2.

**Source Serif 4** (Adobe, OFL): https://github.com/adobe-fonts/source-serif/releases/latest. Inside the release, the `WEB/` directory has the woff2 files.

**Inter** (Rasmus Andersson, OFL): https://github.com/rsms/inter/releases/latest. Inside the release zip, the `Inter Web/` directory has individual weight woff2 files.

## Why woff2 only

The CSS `@font-face` declarations request only woff2. All modern browsers (Chrome, Safari, Firefox, Edge) have supported woff2 for years. Older formats are unnecessary weight on the site.

## When you place the files

Nothing else to do. The CSS already points at these paths. Refresh the browser and the typography should snap into place. If a face fails to load, the `font-display: swap` rule keeps the page legible via the fallback.
