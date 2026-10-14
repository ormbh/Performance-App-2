# HH report — illustration for review

**14 October 2026 · Based on Performance App v154 and TEC design principles, Revision 21**

This is one proposed HH report composition for review. The working app has not been changed. The illustrations do not establish that the proposed design has been implemented or that the app's native PDF exporter has been validated for it.

## Proposed changes

- Reuse the approved TEC header, navigation, actions, typography, surfaces and spacing. Keep **تنزيل PDF** as the primary report action.
- Present sector, organizational unit, concerned entity and leadership filters consistently. Partial selection shows the first selected name **+N**; a single selection shows its name; all or unrestricted selection shows **الكل**. Preserve the underlying selection semantics.
- Use one restrained summary card with a clear main total, the leadership subset, completed projects, the existing working aggregate and other non-completed projects when present.
- Retain the horizontal **توزيع المشاريع حسب القطاع** chart. Sector names remain readable; bars share a zero-based project-count scale, use the approved status appearances and retain exact counts. Show totals by status with the legend below the chart.
- Give full project and entity names sufficient space in the project list. Keep status, recorded progress, manager and end date distinct and readable.
- Keep project details source-driven: title, status and recorded progress; manager and dates; achieved work, next steps, recommendations and other populated source fields. Recorded project progress remains separate from the portfolio completion rate.

## Screen and PDF

The live page reflows for phone use: filters and detail fields stack, long labels wrap and status counts remain available without relying only on color. Use the shared status colors and text treatments throughout.

The PDF concept remains **A4 landscape, 297 × 210mm**. The proposed cover uses the supplied cover image with centered title, scope and period. Content pages use the independent PDF typography and margins; the summary, sector chart, status totals and legend form one coherent section. Project tables repeat their column headings when they continue, and populated detail narratives may continue naturally without clipping or shrinking. Cover treatment and the HH page composition are proposals in this illustration, not claims of prior HH-specific approval.

## Data and scope preserved

All figures come from the current HH model under the same unrestricted scope. Leadership is a subset of the total and is not added to it. The working aggregate retains its existing source-status eligibility, which may include late projects; it is not silently redefined as one direct source status. Filters, source ordering, unknown values and record identities remain intact. Changing the displayed period does not automatically exclude source records.

| Current summary | Count |
| --- | ---: |
| إجمالي المشاريع الخاصة | 62 |
| منها مشاريع للقيادة | 24 |
| المشاريع المنجزة | 23 |
| المشاريع قيد العمل | 38 |
| حالات أخرى غير منجزة | 1 |

| Status totals | Count |
| --- | ---: |
| قيد المراجعة | 3 |
| قيد التطوير | 35 |
| منجز | 23 |
| حالات أخرى | 1 |

The status totals reconcile to **62**. The last category includes the one record with an unrecorded source status. The portfolio completion rate is **23/62 = 37.1%**; the leadership-subset rate is **12/24 = 50%**.

## Source provenance and illustration limits

- Source: `ILLUSTRATIVE-monthly-preview.xlsx`, read through the v154 application's HH model.
- Report reference date: **30/09/2026**.
- Scope: all sectors, units, concerned entities and leadership selections unrestricted.
- Workbook SHA-256: `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`.
- These are illustrative fixture records, not a claim about current operational results.

The fixture has no populated project descriptions, budgets, achievements, next steps, notes or recommendations. Blank optional narrative fields therefore cannot demonstrate real narrative wrapping in the source-backed sample. Any separate explanatory field layout must be marked as a layout example, not invented project content. When present in a real report, all populated narratives and additional source fields must remain, including follow-up on completed projects; true numeric zero must not disappear as if it were blank.
