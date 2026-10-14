# Performance App v155 — independent scoped QA

**PASS: 263 focused checks.** No unresolved defects in this scope. Final evidence is indexed in `FINAL-EVIDENCE.json`.

Source: `ILLUSTRATIVE-monthly-preview.xlsx`, SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`, report cutoff 30 September 2026. This is the approved illustrative fixture, not a production workbook audit. Its bytes and all loaded source records remain unchanged. No Excel recalculation, Power Query refresh or historical-data reconstruction was performed.

## Verified behavior

- HH reconciles to 62 records: 24 leadership and 38 TEC, including the two blank leadership flags. TEC-only selection includes those blanks; sector/unit union and cross-field intersection preserve exact source keys.
- Leadership displays four populated sector rows; TEC displays six. Empty rows and empty cohorts disappear, and a lone cohort uses the available width. No labels appear below individual bars. Per-status totals and the detailed legend remain.
- Row totals sit eight pixels outside the actual bar endpoint. Segment lengths remain proportional. Readable numbers fit inside their true segments; underlying values are not changed to accommodate typography.
- Agenda remains 117 = 100 approved + 17 emerging. Approved statuses are Ready 10, Review 5, Development 51 and Done 34; emerging statuses are 6, 1, 1 and 9. Quarter/source keys and detail rows match the baseline.
- Agenda defaults to aggregate status totals. Hover/focus preserve totals; explicit click/Enter selects a quarter; Escape/outside click restores totals. Export after selection returns aggregate totals.
- Desktop and mobile checks cover 1440, 1100, 768, 390 and 320 pixels where applicable. Filtered HH mobile overflow was fixed and rechecked. The one-topic agenda case keeps totals and in-bar labels within the SVG.
- Missing HH progress cells are blank; displayed numeric zero uses a dash without changing source values. Monthly Ready labels/counts compute to Teal. Source filenames do not appear in HH cards or PDF pages.

## Actual native PDFs

- HH all scope: 72 pages. TEC only: 46 pages. The chart and detailed definitions fit together on physical page 2; the normal HH first block is 681.453 px within the 687.874 px content capacity.
- All 19 HH nonzero segment counts are visible, including seven single-count segments, at 14 pt. Measured text fits within the unmodified bars.
- Agenda all scope: 16 pages. Emerging-only selected entity: 4 pages. Chart and original definitions stay on physical page 2. Native exact count matrices follow so small segments remain fully auditable. Actual PDF matrix labels/positive values use Ready Teal and Done Green; zero dashes remain neutral.
- The paired agenda charts share identical viewBoxes, baselines and physical count scale (approximately 2.7393 px per source count in this fixture). In-bar counts retain 12 pt; compact axis/quarter labels are approximately 8.76 pt after shared headroom.
- All delivered-sample PDF pages were scanned for native text exceeding page bounds. Chart pages were visually inspected at full resolution; contact sheets and representative cards/details were reviewed. The cover has no footer, and every content-page counter excludes the cover.
- Chart pages use native vector marks and selectable text; no chart raster image is embedded.

## Scope and limitations

Browser checks used Chromium, locally served bundled assets, and a route that blocked all nonlocal network access. No external network request was made. This does not claim a cold `file://` run, mobile-device or screen-reader certification. PowerPoint structure/data verification is recorded separately by the export agent; native Office rendering or in-application editing was unavailable. This is a scoped presentation/export regression check, not a new audit of unrelated app calculations.

## Final evidence

- `ui-final3/evidence.json`: PASS 205 checks.
- `focused-final2/evidence.json`: PASS 7 checks.
- `hh-final/evidence.json`: PASS 19 checks.
- `agenda-final3/evidence.json`: PASS 17 checks.
- `agenda-final3/matrix-color-evidence.json`: PASS 6 checks.
- `footer-vector-evidence.json`: PASS 8 checks.
- `shared-scale-evidence.json`: PASS 1 checks.

UI/PDF verification bundle SHA-256: `549d2616a061351b55ea8d3c656b1490648ea21538375c184c37cff5b5f46886`.

An isolated subsequent PPTX-only bottom-left total-cell correction is covered by the export agent’s targeted follow-up; it does not modify the verified UI/PDF modules.
