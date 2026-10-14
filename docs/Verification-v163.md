# Performance App v163 — verification

14 October 2026 · TEC design principles Revision 28

The council decisions report implements the approved issuing-body charts and six-column table. Screen, native PDF and native PowerPoint use the same scoped council model. The clean app ZIP contains 26 runtime, license and start-guide files; no workbook or test report is bundled.

## Audit basis

1. The latest user-approved contract: **م ← الموضوع ← القرار الأخير ← الجهة المعنية ← الحالة ← ملاحظات**. The latest-decision cell places the populated decision number, issuing body and meeting date above the full text, omitting every empty reference field, its label and separator.
2. The source schema and existing v162 follow-up eligibility, status definitions, record identities, filters, dashboard metrics, source snapshots and data-quality observations. Presentation changes do not redefine those calculations.
3. The approved TEC principles: exact status palette, supplied Dubai/DIN fonts, RTL order, readable typography, shared spacing and table appearance, zero-as-dash, missing-as-empty, full source narratives, compact legend, consistent cover and contents/navigation, and no source-note appendix or decision cards.
4. The approved agenda/HH component roles, checked against v162 for equivalent desktop and mobile behavior. Council keeps its own business rules and explicit column sequence.

## Source and scope

The available workbook was **ILLUSTRATIVE-monthly-preview.xlsx**, SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. It is a test fixture, not a claim about the user's latest live report.

- All **672 parsed source records**, dashboard metrics, snapshot values and data-quality observations remain unchanged from v162.
- Council fixture: **164 recorded = 70 requiring follow-up + 94 other recorded decisions**.
- The 70 charted decisions reconcile to **45 المجلس التنفيذي + 9 مجلس الشؤون الاستراتيجية + 16 without an issuing body**.
- Status reconciliation: **38 completed + 31 development/review + 0 late + 1 missing status = 70**. Late remains disjoint from development/review in council calculations.
- Report period is display metadata. The January–September 2026 label does not silently remove older, future-in-period, year-only or undated meeting records. Entity, sector, department and follow-up filters retain their existing meanings.
- Controlled in-memory cases tested additional issuers, unknown/missing status, partial and fully blank references, missing eligibility columns, exact meeting-day ordering, and 28 long Arabic latest-decision paragraphs plus 23 long notes paragraphs. The source workbook was not edited.

## Results

| Area | Result | Evidence |
| --- | --- | --- |
| Independent council source/screen audit | PASS — 474 assertions across all, filtered, empty and controlled scopes; exact record membership, chart partitions, six columns, ordering, blank omission and navigation | [Council audit](checks/council-audit.json) |
| Agenda/HH regression and council editor | PASS — 32 checks; existing chart geometry, table sequence, styles and counts unchanged; live notes, contents, title, period and reset work | [Shared screen checks](checks/screen.json) |
| Council responsive/visual checks | PASS — 36 checks at 1440, 1100, 768, 390 and 320px; correct right/left placement, common scale, count fit, palette, legend and no viewport overflow | [Visual checks](checks/visual.json) |
| Native council PDF | PASS — 132 checks against the actual PDFs from the minimal runtime; all records, source text, page dimensions, headers, contents links, page references, cover/footer and continuation behavior | [PDF checks](checks/pdf.json) · [Cell checks](checks/pdf-cells.json) |
| Native council PowerPoint | PASS for package/data/geometry — 142 checks covering native six-column tables, editable charts and embedded data, source text, numbering, palette, links, fonts and object bounds | [PowerPoint checks](checks/powerpoint.json) |
| Minimal runtime PowerPoint | PASS — 28 checks exercising actual agenda, HH and council menu downloads, required lazy files, embedded fonts, relationships and source titles | [Clean PowerPoint checks](checks/clean-powerpoint.json) |
| Minimal runtime regression | PASS — 30 checks exercising real workbook import, agenda/HH native PDFs, council records/charts, unchanged source data and local dependency loading | [Clean runtime checks](checks/clean-runtime.json) |

The unfiltered native council PDF has 27 pages including its unnumbered cover. All 164 records and 984 actual table cells retain their source words and numbers. Filtered, other-only, empty and controlled PDFs also pass. All 51 numbered long-text paragraphs survive exactly once, including across page breaks. Physical page 2 starts displayed page 1; contents entries resolve to the final displayed page numbers. Additional issuer panels continue at the same physical scale. Ordinary pages were reviewed in contact sheets, with readable-size inspection of covers, charts, tables and long-text continuation samples.

The final source bundles pass `python tools/build-bundles.py --check` and `node --check assets/js/app-bundle.js`. Tested JavaScript SHA-256: `62f3771edc0bc424d3c452b92c768398f2b79356350025a1df9e396968901acb`. The release manifest records every delivered runtime file's checksum.

## Limits and unrun checks

- Production workbook reconciliation was **not run**: only the illustrative fixture and controlled test cases were available. No production figures are hardcoded.
- Native Microsoft Office rendering and a manual chart-edit exercise were **not run** because Office/LibreOffice was unavailable. PowerPoint checks establish editable package structure, embedded values, geometry and links, not an Office visual pass.
- Cold `file://` opening remains **unverified** in this managed environment: the previous check was blocked by Chromium's `ERR_BLOCKED_BY_ADMINISTRATOR` before application code ran. No security bypass was used. The actual minimal package was tested over local HTTP with no external asset requests.
- No workbook refresh, Power Query execution or new historical data reconstruction was required or claimed. Source values were preserved.

## Review previews

- [Council chart page](previews/council-summary-pdf.png)
- [Six-column table and conditional reference line](previews/council-table-pdf.png)
- [Responsive desktop chart view](previews/council-screen.png)

These previews are generated by the delivered application using the illustrative fixture or explicitly controlled QA cases.
