# Performance App v154 — status consistency and agenda totals

## Result and scope

The app uses one status appearance mapping across badges, native chart marks and legends, and PDF/PowerPoint status graphics. The existing badge fill, readable ink and border are canonical. Financial allocation/spending, measurement coverage, source quantities and change-arrow semantics retain their independent roles.

Agenda charts show per-category totals by status by default. Explicit quarter activation shows that quarter’s breakdown; repeated activation, Escape or an outside click restores totals. Hover/focus alone does not alter values. Persistent selection/hover outlines are removed; keyboard focus remains visible. The native PDF always uses aggregate status totals, independent of screen selection.

The updated self-contained TEC skill/principles are Revision 21. Earlier separate chart-status palette rules are superseded. This package update does not claim that the cloud-installed skill has been replaced.

## Source and reconciliation

Source fixture: `ILLUSTRATIVE-monthly-preview.xlsx`, cutoff 30 September 2026; SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. This is an illustrative workbook, not an audit of a production workbook. Screenshot values are not hardcoded into the app. All model files and source records are unchanged from v153.

Baseline/candidate scoped records, totals, quarter/status groups and detail tables match. Tests cover all records, selected entity, approved-only, emerging-only and empty scopes. Synthetic cases are separately identified and include late, undated, additional category, one item and larger counts. Colors are presentation and are excluded from data-equality comparisons.

## Checks completed

- 500 fixture checks and 255 separate synthetic checks, including aggregate defaults, explicit activation, pointer/keyboard behavior, reset/filter transitions, source preservation, zero dashes, scales and filtered totals.
- 69 focused screen checks across six viewport widths, with desktop and phone visual inspection. Undated labels and single-count layouts fit without overlap. Keyboard focus is intentionally visible after keyboard use.
- Shared palette checks: 45 runtime checks plus independent comparison of 17 badge specimens, 117 agenda badges, 22 chart segments and 5 legend swatches. Actual screen fills/ink/borders agree with the shared mapping.
- Native A4 landscape PDFs: charts, status totals and the original definitions stay together on physical page 2. Cover/centered title/entity/period, detail records and content-page numbering remain intact. Export after a clicked quarter uses totals, not the temporary quarter breakdown.
- Normal first-content block measures about 179.14mm; dense three-category/five-status/undated case about 180.49mm within the 182mm content height. Axes/quarter labels retain 9pt, quarter counts 16pt, summary labels 10.5pt and summary values 12pt.
- Native PDF segments remain vectors and text remains selectable. Forty-five segment geometry/color comparisons across seven PDFs passed; chart screenshots are not embedded. PDF reviewer also completed 219 checks of totals, type, bounds and pagination.
- PowerPoint export files were generated for agenda, council and special projects. Status fills/outlines and readable status text were structurally inspected; chart numerical caches and embedded chart workbooks match v153. Slide counts remain 14, 47 and 77 for this fixture.
- A final Council PowerPoint-only correction preserves the existing non-status issuer/follow-up colors. Module-level comparison confirms all native UI, data, interaction and PDF code is byte-identical to the previously tested bundle; affected PowerPoint exports were rechecked. The included final-bundle isolation evidence links the two bundle hashes.
- Source bundles and JavaScript syntax checked. ZIP CRC and extracted file-manifest hashes checked when packaging.

## Limits

PowerPoint was checked structurally and against its native chart data; no Office/LibreOffice renderer was available for a fresh visual render or an in-application edit test. Browser verification used Chromium and local assets. Native mobile devices and screen-reader certification were not tested. Offline PDF export was checked after local assets were primed. This is a focused presentation/interaction release, not a new audit of every app calculation or a production-data analysis.

See the accompanying exact-bundle evidence, previews and Revision 21 principles. The source workbook is not included in the app ZIP.
