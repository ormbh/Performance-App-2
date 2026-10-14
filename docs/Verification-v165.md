# Performance App v165 — council implementation and monthly review

14 October 2026 · TEC design principles Revision 29

## Implemented council change

**قرارات دون جهة إصدار محددة** now spans both columns beneath all named issuing-body charts. It retains its total, status bars, counts, palette and the same physical count scale as the named charts. Desktop uses two status columns; narrow screens stack them. Empty groups disappear. The shared detailed legend remains below the charts and box. Native PDF and editable PowerPoint use the same source model and structure.

No source records, eligibility, metric definitions, monthly source modules or source workbooks changed. The v164 legacy Office square-bullet fix and original Arabic font files are retained.

## Implementation verification

- **493 passing screen/PDF checks** against the exact 26-file clean runtime: nine scopes/cases at 320, 390, 768 and 1440px, six actual PDF downloads, count scale, record membership, empty/only-unassigned cases, all exported table words/numbers, Arabic layout and full source preservation.
- **146 passing PowerPoint structure/data checks** against the same runtime: native charts and embedded workbooks, text, tables, links, ordering and shared count scale. Office visual rendering/manual editing were not run because no Office renderer is installed.
- **Five passing continuation checks:** a controlled six-standard-status case continues named charts and the unassigned box with readable full legends when their combination cannot fit one A4 page. The ordinary fixture keeps the two named charts, full-width box and compact legend together on one A4 landscape summary page.
- Four mixed-square exports retain exactly ten U+F0A7 legacy bullets and ten U+25AA standard squares each. The PDF font-engine checksum matches v164.
- Build freshness and JavaScript syntax pass. [Scope evidence](checks/scope.json) confirms only council modules, release version and generated bundles changed.

The council regression source is `ILLUSTRATIVE-monthly-preview.xlsx`, SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. It retains all164 detail records, of which70 require follow-up:45 TEC,9 SAC and16 without issuer. Controlled cases use in-memory copies. These are fixture values, not constants or a claim about the latest live report.

Actual final PDF renders were reviewed for Arabic, count placement, full-width bounds, shared legend and page footer. No browser errors or external runtime asset requests occurred. The existing A4 height guard can still reject an expanded nonstandard case with seven statuses in every named issuer and seven full definitions; it reports the overflow instead of clipping. Cold file:// opening was not rerun; the clean package was tested over local HTTP in managed Chromium.

## Monthly audit and illustrations — not implemented

[The monthly audit](monthly/README.md) is complete. It found a real special-project subgroup mismatch: monthly24+36 excludes2 blank classifications while the approved detail model is24+38. It also found an overbroad work-status fallback, inconsistent status-label colors, a conditional missing-number display issue and PDF total-caption placement differences. The monthly audit is not reported as a clean pass.

The model audit ran118 checks:116pass, with two failures reproducing the same TEC subgroup issue on the available attachment and fixture. The PDF audit ran34 checks:30pass, with four failures for ready-label color and total-caption placement across continuous/A4 outputs. Tested core totals, record drilldowns, filtering and exported figures otherwise reconcile. Current approved legislation composition is already present and remains intact.

Three review illustrations have16 passing rendering/content checks and use labeled illustrative data. They propose corrected grouping, consistent status colors, directly labeled status bars, a compact shared color key and clear links to detailed reports. The approved legislation example retains late as a subset of work. Monthly calculations and layouts remain unchanged in the delivered app pending the next implementation instruction.

## Evidence and previews

- [Council screen/PDF](checks/council-screen-pdf.json) · [PowerPoint](checks/council-powerpoint.json) · [Continuation](checks/council-continuation.json)
- [Council PDF preview](previews/council-summary-pdf.png) · [Council screen preview](previews/council-summary-screen.png)
- [Monthly audit and illustrations](monthly/README.md) · [Illustration checks](checks/monthly-preview.json)
- [Release file hashes](release.json)
