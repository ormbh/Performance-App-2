# v155 shared presentation audit

Approved scope: numeric metric zero displays as a dash; generated missing-value placeholders are empty; plain ready-status labels and figures use TEC Teal; filled teal badges/segments keep Paper ink. Data, calculations, identifiers and recorded notes remain unchanged.

## Implementation coverage

| Area | Applied boundary |
| --- | --- |
| Shared utilities | `presentationText` removes exact generated placeholders; `fieldDisplayText` formats only schema `num`, `pct`, `progress` cells. Existing `metricText` / `displayNumber` distinguish true zero from tiny positive values. |
| Shared UI | `statusTextColor` resolves Done Green, Late Red, Ready Teal and other plain Ink. Missing progress text is empty; zero geometry remains numeric. |
| Filters | Blank captions are visually empty; exact blank tokens remain selectable. The checkbox retains the accessible name `قيمة فارغة`; yes/no options remain literal. Closed trigger and scope summaries use the same presentation boundary. |
| Monthly dashboard / native monthly composition | Ready caption and figure Teal; zero completion captions have a dash without `%`; follow-up missing unit values empty. |
| Search / results | Zero progress, KPI and financial values use typed formatting, including optional result columns. Empty cells remain empty. Literal narrative notes bypass placeholder cleaning. |
| Generic detail | Known metric fields use typed formatting, missing field values empty, plain recorded status ink shared. Zero-measurement explanatory prose uses verbal `صفر بالمئة`. |
| Projects / PMO | Zero percentages use a dash; visible zero chart ticks use a dash; generated missing row labels are empty. PMO plain status labels/counts use the shared ink separately from segment fill. |
| Entity views / print | Empty generated values and dates remain empty; source-status labels/counts, current status and comparison status use shared ink. Typed changed metric fields keep the zero convention. |
| Comparison | Typed financial/progress/KPI values use the shared boundary; array structures and nonmetric fields remain literal. |
| Council / agenda UI | Plain status captions/counts and agenda definitions use `statusTextColor`. Generated missing field labels are empty. |
| Checks | Summary counts use metric formatting. Known typed source metric issue cells show a dash for zero; their raw text remains in the model, CSV, tooltip and `data-raw-value`. |
| Shared terminology | Generated count captions use `metricText` for zero. |

HH chart/card code, agenda chart geometry, native PDF/PPT export paths and app notifications are owned and verified by the respective task agents.

## Deliberate non-transformations

- `fmtN`, `fmtNum`, `fmtM` remain low-level formatters. Some callers use their output for raw source text, identifiers or geometry. Metric views opt into a display formatter; no global replacement is used.
- Raw workbook cells (`item.c`), cached source display strings (`item.t`), source identifiers, dates, years, boolean values, filter identities and numerical geometry retain their original values.
- Source issue text with unknown/ambiguous types or combined diagnostics remains literal. Only a known metric field whose issue value matches that field's cached source text is reformatted.
- Source notes, explanatory missing-data cohort actions and diagnostic prose retain their meaning. A sentence describing missing ownership is not treated as a blank ownership value.
- Accessible numeric values and descriptions may still say zero / صفر. HTML numerical attributes and bar widths remain `0` / `0%`.
- Unchanged comparison arrows remain suppressed. Existing positive-only count calls, page ordinals and source row references do not have a reachable metric zero.
- Native source exports and CSV are not rewritten with presentation dashes.

## Checks

- `check.js`: 14 focused cases pass, including true zero versus tiny nonzero values, zero-percent suffix suppression, unchanged numeric geometry, typed metric versus ID/date fields, literal narrative preservation, fallback arrays, shared plain/filled ink, and exact blank-filter selection.
- `browser_check.py`: six-page current-source smoke using the illustrative workbook. Injects current source modules after loading while the release bundle is being finalized; it is supplemental evidence, not the final integration bundle run.
- Browser inspection verifies computed monthly and entity Ready ink, generic detail Ready plain ink and Paper badge ink, zero detail metric text with unchanged source zero, all source `c` / `t` fields unchanged, and raw issue values retained.
- The independent integration agent verifies the final bundled application, source totals, responsive layouts and native PDF outputs separately.
