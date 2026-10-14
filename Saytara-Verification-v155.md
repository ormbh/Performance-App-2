# Performance App v155 — charts and shared display rules

## Result and scope

The approved HH revision 3 charts and agenda in-bar counts are implemented. Revision 22 of the bundled TEC skill/principles describes the resulting behavior. No source workbook is bundled or modified.

HH uses two disjoint cohorts: explicit نعم is leadership; all other values, including blank, belong to TEC. Selecting TEC uses this same rule. Empty sector rows hide independently within each chart; empty cohorts hide and the remaining chart fills the width. Bar segments remain proportional, totals follow their actual endpoints, and readable counts appear inside segments. Per-bar captions are removed; aggregate status totals and the detailed HH legend remain. Source filenames are omitted from HH cards and exported card metadata.

Agenda preserves its source scope and quarter/status ordering. Counts appear inside segments only when readable without changing their size. Small counts remain available in accessible quarter descriptions, explicit quarter activation and exact count matrices. Native PDFs print the exact matrix after the chart/definitions page. Quarter interaction retains aggregate totals by default and in print.

Across shared app views, numeric metric zeros display a dash and generated missing-value placeholders render empty. Ready plain labels/counts use Teal; completed uses Green and late Red. Filled Teal badges and bars retain light ink. Typed numeric source-check cells follow the display rule while preserving raw values in their model, tooltip and CSV. Identifiers, dates, freeform notes, underlying numeric geometry and raw exports are not rewritten.

## Source and reconciliation

Fixture: ILLUSTRATIVE-monthly-preview.xlsx, source cutoff 30 September 2026. SHA-256: `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. This is demonstration data, not a production-workbook audit. No screenshot values or fixed example scales are hardcoded into application charts.

- HH: **62 = 24 leadership + 38 TEC**, including both blank leadership classifications. Leadership has four populated sector rows; TEC has six. The TEC filter deliberately includes blank classifications as requested.
- Agenda: **117 = 100 approved + 17 emerging**. Approved statuses are 34 completed, 51 development, 5 review and 10 ready. Emerging statuses are 9 completed, 1 development, 1 review and 6 ready. These reconcile to the raw fixture and fresh model.
- Exact source record identities and raw `c`/`t` fields remain unchanged. All-record, selected-sector/unit unions, intersected filters, leadership-only, TEC-only, selected entity, single category and empty scopes were checked.

## Verification

- The integrated browser run passed 205 checks for source preservation, filtering, hidden empty rows/cohorts, endpoint totals, proportional bars, readable labels, quarter activation and responsive layouts. Seven additional focused cases checked missing progress, zero values, Ready ink and a single-count agenda layout. Desktop and phone screenshots were visually inspected.
- Fourteen shared helper/render checks distinguish true zero from tiny positive values and preserve numeric IDs, dates, source narratives, blank-filter tokens and numeric bar geometry. A six-page display audit covered dashboard, results, projects, entities, comparison and data checks; generic details and monthly/entity Ready colors were also inspected using computed styles.
- Native HH PDFs were downloaded for unrestricted and TEC-only scopes. The unrestricted fixture has 72 physical pages and the TEC-only report 46. Cover has no footer; content numbering starts on physical page 2. Both unrestricted charts and all definitions fit on page 2 within a 681.45px block and a 687.87px content limit. All 19 positive status segment labels fit at 14pt in the paired example, including the seven 1-count segments. All-page text bounds, a contact sheet and representative long detail cards were checked.
- Native agenda PDFs preserve a common physical count scale for paired charts, charts and original definitions together after the cover, aggregate status totals and exact matrices afterward. The all-scope fixture has 16 pages; the selected emerging-only entity report has 4. Both full and filtered outputs were inspected for text bounds, Arabic shaping, labels, pagination and scope. Native exact-matrix pages preserve Ready Teal and completed Green on positive counts and labels, with neutral zero dashes and no repeated grand total in the bottom-left corner.
- HH marks are native PDF rectangles/text; agenda marks are native SVG-derived vectors/text. Chart screenshots are not embedded. Original Dubai/DIN fonts remain bundled and embedded in PDF output. Small in-bar labels that do not fit are omitted without changing data geometry; exact counts remain in details/matrices.
- Actual native editable PowerPoint exports were generated for three HH scopes, three agenda scopes and representative/synthetic-Ready council reports. XML/ZIP integrity, chart data caches, embedded workbook values, chart/shape bounds, source preservation and status colors were checked. Visible zero-axis formatting changes retain numeric zero caches. Chart totals added as native text overlays require manual adjustment if editing chart data in PowerPoint after export.
- JavaScript syntax and generated bundle consistency passed. Release packaging checks verify ZIP CRC, extracted manifest hashes, synchronized Revision 22 principles and absence of workbooks/test output from the app bundle.

## Limits

Browser checks used Chromium and local assets with external requests blocked. Local-file cold startup, native mobile devices and screen-reader certification were not separately tested in this environment. PowerPoint/LibreOffice rendering and in-application editing were unavailable; structural/native-data checks do not substitute for those checks. No historical data refresh, Excel recalculation or production-data audit was requested or performed.

This updates the downloadable TEC skill package and principles. It does not claim to replace a separately cloud-installed skill.
