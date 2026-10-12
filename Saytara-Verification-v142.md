# Performance App v142 verification

Date: 12 October 2026. Scope: monthly PDF filename formatting.

## Result

Monthly PDFs now use **التقرير_الشهري_للأداء[_scope]_Mmm_yy.pdf**. Example: **التقرير_الشهري_للأداء_مكتب_خطة_دبي_Sep_26.pdf**. The Arabic report title and selected scope stay together; the English month/year and `.pdf` extension form the final segment. No generated **+N** is appended to the filename. No hidden direction controls are added: actual Chromium downloads replace these controls with underscores.

The report date supplies the month/year. A partial unit selection takes priority over a partial sector selection. Multiple choices use the first selected name only; full/unrestricted fields omit the scope name. Unsafe filename characters and source direction controls are removed or sanitized. Long Unicode scope names are bounded while retaining the date and real `.pdf` extension.

Dashboard dropdowns, scope summaries and the visible monthly PDF header keep **first selected name +N** for partial selections and **الكل** for full/unrestricted selections. Other reports' filenames retain their existing behavior.

## Executed checks

- **12 filename contract cases pass**: unrestricted scope, sector, unit priority, multiple units/sectors, full selection, sector fallback, invalid Windows filename characters, source direction controls, source date, long Unicode names and other report types. Formatting does not mutate selected filters.
- **Seven browser/PDF checks pass** with no runtime errors. Actual checkbox selections produce a downloaded file named **التقرير_الشهري_للأداء_مكتب_خطة_دبي_Sep_26.pdf**. The continuous PDF has one page and its native header retains the selected unit, **+1**, and report date **30/09/2026**.
- A browser probe confirms Chromium replaces LRM/RLM, embedding and isolation controls in suggested filenames with underscores. The release uses ordinary Unicode text without those controls.
- Source comparison against v141 confirms only `downloadName()` and its generated JavaScript bundle changed among runtime assets. Screen filters, PDF header, data models, CSS, PDF geometry and painting code are byte-identical to v141.
- Bundle consistency and JavaScript syntax checks pass. Release evidence separately records ZIP membership, CRC/manifest hashes and runtime identity; extracted-package evidence records a cold-load download from that package.

| Runtime asset | SHA-256 |
| --- | --- |
| `assets/js/app-bundle.js` | `89c74a30844f0916dcf94fbda4ccafdd286ff4b9553e166822581bb3a62112f5` |
| `assets/css/app-bundle.css` | `c5dca03eb8791f003de61a1519e27d76557ec23f0eafb24d40c4cf7ab43347d4` |
| `assets/css/print-measure-bundle.css` | `b9c76b378417f9c84f09cfc9dd29252c0086172b37bff0eacc0bdd93f0163cd8` |
| `assets/js/lib/offline-pdf-engine.js` | `8038eaa52e8aa4693e6f4d9141f51edfaf78be42621384e608ddfc81d5cb2528` |

## Practical limits

The fixture is illustrative, with report date 30/09/2026 and SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. No operational workbook was supplied. Source records, totals and calculations are unchanged. Workbooks and QA artifacts are excluded from the application ZIP.

Downloads were verified in managed Chromium over local HTTP. Native Windows Explorer, the Windows Save As dialog and Windows file-origin execution were not available for verification. Grouping reduces mixed-direction transitions; the operating system still controls filename alignment. This is focused filename verification, not a new full application or accessibility audit. Earlier release evidence retains its historical scope.
