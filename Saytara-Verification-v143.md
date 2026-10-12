# Performance App v143 verification

Date: 13 October 2026. Scope: monthly PDF English filenames using the user's official organizational names, plus two requested PDF note removals.

## Behavior verified

Monthly PDF filenames use **TEC_Monthly_Mmm_yy[_scope].pdf**, for example **TEC_Monthly_Sep_26_Dubai_Plan_Office.pdf** and **TEC_Monthly_Sep_26_Governance_Sector.pdf**. The report date supplies month/year. A partial unit takes priority over a partial sector; multiple choices use the first selected name with no additional count. Full/unrestricted scope is omitted. Entity is not part of the filename.

All six sector and 23 unit names use the user's supplied English wording. As subsequently requested, terminal **Department** and **Section** are omitted from filenames; **Office** and **Sector** remain where supplied. The General Secretariat receives no added Sector suffix. The English name catalog is in **PDF-FILENAME-NAMES.md**. Spaces and punctuation become underscores, and **&** becomes **and**. No hidden direction controls are used.

The filename mapper recognizes the existing short Arabic source names, the user's full Arabic names with إدارة/قسم/قطاع, official English names and existing bounded legacy aliases. No source strings are renamed. Unknown Arabic scopes use **Selected_Unit** or **Selected_Sector** until mapped; a selected scope never silently becomes an all-scope filename. Other printable ASCII scope names are sanitized. Long filenames remain bounded at 240 ASCII characters, retaining the report date and genuine `.pdf` extension.

Both continuous and A4 monthly PDFs omit the missing-requester note and the incomplete prior-project-status explanation specified by the user. Their on-screen diagnostics, all totals and comparison rules remain. Other source warnings remain; empty source-note containers are omitted.

## Executed checks

- **108 filename checks pass**: all 29 organizational names through short Arabic, full Arabic and official English; unit priority, first-selection order, full selection, sector fallback, entity-only scope, four legacy aliases, invisible marks, punctuation, unknown names, stale choice captions, report date, absent date, long names and unchanged nonmonthly filenames. Formatter inputs are unchanged.
- **16 browser/PDF checks pass** without runtime errors. Actual download-button exports cover unrestricted scope, multiple units with Dubai Plan Office selected first, and Governance sector. Downloaded names match the approved format. Each continuous fixture PDF has one page; native Arabic report title/date/scope remain and the partial-unit header retains **+1**. Export does not mutate scope or counts.
- **16 PDF-note checks pass**: a positive v142 baseline contains both requested notes, while current composition omits them; all printed primary metrics match v142, source diagnostics remain unmodified, unrelated warnings remain, no empty notes container is produced, and the screen requester note remains. Actual continuous and A4 downloads omit both notes and retain the report cards and expected geometry. The fixture diagnostic is injected explicitly for positive completeness-warning coverage.
- Source comparison against v142 confirms runtime changes are limited to the filename helpers, targeted monthly-renderer note removal and generated JavaScript bundle. Screen filters, source models, PDF title/header/geometry/painting, CSS and output profiles are byte-identical.
- Independent review confirmed the official English wording and scope-name coverage, Department/Section shortening, retained Office/Sector, legacy aliases and fallback behavior.
- Build consistency and JavaScript syntax checks pass. Release evidence separately records ZIP membership, CRC/manifest hashes and runtime identity. Extracted-package evidence records the same focused browser checks on the packaged app.

| Runtime asset | SHA-256 |
| --- | --- |
| `assets/js/app-bundle.js` | `d0d747e754ec824995030161ffa6c5383a17c50dd3f93f7dab6facfefcdfc63d` |
| `assets/css/app-bundle.css` | `c5dca03eb8791f003de61a1519e27d76557ec23f0eafb24d40c4cf7ab43347d4` |
| `assets/css/print-measure-bundle.css` | `b9c76b378417f9c84f09cfc9dd29252c0086172b37bff0eacc0bdd93f0163cd8` |
| `assets/js/lib/offline-pdf-engine.js` | `8038eaa52e8aa4693e6f4d9141f51edfaf78be42621384e608ddfc81d5cb2528` |

## Practical limits

Checks use the frozen illustrative workbook dated 30/09/2026, SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. No operational workbook was supplied. Workbooks and QA artifacts are excluded from the application ZIP.

Managed Chromium uses local HTTP; native Windows Explorer, Windows file-origin execution and physical printers were not tested. Entirely ASCII filenames avoid mixed Arabic/Latin direction changes. This is focused filename and note-removal verification, not a new full application or accessibility audit. Earlier release evidence retains its historical scope.
