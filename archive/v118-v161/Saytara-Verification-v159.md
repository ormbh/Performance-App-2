# Performance App v159 verification

**PASS for revised data-observation checks.** 14 October 2026. Visual standard remains TEC Revision 25.

The revised checks use the approved organisation registry for sector/department values and their parent relationship, and loaded LOVs for other controlled fields. Completion percentage membership is included. No source values are corrected automatically.

Removed title-only duplicate alerts, Active/zero alerts, blank leadership warnings, future-year informational alerts and partial historical-status correction notes. Existing source identity warnings remain. Blank follow-up requirements now require follow-up evidence; negative unallocated figures are finance review items. Zero measurement with unspecified state retains an actionable clarification rather than a general calculation explanation.

## Validation

- Actual v158 and v159 bundles loaded with the existing illustrative September 2026 workbook: SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`.
- 71 checks passed, including source-record/derived-field equality, identical dashboard metrics and identical historical comparison metadata.
- Controlled cases cover correct/wrong sector–department pairs, approved aliases, unknown departments added to a workbook list, blank leadership flags, zero completion, conditional follow-up requirements, finance review classification, range checks and percentage-list membership.
- Every applicable schema LOV field was exercised with an invalid controlled value. Unknown values were identified with their source field and row; no source record was mutated.
- Actual data-notes page at 1440px and 390px and native CSV download verified. Page and export use the same revised issues; no browser errors, external asset requests or page overflow occurred.
- The **illustrative fixture** changes from 97 to 47 observations. This is not a recount of the user's uploaded 160-entry production CSV: that CSV was reviewed, but its source workbook was not provided in this turn.
- Build/syntax checks passed. Package CRC and each manifest file hash are verified at packaging.

This change does not alter report calculation definitions or CSS. Actual report PDF/Office rendering was not rerun for this validation-only change; previous v158 evidence retains its original scope. Browser validation used local HTTP, with outside requests blocked; cold file:// startup was not rerun. No workbook refresh or source correction was performed.

## Runtime hashes

- `assets/js/app-bundle.js`: `d43c61a1428582b5c699f49db2ef0be0d22dbad80c1cabc93d22d703d5b13cc7`
- `assets/css/app-bundle.css`: `92dfabb92cc0a439fd86f9ad95e3f116cb41de7de34d04138e9bbde9abc5f596`
- `assets/css/print-measure-bundle.css`: `39ea72c9dba51fe349db3b97034b4154734c6f47ce6f6fd4d598308d27375675`
