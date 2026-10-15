# Performance App v168 — entity report

15 October 2026 (Dubai) · TEC design principles Revision 32

The approved entity-report audit and full-page illustration are implemented. Screen and native PDF share one scoped content renderer: selected entity/relationship/domain/cutoff, contents, overview, source-status charts and compact legend, nonempty follow-up, timing/relationship context and grouped main records. Focused views print their exact active domain/status/search and records.

Recorded statuses stay separate from date alerts. A ready topic with a passed plan remains ready; missing presentation dates do not establish a booking failure. Approved agenda and emerging topics remain separate. All recorded entity council rows retain their source population; the council report's eligible follow-up denominator stays distinct and labeled. No budget, legislation or KPI population was added.

Tables use consistent leading columns, continuous main-list numbering, recorded progress only where supplied, applicable dates and complete populated notes. Decision references omit blank fields and meeting dates do not become deadlines. Repeated filenames and administrative row labels are omitted from the report. Phone tables preserve readable cells and keyboard-accessible local scrolling. Summary and source-status actions retain exact-record drills and return focus. Live query changes also refresh PDF content.

Empty results retain scope and filters but omit empty summary/contents/charts/legend/follow-up/record groups. Missing source names receive a specific completeness explanation. The audited special-project detail guard now excludes unnamed source rows consistently instead of displaying fallback titles as real projects.

## Verification

**273 focused assertions pass**, reusing the v167 audit and model/export baselines. The final runtime hashes are recorded in [evidence](checks/entity.json); comprehensive checks and the final focused binding are distinguished there.

- Current source records, monthly measures, agenda/HH/council chart specifications, comparisons, source date and project-portfolio model match the verified v167 fixture fingerprints. The intended incomplete-source HH eligibility correction is separately tested.
- Entity union, cross-field intersection, primary/contributor union and deduplication, domain selection, unmatched selections, zero/missing values, source-status coverage and exact current record membership pass. The existing unavailable-history message and comparison setup remain accessible. No operational historical changes were invented.
- Actual completed-summary and source-status actions open the correct 4 completed records and 2 approved ready topics in new tabs. Single-record navigation, entity scope, live text filtering and focus return pass.
- Desktop/tablet/phone checks at 1560, 768, 390 and 320px pass: no page overflow, real table cells, readable source text, valid in-page destinations and fitting in-bar figures. Source counts remain available outside tiny bars without changing proportions.
- Actual native entity downloads cover full illustrative scope, selected entity, council-only scope, contributor scope, live-query drill, unmatched scope, incomplete attachment and 85-line source notes. Ordered screen/PDF source rows agree, all native text lines have page placements, headings stay inside their columns, Arabic glyphs render, links resolve, and every page has correct numbering/copyright and no text beyond its bounds.
- The selected 11-row example uses **4 A4 portrait pages**. The full 343-row example uses **40 pages**, including its 38-row follow-up subset and entity relationship context. Council and contributor scopes each use **2 pages**; a focused single-result query uses **1 page**. Unmatched scope and the actual incomplete attachment each use **1 explanatory page**. Long notes use **13 pages**, preserving all 85 numbered lines with repeated headings and no gap-only page.
- The long-row fix includes the full section-heading/count area in the first continuation region, so a section count is not cropped by table padding. Fitting priority panels stay together, preventing an orphan border at a page end. Chart actions preserve exact native text/geometry.
- The shared portfolio exporter passes its focused regression suite and exactly matches v167 page plans, ordered rows, headings and native text geometry. The affected HH incomplete-source view exports its existing cover and empty body as **2 A4 landscape pages**, with no fallback project records or export errors.
- The four selected PDF pages and affected phone/chart/table views were visually inspected. Full-scope and long-note pagination were inspected through page contacts, with readable continuation examples checked at full size. Native text/bounds checks cover every page. Original Arabic fonts and PDF engine remain unchanged.
- Build freshness, JavaScript syntax, clean ZIP integrity and runtime file hashes pass. Both source workbooks remain byte-for-byte unchanged.

## Scope and limits

The available attachment is dated **30 September 2026** and contains **343 raw agenda/council/special-project rows with blank titles**. It provides **zero eligible named entity rows**. That does not prove zero operational workload. Public populated examples use the separate anonymized illustrative fixture, including the selected 11-row entity example; none of those figures were copied into the attachment.

Entity totals count eligible source rows, not unique real-world projects across portfolios. Primary/contributor memberships and entity subtotals can overlap and are not a performance ranking. Across the illustrative all-entity scope, 39 missing source statuses remain in totals and neutral marks. Unresolved contributor strings are not inferred into entity identities.

Tests used the clean runtime over local HTTP in Chromium. Cold file opening was not re-certified; the managed browser blocked file navigation in the earlier environment check. No Excel recalculation, Power Query refresh, Office rendering or full accessibility certification was performed. No actual previous operational workbook was available for an entity historical comparison; unchanged comparison definitions and unavailable-history handling were checked.

## Delivery

The clean app contains exactly **26 runtime files**, without source modules, workbooks, QA folders or previews. Readable development source and v167 are archived separately.

- [Actual entity screen and illustrative native PDF](entities/README.md)
- [Design principles — Revision 32](TEC-Design-Principles.md)
- [Verification evidence](checks/entity.json)
- [Original approved audit and proposal](../archive/v167/docs/entities/README.md)
- [Release hashes](release.json)
