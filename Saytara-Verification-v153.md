# Performance App v153 — agenda chart verification

## Implemented

The agenda page and native PDF use the approved vertical quarter-count chart. The visible columns show quarter totals and disjoint source status segments on one shared, zero-based, whole-count scale. Percentages and selected-quarter ratio lines are omitted. The original status-definition legend remains below the chart.

## Validation scope

Source: **ILLUSTRATIVE-monthly-preview.xlsx**, an illustrative workbook with cutoff **30 September 2026**. SHA-256: `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. The fixed values in the earlier illustration are not used by the app.

- Baseline and candidate source records, category totals, status counts and quarter groups are reconciled under the same all/entity/approved-only/emerging-only/empty filters.
- Empty cohorts hide; populated categories use the available layout. Active quarters remain aligned across categories. Zero intersections remain dashes. Unknown/undated records retain their source meaning.
- The scale follows the largest quarter total, not the largest individual status segment. Synthetic scenarios cover late records, an undated fifth group, a third category, a single topic and larger totals. Synthetic cases are recorded separately from fixture results.
- Screen checks cover desktop, tablet and phone widths, keyboard selection, click after rerender, selected status counts/colors, readable labels and an expandable count table. Long undated labels are included in SVG text-bound checks.
- Native A4 landscape PDF checks reconcile chart text and source detail records; charts and the full definition legend share physical page 2. Cover imagery, centered cover text, entity/period, continuation tables and numbering from physical page 2 are retained.
- Chart marks remain vector shapes with selectable text; no chart screenshots are embedded. Axis and quarter labels use 9pt and quarter counts 16pt in the tested one/two/three-category PDF compositions. Interactive selection feedback and disclosure controls are excluded from the PDF.
- Bundles are checked against source and JavaScript syntax is checked. The packaged ZIP is checked for CRC and verified against all manifest hashes after extraction.

## Limits

This is focused agenda-chart validation, not a new audit of every app page or a new analysis of a production workbook. Screen-reader certification and native mobile devices were not tested. Browser validation used Chromium and local assets; offline export was checked after local assets were primed. Models, workbook matching and unrelated report logic are unchanged from v152.

See the accompanying release evidence and screen/PDF previews for the actual checked output.
