# Performance App v145 verification

Date: 13 October 2026. Scope: approved search-results concept, shared search wording, responsive controls, selection summaries and matching-row exports.

## Changes

The shared search prompt is **ابحث عن بند أو مشروع أو مسؤول**. The accessible name retains number search. The search home keeps the approved logo/title/field composition. Results use one functional search icon, a compact toolbar and four default columns: title, status/progress, timing and organizational unit. Existing saved column choices are retained; users can expose all six fields or open the full record. Match highlights use Mist behind Ink with regular 16px Dubai text. Result titles have a detail arrow and a hover/focus underline.

Phone results stack every selected field without a desktop-width table. Sorting remains directly accessible; column, CSV and PDF controls are in the options disclosure. Search filters and applicable PDF scope text reuse the dashboard's first-selected **+N** / **الكل** display rule while preserving actual selected source tokens and inherited drill constraints.

## Executed checks

- **101 browser/PDF checks pass**, with no JavaScript errors. Queries, matching keys and order are compared with v144. All 672 fixture records remain reachable across 14 screen pages without omission or duplication. Original source item objects remain identical.
- Desktop, tablet and phone layouts were exercised at 1440, 768, 390 and 320 CSS pixels. The default table fits its region, phone rows retain all selected fields, and the document has no horizontal overflow. Actual rendered Arabic, alignment and matching text were inspected.
- Search suggestions, numeric queries, title-detail opening, Escape/focus restoration, sorting, column preferences/reset, first-selected chronology, full selection, clearing filters, pagination and empty results were exercised. The phone column picker uses the shared dialog lifecycle.
- Actual CSV download contains all 672 matching records. Actual native PDF download uses a source-backed 67-match filtered scope, exceeding the 50 visible screen rows. Prepared rows match all 67 ordered keys; downloaded PDF includes the final match, title, report date, embedded fonts and selectable text. Every page uses A4 portrait geometry and was visually reviewed. Phone export uses the report table rather than the phone card layout.
- After loading the bundled local assets, the browser is switched offline and exercises a new search and native PDF download with no external requests. The request observer preserves the browser cache. Cold **file://** launch is not tested: this managed Chromium environment blocks it by administrator policy. Native Windows and other browser engines were not tested.
- Independent source review checks protected model/search definitions, source-backed display and export behavior, saved-column compatibility and filter-summary semantics. Bundle consistency and JavaScript syntax pass. Package membership, CRC and all per-file hashes are checked after extraction; the extracted-package rerun is recorded separately with published evidence.

## Source and limits

Tests use the frozen illustrative workbook dated 30/09/2026, SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. No operational workbook was supplied or bundled. Screenshots are illustrative records, not the operational workbook in the user's screenshots. This focused release does not constitute a fresh audit of every app feature, accessibility certification, physical printing verification or a claim about every PDF page count. Prior release documents remain historical.

## Runtime hashes

| Asset | SHA-256 |
| --- | --- |
| `assets/js/app-bundle.js` | `59d49fe2b05a3e107fe2ec7f4ff11352a18b50b2780b448adfe82a4a32978014` |
| `assets/css/app-bundle.css` | `52dfcafec004e0a8eb4cbf0a74392ef7ea6c4343ecbd1dd9f3e5759c954994cd` |
| `assets/css/print-measure-bundle.css` | `af18ecfaef53bbee841904e070048335c64dd94ce62f7bca0be0f08d36082bfd` |
