# Monthly screen/PDF audit — v164 baseline

Audit-only evidence for the proposed monthly update. No application code or source workbook was edited. These artifacts use the illustrative workbook only; production source contents are not published here.

## Verdict

Native exports preserve the tested figures, source records, readable Arabic, card boundaries and report flow. Presentation consistency needs revision, and the special-project cohort defect propagates to both PDF formats. This is **not a clean monthly QA pass** until those issues are resolved.

## Source and output profiles

- Source: `ILLUSTRATIVE-monthly-preview.xlsx`.
- SHA-256: `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`.
- Source report date: **30/09/2026**. The PDF header and filename preserve that date rather than current execution date.
- Full scope continuous PDF: **1 page, 297 × 655 mm**.
- Full scope A4 PDF: **3 pages, 210 × 297 mm each**.
- Additional actual filtered continuous PDF: sector **الأمانة العامة للمجلس التنفيذي**, unit **مكتب خطة دبي**; header includes both names; filename `TEC_Monthly_Sep_26_Dubai_Plan_Office.pdf`.

## Defects and recommendations

| Priority | Evidence | Expected treatment |
| --- | --- | --- |
| P1 | Special projects: total **62**, leadership **24**, TEC **36**, with 2 blank classifications missing from subgroup. The same mismatch appears on screen, continuous PDF and A4. | Apply approved grouping: blank leadership classification belongs in TEC unless explicitly نعم. TEC becomes **38**; recompute subgroup statuses, completion denominator and drilldowns using those exact records. Root model audit independently reconciles source statuses. |
| P2 | PDF ready label **جاهز للعرض** computes to `rgb(79,78,78)` while its figure is Teal `rgb(17,94,103)`. Screen ready label/figure both use Teal. | Apply identical Teal label/figure role in both native PDF profiles. |
| P2 | Common done labels in agenda, council, special projects and budget projects remain neutral on screen and PDF, while figures are Green. The legislation custom done label is already Green. | Share the approved Green status label/number mapping consistently; retain neutral roles for non-status fields. |
| P2 | In every PDF main total, **الإجمالي** sits alongside the number, inside its vertical interval. On screen it is beneath. | Use the shared title/total hierarchy with the caption below the total in PDF too. |
| P2 recommendation | Seven follow-up rows display generated **لا توجد ملاحظة مسجلة**. Actual note content remains intact. | Reconcile against the global blank-value rule: leave missing note cells empty, retain supplied notes. This is an explicit recommendation rather than missing PDF content. |
| P3 refinement | A4 page 1 has unused space beneath the left special-project card because the whole budget card moves to page 2; page 2 right contains only strategy. | Explore spacing/balance without changing the approved two portfolio columns, shrinking type or splitting a fitting card. This is **not clipping or data loss**. |

## Verified behavior

- Exact screen/print metric strings match; every actual PDF metric contains the expected isolated numeric line in its mapped native rectangle. Initial whole-rectangle comparisons were refined because CSS line-height boxes can include adjacent labels/changes; those were harness false positives, not value defects.
- All six metric cards remain whole. Projects stay physically left; executive portfolios stay physically right. All eight follow-up records appear exactly once in actual PDF text; A4 continuation repeats table headings.
- Approved legislation composition is present: total **191**, done **180**, work **11**, late subset **2**, completion **94.2%**. Late is nested and not double-counted into the total/bar.
- Native text is within physical page bounds; rendered pages were visually inspected for Arabic/RTL, numbers, badges, pagination and footer clearance. No runtime browser errors or external requests occurred.
- Source record JSON is unchanged after export; workbook bytes unchanged.
- Filtered exports omit empty metric portfolios and retain selected sector/unit in the header. Entity header omission remains intentional per the approved monthly profile.
- The existing PDF-only omission of the missing-requester diagnostic and prior-project-status completeness explanation is **approved** in design principles section 8. It is not reported as a PDF defect.
- The 297mm continuous profile and A4 portrait profile remain approved section 10 behavior. A4 landscape or a fixed page count is not proposed.

## Audit coverage and limits

This evidence covers the native HTML-to-PDF engine actually used by the app, full-scope and one sector/unit-filtered scenario. Historical changes were checked for screen/PDF parity but not independently recalculated here. No Excel/Power Query refresh, PowerPoint or Office rendering was performed. The production workbook was not exported. No new visual direction or monthly implementation is applied by this audit.

## Evidence

- `evidence.json`: 34 automated checks; 30 pass and 4 intentionally fail for the ready-label color and total-caption placement across both profiles. Other documented issues are independently grounded observations, not counted as passing checks.
- `monthly-continuous.pdf`, `monthly-a4.pdf`, `monthly-filtered-continuous.pdf`: actual native exports.
- `monthly-a4-page-1.png` through `monthly-a4-page-3.png`: every A4 page inspected.
- `monthly-continuous-part-1.png` through `monthly-continuous-part-3.png`: all continuous output inspected in readable crops.
- `monthly-screen.png`: current desktop baseline after the upload toast disappears.
- `monthly-*-geometry.json`: native page plan, card placements, metric values and follow-up keys.

Runtime SHA-256 values:

- `assets/js/app-bundle.js`: `b64869ed1e456265faf5e679a0e7757618234185197c43f00e8cfbb9b2658b4c`
- `assets/css/app-bundle.css`: `85f803fec7a85da7cc73a51c8cfa47a06fdf56a9161cfbf9e907715f898addd8`
- `assets/css/print-measure-bundle.css`: `79a00c0ebf2c15120229f80e042e46eefec346f043b1353be3883101a8f060f2`
- `assets/js/lib/offline-pdf-engine.js`: `647b32e4d4481fbc4df6edfa77ac71853131448ea4602d6b054f713ef6ee7069`
