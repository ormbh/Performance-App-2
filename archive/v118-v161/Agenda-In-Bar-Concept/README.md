# Agenda in-bar counts — review illustration R1

Review-only illustration derived from the unchanged Performance App v154 agenda model and the existing **illustrative** workbook `ILLUSTRATIVE-monthly-preview.xlsx`. No application/repository files were modified.

- Source period: January–September 2026; source cutoff: 30 September 2026. This is illustrative data, not a live production report.
- Workbook SHA-256: `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`.
- Scope: all sectors, units, entities and agenda types; 117 records, 100 approved and 17 emerging. Model keys are unique.
- `Agenda-In-Bar-Paired.png`: fixed desktop paired charts, aggregate status totals and full original definitions.
- `Agenda-In-Bar-Desktop.png`: full composition with expanded exact count matrices.
- `Agenda-In-Bar-Illustration.html`: self-contained interactive illustration with embedded original Dubai/DIN fonts and no network asset dependencies.
- `Agenda-In-Bar-A4-Landscape.pdf`: two A4 landscape pages. Page 1 contains charts, aggregate totals and complete definitions; page 2 contains all exact count matrices.

| Category | Q1 | Q2 | Q3 | Q4 | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| Approved agenda | 27 | 17 | 10 | 46 | 100 |
| Emerging topics | 7 | 2 | 6 | 2 | 17 |

| Category | Completed | Development | Review | Ready |
| --- | ---: | ---: | ---: | ---: |
| Approved agenda | 34 | 51 | 5 | 10 |
| Emerging topics | 9 | 1 | 1 | 6 |

Independent openpyxl counts of the workbook's raw agenda rows confirm these status totals. A fresh v154 model produces the same counts. Earlier 35/50 approved completed/development figures do not match this fixture and are not used.

## Presentation and specific limit

Both charts retain the shared numeric 0–50 count axis, source status/quarter ordering, approved category physically right, emerging left and Q1 physically right. Zero displays as `–`, including the zero baseline label, while all calculations retain numeric zero. Status fills/borders are unchanged. Ready labels and ordinary counts are Teal; numbers placed on solid Teal use Paper for readable contrast.

The desktop plot is taller to allow legible numbers while all segment heights remain exactly proportional to their counts. At the supplied 1440px view, every segment with a count of 2 or more receives a number; 1-count segments are too short for legible text and are not expanded, merged or given overlapping labels. The visible in-bar font is at least 16 CSS pixels. The fit rule measures actual DIN numeral ink bounds plus vertical padding and responds to available width. At smaller widths fewer numbers may fit. Exact small counts remain in each quarter's accessible name/native tooltip, activated quarter details and expanded count matrices.

A4 print uses the same shared 0–50 scale with a shorter plot and approximately 12pt in-bar figures, so additional small labels are omitted when they do not fit. Every exact value is printed in the matrices on page 2. This PDF is a browser-rendered review artifact, not a new application export implementation or complete agenda report with cover/detail records.

Hover and keyboard focus preserve aggregate totals. Click or Enter/Space activates a quarter; Escape, repeated activation or outside click restores totals. There is no persistent selected outline; keyboard focus remains visible. Printing restores aggregate totals regardless of the last activated quarter.

## QA result

**PASS — 71 recorded checks; no browser errors.** See `evidence.json` and `source-model.json`.

Checked raw workbook totals against the fresh v154 model, status/quarter reconciliation, proportional segment geometry, shared scale, physical ordering, ready text treatment, true-zero display, original detailed definitions, original embedded fonts, offline asset independence, activation/reset behavior, lack of a persistent selection outline, exact matrices and no document overflow at 390/768px. Inspected the actual desktop composition and both delivered PDF pages for Arabic shaping, readable labels, clipping and pagination. Charts and definitions share PDF page 1; exact matrices occupy page 2; original fonts are embedded.

No production workbook refresh, historical snapshot comparison, PowerPoint export or production deployment was requested or performed. This scoped illustration does not claim a fresh full-app accessibility audit.
