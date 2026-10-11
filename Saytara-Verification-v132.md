# Performance App v132 verification

**Verdict: PASS for the approved design and tested workflows.**

This release implements TEC Apple-Inspired Design Standard Revision 7 and the latest approved search-spacing and menu corrections. Checks use the actual bundled application in Chromium 151 at 100% zoom, plus native PDF output and a clean extraction of the release ZIP.

## Applied design and navigation

- DIN Next Arabic Regular headings: 38px pages, 36px search home, 30px portfolios and 28px cards. DIN Next LT Arabic Regular figures retain the approved 34–40px main and 28px secondary scale.
- Monthly special-project subgroup names are 18px Dubai Regular; short value/status labels and strategy metric names are 14px Ink. Compact columns remain; labels sit above figures and differences below their own values. The total label stays beneath the card-header total. Mobile strategy labels also remain above their values.
- Actual table names, content and notes use 16px Dubai Regular Ink; column headings use 18px Dubai Bold. Status text remains 16px with its approved independent palette. Neutral differences use 15px Dubai Regular Taupe, and minor metadata uses 14px Taupe. Meaning-based performance colors are preserved.
- Remaining source-card, summary and detail roles follow the same font/color contract without changing chart axes, status glyphs or source meaning.
- Search title placement accounts for the supplied logo transparency and font metrics. Visible upper/lower gaps are within 1px at desktop and mobile widths. The logo, field and action geometry match v131; title size remains 36px. Search results render the official logo as an image, including on mobile.
- Search home remains menu-only. Other pages retain Search plus the current destination. The three reports (agenda, council and special projects/HH) appear as distinct real links in every loaded page menu. Normal clicks passed on 12 routes × 3 destinations; Ctrl-click/new-tab hrefs passed on home and monthly routes. Keyboard dismissal restores focus.
- Financial bars are solid on screen and in print. Allocation uses Taupe #756B5F, spending Teal #115E67 and the track Linen #EFEBE7. Financial hatching, completeness classes and passive numeric-availability annotations are removed; no replacement note or marker is added.
- Generic title subtitles remain removed. Actual recorded notes, metric definitions, nonfinancial measurement/progress coverage and existing actionable missing-record drilldowns remain.

## Browser, mobile and PDF checks

The final focused browser run passed 291 checks plus 642 unaffected passing checks, with zero JavaScript runtime errors. It covers monthly typography/alignment, shared tables, responsive layouts, approved badges, menus, filters, source identities, partial financial data and search geometry. Additional source-role checks cover comparison, entity and HH report views: 16,809 screen-node and 1,609 print-node role assertions passed. A populated in-memory entity-note case verifies actual printed note text at 12pt and its field label at 9pt. The legacy entity methodology footer is hidden from print, leaving only copyright and page numbering; source notes remain intact and the scoped sample fits one page. Manual visual inspection covers actual desktop/mobile cards and tables and native PDF pages.

Print retains its own approved scale: 12pt table body, names, notes and in-table statuses; 13.5pt Dubai Bold headings; 24pt first-page title; 11pt differences; 10.5pt footer. Source-report print roles use explicit point sizes independently of screen sizes; legacy HH source text and comparison summaries are corrected to this print contract. The first page has only the official logo and report title including the cutoff date. Later pages have no masthead; column headings repeat. Every footer contains only the exact copyright line and generated page X of Y. The entity filter field is hidden while the selected scope still determines exported rows.

Illustrative native A4 landscape exports contain 4 monthly pages, 7 project pages, 2 search-result pages and 42 entity pages. Page counts accommodate the actual content rather than forcing a preview page count. Actual title/footer sizes, counters and row keys/order were checked; the printed title is `التقرير الشهري للأداء والتنفيذ - لتاريخ 30/09/2026`. Wider reports retain the existing A3 option. Focused comparison and HH exports contain 5 and 71 pages respectively; all pages retain copyright/page footers and source membership. These counts describe their illustrative fixture/scopes only.

## Source and numerical regression

Frozen illustrative workbook: `ILLUSTRATIVE-monthly-preview.xlsx`, cutoff 30/09/2026; SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`.

| Check | Result |
| --- | --- |
| 672 canonical source records and keys | Identical to v131 |
| Monthly counts, budget, strategy denominators/averages and history | Identical to v131 |
| 84 project records and report cohorts | Identical membership and order |
| 8 monthly follow-up rows | Screen/print keys and order identical |
| 4 search matches | Screen, CSV and print keys/order identical |
| Type / OR / AND filter cases | 59 / 84 / 67 rows reconcile to source |
| Reset and empty scope | 84 rows restored; genuine zero-count scope rendered as dash |
| 16 model/report modules | Byte-identical to v131 |
| 34 protected font/logo/icon/library/model/report files | Byte-identical to v131 |
| 52 financial display values / 54 bar styles / 32 scopes | Calculations and encoded lengths unchanged |
| Partial financial cases | Eligible/excluded keys, nulls and recorded-zero semantics identical |
| All revised amounts missing | Null subtotal/ratio, zero eligible financial rows; all source records retained |

Financial edge cases use temporary in-memory copies of the illustrative fixture, including empty/invalid cells and a genuine recorded zero. The source workbook is never edited. Removed presentation comprised five partial-style classes and eight passive financial coverage annotations; five nonfinancial progress notes and eight existing missing-finance drilldown links remain.

## Release integrity and practical limits

Readable sources and generated local bundles are included. The bundle source-order check (60 CSS files / 48 JavaScript files) and JavaScript syntax checks pass. `SHA256SUMS` and `release-manifest.json` record release file integrity; the manifest excludes itself. ZIP CRC, path safety, complete extracted file membership and every manifest hash are verified before publication. The clean extracted package is tested through native upload, search, detail navigation, menus, monthly/table typography, responsive projects and native PDF generation.

Operational workbooks, uploaded operational PDFs, illustrative workbook records and internal QA snapshots are excluded from the release. Numerical checks describe the frozen illustrative fixture and controlled edge cases, not an unseen operational refresh. The app reads cached Excel results; it does not refresh formulas or Power Query.

Native Windows file opening, physical printing and full accessibility certification were not performed. Managed Chromium blocks `file://` navigation, so browser workflow checks use a local HTTP origin. The app's generated page counters require a browser with CSS page-margin support; Chromium 151 was verified. Disable the browser's own headers/footers to avoid duplicate URL/date text.

Internal evidence retained for review: `qa-v132/browser/final-browser-evidence.json`, `visual-review.json`, `search-final-optical-evidence.json`, `qa-v132/browser/source-roles/source-role-evidence.json`, `qa-v132/regression/source-role-contract-evidence.json`, `qa-v132/regression/VERIFICATION.md`, source/data/partial-finance evidence, financial-presentation evidence and final clean-release/integrity evidence. Earlier bundled verification files are historical.
