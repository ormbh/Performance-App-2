# Performance App v119 — verification

Updated 10 October 2026. Verdict: **PASS for the implemented projects dashboard,
source guards, tested calculations and browser layouts. Actual financial amounts
cannot be reconciled from the anonymized supplied mold.**

## Changes

The projects dashboard now contains the requested combined status/count/budget/
mean-progress table, priority-by-type count and budget stacks, actual year/quarter/
month progression, three financial allocation/spending/work-value panels and
manager follow-up portfolios. It uses the monthly dashboard's existing TEC palette
and Dubai/DIN font assets. English Ample is an existing local-font preference,
with the same fallback chain; no new font download or redistribution was added.
The derived «سبب المتابعة» column was removed from dashboard and follow-up views.
Complete source manager/finance notes remain visible and escaped.

## Source and scope

Source: **Saytara_2026_Mold_v2.xlsx**, cutoff **30/09/2026**.
SHA-256: `1638e2d9e194c21d8d8e258a2bcad7c121cbeb9a4f529f90cea632f212cc66f2`.
The original bytes are unchanged. Workbook text is treated as source data, not as
new instructions to alter formulas or publish data.

All84 project names and all project financial amounts are blank in this mold.
The user's confirmed choice to preserve title-required formulas remains in force:
the actual named-project dashboard population is **0**. The app exposes missing
names for review; it does not invent titles or money to reproduce screenshots.
The unnamed source rows contain statuses10 completed,61 active,7 not started,
3 suspended,2 transferred and1 cancelled. Their priority/type intersections are
H67 (51 strategic,16 operational), M17 (8 strategic,9 operational), L0; types59/25.
Dates are81 in2026 (June1, October1, December79) and3 in February2027.
These describe the supplied rows, not84 qualifying named projects.

## Metric definitions

- Each project uses the existing nonblank-title eligibility and current filters.
  Source-status groups are exclusive; mean progress is the unweighted mean of
  valid numeric percentages0–100, including recorded zero.
- Counts and monetary values use separate fixed scales. Each priority stack uses
  its actual type intersections. Calendar membership follows the calculated
  month-end deadline; explicit dates retain their year, while month-only values
  follow the workbook reference year. Undated rows are separate. Quarter means
  use project percentages rather than averaging monthly averages.
- Financial panels use one matched cohort per panel: positive revised budget
  plus nonnegative numeric committed/non-committed, invoice spending, or work value.
  Every numerator and denominator uses that panel's same projects. Remaining
  invoice/work value equals revised budget minus the recorded value. Missing,
  negative, inconsistent or over-budget inputs remain visible; invalid chart
  proportions are not normalized to hide the discrepancy. Coverage and exclusions
  are shown. Work value, invoice spending and mean physical progress are separate.
- Manager rank is50% of unfinished-project-count share plus50% of unfinished-
  budget share among valid recorded managers. Completed status determines the
  completed project/budget cohort. Unknown statuses and unassigned managers remain
  reviewable outside ranking. Weighted ranking requires complete nonnegative
  budgets, resolved statuses and positive denominators. Otherwise the app explicitly
  shows an unscored order by unfinished count. This is portfolio size, not evidence
  of stalled progress. Fully completed portfolios are shown separately.
- Arrows require two confirmed, different monthly snapshots and approved exact
  identities. Missing/duplicate identities suppress them. The same filters apply
  to both snapshots. Incomplete financial/progress coverage suppresses those
  deltas. Percentage changes use percentage points. Date-based deltas require
  each cutoff to match its confirmed snapshot. Prior absence is not invented data.

## Verification evidence

**Source regression PASS:**191 legislation U/V rows,19 organizational scopes and
16 date/type edge cases retain152 on time,28 completed after original SLC,
11 in progress and2 pending overdue. The KPI source retains54 total,39 measured
and full-precision averages. Project title guards remain unchanged.

**Arithmetic PASS:**13 independent synthetic scenarios exercise status budgets/
means/drills; actual2025/2026/2027 calendar membership and undated reconciliation;
priority/type intersections including zero L; financial paired denominators,
missing/zero/negative inputs and per-record overspending; exact50/50 manager scores,
invalid-manager exclusion and fallback; guarded history including prior-only
months/managers, duplicate identities and unconfirmed snapshots.

**Browser integration PASS:** a separate, explicitly synthetic workbook fills QA
titles, managers and financial values while retaining source statuses/dates.
Independent workbook calculations reconcile84 project rows and every status,
priority/type intersection, year/quarter/month and financial panel. Matched ratios
are80% allocation,35% invoice spending and39.499141999142005% work value for this
QA fixture only. They are not operating results. A missing-data variant confirms
82/84 allocation coverage,83/84 invoice/work coverage,83/84 progress coverage,
one undated row, one unassigned manager and one unknown status. Weighted ranking
and incomplete financial/progress deltas are withheld. An active drill returns61
matching rows; multi-manager union intersects high-priority filters consistently.
Confirmed August/September QA snapshots produce the expected completed/progress/
money deltas; unconfirmed or duplicate-identity snapshots hide arrows.

**Layout PASS:** desktop1500px, narrow390px, Arabic RTL labels and full escaped
notes. Narrow tables retain headers and scroll within keyboard-focusable regions
without body overflow. Browser exports contain native text, repeated table headers,
the complete long-note fixture and the legal footer. All pages of the ten-page A4
and A3-scaled synthetic exports were visually reviewed. Export page count depends
on source rows and notes; these PDFs are QA evidence and are not bundled. No browser
runtime errors were recorded. Bundles match45 CSS and46 JavaScript source modules.

## Limits and delivery

The ZIP contains the app, assets and verification documents only. It contains no
uploaded workbook, synthetic fixtures, operational financial values or invented
previous snapshot. `release-manifest.json` records SHA-256 for every delivered
file except itself. The GitHub ZIP is checked against its local SHA-256.

Native file:// navigation is blocked by the managed browser policy; browser checks
used local HTTP. Double-click startup on a user's desktop, physical printing,
full screen-reader certification, native Microsoft Excel/Power Query recalculation
and Microsoft PowerPoint editing were not run. Font licensing provenance is retained
in `FONT-ASSETS.md`; no new license certification is claimed. Unrelated exports
and app workflows were not newly retested. v118 verification remains available as
the historical record of the legislation/requester-comment correction.
