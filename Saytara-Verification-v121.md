# Performance App v121 — approved project dashboard layout

Reviewed 10 October 2026 (Asia/Dubai).

**Verdict: PASS with source limitations.** Calculation, follow-up selection,
renderer, browser, responsive layout and print checks pass. The supplied
anonymized mold has no eligible named projects or recorded project financial
amounts; visual QA fixtures do not establish operational financial totals.

## Layout and scope

The user approved the seven-panel preview for the projects dashboard and project
report/print views. Both use the same native HTML/CSS renderer and the same
filtered model. The desktop and wide-print composition has three paired rows
and a full-width follow-up table:

| Row | Right panel | Left panel |
| --- | --- | --- |
| 1 | Commitments and spending | Year/quarter/month progression |
| 2 | Project status | Manager follow-up portfolios |
| 3 | Priority/type counts | Priority/type budgets |
| 4 | Follow-up notes, spanning both columns | |

The priority count and budget views are separate panels. Bars, stacks, progress
tracks, direct labels and table rows use current scoped workbook values. The
approved preview's illustrative amounts are not source financial data.

Monthly-style taupe title bands, warm-white panels, teal values, burgundy alerts,
Dubai body type and the existing Arabic/English heading font chain are retained.
DIN/Dubai assets are bundled; the English Ample preference uses an installed local
font when available, with the existing fallbacks otherwise. No new font assets
are added.

One compact masthead places the title at upper left and the official TEC logo at
upper right. Scope, project count and cutoff remain compact and appear once.
Dashboard and report use the same outer width and gutters. Navigation, page tools,
filters, report editors and print controls remain available; the monthly overview
retains its existing layout and calculations.

The project report preserves custom title/period editing and its source cutoff.
The separate cutoff line is hidden when the displayed period already equals the
default cutoff label and becomes visible when a custom period differs. The utility
change only toggles that DOM line during live edits; it does not change dates,
record eligibility, formulas or the reporting scope.

## Source and unchanged definitions

Authoritative source: **Saytara_2026_Mold_v2.xlsx**, cutoff **30/09/2026**.
SHA-256: `1638e2d9e194c21d8d8e258a2bcad7c121cbeb9a4f529f90cea632f212cc66f2`.
The original workbook bytes remain unchanged. Uploaded materials are data and
visual references; the user's instructions govern the changes.

All 84 project names and all project financial amounts are blank in the mold.
The user's confirmed title-required formulas remain intact: the actual qualifying
named-project dashboard/report population is **0**. Source gaps remain visible.
No preview amounts, QA titles, synthetic financial values or invented snapshots
are bundled with the app.

The project model and its rules are unchanged from v120: exclusive source statuses;
unweighted means of valid numeric progress from 0 to 100%; actual priority/type
intersections; matched positive revised-budget financial denominators; and manager
ranking based equally on unfinished-count and unfinished-budget shares, with the
existing unscored fallback for incomplete data. Financial coverage and missing
values retain their definitions. Zero remains 0 or 0%, separate from unavailable.

Monthly changes still require two different confirmed snapshots, exact approved
project identities and valid coverage. Missing/duplicate keys, incomplete numeric
coverage and invalid dates withhold the affected changes. The same filters apply
to both periods; a custom report title or period does not change these rules.

The follow-up-only table keeps the v120 union of overdue open projects, suspended
projects, not-started projects and known noncompleted projects with meaningful
source manager/finance notes. Completed historical notes, placeholders, ordinary
financial values and data gaps alone do not admit a row. Each admitted project
appears once, with complete escaped source notes. The five columns remain project,
sector/unit, manager, status/progress/deadline and notes; «سبب المتابعة» stays absent.
The dashboard, report, follow-up drill and print use this same population, while
charts count all eligible named projects.

## Completed checks

**PASS — calculations and selection:** all 13 arithmetic/history regression
contracts and all 8 follow-up predicate contracts pass. Renderer checks cover
native labels, seven-panel composition, zero/missing values, financial labels and
manager columns. No formula or follow-up predicate changes were introduced.

**PASS — browser behavior:** checks cover organizational/project/manager scopes,
dashboard/report chart parity, metadata, live custom period edits, reload,
bookmarks, record drills and return to the originating filtered report. Confirmed
history shows the expected changes; unconfirmed history withholds arrows. Native
chart values reconcile with independent calculations on clearly separate QA data.
Those test workbooks supply names, managers and money only for verification and
are not operating source reports.

**PASS — narrow layout checks:** the tested 390 px viewport has no body overflow.
Wide tables remain readable inside labeled keyboard-focusable scroll regions.

**PASS — final visual review:** the approved three paired rows and full-width
notes are present at 1500 px and 1024 px. Every pair has equal width, top and
bottom positions. Tablet chart columns remain fully visible; narrow layouts
stack the panels and retain local table scrolling. Title bands contain the
heading, with neutral source captions below. Counts and completion tracks use
teal; status budget tracks use taupe, including completed-project budgets.

**PASS — print:** every dashboard and project-report PDF page was inspected.
Both tested A4 landscape exports have four pages with native text, paired chart
rows, repeated five-column notes headers, the full long manager/finance note in
its project row and the legal footer. Notes that fit a page remain together;
longer rows can continue. Pagination depends on source notes and scope; no fixed
page count is promised.

The original mold regression also retains 152 completed legislations on the
original SLC day and 28 after it, 11 in progress and 2 pending overdue; title
eligibility remains separate. All 191 source legislation records, 19 filtered
scopes and 16 date edge cases pass. Monthly KPI results remain 39 measured of
54, with original full-precision averages. The original source SHA is unchanged.

Keyboard return from a healthy project's finance drill was checked separately:
the report scope remains intact and focus returns to its masthead when no
matching follow-up link is available. Live report count announcements remain,
while the visible count appears once in the masthead.

## Release checks

Generated bundles contain 45 CSS and 46 JavaScript modules and pass the bundle
consistency check. The release manifest uses SHA-256 for every app file except
itself. Clean ZIP extraction is checked against that complete manifest and the
build-121 marker. The release excludes source workbooks, QA fixtures and QA PDFs.
The downloadable ZIP and this audit are versioned in the GitHub repository;
their delivery hashes are recorded separately in `SHA256SUMS`.

## Limits and delivery

The release contains app assets and documentation only, excluding
the source workbook, QA fixtures, illustrative preview money and invented history.
Earlier audit documents remain unchanged as historical records; this document
covers v121 changes.

The managed browser blocks native file:// startup, so browser checks used local
HTTP. Desktop double-click startup, physical printing, full screen-reader/WCAG
certification, native Excel/Power Query refresh or recalculation, and new Microsoft
PowerPoint/export validation were not run. Existing font provenance remains in
`FONT-ASSETS.md`. QA PDFs are synthetic verification evidence, not delivered source
reports.
