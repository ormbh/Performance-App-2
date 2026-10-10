# Performance App v122 — projects dashboard review fixes

Reviewed 10 October 2026 (Asia/Dubai).

**Verdict: PASS with source limitations.** The calculation, source eligibility,
follow-up, browser, keyboard and responsive checks pass. The source workbook has
no eligible named projects or recorded project financial amounts; populated QA
fixtures do not establish operational totals.

## Changes and preserved layout

The projects dashboard and project report use the same scoped summary and native
seven-area renderer. The approved equal-width paired grid remains:

| Row | Right panel | Left panel |
| --- | --- | --- |
| 1 | Commitments and spending | Year/quarter/month progression |
| 2 | Project status | Manager follow-up portfolios |
| 3 | Priority/type counts | Priority/type budgets |
| 4 | Follow-up notes across both columns | |

A compact five-metric summary shows eligible project count, completed status,
follow-up count, recorded revised budget in millions of AED, and unweighted mean
recorded progress. Summary buttons drill into the same scoped records. Screen
headline totals are 24–28 px; section headings are 24 px. The monthly dashboard's
existing TEC palette, logo, Dubai/DIN fonts and font fallbacks remain. No new font
assets were added.

Changes retain their numerical direction and gain metric-specific tone: increases
in completed count or recorded progress are favorable, decreases in follow-up
count are favorable, and other counts, monetary amounts and financial composition
ratios are neutral. This avoids implying that greater expenditure or a smaller
active population is automatically better or worse. Unavailable history remains
withheld.

Known zero is explicit in the project masthead, count announcement, summary,
record progress and financial details.
The original untitled mold shows a source-name explanation and a data-review
recovery action. A populated source with no filter matches offers filter reset.
Missing numeric data remains unavailable and is never silently replaced by zero.

The status view labels mean recorded progress separately from completed-project
share; count and budget scales are labelled. Monthly status stacks describe
within-month composition totaling 100%, with separate actual counts. Financial
work value is labelled «قيمة الأعمال المنجزة», distinct from invoice expenditure.
Manager budget bars describe budgets of completed projects, not expenditure.

The follow-up title is «المشاريع التي تتطلب المتابعة», with visible eligibility
criteria and the same five columns. Phone rows become vertically labelled cards
with complete source notes. Native table roles and visually hidden column headers
remain available. Other wide tables remain in keyboard-focusable local scroll
regions; hints appear only when actual horizontal overflow is measured. Tiny
proportional stack segments are visual spans; equivalent drills remain on their
explicit labels. Tested chart controls are at least 24 px on desktop and 44 px on
phone/coarse-pointer layouts. These checks are not full accessibility certification.

Project-only print settings offer A4/A3 landscape and comfortable/compact spacing.
The native dialog supports keyboard opening, Escape, focus return, reset and
session preferences. Paper/spacing changes preserve source scope and full notes;
compact reduces spacing without reducing note text size. Monthly layout and its
separate print settings remain unchanged.

## Source and calculation contracts

Authoritative source: **Saytara_2026_Mold_v2.xlsx**, cutoff **30/09/2026**.
SHA-256: `1638e2d9e194c21d8d8e258a2bcad7c121cbeb9a4f529f90cea632f212cc66f2`.
The original workbook bytes are unchanged. Attached materials are data and visual
references; the user's instructions govern the work.

All 84 project names and all project financial amounts are blank in this mold.
The user's confirmed title-required formulas remain intact: the actual eligible
project dashboard/report population is **0**. No names, money or history were
invented to populate it. All 15 JavaScript model files, monthly-specific modules,
and the entire project report calculation/eligibility prefix are byte-identical
to v121.

Preserved definitions include exact source status counts, unweighted means of
valid numeric progress, actual type/priority intersections, matched positive
revised-budget financial denominators, incomplete-coverage guards, and manager
ranking equally based on unfinished count and unfinished budget shares. Historical
changes require two different confirmed snapshots and exact approved unique keys;
partial values, ambiguous identity and unconfirmed dates withhold affected deltas.

