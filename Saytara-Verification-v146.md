# Performance App v146 verification

Date: 13 October 2026. Scope: approved agenda page and native offline PDF. Verdict: **PASS within the tested scope**.

## Applied changes

The agenda uses the approved status-row / quarter-column matrix with a shared legend. Zero counts display as **–** while numeric zero and accessible zero text remain intact. Only completed and late status names use Green **#01831E** and Red **#C00000**; other names use Ink. Established bar/legend swatches remain. Percentages and duplicate bottom-left grand totals are removed; headline, status and quarter totals remain.

Statuses and quarters absent across the filtered scope hide. Shared rows and columns remain aligned across approved/emerging cohorts, including dash intersections. Late is taken from recorded source status. Source undated groups remain distinct. No date-derived late classification is introduced.

The page uses shared TEC spacing, responsive filters and editable report metadata. A selected entity appears beneath the title. Agenda PDF uses A4 landscape, 10mm margins and copyright/page footer only. Title, entity and reporting period appear only on page one, with both chart matrices together. Table column headings repeat. Topic/entity columns are wider; the source-notes appendix and links are removed from the agenda page/PDF. Existing record notes and editorial content remain. The PowerPoint pipeline is unchanged.

## Executed validation

- Independent verification passed **3,596 assertions**, covering **35 screen states** (7 scopes at 1440, 1024, 768, 390 and 320px) and **7 actual toolbar PDF downloads**. All, single entity, multiple entities, sparse, empty, emerging-only and synthetic late/undated scopes were exercised. No runtime errors or external internet requests occurred.
- Counts and exact record keys reconcile with the unchanged v145 agenda model. All 162 topic cells across the seven PDF scenarios match the source, using full-page glyph extraction and cell geometry. An initial clipped-extraction artifact was resolved in the verification harness; full-page PDF text was correct.
- Zero display, shared scale, filter-dependent visibility, label colors, legend order, status-header alignment, absence of duplicate totals and source appendix, and no document horizontal overflow were checked. Actual desktop/phone screenshots and rendered PDF pages were visually reviewed.
- Actual filter interactions covered first-selected +N, all/clear, single/multiple entity selections, phone disclosure, topic type, Escape/focus restoration and report metadata editing/reset.
- All seven PDFs have A4 landscape geometry, embedded fonts, selectable text, complete ordered source records and both charts on page one. Selected entity and period are absent from continuation mastheads; table headings and copyright/page footers remain. Representative fixture page counts are 14 for all 117 records, 4 for a 10-record entity, and 1 for empty scope; these are fixture results, not guarantees for other workbooks.
- Stress cases include five statuses plus an undated column, a 140-character title, long entity names, and a 3200-character Arabic row. Content is retained; long rows continue without text omission. Measured first-page overflow uses compact spacing while preserving fonts. Extreme metadata beyond the safe area gives a clear export error rather than clipping.
- True-offline PDF download succeeds after loading bundled local assets and disabling browser networking. Native Windows/file-origin cold launch was not tested: the managed browser blocks file://. Loopback HTTP was used for browser verification. Other browser engines and physical printing were not tested.
- Council/HH page plans and geometry match v145. Search toolbar PDFs match v145 in geometry, text and byte size; the monthly report remains a single continuous page. This is a focused regression check, not a fresh audit of every app feature or accessibility certification.
- Generated bundles match their 71 CSS and 52 JavaScript inputs; JavaScript syntax passes. ZIP membership, CRC, per-file hashes and fresh extraction are verified during packaging. Extracted-runtime smoke evidence is published separately.

## Source and limits

Tests use the frozen illustrative workbook dated 30/09/2026, SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. Synthetic cases modify an isolated in-memory copy only. No operational workbook was supplied or bundled. Preview records and counts are illustrative. Prior release documents retain their historical scope.

## Tested runtime hashes

| Asset | SHA-256 |
| --- | --- |
| `assets/js/app-bundle.js` | `a0396df8c1a17b92047b5c078d0254e0682ee93c876ef899fa055e104cd2079e` |
| `assets/css/app-bundle.css` | `3c9ec3dcb89e45e1ceedeb8f29976514e91c7e17c0cebf73df28d58960f4fb34` |
| `assets/css/print-measure-bundle.css` | `899ddcf543018ffdb83988bff1caac88dc88a516f5685863f525c2f04fe12c49` |
