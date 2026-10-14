# محفظة المشاريع — review proposal, 15 October 2026

This is an illustration for review. It does not change the v166 application or release ZIP. The illustrations were rendered as HTML with the approved local TEC fonts and official logo, rather than generated as chart images.

## Data scope and limitations

All displayed values come from the anonymized **ILLUSTRATIVE-monthly-preview.xlsx** fixture and the independently reconciled aggregate checks in `evidence.json`. They are illustrative values, not figures from the currently uploaded report. The current available source attachment does not establish an eligible populated budget portfolio: its project-title, manager and financial fields are blank. No missing attachment values were filled with fixture data.

The fixture has 84 named budget-portfolio projects: 10 completed, 61 active, 7 not started, 3 frozen, 2 transferred and 1 cancelled. There are no overdue budget projects at its 30 September 2026 cutoff. Its six follow-up records are the frozen, cancelled and transferred projects. The eight follow-up records shown in the monthly example also include two late records in another portfolio; they must not be imported into this page.

Its approved budget is 58,275,000 AED. Allocated 46,620,000 + unallocated 11,655,000 reconcile to that budget. Invoice spending is 20,396,250 (35%). Recorded work value is 23,018,125 (39.5%). Completed-project count share is 10 / 84 = 11.9%, whereas mean recorded project progress is 38.9% over 84 records. These are distinct measures and remain separately labeled.

Manager names and project titles in the plates are anonymized fixture text. Manager ranking preserves the existing 50% unfinished-count share / 50% unfinished-budget share calculation, source population and order. The proposal does not equate ranking with performance, infer completion from progress, infer a recorded status from a blank, or invent historical changes.

## Full-page composition

1. One common report title, logo and source-derived reporting period. Existing report options and PDF action remain available.
2. Eight direct labeled filter fields: sector, unit, concerned entity, project type, priority, finish quarter, status and project manager. Their unions, intersections, dependent options and exact source-record scope remain unchanged.
3. Compact contents links in the same order as the rendered page.
4. Overall project total at the top, with a compact row distinguishing completed count, completed-project share, mean recorded progress and follow-up count. The five separate summary cards are not repeated.
5. **Budget physically right / quarter-and-month schedule physically left.** Financial amounts use full values in AED, maintaining source-defined denominator eligibility. Invoice spending, allocations and work value retain distinct roles.
6. Source-status table with separate comparable count and budget bars and a distinct recorded-progress column. Do not stack lateness as an additional source-status population.
7. A compact detailed status legend below the charts. It preserves the established fill/ink/border palette, including frozen, transferred and cancelled. Lateness is described as a derived follow-up condition that overlaps recorded status.
8. Manager follow-up ranking, preserving the existing top-three weighted ranking and exact count and budget ratios.
9. Priority × type counts and budgets as separate charts with their own units and scales. Actual intersections are used. Empty priority groups are hidden.
10. Full operational follow-up table with all six example rows and complete recorded notes. Missing notes remain blank and zero progress is a dash.
11. An explicit link to the main project-list view. No new special-project-style narrative appendix or detailed-update cards are introduced.

## Proposed chart change requiring review

The current schedule displays each month as a 100% status stack. Consequently a month with one project is as wide as a month with 79 projects. The proposal changes this visual encoding to **count-scaled stacked month bars**, using one zero-to-79 count scale across all displayed years. The largest month contains 79 projects; a one-project month has exactly 1/79 of that length. The actual year/quarter/month populations do not change.

Quarter totals remain explicit: 2026 Q2 = 1 and Q4 = 80; 2027 Q1 = 3. The year totals remain 81 and 3. Empty quarter groups are omitted. The mean recorded completion percentage remains in a separate column; it is not used as bar geometry and is not printed under a quarter as a count-distribution percentage.

Counts fit inside a segment when there is sufficient space. Small segments keep their true width and do not receive enlarged or overlapping labels. Exact aggregate status counts remain visible beneath the schedule; an implementation must preserve the existing exact-record drilldowns and accessible underlying monthly values.

Month and priority count totals sit at the actual bar ends. In-bar figures remain at least 16px on the phone illustration and are suppressed only when measured text plus padding does not fit. Frozen and other small count rows use either the in-bar label or its outside label, never both. If an eligible group contains an unclassified status, implementation must preserve it as a neutral residual segment and in the total; the normal fixture contains none, so the preview does not fabricate an unknown row.

## Tables and links

The shared leading RTL sequence is:

**م ← المشروع ← الجهة المعنية ← الحالة ← نسبة الإنجاز ← موعد الإنجاز**

The operational follow-up table appends **ملاحظات**. Its project-manager field remains visibly associated with the project identity, retaining the operational follow-up function without adding a separate narrow PM column. Concerned entity remains the General Secretariat; sector and unit are separately labeled context and are not renamed as entity. A blank unit stays blank.

The main-list review plate shows the first six actual fixture rows in source order, explicitly labeled as an illustration of the larger 84-project list. Type and priority appear beneath the project identity. Existing populated manager, financial and other record fields remain available through the existing record view. The illustration does not add a table-customization feature or imply the six-row excerpt is the entire report.

Contents and return links follow section order. The preview uses real local anchors for review navigation. Filter controls, report actions and row drilldowns are visual placeholders here; production behavior is not claimed to have been implemented or tested in this illustration.

## Shared presentation

- Approved TEC DIN / DIN LT / Dubai fonts and existing exact color tokens; Paper panels, Linen table headings, Sand boundaries and restrained spacing.
- Completed plain labels and counts use green; other ordinary status text remains Ink. Badge and chart-segment ink follows the approved fill contrast rules.
- True numeric zero displays **–**; missing values remain empty. No source filename, circular progress indicator, unsupported ready-status row or fabricated historical arrow appears.
- Financial and recorded-progress figures stay beneath their own labels. The overall total remains deliberately at the upper left.
- Desktop keeps paired panels at full width. The optional mobile plate demonstrates reflow and contained table scrolling; it is a review illustration, not a certification of production mobile accessibility.

## Deliverables and verification

- `review.html`: complete review composition plus the separate main-list plate.
- `portfolio-full-page-proposal.png`: complete desktop page.
- `portfolio-overview-proposal.png`: title, controls, filters, total, budget and schedule.
- `portfolio-charts-proposal.png`: budget/schedule detail at readable size.
- `portfolio-status-manager-proposal.png`: status table, detailed legend and manager ranking.
- `portfolio-priority-proposal.png`: separate priority count and budget charts.
- `portfolio-followup-table-proposal.png`: all six follow-up records and explicit main-list link.
- `portfolio-main-list-proposal.png`: shared table order in the main-list view.
- `portfolio-mobile-proposal.png`: optional responsive composition.
- `evidence.json`: source scope, scales, roles and rendering checks.

All standalone plates carry an explicit illustrative-data review notice. The rendered preview has been checked for approved font loading, source-grounded totals, shared table sequence, blank-note preservation, zero-as-dash behavior, proportional chart widths, physical budget/schedule placement and viewport overflow at 1560, 390 and 320 pixels. This task does not implement an app change or claim a new production PDF export.
