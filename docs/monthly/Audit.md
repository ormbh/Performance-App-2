# Monthly report audit — v164, before proposed redesign

**Verdict: the core monthly totals are consistent with the available workbook, but the special-project grouping and status presentation have drifted from the approved detailed reports.** This is an audit and design recommendation only; no monthly application files were edited.

## Source and limits

- Application audited: `/workspace/saytara-work/Performance-App-v164`.
- Available user attachment: `Saytara_2026_Mold_v2.xlsx`, SHA256 `1638e2d9e194c21d8d8e258a2bcad7c121cbeb9a4f529f90cea632f212cc66f2`. It is populated, despite its “Mold” filename. It has 672 titled records: 62 special projects, 84 budgeted projects, 117 agenda topics, 164 council decisions, 191 legislation records and 54 KPIs.
- Actual source cutoff: **30 September 2026**, fixed named reference `ValidationDate → Logic!$B$1`; not today’s date. The original workbook has 2,326 formula cells, 1,668 with nonempty saved caches and no TODAY formulas. We inspected those caches; no Excel recalculation or Power Query refresh was run or claimed. The app derives report metrics from the source rows and its explicit rules.
- Public review values come from `ILLUSTRATIVE-monthly-preview.xlsx`, SHA256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. Its current aggregate values happen to match the attachment; its formulas have no saved caches. This is a test fixture, not a current live report.
- Later conversation screenshots show other totals, including 64 special projects. Those screenshots are not a replacement source workbook. Do not label these 62-project results as the latest operational figures, and do not hard-code either set into the application.
- Source rows/workbooks were not edited. Both browser snapshots retained their exact source JSON after the audit interactions. No source narratives are needed in public previews.

## Reconciliation and denominators

| Area | Audited current figures | Definition / interpretation |
| --- | --- | --- |
| Agenda | 117 = 100 approved + 17 emerging; 43 done + 16 ready + 58 in work | Work = 52 development + 6 review. The existing combined completion caption is 43/117 = 36.8%, as approved for monthly; it is not the approved-agenda-only rate. Keep approved/emerging counts visibly separate. |
| Council | 70 eligible = 38 done + 31 work + 1 without status; 94 excluded from 164 source decisions | Eligible follow-up requirements are the approved formal-letter / organizational-unit-email predicates. Total and completion denominator are 70, never all164. 38/70 =54.3%. Missing issuer is retained; missing status is retained separately. |
| Special projects | 62 total; detailed report24 leadership +38 TEC | “Yes” means leadership; everything else belongs to TEC under the user’s approved rule. Detailed leadership24 =12done+12development. TEC38 =11done+23development+3review+1other. |
| Strategic-budget projects | 84 total; headline61active,10done,4frozen/cancelled | Seven Not Started and two Transferred records remain included in total and completion denominator. Their omission from headline tiles is explicitly approved. Completion10/84 =11.9%, not10/75. |
| Budget | Revised approved58,275,000; spent20,396,250; allocated46,620,000; unallocated11,655,000 AED | Spending35%; allocation80%; allocated+unallocated = approved. The approved denominator is revised budget, not original52,447,500. Finance arrows show direction without treating all increases as good/bad. |
| Finish quarters | Q1–,Q2=1,Q3–,Q4=80;2027=3 | Quarters account for81 projects within2026; the approved separate2027 annotation accounts for the other3. No undated records in this source. |
| Legislation | 191 =180done+11work;2late are inside11work | Done is the union of152completed withinSLC and28completed afterSLC, counted once. Completion180/191 =94.2%. Late is never added a second time or treated as a peer completion-bar segment. |
| Strategy | 54registered,39measured; average measured83.2%, average target87.8% | The result mean uses39 measured records; target mean uses49 targeted records. They are independent populations. Measurement coverage39/54=72.2%; do not imply83.2/87.8 is target achievement. |
| Follow-ups | 8 | 2late +3frozen +1cancelled +2transferred. Keep source ordering within approved category ordering. |

## Confirmed inconsistencies requiring correction in a later monthly implementation

1. **Special TEC scope disagrees with its detailed report.** The monthly card and its drill use `specialGs` = exact«لا», yielding36. Detailed HH uses not«نعم», yielding38. The monthly24+36 groups do not exhaust its62 total. One completed project and one unclassified-status project sit outside the monthly subgroups. This affects subgroup counts, completion, links and historical deltas; a CSS-only correction would be wrong. Use one approved grouping function for summary, detailed report, drill and exports. Recalculate eligible history under that same definition; do not carry the old36-based changes onto a38-based label.
2. **The special-project “in work” fallback is overbroad.** Monthly `specialGsProgress` / `specialLeadProgress` classify every non-done/non-late value as work. The source has one missing status; the detail report correctly calls it other. Proposed TEC38 should be **11done +26known work +1other**, where26 =23development+3review. Preserve missing internally and never invent an active status from a blank. The same fallback could misclassify future ready/other values.
3. **Done labels are not consistently colored with their values.** Browser computed styles show gray “منجز” labels in agenda, council, special and budget monthly cards while their numbers are green. The legislation label and number are both green. Ready label and value are already correctTeal. Apply the shared label/value color roles consistently; keep ordinary body text neutral and delta polarity separate from status meaning.
4. **Missing numeric presentation still has a divergent branch.** `dashboard.valueHtml(null)` renders an em dash, whereas zero renders a hyphen and generated “غير مسجل” table cells correctly become empty. This is a code-path finding, not a populated-baseline numeric failure. Apply the approved blank missing-value treatment while retaining an accessible unavailable description; do not turn missing into a numericzero. Use one display formatter for screen and print.

