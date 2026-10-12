# Saytara verification — v136

**Verdict: PASS for the approved changes and tested workflows.**

The monthly report now defaults to a continuous digital PDF: 260mm width, 12mm margins, 236mm content and content-measured height. It retains paired projects on the left, executive portfolios on the right, all full-width followups below, approved typography, one header and one copyright/page footer. Cards and followups use 5mm padding, columns a 6mm gap, stacked cards 4mm, card headings 3mm bottom spacing, bars/metric rows 2.5mm top spacing and table cells 3mm padding. Monthly A4 portrait remains selectable; other document orientations are unchanged.

| Gate | Result and scope |
| --- | --- |
| Source regression | PASS: all 672 illustrative records, KPI/budget/counts/changes, bars, 37 printed metric entries and eight followup keys match released v135 in both continuous and A4 modes. 502 null and 27 zero progress values remain distinct. |
| Protected modules/assets | PASS: 44 files remain byte-identical, including all 15 model modules and 11 report/PPT/template modules; bundled font assets are unchanged. |
| Native browser/export checks | PASS: 229 checks across ten print cases, including a full and source-filtered empty continuous report, monthly A4, agenda/council/HH landscape, projects/entities/comparison/search portrait, settings persistence, focus, mobile controls, source cutoff, copyright and native text bounds. |
| Continuous sample | PASS: one native PDF page, nominal 260 × 602mm (actual Chromium 260.01 × 601.81mm). Actual height follows selected content. No fixed sample page-count promise for other sources. |
| Independent visual verification | PASS: full page and readable detail crops; paired positions, aligned SLC/strategy figures and retained changes, all eight complete table rows, native fonts/colors/sizes, no clipping or overlap. Footer clearance is 34.43pt. Character/font/size/color content matches the earlier continuous preview; widening changes wrapping and spacing. |
| Final PDF binding | PASS: the fresh extracted final-runtime PDF has identical native text, page dimensions and rendered pixels to the independently reviewed PDF. The later controller change only defers a fallback notice until print exit. |
| Asynchronous print lifecycle | PASS: 22 checks for toolbar and actual print-media entry, delayed local fonts/images, pending callbacks after cancel, safe height fallback, source retention and one deferred notice after a print hold. |
| Fresh extraction | PASS: 26 checks including actual upload, search and details, report menu destinations, mobile HH view, continuous PDF, selected monthly A4 and agenda landscape; no script or asset failures. Runtime bundle hashes match the release. |
| Direct file navigation | NOT RUN: managed Chromium blocks file navigation with ERR_BLOCKED_BY_ADMINISTRATOR before app execution. Extracted-package checks used local HTTP. No policy bypass was attempted. |
| Windows, hardware printing and Office editing | NOT RUN in this managed Linux browser environment. Native Office/template modules are retained, not newly edited or independently certified. |
| Formal accessibility certification | NOT RUN; keyboard/focus/mobile checks are targeted functional checks only. |

The ordinary continuous page is measured after print fonts and images are ready. If it would exceed 5080mm, the current print session uses A4 portrait and shows a notice after print closes. No records or notes are removed, text is not shrunk and the saved format preference is retained. This limit is a native PDF size constraint, not an A3 option. Choose Save as PDF in the browser dialog for continuous digital output and A4 portrait for paper.

All populated checks use the frozen illustrative workbook `ILLUSTRATIVE-monthly-preview.xlsx`, cutoff 30/09/2026, SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. No operational workbook was supplied. The fixture and its test records are excluded from the app ZIP. No formula or Power Query refresh is claimed.

Final runtime hashes:

- JavaScript: `5a9d8072c1ec62c9efae354f43ebd2e6e726ece9f1c5ef27992a3eacb07f8570`
- CSS: `81805c36048d18cf468bd5f62e0f7cfbd953911e0467b9f9d05b9da5a9aec792`

Build and syntax checks pass for 65 CSS modules and 48 JavaScript modules. The release manifest records every packaged file except itself; final extraction verifies the complete file set and all hashes. Source, comparison, filtering, zero/missing semantics, status definitions and native Office templates retain their existing contracts. Earlier verification files are historical evidence for their own releases.