The follow-up population remains the union of overdue open, suspended,
not-started, and known noncompleted projects with meaningful source notes. Each
qualifies once. Completed historical notes, whole placeholders, ordinary financial
values and gaps alone do not qualify. Charts retain all eligible named projects;
the table and its drill use the exact follow-up subset. Escaped manager and finance
notes are complete. The removed reason column stays absent. Monthly follow-up has
its own preserved definition; its population is not forced to match this table.

## Completed verification

- **13 arithmetic/history contracts, 8 follow-up contracts, 11 existing renderer
  cases and 12 new semantic renderer cases pass.** Tests cover reverse deltas,
  financial neutrality, preserved selection IDs/stack geometry, guarded history,
  zero/missing values and complete source notes.
- **Original workbook regression passes:** 191 legislation rows, 19 scopes and 16
  date edges retain 152 on original SLC day / 28 after, 11 in progress and 2 pending
  overdue. Monthly KPI results remain 39 measured of 54 with full precision
  averages. Title eligibility remains separate.
- **Independent browser checks pass:** source-title recovery, filter-reset recovery,
  summary/table/model reconciliation, exact full notes, dashboard/report renderer
  parity, keyboard drills, scoped report return, hash reload, custom report period
  versus source cutoff, dialog preferences/focus and monthly isolation.
- **Independent saved-workbook QA oracle:** 84 synthetic named records / 12 admitted
  follow-ups; two-manager union intersected with H gives 42 records / 38 active /
  5 follow-ups. Missing money/progress retains partial coverage and suppresses
  unsupported ranks. These workbooks are test-only and are not included in release.
- **Responsive checks pass at 1500, 1024, 768 and 390 px:** paired row tops, bottoms
  and widths remain equal on wide screens; full-width notes remain below them.
  Narrow screens have no body overflow; hints follow actual overflow; phone cards
  retain all source text. Independent target-size and semantic-color probes pass.

**PASS — final print review:** six paper/density combinations were checked,
including both A4 modes in the dashboard and report and both A3 modes in the
dashboard. Native page sizes, page-one Q4/2027 calendar and every admitted project
ID pass. All generated pages were visually inspected; the affected A4 comfortable
report was regenerated and all four final pages inspected after correcting the
method-only page. Both A4 dashboard/report modes produce four pages on this QA
fixture; both A3 dashboard modes produce three. Full notes remain 9pt with repeated
five-column headers and legal footer. The source definition remains below the
table. The phone print-dialog close is 44 × 44 px. No standalone summary cover or
method-only page remains in these checked final outputs.

**PASS — focused zero/missing UI:** known source 0% remains explicit in both
follow-up and standard record drills, numeric zero work value prints as 0 in
financial details, missing revised budget remains «غير مسجل», and a QA-only
all-zero scope shows 0 / 0% in the summary. No source workbook was edited.

## Release and limits

Generated bundles contain **46 CSS and 47 JavaScript** source modules and pass
bundle consistency and JavaScript syntax checks. The release manifest uses SHA-256
for each app file except itself. Clean ZIP extraction is checked against the full
file set, hashes, build-122 marker and rebuilt bundle consistency. Source workbooks,
synthetic QA workbooks, QA PDFs and browser evidence are excluded. The ZIP and audit
are versioned on GitHub; delivery hashes are in `SHA256SUMS`.

Earlier audit documents remain unchanged as historical records. This document
covers v122. Managed browser checks used local HTTP; native file:// startup is
blocked by this browser environment. Desktop double-click startup, physical
printing, full screen-reader/WCAG certification, native Excel/Power Query refresh,
and new PowerPoint validation were not run. Existing font provenance remains in
`FONT-ASSETS.md`. Pagination varies with scope and note length; no fixed page count
is promised.