## Current behavior that passed or is an approved exception

- Monthly aggregate agenda and council totals equal their respective detailed report models under the same unfiltered scope; special overall62 also matches. The discrepancy is in special grouping, not its overall total.
- The full set of visible numeric metric drilldowns matched exact source record membership on both available source and fixture. A real clicked council heading opened a new tab with all8 expected filtered records and the exact sector scope. Status tiles currently open generic filtered results, which is working behavior; it is distinct from opening the formatted detailed report.
- Six filter cases were exercised: unrestricted, sector union, unit union, sector/unit intersection, entity union and empty scope. Independent literal-record membership matched application scope. Selected detail drills retained filters. Empty scope hides all six portfolio cards.
- Legislation has no concerned-entity field, so an entity filter excludes it; KPI and budgeted-project concerned entity use the already approved General Secretariat mapping. This is a scope contract, not a missing-record error.
- Legislation’s approved combined-done layout is already implemented on screen and in print. The user’s183/178/5/2 screenshot is a design example, not the current data.
- The budgeted-project card intentionally omits the extra-status disclosure (7notstarted and2transferred here), while retaining the full denominator. Do not re-add that previously rejected disclosure.
- The PDF-only missing-requester note omission and specified prior-project-status completeness explanation omission are explicitly approved by principles§8. They are not PDF parity defects. Similarly, entity scope is intentionally omitted from the exported header under§9 while still affecting data. These exceptions do not excuse the special cohort inconsistency.
- Zero-current status categories are intentionally hidden and unused cards suppressed. Keep internally distinct missing/zero states. A zero-current improvement delta may therefore be hidden with its status tile; do not add empty metric columns simply to show an arrow.
- The existing monthly arrangement is executive follow-up portfolios physically right (agenda,council,legislation,strategy) and projects physically left (special,budget), followed by full-width follow-ups. Screen and print produce this same logical grouping.

## Historical comparison audit

- Current fixture embedded-summary deltas are source-derived, not invented. For example, agenda117 vs114 gives+3; legislation191 vs166 gives+25 and180done vs164done gives+16. The saved-summary source does not itself supply a trustworthy row-level history or an explicit prior cutoff; the app calls it saved previous-month data rather than claiming a current workbook-to-workbook audit.
- The separate previous illustrative workbook was loaded and explicitly dated31August2026 against30September2026. This test produced workbook mode and recomputed both snapshots with the same metric functions. It is a controlled test, not operational history.
- Exact typed composite identities are enforced. There are65 rows without complete approved composite keys in each snapshot,130 quarantined source rows in total;607 exact unique rows are pairable. No duplicate complete composite keys were found. This allows defined aggregate arithmetic but not a claim that every record-level change was reconciled. Do not label absent rows as deletions or fabricate missing matches.
- Redesign should retain source-qualified comparison tooltips, percentage-point units for KPI-average changes, neutral volume/finance direction, and completed/late polarity. Suppress unavailable/zero change; never generate new historical values from an illustration.

## Proposed design approach for review

1. Preserve the approved two-column monthly hierarchy, typography, palettes and fixed card roles. Give each card a clear title-right / overall-total-left header and consistent vertical spacing. Keep presentation changes separate from source definitions.
2. Correct the special leadership/TEC split as above and expose other status only when present. Reuse the detailed report’s canonical status model; if the monthly card groups review and development, explicitly define that grouping in the compact legend.
3. Keep the agenda approved/emerging boxes and the council follow-up scope. For monthly distributions, counts belong inside adequately tall colored segments when they fit; a tiny segment retains its number in the compact status summary. Completion, allocation, spending and measurement strips retain their distinct ratio meanings and approved captions; do not decorate every strip with a count.
4. Use one compact shared status legend, with a short portfolio-specific note only where semantics differ (especially legislation late-subset and council eligibility). Keep it on the same printed summary area as its charts. Do not repeat long detailed-report definitions inside every monthly card.
5. Retain the approved legislation card: done on the right, in work on the left, red “منها متأخر” nested under in work, one completion strip below. Live values come from the current filtered workbook.
6. Make navigation explicit: **عرض التقرير** leads to the formatted agenda/council/special report with the monthly filters retained and unrelated report-local filters reset; clicking a metric retains the existing exact-record drill. Preserve direct links for keyboard users and a predictable return route. Do not make the same number alternately open different destinations.
7. Keep full-width follow-up table in the same content order on screen/PDF. Remove generated empty-note filler only if included in approved cleanup; retain every meaningful source note and legible continuation.
8. Test proposed design with the actual source schema, the anonymized fixture, one-portfolio scopes, sparse statuses, longArabic labels, missing fields, both PDF formats and confirmed previous/current snapshots. Reconcile exact member sets before screenshots.

## Evidence and completion status

- `evidence.json` (public aggregate evidence):118 executed browser/model checks,116passed;2failures are the same confirmed TEC36vs38 mismatch on the two datasets. Additional presentation findings are recorded explicitly rather than counted as a passing test. No browser runtime errors or external runtime requests.
- `workbook-inspection.json`:read-only formula/cache/table/date inspection and hashes.
- `illustrative-values.json`:safe structured review values and proposed grouping.
- Native PDF visual/page/Arabic review is delegated separately under [the PDF audit](pdf-audit.md). This document does not claim a native-PDF visual pass solely from DOM/model checks.
- Excel formulas were not recalculated; Power Query refresh and native PowerPoint monthly output were not run. This task requested monthly audit and illustrations, not monthly implementation or a new PowerPoint export.
