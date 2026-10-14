# Performance App v158 verification

**Verdict: PASS for the tested app and PDF scope.** 14 October 2026. Current design contract: TEC principles Revision 25.

## Changes

Agenda and special-project reports use shared roles throughout headers, scope controls, settings, navigation, chart cards, status summaries, legends, section headings, tables and detailed/mobile records. Equivalent roles share supplied fonts, palette, spacing and surfaces; the quarter and sector chart meanings remain independent.

Removed the unrequested agenda export count-matrix pages/slides, and removed the PM column from the HH main list. Kept the original agenda topic tables, interactive exact-count details, full legends and underlying source data. HH detail cards retain recorded managers. Empty HH open/completed appendix groups and their contents entries are omitted; screen navigation does not print. No circular progress indicators were restored.

## Source and scope

- Existing illustrative workbook: ILLUSTRATIVE-monthly-preview.xlsx, cutoff 30 September 2026.
- SHA-256: `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`.
- Agenda 117 = 100 approved + 17 emerging; all 117 records preserved. Filtered emerging-only scope retains 2 records.
- HH 62 = 24 leadership + 38 TEC, including 2 blank leadership flags. All 62 records preserved; selected police scope retains 2 projects. Actual source status counts and percentages are unchanged.
- Full source objects, parsing/model definitions and agenda/HH chart specifications remain unchanged. The approved monthly legislation card matches v157 in source metrics, history eligibility, drill membership and desktop/phone composition.

## Actual verification

| Area | Result |
| --- | --- |
| Shared pages and interactions | PASS, 129 checks at 1440/768/390/320px: matching role sizes, gutters and frames; title-first labelled phone records; direct/collapsible filters; first-selected +N, all = الكل, reset; existing report editing; no page overflow. |
| Agenda native PDF/PPTX | PASS, 56 checks. Actual all-scope PDF 14 physical pages; filtered 3. Cover is full bleed with no footer, charts+definitions share physical page 2, footers exclude cover, no extra matrices, every source topic row retained. Native editable charts and table data/styles checked. |
| HH native PDF | PASS, 120 checks. Actual all-scope PDF 71 physical pages; selected entity 6. Six-column list, correct source values/percentages, managers retained in detailed cards, no empty appendix/contents entry or printed return links, charts+definitions share physical page 2, source rows/cover/footer/bounds verified. |
| HH native PPTX | PASS, 445 structure/data/link/geometry checks across all 62, open-only 2 and done-only 1. Six exact list fields, recorded managers in cards, matching chart counts, absent empty sections, valid section/card/return targets, and native Paper/Linen tables. |
| Monthly/data preservation | PASS, 13 grouped checks against actual v157/v158, all-source and Governance scopes at 1440/390px. No source mutation or browser error/external request. |
| Build/package | Generated 75 CSS/53 JS files; syntax and source-bundle checks passed. Release packaging verifies ZIP CRC, every extracted manifest hash and canonical principles parity. |

Actual PDF pages were rendered and visually inspected for Arabic alignment, table separators, numeric progress, chart/legend placement, selected entity cover and footer clearance. The PDF exporter retains native text/vector output. No browser print dialog or outside asset request was used.

## Runtime hashes

- `assets/js/app-bundle.js`: `783c344a876573b4f559d08a1fe419ca6484e8dc782d2b994dff734ceba66966`
- `assets/css/app-bundle.css`: `92dfabb92cc0a439fd86f9ad95e3f116cb41de7de34d04138e9bbde9abc5f596`
- `assets/css/print-measure-bundle.css`: `39ea72c9dba51fe349db3b97034b4154734c6f47ce6f6fd4d598308d27375675`

## Limits

No Office/LibreOffice renderer was available: PPTX structure, native editable objects, chart/table data, links and geometry passed, but actual native editing and Office rendering were not run. Functional browser checks used local HTTP with external requests blocked; cold file:// startup was not rerun. The illustrative fixture establishes regression evidence, not a newly supplied production report. No Excel refresh was requested or claimed.

Earlier verification files describe their original releases and are not new v158 test claims.
