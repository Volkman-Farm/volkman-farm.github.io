# Font files (place woff2 here)

The v2 design system expects these self-hosted woff2 files in this directory. Until each one exists, the CSS falls back to Georgia (for serif) and system-ui (for UI), which works but is not the final visual.

## Status

| File | Family | Status |
|---|---|---|
| `dm-serif-display.woff2` | DM Serif Display, 400 | shipped |
| `source-serif-4-regular.woff2` | Source Serif 4, 400 | pending |
| `source-serif-4-italic.woff2` | Source Serif 4, 400 italic | pending |
| `source-serif-4-600.woff2` | Source Serif 4, 600 | pending |
| `inter-600.woff2` | Inter, 600 | pending |
| `inter-700.woff2` | Inter, 700 | pending |

## Why DM Serif Display

The original Brand Guardian pick was Bely Display. Bely turned out to be a paid TypeTogether font, not OFL as documented. DM Serif Display is a free OFL alternative with similar high-contrast confidence, pulled from Google Fonts.

If you ever want to upgrade to Bely Display or to Recoleta, the swap is a one-line change in `assets/css/main.css` and a one-line change in `_layouts/default.html` font preload. The rest of the system holds.

## Where to get the rest

**Source Serif 4** (Adobe, OFL): https://github.com/adobe-fonts/source-serif/releases/latest. Inside the release, the `WEB/` directory has the woff2 files. Pick the static subset for regular, italic, and SemiBold (600).

**Inter** (Rasmus Andersson, OFL): https://github.com/rsms/inter/releases/latest. Inside the release zip, the `Inter Web/` directory has individual weight woff2 files. Use `Inter-SemiBold.woff2` (600) and `Inter-Bold.woff2` (700).

## Why woff2 only

The CSS `@font-face` declarations request only woff2. All modern browsers have supported woff2 for years.

## When you place the files

Nothing else to do. The CSS already points at these paths. Refresh the browser and the typography snaps into place. If a face fails to load, the `font-display: swap` rule keeps the page legible via the fallback.
