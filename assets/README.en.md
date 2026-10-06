# Assets

Public brand media, diagrams and presentation graphics for UNITERA documentation.
Prefer Mermaid in Markdown for architecture diagrams.

## Current brand media — 6 October 2026

The brand media come from the asset package supplied by the owner. Imported SVG
originals are unmodified copies. Derived variants are described separately
below. This binding is a visual update; it creates no semantic adoption,
permission or product maturity.

| Medium | Use |
|---|---|
| [UNITERA OS wordmark](identity/os/svg/unitera_os_wordmark_light.svg) | Product name on the entry pages. |
| [Crane Hero](identity/os/masters/svg/unitera-crane-hero-graphite.svg) | Large emblem on the repository landing page and in both language editions. |
| [Crane Glyph](identity/os/masters/svg/unitera-crane-glyph-graphite.svg) | Compact emblem for medium display sizes. |
| [Crane Micro](identity/os/masters/svg/unitera-crane-micro-graphite.svg) | Simplified emblem for favicons and the smallest displays. |
| UNITERA Systems wordmark and mark | Company identity; remains separate from the product wordmark and crane. |

The entry pages use SVG instead of the previous large PNG media. Color-scheme
selection uses Graphite on light backgrounds and Ivory on dark backgrounds.
All supplied Hero, Glyph and Micro variants are under `identity/os/masters/svg/`,
including the neutral `currentColor` sources. A separately embedded SVG does
not inherit the surrounding page's text color; the entry pages therefore use
the variants with explicit colors.

## Derived variants

- The dark OS wordmark is derived from the supplied light wordmark: only the
  UNITERA text color changes from Graphite to Ivory; geometry, typography and
  the OS accent stay the same.
- Favicons use the supplied Micro silhouette. PNG and ICO show Graphite on an
  Ivory surface. The additional SVG favicon adapts its color to the color
  scheme; the Safari mark is monochrome.
- The ICO file contains 16, 32 and 48 pixel sizes; PNG files are supplied in the
  same sizes.

## GitBook media

Both language editions contain identical copies under
`docs/<lang>/.gitbook/assets/brand/`: OS wordmarks, Hero/Glyph/Micro in Graphite
and Ivory, Systems media and `platform-icons/favicon/`.

The Systems files present in the package are imported. The light Systems mark
and light Systems lockup are absent from the package; their existing versions
remain bound. The media directory does not replace separately configured
GitBook interface settings.

## Icon set

`iconography/20/` contains 18 object icons. `iconography/modifiers/20/` contains
11 modifiers. Both groups are unmodified SVG originals from the package;
their embedded status labels are preserved.

Person, role, decision, grant, receipt and verification remain separate signs.
An approval modifier is not a grant; a receipt icon does not prove a verified
outcome. An icon creates no authority.

The [trademark notice](../legal/TRADEMARKS.md) continues to apply.
