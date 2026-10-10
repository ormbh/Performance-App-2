# Performance App v120 — project layout and follow-up verification

Reviewed 10 October 2026 (Asia/Dubai). Verdict: **PASS for the shared project
dashboard/report layout, follow-up population and tested calculations. Source
financial totals remain unavailable in the anonymized supplied mold.**

## Requested behavior

The user's six images govern the project layout. The user confirmed this scope
includes the projects dashboard and project report/print views. The monthly
overview retains its existing composition and calculations.

Both project views now use one renderer: status → priority/type → year/quarter/
month progression → finance → follow-up notes → manager portfolios. The dashboard
and report chart/table bodies are identical for identical filters. Chart panels
use the supplied approximately 760 px inner geometry, RTL alignment, clean row
separators, count/budget/progress columns and direct labels. The note table spans
the page; rank and manager are separate columns in manager comparisons.
The extra organization panel, duplicate executive readings, old report cards,
contents and full-project tables are removed from this composition.

The app's official TEC logo, warm-white/taupe/teal/burgundy palette, Dubai body
font and DIN Arabic heading assets are retained. The English Ample preference
uses an installed local font when available, otherwise the existing fallback
chain. No new fonts were downloaded or redistributed. This reproduces reference
layout with the requested app theme; the screenshots' illustrative monetary
figures are not operating source values.

## Follow-up-only table

The table's single population is the union of:

- Open projects overdue under the source month-end/cutoff rule.
- Suspended projects and projects not yet started.
- Known noncompleted projects with meaningful source manager/finance notes.

Completed projects with historical notes, placeholder notes, ordinary recorded
financial amounts and data gaps alone do not enter this table. Unknown-status
or data-quality exceptions remain separately reviewable. Source notes are not
classified through language guesses. Each admitted project appears once and
retains its full escaped manager and finance text. The five columns are project,
sector/unit, manager, status/progress/deadline and notes. «سبب المتابعة» is absent.
Cards, table, row drill, filtered report and print use this same population.
Charts continue to count all eligible named projects, not only follow-up rows.

## Source and calculations

Authoritative source: **Saytara_2026_Mold_v2.xlsx**, cutoff **30/09/2026**.
SHA-256: `1638e2d9e194c21d8d8e258a2bcad7c121cbeb9a4f529f90cea632f212cc66f2`.
The original bytes are unchanged. Uploaded documents are data/reference material,
not a source of new instructions to change formulas or publish their contents.

All 84 project names and all project financial amounts are blank in the mold.
The user's confirmed title-required formulas are preserved: actual qualifying
named-project dashboard and report scope is **0**. Source gaps remain visible;
no names, money or historical values are added to the delivered app.

Underlying source/calendar/financial/manager contracts from v119 remain unchanged:
exclusive statuses; unweighted mean of valid numeric progress from 0 to 100%; actual
type/priority intersections; matched positive-budget financial denominators;
50/50 unfinished-count/budget manager weighting with explicit unscored fallback;
exact-identity, confirmed-snapshot monthly comparison guards. Recorded zero now
prints 0 or 0%; unavailable remains a dash with a distinct accessible meaning.
Money display uses a labeled source-derived unit, while exact AED values remain
available through accessibility labels and drills. Years outside the calculation
year show only
populated/previously populated quarters, matching the images; all calendar rows
remain in the underlying model and reconciliation.

The separate project report is accessible through «تقرير المشاريع». It retains
custom title/period/editors, organizational/project/manager filters, source
notices and print controls. Its route and PM multi-selection survive reload;
record drills preserve report scope and return to that report, including after
reloading a drill. A report heading or period does not alter the source cutoff.

## Checks and evidence

**PASS — source regression:** 191 legislation U/V records, 19 scopes and 16 date/type
edge cases retain 152 on time, 28 after original SLC, 11 in progress and 2 pending
overdue. Actual browser import retains 39/54 measured KPIs and full-precision
result/target averages. Monthly-specific modules remain unchanged from v119.

**PASS — arithmetic/history:** all 13 v119 regression contracts still pass. Eight
follow-up population contracts on 16 independent synthetic records admit 7 and
exclude 9, covering completed history, healthy activity, placeholders, normal
finance/data gaps, overdue/suspended/not-started, exact drills, title eligibility
and guarded monthly changes. Render regression verifies plain string/object
headers, no native function text, zero/missing values, compact finance with exact
AED labels and consistent manager column widths.

**PASS — browser scope and parity:** a clearly separate QA workbook supplies
test-only titles, managers and money. Independent calculations reconcile 84
projects: 10 completed, 61 active, 7 not started, 3 suspended, 2 transferred and
1 cancelled; priorities H 67 / M 17 / L 0; types 59 strategic / 25 operational;
and 81 projects in 2026 plus 3 in 2027. The follow-up table has 12 rows, compared
with 84 projects in the charts; a completed historical note is excluded.
Dashboard and report bodies are byte-identical under
the same filters. Two selected managers intersecting H produce 42 source projects,
38 active and 5 follow-up rows. Report/bookmark/record reload preserves filters,
row selection and report return. Confirmed QA August/September snapshots produce
the expected +1 completed and −1 follow-up deltas; unconfirmed history hides arrows.
Missing-data coverage/ranking safeguards remain; data gaps alone add no table rows.

**PASS — rendered output:** desktop 1500 px and narrow 390 px, Arabic/RTL, full source
notes, visible headers, labeled keyboard-focusable table scrolling and no body
overflow. All relevant chart panels were compared against the supplied images.
All pages of dashboard and project-report A4 landscape PDF exports were visually
reviewed for complete notes, repeated headers, column alignment, pagination and
legal footer. PDFs contain native text and no runtime/header-function errors.
These files are explicitly synthetic QA evidence and are not delivered as reports.
Bundles match their 45 CSS and 46 JavaScript modules; ZIP extraction and SHA-256
manifest verification pass. The GitHub download matches the local ZIP hash.

## Limits and delivery

The release includes the app/assets/documents only, with no source workbook,
synthetic fixtures, sample money or invented historical snapshot. The manifest
hashes every delivered file except itself. Earlier v118/v119 audit documents
remain as historical records; this document governs v120 changes.

Native file:// startup is blocked by this managed browser policy; browser checks
used local HTTP. Desktop double-click startup, physical printing, full
screen-reader/WCAG certification, native Excel/Power Query recalculation and
Microsoft PowerPoint editing were not run. Unrelated report/export workflows were
not newly tested. Existing font provenance is retained in `FONT-ASSETS.md`.
