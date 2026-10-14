# TEC shared workspace review — verification

11 October 2026. This is the Revision 3 component proposal, with the approved
Revision 2 design retained. It is a review pack, not a new app release.

## Evidence

- Before images were captured from the actual bundled v129 app using the frozen
  illustrative workbook. Desktop captures use 1440 CSS pixels and device scale
  1; mobile captures use 390 CSS pixels. Paired boards keep native pixel scale.
- After images use the exact supplied DIN Next Arabic Regular, DIN Next LT
  Arabic Regular, Dubai Regular and Dubai Bold files and official TEC logo.
- The prototype checks header type, 12px/16px field text, 72px fields, 44px
  controls, approved field hover, button states, chip colors and existing icons.
- Keyboard/interaction checks cover menu movement, outside/Escape dismissal,
  focus restoration, Tab leaving the app menu, live filter scope, bulk selection
  despite option search, filters-only reset, persistent specimen settings, mobile
  inert background, focus containment and dismiss-only «تم».
- Popup bounds were checked at 1440, 1024, 768 and 600px widths, including a
  500px-high desktop viewport. Mobile sheets and menus were checked at 390px.
- Native print opens the illustrative print specimen directly; settings are a
  separate optional dialog. Prototype preferences demonstrate interaction only;
  the fixed specimen is not a live, scoped report exporter.
- All three specimen PDF pages were rendered and visually inspected. The PDF
  retains 24pt first title, 16pt continuation context, 13.5pt table headings/body,
  10.5pt metadata/footer, 9pt minimum support and 20pt secondary figures. Content
  remains inside the usable 10mm outer margins with no body/footer overlap.
- The eight frozen illustrative row keys, membership and source order are
  unchanged in the print specimen. Approved status treatments are preserved.

Detailed evidence is in `after/interaction-checks.json`,
`after/alignment-checks.json`, `print/print-proposal-verification.json` and
`print/standalone-verification.json`.

## Supplied PDF findings

The five-page operational PDF was inspected privately, page by page. Its table
body and badges already use 13.5pt, with neutral names and readable wrapping.
Page 2 lacks report continuation context; pages 3–5 repeat the full title inside
the repeated table header. Some labels are 7.5–8.5pt and quarter values are 18pt,
below the approved print roles. Its legal footer is already 10.5pt; the proposal
adds document context and page numbering rather than reducing that text.

The supplied PDF and its private text/renders are excluded from this pack. Public
before/after print comparisons use the actual v129 illustrative export.

## Review limits

The three-page PDF demonstrates selected overview components and two continued
table pages. It is not the complete operational export and does not establish a
three-page target. Production calculations, workbook data, report pagination
logic and the installed skill were not changed. Full live data parity and
screen-reader/PDF accessibility certification are outside this component review.

The v129 release bundle remains unchanged:

| File | SHA-256 |
| --- | --- |
| CSS bundle | `4a15447ee4d6afd14c9876b65ef66a4c0c1e9122836e69f3d3cc2450d3117d0c` |
| JS bundle | `aa5b57091038cba975b8781a73f9f3c6af0342ffb44b11f2c3e0abc0dc20b079` |

For review, extract the ZIP with all bundled assets and open `index.html`.
The isolated prototype and native PDF are included alongside the specifications.
