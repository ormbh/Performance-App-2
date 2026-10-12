# Performance App v144 verification

Date: 13 October 2026. Scope: approved monthly completion captions, budgeted-project completion bar and independent agenda-category boxes, on screen and in continuous/A4 PDF exports.

## Changes

Approved agenda and emerging topics occupy separate equal Linen boxes, with 12px screen / 3mm PDF gaps. Screen category labels retain 18px Dubai Regular and figures retain 28px DIN Next LT Arabic. At phone widths, reserved label height keeps figures and changes aligned.

Annual agenda, council decisions and legislation receive completion captions beneath their existing status bars. Special-project subgroup captions move beside their percentages. Budgeted projects receive a green/Linen completion bar and caption below status figures and before quarters. All captions use **نسبة المنجز** beside an isolated percentage, with an 8px screen / 2mm PDF gap. Screen captions retain 14px Dubai Regular; PDF captions retain their existing 9pt size.

Ratios use the scoped source counts: agendaDone/agendaTotal, councilDone/councilTotal, (legOnTime+legOverrun)/legTotal, each special subgroup's completed/total, and secDone/secTotal. The budget denominator includes statuses omitted from the headline figures. Council includes required-follow-up decisions without approved statuses. Both completed SLC cohorts count toward completion. Missing or invalid values and zero totals suppress a percentage; a valid zero completed count displays 0%.

## Executed checks

- **223 browser/PDF checks pass**, with no JavaScript errors: six caption locations and ratios, 14px Dubai Regular screen text, adjacent alignment, bar placement, equal boxes, physical RTL order, preserved drilldown keys, and no overflow at 1920/1440/390/320px. Mobile category figures share a baseline.
- **21 helper guard cases** within those checks cover zero/full completion, missing/null/string/negative/nonfinite inputs, unavailable metrics, zero denominators, impossible ratios, multi-cohort completion and invalid/overlapping distributions.
- Actual download-button exports pass for the continuous all-scope report, A4 portrait report, and filtered Dubai Plan Office report. PDF text contains every completion caption and percentage exactly as the prepared report; filenames, title/date, scope and requested geometry remain. Source records/counts/scope do not change during export.
- The complete continuous report, all three A4 pages, the filtered report, desktop composition and narrow-phone agenda were visually inspected for Arabic layout, clipping and placement. The frozen fixture produces one continuous page and three A4 pages; this is not a page-count promise for other source workbooks.
- Direct comparison with v143 preserves all source keys/counts, financial section markup, strategy section markup and displayed changes. Both financial bars remain unchanged; no financial or strategy completion caption is introduced.
- **64 independent source/helper checks pass**, without findings. Model, font, vendor, PDF download and pagination sources retain their previous behavior. The new ratios are derived from the scoped model, never from preview constants or rendered text.
- Bundle consistency and JavaScript syntax checks pass. Release evidence records ZIP CRC, complete membership, per-file hashes and identity with the tested runtime. The extracted-package browser rerun is recorded separately in the published evidence.

## Source and limits

Checks use the frozen illustrative workbook dated 30/09/2026, SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. Its agenda has 43 completed of 117 (36.8%); the earlier user-screenshot concept had 44 of 117 (37.6%). The app calculates from the loaded workbook rather than hardcoding either specimen. No operational workbook was supplied or bundled.

Managed Chromium was exercised over local HTTP. Native Windows file-origin execution, Windows Explorer, physical printers and other browser engines were not tested in this release. This focused change does not constitute a fresh audit of every app feature or accessibility certification. Prior verification documents remain historical.

## Runtime hashes

| Asset | SHA-256 |
| --- | --- |
| `assets/js/app-bundle.js` | `0ee4ac3761322c057a7744d1250497e1c18de19088e910f91ebe8c52c35d64b6` |
| `assets/css/app-bundle.css` | `6e236a3cb6904a9f1bcf3aa44700532f7c4aa884abe4d409bf5bb86bc2ac1032` |
| `assets/css/print-measure-bundle.css` | `e10f1c13a809cde50ad24ae0e14fe6c82d299a049c8b57155f0bfd1281d15aa2` |
| `assets/js/lib/offline-pdf-engine.js` | `8038eaa52e8aa4693e6f4d9141f51edfaf78be42621384e608ddfc81d5cb2528` |
