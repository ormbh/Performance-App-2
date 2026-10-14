# Agenda chart — Revision 4

**Illustration only. App v145 unchanged.**

This revision applies the requested cleanup to the transposed chart:

- Remove the repeated **الإجمالي** column, its status percentages and the bottom totals row from both charts.
- Align **الحالة** to the same right edge and padding as the status names beneath it.
- Remove the unused spacing on phones.
- Keep the headline counts **117 / 100 / 17** and every quarterly status count. “Remove the totals” is interpreted here as removing the repeated chart totals, not those headline figures.

The quarter-panel alternative from Revision 3 has been set aside. This package shows all three requested replacement directions alongside the cleaned matrix:

| Alternative | Reading approach | Main tradeoff |
| --- | --- | --- |
| 1. Grouped horizontal bars | Compare quarters within each named status | More repeated quarter labels; bar lengths make comparisons visible |
| 2. Vertical bars within quarter columns | See each quarter's status profile | Full-width category plots keep names readable; small counts remain short on the shared scale |
| 3. Text and numbers | Look up exact counts in a quieter matrix | No visual encoding of relative size; still requires reading figures |

The bar alternatives retain one common count scale across both cohorts within the selected view. Each vertical cohort uses the same plot height. No new color semantics, minimum bar sizes, subtotals or percentages were added. The text alternative has no irrelevant bar-scale caption. None of these alternatives is implemented in the app.

## Review files

- [Updated chart](a-all-1440.png)
- [Before and after](01-Before-After.png)
- [All three alternatives](03-Three-Alternatives.png)
- [Side-by-side comparison at native scale](05-Side-by-Side.png)
- [All three with a selected entity](04-Three-Filtered-Alternatives.png)
- [Selected-entity A4 proof](02-Filtered-A4-Preview.png)
- [All entities — first-page PDF proof](Agenda-A-All-A4-First-Page.pdf)
- [Selected entity — first-page PDF proof](Agenda-A-Entity-A4-First-Page.pdf)
- Open **Agenda-Chart-Revision-4.html** after extracting the ZIP to try six prepared scope examples offline.

The package contains eight PDFs: the revised matrix and each of the three alternatives, each shown for all entities and a selected entity. Each PDF contains one **first-page chart proof**, not a complete report. Both cohort charts fit on the same A4 landscape page. The selected entity and January–September 2026 appear beneath the title; the footer contains copyright and the proof page count only.

| Design | All entities | Selected entity |
| --- | --- | --- |
| Revised matrix | [PDF](Agenda-A-All-A4-First-Page.pdf) | [PDF](Agenda-A-Entity-A4-First-Page.pdf) |
| 1. Horizontal bars | [PDF](Agenda-Grouped-All-A4-First-Page.pdf) | [PDF](Agenda-Grouped-Entity-A4-First-Page.pdf) |
| 2. Vertical bars | [PDF](Agenda-Vertical-All-A4-First-Page.pdf) | [PDF](Agenda-Vertical-Entity-A4-First-Page.pdf) |
| 3. Text and numbers | [PDF](Agenda-Text-All-A4-First-Page.pdf) | [PDF](Agenda-Text-Entity-A4-First-Page.pdf) |

## Data and checks

The unchanged source specification is carried from Revision 3, derived from the v145 agenda model using `ILLUSTRATIVE-monthly-preview.xlsx`, report date 30/09/2026. Fixture SHA-256: `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. These are illustrative records, not an operational agenda workbook.

All entities: **117 = 100 approved + 17 emerging**. هيئة الطرق والمواصلات: **10 = 8 + 2**. دائرة المالية: **1 = 1 + 0**. Both selected entities: **11 = 9 + 2**. Emerging-only: **17**. Empty scope: **0**.

Counts, status colors, source order and effective-quarter grouping are preserved. The two cohorts share the union of active quarter columns and one zero-based count scale within each filtered view. A zero intersection adds no records. Only the repeated presentation totals and percentages are removed; the source calculations and values remain unchanged.

The illustration uses the supplied Dubai and DIN fonts. 120 screen states were rendered across four designs, six scopes and five viewport widths (1440, 1024, 768, 390, 320px), and eight actual A4 PDF proofs were produced. See `verification` for the independent review and precise limits. The self-contained HTML needs no network access. No application source, production export engine or approved standard document was edited.
