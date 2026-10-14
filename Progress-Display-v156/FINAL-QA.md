# v156 focused HH PDF QA — PASS

40 checks passed: 24 initial source/integration checks and 16 focused checks after the final table typography fix.

- Actual native download: `hh-all.pdf`, 72 A4 landscape pages.
- Charts and detailed definitions remain together on physical page 2. All 19 positive in-bar counts fit. Native vector charts and selectable text retained.
- Duplicate PDF overview removed; contents retained. No recorded-progress ring objects or Harvey glyphs.
- All 62 source keys and recorded progress values retained in table and cards; 55 populated values and 7 empty values. Source workbook bytes unchanged.
- Actual PDF table figures use 12pt DINNextLTArabic-Regular. All fit their cells. Card numeric percentages remain unchanged.
- All 72 pages pass native text bounds and footer numbering; cover has no footer and content starts at page 1 of 71.
- Focused visual review passed for the table, card, and chart/definitions pages.

Fixture: `ILLUSTRATIVE-monthly-preview.xlsx`, cutoff 30 September 2026, SHA256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. This is an illustrative fixture, not a production-data audit.

Evidence: `evidence.json`, `native-geometry.json`, `table-font-proof.json`.
Preview images: `page-4.png` (table), `page-11.png` (card), `page-2.png` (charts and definitions), `page-3.png` (contents).

Actual final bundled app tested over ephemeral local HTTP in Chromium with all external requests blocked. No cold file:// or new PowerPoint-renderer claim. Desktop/phone/shared entity screen checks are separately owned by the progress-removal agent.

## Tested bundle hashes

- `assets/js/app-bundle.js`: `883cce5e8ce5134fe51c2edc501e351258b28592fcc9882e130e32fd1bf39113`
- `assets/css/app-bundle.css`: `20dec07e970fa320ff913459cf2dd6227910d6df340eb4cddfb4283d43978732`
- `assets/css/print-measure-bundle.css`: `c4bc39d81c82e8bc266d65139f3796b8b4504e8c6415f47ad29c7142ee255d18`
