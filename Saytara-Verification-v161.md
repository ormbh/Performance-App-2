# Performance App v161 verification

**PASS for the approved agenda and special-project report consistency changes.** 14 October 2026. TEC design Revision 26.

## Applied result

Both reports share contents/navigation, reading order, table-column sequence, continuous record numbering, cover-title/date treatment, compact detailed legends, notes/recommendations and empty states. **المستجدات التفصيلية** occurs only in special projects. The PDF order is cover → contents → charts and full definitions → records → applicable special-project details → notes/recommendations. PDF contents uses actual displayed page numbers and working internal links. Printed numbering and copyright start after the cover.

Agenda retains its five source-backed columns; special projects additionally retains its recorded completion percentage. Agenda approved/emerging/other ordering agrees across contents, charts and records. Special-project main rows and detailed cards share open/completed ordering and record numbers. Screen return links target the exact project row; PowerPoint returns to its containing table slide. PDF omits screen return controls.

## Evidence

- **410 independent browser, source, content and PDF checks passed** against the actual final bundle. Desktop/tablet/phone widths: 1440, 1024, 768, 699, 650, 390 and 320px. Full, filtered, single-cohort and empty scopes passed. Contents links, keyboard chart controls, counts, source keys, continuous numbering, live notes entry without lost focus, custom metadata and reset behavior were verified.
- **50 additional native-PDF checks passed** across full, filtered and empty agenda/special-project exports. Full agenda: 15 physical pages; full special projects: 71. Both include an unnumbered cover. Filtered reports omit empty sections; zero-result exports contain a cover and one message. Charts, totals and full definitions share their summary page in these scopes. Actual page references, internal link destinations, page geometry and text bounds were checked.
- Long Arabic recommendations exposed a page-break defect during review: overlapping font Range rectangles could exclude one complete line from both pages. The PDF renderer now uses measured visible glyph bounds around the unchanged baseline. Final agenda and special-project stress exports preserve **all 28 complete numbered recommendations exactly once**, including the line at the break. Representative pages were visually inspected. Font size, line spacing and source content are preserved.
- **15 monthly PDF regression checks passed** after that renderer fix. The actual three-page A4 portrait export retains native text, correct footers and identical source records/dashboard values. Representative pages were visually reviewed.
- **92 native PowerPoint package checks passed** for full and filtered agenda/special-project exports: source counts, table rows, chart data, slide order, contents page references, internal relationships, cover/footer metadata and geometry. Controlled notes/recommendations are included in these test decks. Native Office visual rendering was unavailable.
- Representative final screen and PDF covers, contents, charts/legends, tables and long-note continuation pages were visually inspected. Automated geometry and text checks cover all generated PDF pages; this is not a claim of manual review of every page.
- Build freshness, JavaScript syntax, ZIP CRC and every release-manifest file hash passed. The release contains no workbook, CSV, generated report PDF or test input.

## Source preservation

The existing illustrative workbook is unchanged, SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. All 672 source records, derived fields, dashboard values, report date/snapshot metadata and data observations match v160. Agenda remains 117 = 100 approved + 17 emerging. Special projects remains 62 = 24 leadership + 38 TEC, including two blank leadership classifications in TEC. The v159/v160 approved data-quality checks remain intact.

No new production workbook was supplied. Controlled test copies cover extra agenda classifications and long notes without modifying the original illustrative file. Earlier screenshots may have different recorded values and are not the verification source for this release.

## Practical limits

Browser checks use local HTTP with outside requests blocked. No runtime errors or outside requests were recorded. Cold file:// startup, native Windows behavior and physical printer output were not rerun. Search/council export code was reviewed for scope isolation but those PDFs were not newly exported. Native PowerPoint XML, data and relationships were validated; Office/LibreOffice rendering and editing were not available. Very long real source labels or narratives may require readable continuation; no fixed page-count guarantee is made.

This report verifies the implemented changes and named regression cases. It does not certify accessibility or assert a complete revalidation of every unrelated app page.

## Final runtime hashes

- `assets/js/app-bundle.js`: `86e45fae176c7113282ad3469f41a106b6699eef5b7228019f3ae4878927f1e8`
- `assets/css/app-bundle.css`: `68bbe13e375feb6eaacd7cdf84c822022756242bfe26789666d3d9dd6f2c8f6d`
- `assets/css/print-measure-bundle.css`: `adb6e6e6892025c6f66d13e2796f0715147da7c257b2590df9769523edacbb97`
