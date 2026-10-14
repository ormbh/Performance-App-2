# Monthly-report illustration proposal

Preview stage only. No monthly runtime files were edited.

## Review images

- `monthly-overview-proposal.png`: first report portion, projects physically left and executive portfolios right. Shows the proposed corrected special-project grouping, agenda summary, explicit report links, direct segment counts, and compact common color legend.
- `monthly-detail-proposal.png`: continuation portion, preserving the approved budget order, quarterly counts, eligible council denominator, and independent strategy metrics.
- `monthly-legislation-approved-example.png`: the already approved legislation card, enlarged for review. The historical screenshot example of 183 total, 178 completed, 5 in progress, and 2 late is explicitly labeled outside the report card; these are not values from the loaded fixture.
- `index.html`: standalone editable HTML source for all three illustrations; embeds the approved DIN/Dubai fonts and TEC logo. The displayed controls and links are visual proposals, not connected application actions.

## What changes in this proposal

1. Preserve the existing monthly two-column composition, fonts, palette, report controls, totals, completion captions, and individual source denominators.
2. Apply the approved special-project classification consistently: leadership is explicit yes; all remaining records, including a blank leadership flag, form the TEC group. Fixture totals become leadership 24 + TEC 38 = 62. Within TEC, show 11 completed, 26 in progress (23 development + 3 review), and 1 neutral other, instead of treating the last record as active work. Completion is 11/38 = 28.9%. No historical change is fabricated for this changed cohort. The valid unchanged overall-total change of +7 is retained. All other valid source-history changes must retain their own metric eligibility during implementation; these review plates do not authorize deleting comparisons.
3. Match completed labels and values in Green, ready labels and values in Teal, and late in Red. Use the same effective label/number colors in screen and actual PDF, and place الإجمالي beneath the primary total in both formats (the current monthly PDF has placement and label-color differences). Neutral change arrows retain Taupe. Keep readable ink inside status bars, including Teal on Mist and Paper on Teal/Green.
4. Add readable counts inside the agenda and council status-distribution bars. Keep all directly labeled metric values visible. A very small council unclassified segment retains its separate visible count; its label is not squeezed inside.
5. Make a distinct, quiet report link visible at the bottom of each summary. In implementation these links should preserve the active scope and open the corresponding report, while count/status actions retain their exact matching-record drilldowns.
6. Use a compact shared color legend, with stable status appearance. The common palette does not equate portfolio-specific metric definitions. Its source-preserving order follows the approved monthly metric rank: late, completed, ready, work, other.
7. Preserve the already approved legislation card exactly in meaning: late nests under in-progress, is counted once, and is not a separate segment in the completion strip.

## Source and meaning

The first two images use only aggregates from `ILLUSTRATIVE-monthly-preview.xlsx`, with report cutoff 30 September 2026. They contain no real record titles or notes. The third image uses the separately approved user screenshot values, clearly identified as a reference example. Do not replace runtime values with any illustration constants.

- Agenda: 117 = 100 approved + 17 emerging; 43 completed + 16 ready + 58 in progress. Completion 43/117 = 36.8%.
- Special projects: 62 = 24 leadership + 38 TEC. Approved leadership logic is applied in the illustration. Completed 12 + 11 = 23; in-progress 12 + 26 = 38; other 1. Other remains included in the denominator and neutrally identified.
- Council: 70 eligible decisions = 38 completed + 31 in progress + 1 without an approved status. The 94 out-of-scope decisions are not folded into this card. Completion 38/70 = 54.3%.
- Budgeted projects: 84 total, including categories not in the existing headline metrics; the full denominator yields 10/84 = 11.9%. No rejected extra-status disclosure is introduced. Quarter values are 0, 1, 0, 80 for 2026, with the existing 3 projects in 2027 note.
- Strategy: 54 approved indicators, 39 measured. Result mean 83.2% uses the 39 measured results; target mean 87.8% uses 49 targets. The means are independent, and no invented attainment ratio is drawn.
- Budget: approved AED 58,275,000; invoice spending AED 20,396,250; allocated AED 46,620,000; unallocated AED 11,655,000. Spending is 35% and allocation 80% of approved budget; their bars retain distinct Teal/Taupe roles.
- Legislation reference example: 183 total, 178 completed, 5 in progress, including 2 late. Completion 178/183 = 97.3%. The real fixture monthly legislation values are 191 / 180 / 11 / 2 (94.2%) and are deliberately not substituted into this exact approved reference card.

The proposal focuses on summary presentation. Full follow-up table rows, comparison tooling, responsive states, and final PDF pagination remain future implementation/audit work, not functionality certified by these static images. The intended report order retains legislation before strategy; the enlarged separate legislation illustration is a review plate, not a reordered production section.

## Verification performed

Rendered in Chromium using the actual approved embedded font assets. All three complete compositions were visually inspected. No horizontal overflow; segment count labels fit within their bars; independent primary values and source denominators reconciled to the illustrative audit; approved exact status fills/ink checked. Preview controls are deliberately static. Rendering evidence is in `preview-verification.json` and `render-checks.json`.
