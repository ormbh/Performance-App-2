# Performance App v140 verification

Date: 12 October 2026. Scope: four approved monthly presentation refinements.

- Show only **مشاريع 2027: N** under the strategic-budget project quarters when the filtered valid-2027 count is positive. Otherwise omit the paragraph and spacing. Preserve the separate quarter reference year and all quarter values.
- Keep the approved budget total first; show spending amount/change and solid Teal bar before the allocated/unallocated pair and solid Taupe allocation bar.
- Remove the visible **الإنفاق …% من الموازنة المعتمدة** caption. Preserve the spending value, difference, approved-budget denominator, bar ratio and accessible label.
- Apply the existing completion-change colors to the arrow and difference for **SLC منجز بعد موعد**: positive Green #01831E and negative Red #C00000. Main-figure color and SLC text isolation remain unchanged. Zero stays hidden; unavailable retains its existing screen explanation and is omitted in PDF.

## Checks

- **57 focused browser/PDF checks pass**, with no runtime errors. Actual button downloads cover the full continuous monthly report (one page), a source-derived sector with no 2027 projects (one page), and full A4 portrait monthly (three pages).
- The frozen illustrative fixture has 81 valid-2026 and three valid-2027 strategic-budget projects. Only **مشاريع 2027: 3** is shown in full scope; a filtered scope with projects but no 2027 projects has no annotation in screen/export DOM or native PDF text. The shared helper emits no empty paragraph.
- Screen budget values and differences match v139 exactly. Actual screen/PDF coordinates confirm spending above allocation; the removed visible spending caption is absent. Source keys, counts, filters and follow-up membership are unchanged by download.
- The SLC positive change arrow and difference are Green in computed screen styles. A separate native-text color inspection confirms **both glyph runs** are #01831E in continuous and A4 PDFs, including the wrapped A4 caption. The unchanged main figure is Green.
- All five downloaded pages retain their format, first-page title/date/sector-unit header, copyright footer and in-page text bounds. Desktop and 390px viewport checks pass without horizontal document overflow. Screen and native PDF budget/legislation blocks were visually inspected.
- Independent contracts pass **16 finish-year edge cases / 32 screen-and-print contexts**, plus **four SLC change-state cases**. The financial source audit confirms unchanged money keys, deltas, drill targets, eligibility, numerator/denominator formulas and meter tones. The finish-year summarizer and 31 protected model/report/font files are identical to v139.
- Bundle generation and JavaScript syntax checks pass. CSS and the offline PDF engine remain byte-identical to v139. Runtime changes are confined to the monthly coverage renderer, the dashboard/paper presentation changes above, index build/cache version and generated JavaScript; release documentation/manifests are updated separately.

| Runtime asset | SHA-256 |
| --- | --- |
| `assets/js/app-bundle.js` | `41dacb90e394ca9aa4de452b2be1b6424b16f56986b59b01ca31254ec0a3d3d7` |
| `assets/css/app-bundle.css` | `c5dca03eb8791f003de61a1519e27d76557ec23f0eafb24d40c4cf7ab43347d4` |
| `assets/css/print-measure-bundle.css` | `b9c76b378417f9c84f09cfc9dd29252c0086172b37bff0eacc0bdd93f0163cd8` |
| `assets/js/lib/offline-pdf-engine.js` | `8038eaa52e8aa4693e6f4d9141f51edfaf78be42621384e608ddfc81d5cb2528` |

## Source and limits

QA uses the unchanged illustrative workbook, cutoff 30/09/2026, SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. It is excluded from the app ZIP. No operational workbook was supplied. Tests use Chromium over local HTTP; the user's Windows file-origin environment, physical printers and Office exports were not re-run for these presentation changes. Prior releases retain their own verification scope.

The release package is checked through extraction, exact file membership, CRC integrity, manifest hashes and correspondence with the tested runtime. Source workbooks and QA artifacts are excluded from the app package. The accompanying release evidence records those checks and a cold-load download from the extracted app.
