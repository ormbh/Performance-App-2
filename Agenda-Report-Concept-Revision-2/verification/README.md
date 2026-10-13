# Agenda revision 2 — independent illustration review

**Verdict: PASS for the supplied illustration artifacts and stated fixture cases.** This is a preview review, not approval of a production implementation. The v145 application remains unchanged.

## Evidence and scope

- Source: `ILLUSTRATIVE-monthly-preview.xlsx`, SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`.
- Source report date: 30 September 2026. The illustrated heading uses **يناير – سبتمبر 2026** as the requested month-to-month presentation. January is the preview assumption; this does not establish a newly approved date-filter calculation or change the source cutoff.
- All scope: **117 records = 100 approved + 17 emerging**. Selected entity **هيئة الطرق والمواصلات**: **10 records = 8 approved + 2 emerging**.
- Eight states checked: all, one entity, two entities, single-record entity, empty selection, emerging-only, long Arabic text, and an undated-quarter specimen. Long text, undated and source-note cases use temporary browser specimens only; the workbook was not changed.

## Passed checks

| Check | Result |
| --- | --- |
| Ordered source records, table values and grouping | Preserved in all eight states. Topic/entity columns were moved without dropping fields. |
| Chart counts, quarter/status ordering, totals and denominators | Match the unchanged report model. Approved and emerging percentages use separate cohort totals. |
| Mini-bar lengths | Match their counts on the same zero-to-maximum count scale in each filtered overview. Zero denominators do not create percentages. |
| Sparse and empty scopes | A one-record scope remains one record; empty scope remains empty. Empty quarters do not acquire records. Undated items remain distinct. |
| Screen geometry | No page overflow or clipped matrix text at 1440, 1024, 768, 390 and 320px in the tested states. |
| Wider table layout | Final columns measure 4% index, 45% topic, 28% entity, 9% deadline and 14% status. Long Arabic values wrap at the retained 16px body size. |
| Source-notes appendix | Entire appendix and its record boxes/links are absent after the transformation, including a controlled source-note specimen. Other report records and definitions remain. |
| Downloaded PDF records | Independently extracted all 117 / 10 topic identifiers from the two PDFs in the exact expected table order. |
| A4 output | All 15 pages inspected: all-scope PDF 12 pages, selected-entity PDF 3 pages. Every page is approximately 297 × 210mm. |
| Chart pagination | Both chart families stay together on page 1 in both PDFs. No split chart or continuation masthead. |
| First-page header | Report title and month range occur on page 1 only. Selected entity is beneath the title only on the first-page masthead; ordinary entity cells remain in tables. |
| PDF visual quality | Every page inspected for Arabic layout, clipping, overlap, table continuation and footer clearance. Text bounds remain within the 10mm page insets. |
| PDF fonts | Actual PDF Type3 glyph programs and Unicode maps are embedded. Arabic shaping and supplied DIN/Dubai appearance were visually checked; these are not missing-font fallbacks. |
| Offline standalone screen previews | Both final HTML previews render with all network requests blocked: zero external requests, logos and embedded TEC fonts loaded, expected record counts retained, no overflow at 1440/390px. |
| Production preservation | All **188 v145 application files** match the independently recorded baseline hashes. |

## Limits

These checks use the illustrative fixture, not the user's operational workbook. Page counts change with content. The standalone HTML files are static visual snapshots; their filter/download buttons are not a new working application. This review does not claim production offline-export integration, full keyboard/screen-reader certification, historical-source reconciliation, a workbook refresh, PowerPoint validation or arbitrary-length editorial-note pagination.

The internal `*-composed.html` files are working PDF capture documents and are excluded from the review pack; reopening them is not the supported preview. The actual final PDFs and the two self-contained `Agenda-*-Preview.html` files are the reviewed artifacts.

## Evidence files

- `independent-v2-review.json` — source invariants and responsive checks.
- `independent-pdf-actual-review.json` — actual PDF record extraction, geometry, embedded glyphs and every-page visual verdict.
- `standalone-offline-review.json` — final standalone HTML with networking blocked.
- `baseline-contract.json` — internal source contract and v145 file hashes; retained in the working directory, not required for the user download.
