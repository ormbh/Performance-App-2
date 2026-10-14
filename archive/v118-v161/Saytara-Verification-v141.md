# Performance App v141 verification

Date: 12 October 2026. Scope: monthly filter summaries and scoped PDF filenames.

## Result and behavior

The monthly dashboard dropdowns, scope summary and monthly PDF header show the first selected choice plus **+N** additional distinct choices. A single choice shows its name. Full and unrestricted selections show only **الكل**, without a count. Existing selection order, source alias grouping and exact selected tokens are retained. The entity dropdown uses the compact display, while entity remains excluded from the exported header as previously approved.

Monthly filenames use **التقرير_الشهري_للأداء_Mmm_yy[_scope].pdf**. The report date supplies the month/year. A partial unit selection takes priority over a partial sector selection; multiple choices use first name and **_+N**. Unrestricted/all-selected scope omits that field's suffix. Unsafe characters are sanitized and unusually long names are bounded without dropping the date or additional count. Other reports' filenames and visible report titles are unchanged.

## Executed checks

- **67 browser/PDF checks pass** with no runtime errors. Actual checkbox interactions cover 1/2/3/4 units, selection order differing from dropdown order, removing/reselecting the first choice, reopening, all, clear, sector union, sector/unit intersection, cascaded all-unit selection, entity display and 390px layout.
- Scoped counts, source keys and follow-up membership match the immutable v140 baseline in five selected scopes. Explicit all-selected keeps its exact token array; display does not remove or widen filters.
- Actual download-button PDFs: four selected units in continuous format (one page), all units in continuous format (one page), and combined partial sector/unit scope in A4 portrait (two pages). Native text retains the compact captions and correctly ordered **+N**. Page text stays within bounds. Generated filenames follow report date and selected scope.
- **Nine filter edge cases pass**: unrestricted/all, source-selection order, blank value, aliases counted once, partially selected alias groups, all alias tokens, stale saved choices and empty options. Formatting does not mutate selections.
- **Eleven filename cases pass**: no scope, sector, unit priority, multiple units/sectors, all units, sector fallback, Windows filename characters, source month/year, long Unicode names with retained count, and unchanged names for other reports.
- The 19 protected model/controller/monthly-renderer/CSS/PDF-engine files are identical to v140. The PDF collection, geometry and painting helpers are unchanged; only its filename function/return name changes. A shared pure formatter and the monthly display consumers supply the scope presentation change.
- Screen desktop/mobile and the actual continuous/A4 header renders were visually inspected for Arabic labels, counter direction, wrapping and clipping. Bundle generation and JavaScript syntax checks pass.

| Runtime asset | SHA-256 |
| --- | --- |
| `assets/js/app-bundle.js` | `90f73e067c63eaf3e96cc5898be9f54977d1d49236dc64d6896873acb2a14452` |
| `assets/css/app-bundle.css` | `c5dca03eb8791f003de61a1519e27d76557ec23f0eafb24d40c4cf7ab43347d4` |
| `assets/css/print-measure-bundle.css` | `b9c76b378417f9c84f09cfc9dd29252c0086172b37bff0eacc0bdd93f0163cd8` |
| `assets/js/lib/offline-pdf-engine.js` | `8038eaa52e8aa4693e6f4d9141f51edfaf78be42621384e608ddfc81d5cb2528` |

## Source and practical limits

Tests use the frozen illustrative workbook with report date 30/09/2026 and SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. No operational workbook was supplied. The workbook and QA artifacts are excluded from the app ZIP. Data formulas, cutoffs, chart meanings and source eligibility retain their definitions.

Managed Chromium runs through local HTTP. The user's Windows file-origin environment, physical printers and Office exports were not re-run for this targeted change. This is focused functional/visual verification, not accessibility certification. Prior releases retain their historical verification scope.

Release evidence records extracted file membership, CRC/manifest hashes, runtime match to this tested candidate, and a cold-load download from the extracted package.
