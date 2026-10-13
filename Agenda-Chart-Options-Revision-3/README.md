# Agenda chart options — Revision 3

**Illustrations for review. Performance App v145 is unchanged.**

Two ways to read the same filtered data, using the TEC skill’s fonts, colors, spacing and hierarchy. This package refines only the agenda chart area. The Revision 2 table, first-page-only entity/period header and removal of the source-notes appendix remain the surrounding report concept.

Open **Agenda-Chart-Options.html** after extracting the ZIP. It is self-contained, including fonts, logo and illustrative values; it needs no web connection. Its review controls switch between the two designs and six prepared filter examples. These are illustration controls, not new app controls.

## The two options

| | A — Transposed matrix | B — Quarter panels |
| --- | --- | --- |
| Reading order | Status rows, quarter columns | One quarter at a time; status directly beside its bar |
| Best use | Exact comparisons across quarters | A quicker visual overview |
| Visible values | Every cell, quarter/status totals and status percentages | Quarter totals and counts for each nonzero status |
| Zero handling | Explicit zero cells; quarter columns align across both groups | Zero status rows omitted visually; underlying zero values retained |
| Phone | Each status becomes a strip of quarter values | Quarter panels stack vertically |

**Design recommendation: B for a quicker first read.** It avoids looking up a row–column intersection and removes repeated percentages. A remains useful when precise quarter-by-quarter comparison is the main task. This is a design judgment, not a tested claim about dyslexia or any other diagnosis.

## Illustrations

- [Before and both new options](01-Before-and-Two-Options.png)
- [Selected entity: both options](02-Selected-Entity.png)
- [A4 landscape first-page proofs](03-A4-Landscape.png)
- [Phone comparison](04-Phone-Options.png)
- [Option A — native desktop capture](a-all-1440.png)
- [Option B — native desktop capture](b-all-1440.png)

## Downloadable PDF proofs

Each PDF is **one first-page chart proof**, not a complete agenda export and not a claim that the detailed report fits on one page. Both cohorts stay together on that page. A4 landscape is 297 × 210 mm with 10 mm margins. Selected entity and January–September 2026 appear beneath the title. The footer contains copyright and the proof’s page count only.

- [A — all entities](Option-A-All-A4-First-Page.pdf)
- [A — selected entity](Option-A-Entity-A4-First-Page.pdf)
- [B — all entities](Option-B-All-A4-First-Page.pdf)
- [B — selected entity](Option-B-Entity-A4-First-Page.pdf)

## Meaning and scope

The bars show **counts**, not percentages or a completion rate. All bars within one filtered view share a zero baseline and the same maximum cell count. The maximum is recalculated for the selected scope and printed beside the chart heading. No minimum fill width exaggerates small counts. Quarter totals appear separately.

The approved and emerging cohorts remain separate. Option A’s status percentages use the respective cohort total, never the combined annual total. Ready-for-presentation is Stone `#ABA394`, completed is Green `#01831E`, and review/development retain Taupe `#756B5F`. Review and development remain distinct, directly named statuses even though their approved color is shared.

Both alternatives consume the same `chart-specs.json`. The specification comes from the unchanged v145 agenda model and its effective-period grouping, not a screenshot or raw spreadsheet quarter column. Amended periods and retained carryover logic remain intact. Source status/quarter order is preserved. In A, the union of active quarter columns keeps equal counts at equal physical bar lengths across cohorts; absent-quarter zero cells add no records. B omits quarters without topics. Undated groups, when present, remain separate; no date is inferred.

## Source and verification scope

This is illustrative data from `ILLUSTRATIVE-monthly-preview.xlsx`, report date 30/09/2026, SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. It is not a supplied operational agenda workbook.

- All entities: **117 = 100 approved + 17 emerging**.
- هيئة الطرق والمواصلات: **10 = 8 approved + 2 emerging**.
- دائرة المالية: **1 = 1 approved + 0 emerging**.
- Both selected entities: **11 = 9 approved + 2 emerging**.
- Emerging-only: **17**. Empty scope: **0**.

Six scopes were rendered in both options at 1440, 1024, 768, 390 and 320 CSS pixels. Four actual A4 PDFs were rendered and checked. The review HTML was exercised with browser network access disabled. No production export engine, app source, source workbook or approved design-standard document was changed. Browser/HTML and PDF verification do not constitute full accessibility certification or a PowerPoint/editability check.

Construction uses the supplied Dubai Regular/Bold, DIN Next Arabic and DIN Next LT Arabic assets. Screen chart annotations are 24px; category names are 18px and status labels 16px. The independent print chart scale retains 9pt status labels. Neither table content nor the app’s approved metric scale was shrunk to fit.

The attached QA evidence records reconciliation and rendering checks. `option-a.js/css` and `option-b.js/css` are isolated prototype components, not application patches.
