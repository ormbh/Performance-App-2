# Agenda v146 — independent QA

**PASS.** Verified the final production bundle, not the earlier illustration. Runtime JS, screen CSS and print CSS hashes in `evidence.json` match the implementation reviewed.

## Source and scope

- Source: `ILLUSTRATIVE-monthly-preview.xlsx`; cutoff 30 September 2026; SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`.
- Fixture is illustrative; this audit makes no assertion about a separate operational workbook.
- Exact v145 eligibility, record keys, cohort membership, effective-quarter grouping, status counts and order were reconciled for six unchanged scopes: all 117, RTA 10, Finance 1, empty 0, emerging only 17, RTA plus Finance 11.
- A seventh isolated in-memory scope exercises six records with recorded late, done, neutral statuses, absent quarters, an undated group, a long Arabic topic and long entity name. No source file was edited. Late was not inferred from dates.

## Verified

- 35 screen states: seven scopes at 1440, 1024, 768, 390 and 320 CSS pixels; no page or chart overflow.
- Active status and quarter union across cohorts; absent categories hide, retained empty intersections show a dash with numeric zero metadata and an accessible “صفر” label, with no colored zero bar.
- Status names use Ink except recorded late Red and done Green; legend membership follows the filtered scope. Approved bar colors and shared count scale remain intact.
- Quarter/status ordering, aligned status heading, source subtotals, equal physical bar scale, no percentages and blank bottom-left grand-total corner.
- Source-notes appendix and its navigation link absent; all detail record keys occur exactly once.
- Seven real toolbar PDF downloads, each A4 landscape: 14 / 4 / 2 / 1 / 4 / 4 / 4 pages respectively. Page counts are fixture-specific.
- Both cohort charts stay together on page one; report title is on the first page only; actual native PDF chart number multisets match the rendered source view.
- All 162 rendered PDF topic cells preserve their source words and numbers, including the long Arabic topic; actual red/green/neutral label colors verified in PDF text spans.
- Every exported page contains the copyright and page counter. Text remains within page bounds. Desktop, phone and PDF images were visually inspected.
- No JavaScript runtime errors or external-network requests in the scoped run.
- A separate final-bundle export succeeded after priming local assets and explicitly setting Chromium's browser context offline. No failed requests and no internet requests. See `offline-evidence.json` and `offline-no-network.pdf`.

## Method and limits

`review.py` performs model, DOM and actual native export checks. `review-title-cells.py` validates full-page raw PDF glyphs within each mapped title-cell rectangle, avoiding a PyMuPDF clipped-extraction artifact that inserts a phantom zero-width Arabic letter. Actual full-page glyph data, normal extracted text and visual rendering are correct.

The cloud browser blocks direct `file://` navigation by administrative policy. Browser launch therefore used loopback HTTP; final offline export was tested with network explicitly disabled after local priming. Direct file launch in the user's desktop browser was not run here.

This is focused browser/PDF verification, not accessibility certification. Excel source refresh, historical recalculation, PowerPoint redesign and other report-page changes are outside this agent's audit scope. Root/other-agent regression evidence is separate.

## Frozen ZIP extraction

A fresh extraction at `release-check-v146/Performance-App-v146` passed 56 additional targeted checks. Its runtime bundle hashes match the full audit. A real filtered RTA toolbar download produced four A4 landscape pages with all 10 source records, exact title cells, both charts on page one and the selected entity/month range in the first header only. Desktop and phone legend, dashes, label colors and layout passed. See `extracted-evidence.json` and `extracted-entity.pdf`.
