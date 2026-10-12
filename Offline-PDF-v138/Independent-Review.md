# Final v138 direct PDF verification — PASS

Independent review covers **10 actual Download PDF cases / 165 pages** from the final offline renderer. The PDFs are frozen under `final-native-v3/`; their full hashes and the exact generation hashes are recorded in its manifest and `INDEPENDENT-VERIFICATION.json`.

| Export | Pages | Format |
|---|---:|---|
| Monthly full | 1 | Continuous 297 × 622 mm |
| Monthly filtered | 1 | Continuous 297 × 453 mm |
| Monthly A4 | 3 | A4 portrait |
| Agenda | 16 | A4 landscape |
| Council | 30 | A4 landscape |
| Special projects / HH | 71 | A4 landscape |
| Projects | 6 | A4 portrait |
| Entities | 34 | A4 portrait |
| Comparison | 1 | A4 portrait |
| Search results | 2 | A4 portrait |

All final pages have readable joined Arabic, native text and vector charts, embedded DIN/Dubai Type0 fonts with Unicode maps, and no text clipping or body/footer collision. The only raster image is the official first-page TEC logo. Table and status text remain **12 pt**, table headings **13.5 pt Dubai Bold**, report title **24 pt DIN**, and footer **10.5 pt**. Approved metric roles, colors and sizes remain intact.

The full continuous page retains all source values, eight follow-up rows and notes, SLC captions, paired projects-left/executive-right columns, one masthead and copyright/page-only footer. Its in-bounds perimeter is entirely Linen `#EFEBE7` (7,958 pixels checked, zero white-band pixels). Footer text is at least **8.93 mm** above the physical bottom edge. Ordinary A4 retains its existing approximately 2.93 mm footer inset.

The monthly A4 requester note stays inside the whole first-page Special Projects card. Fitting cards remain whole; follow-up rows start after the paired columns and continue with repeated table heads. Agenda/Council table heads stay with opening rows, and entity/Council outer headings stay with their opening table. The comparison exports one clean page and excludes closed details.

Independent source checks confirm the monthly numeric/date/ID footprint matches canonical v137 exactly; all 117 agenda IDs, 164 council IDs and 62 HH table IDs appear once. All 62 HH detail titles remain present. Entity source names and project/entity numeric footprints match the browser-export baselines. The final source audit separately passes 672 records, 37 monthly metric entries and eight follow-up keys.

The earlier DIN shaping/Unicode errors, split requester note, orphan or missing table heads, omitted HH table names, outer heading orphans and blank comparison page are resolved. **No material or new layout findings remain.** The rejected prototypes are archived separately.

Generation: app bundle `5a34e9cfbd62ad909effddfa841d0633db594cc46956b076d68ef76caff2591c`; PDF engine `8038eaa52e8aa4693e6f4d9141f51edfaf78be42621384e608ddfc81d5cb2528`; measurement CSS `1305fa85010c66e8d39da391c07205cb78f1ee6ad1b11e9b543aed3a8a6b57b6`.

Detailed evidence: `FINAL-V3-NATIVE-VERIFICATION.json`, `FINAL-MONTHLY-NUMERIC-COMPARISON.json`, `FINAL-REPORT-NAME-ID-COMPARISON.json`, `FINAL-MONTHLY-PERIMETER.json`, `hh-helper/HH-DIRECT-PDF-REVIEW.md`, `other-routes-helper/FINAL-v3-REVIEW.md`, and `../data-regression/DATA-VERIFICATION.json`. Nine final routes exactly match the reviewed repaired outputs in native text, geometry, fonts, colors, vectors and images; helper raster comparisons also confirm equivalence. The changed final one-page comparison was inspected directly.

Scope: frozen illustrative fixture and the cases above. This is not formal PDF accessibility certification or a physical-printer test.
