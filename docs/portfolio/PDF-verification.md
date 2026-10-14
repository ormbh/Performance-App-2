# Portfolio PDF verification — v167

**PASS — 185 checks, including final clean-build binding.** The comprehensive export set passed before the last screen-only narrow-label CSS adjustment. A fresh download from the final build has identical page plans, source text geometry, rows, charts and labels; its clearly labeled sample PDF was regenerated. Actual PDFs were downloaded through the app's PDF action, rendered, and inspected. The current supplied attachment and the populated illustration fixture were loaded in separate browser contexts.

## Source scope

- The supplied attachment has 84 raw secretariat rows and **zero eligible named projects**. A fresh load prints its source-completeness explanation on one page. Missing source data was not populated from the fixture.
- The anonymized illustration fixture contains 84 named projects. Its figures are used only for populated-layout tests and the explicitly labeled sample PDF. It preserves 10 completed, 61 active, 7 not started, 3 frozen, 2 transferred and 1 cancelled; 6 require follow-up.
- Both workbooks remain unchanged. Their SHA-256 identifiers and the exact loaded JavaScript/CSS identifiers are recorded in [native PDF evidence](../checks/pdf.json).
- The source cutoff remains 30 September 2026. A custom display period does not replace the source cutoff or change the scoped dataset.

## Downloaded cases

| Case | A4 portrait pages |
| --- | ---: |
| Portfolio overview, all illustrative records | 6 |
| Formatted project report, same scope | 6 |
| Compact spacing | 6 |
| Completed-only filter | 5 |
| Empty filter result | 1 |
| Main project list, all 84 records | 14 |
| Custom report title and display period | 6 |
| Deliberately long 85-line source note | 20 |
| Fresh actual attachment, zero eligible named projects | 1 |
| Clearly labeled illustrative sample | 6 |

Page counts follow the rendered content. Long notes continue in their source table columns with repeated column headings; they are not truncated or converted into a separate narrative appendix.

## Verified

- Screen and PDF retain identical ordered source-record keys in every printed operational table.
- Every visible native source text line has a placement in the final page plan, including long notes.
- Table sequence is **م ← المشروع ← الجهة المعنية ← الحالة ← نسبة الإنجاز ← موعد الإنجاز**. Follow-up adds **ملاحظات**. Header rectangles stay inside their own columns, including the one-line deadline heading.
- Project title, display period, selected filter scope and actual source cutoff are retained. Custom metadata is tested.
- The status table and its compact definitions remain on one page for the tested scopes. Counts fit inside their true bar segments or use the approved outside placement; no visible in-bar label is below 14 CSS px in the A4 geometry.
- Summary and finance share the first page when their actual geometry fits. Comfortable and compact spacing preserve the same content and font roles.
- All pages have correct sequential page/total footers and copyright, no empty trailing sheet, and no text beyond page bounds.
- Native contents links resolve to valid PDF destinations. App-only actions do not become fake PDF destinations.
- The final files retain selectable Arabic text, vector chart/table geometry and embedded DIN Next Arabic, DIN Next LT Arabic and Dubai font subsets. The official logo is the image asset; charts are not flattened screenshots.
- No replacement glyphs, clipped table headings, or JavaScript export errors were found. Source-zero and missing-value behavior follows the app's shared renderer.
- All overview pages and contacts for every case were visually inspected, with full-size inspection of tables, repeated headings, custom metadata, empty-source output and long-note continuations.

This is rendering and content verification, not a tagged-PDF accessibility certification or an Excel recalculation/Power Query refresh. PDF page counts and layout are not forced to match the demonstration when a user's source scope or notes differ.

## Sample

[Illustrative portfolio PDF](portfolio-illustrative-a4.pdf) is an actual native export from the clean application. Its first-page display period explicitly says **بيانات توضيحية للمراجعة**. These values are not represented as the figures in the supplied operational attachment.
