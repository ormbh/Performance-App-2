# Performance App v134 verification

**Verdict: PASS for the approved design and tested workflows.**

The acceptance target is the approved TEC Revision 8 paper amendment plus the latest dashboard and legislation changes, consolidated in Revision 9. Checks use the assembled application, its readable sources and native Chromium PDFs at 100% scale. The entity-dashboard redesign remains a separate concept.

| Area | Applied change / acceptance check |
| --- | --- |
| Paper | A4 landscape for agenda, council and HH; A4 portrait for monthly, projects, project report, entity, comparison, search and all other browser-print views. No A3. Stored larger-paper preferences normalize to A4. |
| Print composition | 10mm margins; portrait panels reflow; fit-sized cards and rows stay together; oversized content continues without whole-report shrinking. Table headings repeat and stay with opening rows. |
| Header and footer | First printed header: official logo and report title with the source cutoff inline. No continuation masthead. Footer: exact copyright and generated page X of Y only. Menus, filters and operational controls are omitted; selected scope still determines exported content. |
| Print typography | Title 24pt; table content, names, notes and in-table statuses 12pt Dubai Regular; column headings 13.5pt Dubai Bold; footer 10.5pt. Screen label changes do not enlarge this independent print scale. |
| Monthly metric names | Short value/status labels and strategy metric names 15px Dubai Regular Ink on screen. Agenda category labels/subgroup names remain 18px, table/badge text 16px, table headings 18px Bold and supporting explanations/metadata 14px. |
| Legislation | Generated labels: **SLC منجز ضمن موعد** and **SLC منجز بعد موعد**, with the Latin run isolated in RTL layout. The repeated SLC comparison paragraph is removed on screen and in print. Timing definitions, source fields and disjoint cohorts remain. |
| Previous approvals | Supplied TEC fonts/colors, neutral regular source names, Ink/Taupe text roles, approved status badges, solid financial bars, removed title subtitles, search spacing and Search/current-page navigation retained. All three reports remain in every loaded-page app menu. |
| Audit corrections | Primary/filter/disabled states and export loading indicator corrected. Native chart status fills match the approved palette. HH screen and print figures use the supplied DIN family; summary panels use Paper/Sand without status stripes. The progress ring fits the approved figure font. |
| Readability fixes | Search/upload print without duplicate branding or blank trailing pages. Checks badges wrap at 12pt Regular. Comparison headings and source captions stay with their associated content. |

The browser audit covers all twelve loaded routes at 1920, 1440, 390 and 320px: upload, search home/results, monthly, projects, agenda, council, HH, project report, entity, comparison and checks. It exercises menus, keyboard/Escape focus, filter selection/reset/empty scope, report links, A4-only preferences, busy/disabled controls and reduced-motion behavior. Tables retain their readable sizes and scroll within labelled regions on narrow screens.

Native PDF checks cover all document types, selected sector exports, populated historical comparison, initial upload and an oversized table row. They check A4 dimensions/orientation, source membership, actual font sizes and font resources, every page counter, footer clearance, content completeness, unexpected blank sheets and readable continuation. An independent reviewer visually checks the rendered pages. Page counts depend on content; they are not product limits.

Source regression compares v134 with a fresh extraction of the immutable released v133 ZIP. All 672 illustrative records, raw statuses, unique keys, dates, null/zero distinctions, calculation results, financial cohorts and search/follow-up/export membership remain identical. Fifteen model modules and 34 protected assets—including native PowerPoint/report-export modules—remain byte-identical. Additional agenda, HH, entity and historical ambiguity cases retain their results. No workbook is rewritten.

Fixture SHA-256: `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`.

The final 46-rule compliance matrix has no unresolved material finding. Independent visual/font/geometry verification passed for **24 PDF cases / 394 pages**. Every reviewed page has the required A4 orientation and footer; embedded font resources are present. The latest screen-only HH table-weight correction is bound to the final asset hashes and preserves the reviewed print composition. The checks section summary can precede its table on the next page; its table heading stays with the first row and all content remains readable.

| Final production asset | SHA-256 |
| --- | --- |
| assets/css/app-bundle.css | `dffaf6936732f0679fd5cf5ff6b4da8c6eb8985dac4b7e4f98ee061caf309a92` |
| assets/js/app-bundle.js | `e5decf966414446dc9562b979c7089b50522c74d6536f92d55efdf3b88359dc4` |

The complete ZIP is integrity-checked and tested from a fresh extraction before release, including actual upload, search/details, menus, narrow HH layout and native portrait/landscape PDFs. The release ZIP contains the complete app, approved local fonts, readable source modules, standard, verification and an integrity manifest. Workbooks, test records, generated QA PDFs and browser evidence are excluded.

The populated checks use frozen, explicitly illustrative workbooks. The operational workbook shown in earlier screenshots was not supplied for this release, so this is not reconciliation of that workbook. Native Windows Chrome, physical printing and native Office editing were not tested. Managed-browser file navigation is restricted; functional tests use an HTTP origin. These checks do not constitute formal accessibility certification.

The full requirement-by-requirement matrix is included as **COMPLIANCE-AUDIT-v134.md**. Detailed generated QA pages and illustrative workbooks are retained outside the app package.

Rebuild: `python tools/build-bundles.py`. Verify bundled sources: `python tools/build-bundles.py --check`. The manifest records SHA-256 for every packaged file except itself.
