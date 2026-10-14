# Performance App v160 verification

**PASS for both newly approved data checks.** 14 October 2026. The visual standard remains TEC Revision 25.

Added project end-before-start warnings and numeric-text storage warnings. Secretariat dates use valid Excel dates; special-project dates use recorded month/year. Month-only precision is respected; same-day/same-month periods are allowed and missing/ambiguous dates are not guessed. Numeric-text detection covers amounts, percentages, progress and year fields, including grouped numbers, Arabic digits, negatives and percentages. IDs and narrative fields are excluded.

Source values, dashboard calculations, report CSS and historical comparison safeguards are unchanged. No date reversal, number conversion or workbook refresh is performed.

## Verification

- 102 regression/control checks passed against actual v159/v160 browser bundles, including source-record/derived-field equality, identical dashboard totals and snapshot metadata, and retained v159 validation rules.
- Date cases cover reversed dates, valid future dates, equality, time fractions, month-only precision, special-project month/year boundaries, missing dates and ambiguous strings.
- Numeric cases cover grouped values, percentages, Arabic/Persian digits, accounting parentheses, scientific notation, text zero and actual numeric zero. Identifiers/narrative text and nonnumeric placeholders are not mislabeled.
- 14 additional actual workbook-import/screen/CSV checks passed. A separate controlled copy contains reversed project dates, a budget string `1,000` and progress string `50%`. All three warnings identify the actual source row/field on the data-notes page and in its downloaded CSV. Literal source cell types and values remain intact.
- The original illustrative workbook remains byte-identical: SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`.
- Original fixture observations remain 47 to 47; controlled-case evidence demonstrates the new rules. No production workbook was supplied for this turn.
- Actual data-notes page at 1440px/390px and CSV export verified. No runtime errors, external requests or page overflow. Build/syntax checks passed; ZIP CRC and every manifest hash are checked during packaging.

This validation-only update does not change report geometry or calculation definitions. PDF/Office rendering was not rerun; prior v158 export verification retains its original scope. Browser checks use local HTTP with outside requests blocked; cold file:// startup was not rerun. Controlled input workbooks are not included in the app release.

## Runtime hashes

- `assets/js/app-bundle.js`: `4253b6e49234b8395ca674bf6ff126ce01be0f269855386b3eabc5f2b5d16a07`
- `assets/css/app-bundle.css`: `92dfabb92cc0a439fd86f9ad95e3f116cb41de7de34d04138e9bbde9abc5f596`
- `assets/css/print-measure-bundle.css`: `39ea72c9dba51fe349db3b97034b4154734c6f47ce6f6fd4d598308d27375675`
