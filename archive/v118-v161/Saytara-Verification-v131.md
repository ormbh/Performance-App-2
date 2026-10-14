# Performance App v131 verification

**Verdict: PASS for the approved design and tested workflows.**

11 October 2026. Baseline v130. Implements the latest requested search spacing, contextual navigation and smaller printed table content. The bar guide proposes shorter availability wording separately; financial notes, calculations and chart colors remain in the app.

| Requested change | Result |
| --- | --- |
| Search-home title 38→36px and centered between logo/field | PASS: exact native geometry at 1920 and 390px |
| Logo, search field and search-action positions | PASS: bounds identical to v130 within 0.05px |
| Search home menu only; other pages Search+current | PASS: seven loaded desktop/mobile routes; current underline and menu destinations retained |
| Search-menu/shared-menu Escape and trigger focus | PASS |
| Printed table body/name/note/status text 13.5→12pt | PASS: actual bundled/native monthly and search PDFs |
| Column headings 13.5pt Bold; title 24pt; footer 10.5pt | PASS: unchanged |
| Table row/head/badge padding | PASS: identical before/after |
| Monthly/search membership | PASS: same 8/4 illustrative source keys |
| Native A4 page count and every page counter | PASS: monthly 4 pages, search 2 pages, exact generated X/Y |
| Source models, original fonts/images/libraries and icons | PASS: byte-identical to v130 |

Actual Chromium 151 browser captures, device scale 1/100% zoom. No substitute UI styles or application scripts injected for the native before/after checks. Monthly and search PDFs were rendered at scale 1; comparison table images use the same PDF clipping rectangle and 1.5 rendering matrix on both sides. Native PDF text spans confirm 12pt body text in the new table. Screen table/body/status text remains 16px and column headings 18px.

The frozen illustrative workbook SHA-256 is `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`, source cutoff 30/09/2026. Its 672 records, and source calculation modules, are retained. It is excluded from the release. Numerical verification does not cover an unseen operational workbook.

Readable modules are bundled. `python tools/build-bundles.py --check` covers 58 CSS and 48 JavaScript sources; `node --check assets/js/app-bundle.js` passes. The released bundles match those used for before/after evidence. `SHA256SUMS` and `release-manifest.json` identify all release files.

The current bar contract was traced to source functions: completion count ratios, disjoint status distributions, source-defined budget ratios and metric-specific numeric coverage. Diagonal hatching marks incomplete financial aggregates;59/61 means two unusable values excluded from the subtotal, not zero. Its width encodes the subtotal; 59/61 describes coverage. The cropped 44 unit is not supplied by the image. The guide does not claim to reconcile that subtotal against an operational workbook.

Existing v130 verification is historical and documents the broader regression/mobile/upload/print coverage. This update retains those calculation/loader/report definitions; relevant UI and native-print checks were rerun. No full accessibility certification, Power Query refresh, Windows file-opening or physical-printer check is claimed. The managed test browser blocks file:// navigation; final package smoke verification uses a local HTTP origin. Page-margin counters require a current compatible browser, verified in Chromium 151. Retain the previous extracted folder until existing browser notes/settings are checked.
