# Performance App v175 — focused correction verification

**16 October 2026 · Design Principles Revision 39 · Desktop/PDF only**

**PASS for the targeted corrections in the tested HTTP desktop/native-PDF environment. Mac Chrome direct-file acceptance remains open.** The supplied Mac v174 reports and three actual PDFs independently demonstrated defects missed in the previous sign-off. This release corrects those defects without a new visual direction or business-rule change.

## Exact delivery and source

- ZIP: `Performance-App-v175.zip`; 7,042,886 bytes; 23 runtime files.
- SHA-256: `841a338501157ebb03146ce3221af5dd523b041ab329081f9540f79a7fbbb32c`.
- Baseline: v174 / `531e921431fe70dec57e033f143a503c0afc525c`; ZIP SHA-256 `39de0ffa055857d6983f5589c7e7454aebbd28abac46278c9cf5542c8515a99e`.
- Original dummy workbook: `Saytara-Dummy-Test-Data.xlsx`, source cutoff **30 September 2026**, SHA-256 `5de17c2ba49534dccbab911d4cd7ada234786b7fb03209bfc9b8cf5a9acb41a5`. Unchanged; no workbook is bundled or published.
- Extract the whole `Performance-App` folder. No test, source dataset or audit folder is included.

## Findings and corrections

| Finding | Original evidence | Correction and verification |
|---|---|---|
| Formal PDF contents omit labeled record counts | The supplied agenda PDF's physical page 2 has correct page references but omits labeled counts. Released code discards source count labels for all three formal reports. | Preserve each dynamically scoped source count label next to its title. Keep real final page numbers separate. All three actual reports pass unfiltered, filtered, empty and notes/editorial cases; no count is invented for a section without one. |
| Monthly PDF metadata/caption sizes | Actual supplied year/currency are 7.5pt; follow-up unit is 8pt. | Year/currency are native 10.5pt metadata; follow-up unit is native 9pt caption. Independently checked in actual outputs and again in the exact packaged download. |
| Comparison PDF metadata size | Actual supplied period and scope metadata are 10pt. | Both are native 10.5pt. Current-only output keeps its honest unavailable-history explanation. |
| SRC-SESSION-01 fallback expiry | Released source writes/restores fallback workbook binaries without a retention timestamp. This was a source finding, not an observed 24-hour Mac failure. | Same timestamp validation applies to shared storage, fallback and transfers. Reject at/beyond 24 hours; remove invalid/undated/future timestamps. Reload, transfer and fallback promotion preserve retention age. Actual HTTP browser scenarios cover boundaries and failures using a controlled clock and fault injection. |

Revision 39 clarifies these existing Revision 38 requirements. Calculations, source identities, eligibility, financial populations, filter inventories, original chart types and approved monthly thin strips remain unchanged. Fractional portfolio tick formatting and `Source.Name` in raw provenance are outside this correction set; the qualified observations were not silently restyled. Compact entity priority records remain permitted.

## Focused verification

Separate ownership prevented duplicate implementation: the main agent owned storage and release integration; the export specialist owned PDF source corrections and export runs; an independent reviewer inspected supplied originals, changed native outputs, storage evidence and the final package.

| Evidence group | Result and boundary |
|---|---|
| Original supplied PDFs | Three unchanged Mac-produced PDFs inspected natively and through readable affected crops. The typography/count omissions are corroborated. |
| PDF correction suite | **161 passing checks, 14 actual exports**, zero browser runtime errors. All-page native glyph bounds, full ordered main-record keys, correct profile, page plans, cover-excluded numbering and named destinations/link annotations checked. |
| Independent actual-PDF review | **97 passing assertions** across those same exports, with readable affected metadata, full contents, editorial and empty-page renders. This is independent review of existing artifacts, not 14 additional exports. |
| Storage suite | **31 passing checks**: actual import/reload, shared expiry cleanup, blocked shared store, current/previous fallback restore, exact 24-hour rejection, malformed/missing/future timestamps, fallback tab transfer/reload, promotion retaining age, session end and quota failure. Clock and faults are controlled fixtures. |
| Shared-storage transfer supplement | **4 passing checks**: explicit versioned save, actual new-tab transfer, reload and runtime-error check. Controlled time advance verifies a new explicit save can date a new version. |
| Exact packaged application | **26 passing checks**, including real import, existing baseline monthly populations/financial sums/metric source-row sets, approved filter inventories, entity record population, an actual monthly PDF download and browser-loaded bundle hashes. |
| Independent package review | **36 passing assertions**: exact ZIP SHA, 23 entries, every entry byte-matches frozen candidate, tested storage/PDF bundle hashes match, unchanged inventory and assets outside targeted changes. |
| Build | Existing bundle builder and `--check` pass: 85 CSS source modules, 52 JavaScript source modules, existing 23-file runtime. |

These are separate, partly overlapping evidence groups; counts are not summed into a claim of distinct end-to-end scenarios. Previous verified checks for unaffected components are reused rather than relabeled as new testing.

## Actual PDF coverage

| Scope | Agenda | Council decisions | Special projects |
|---|---:|---:|---:|
| Full source | 14 pages | 31 pages | 70 pages |
| Selected entity | 5 | 6 | 8 |
| Empty scope | 2 | 2 | 2 |
| Selected entity plus controlled editorial note | 5 | 6 | 9 |

All above use **A4 landscape**. Notes/editorial content changes are controlled presentation fixtures, restored afterward. Empty reports retain their cover/meaningful empty state and omit contents/records. The additional monthly and current-only comparison PDFs use full content-height print; both have one physical page. A further monthly PDF was downloaded from the exact extracted release ZIP.

Internal PDF destinations, annotation targets and displayed page numbers are structurally checked. Viewer clicking and copied Arabic reading order are not inferred from those checks. Native bounds cover every page; readable visual inspection focuses on affected content and selected continuation/empty cases, not every source row or pixel.

## Integrity and failed-check provenance

All released runtime entries and tested bundle hashes are recorded in [release.json](release.json). Original workbook and supplied PDFs remain unchanged. Workbooks, record screenshots and PDFs containing supplied dummy records are retained privately, not committed to the public repository.

Raw initial measurement failures remain available with passing replacements: a new-tab test wait accessed an undeclared global before page startup; a package PDF probe incorrectly required a complete Arabic currency label in one native span rather than its adjacent shaping runs; independent PDF probes initially treated a valid no-count editorial entry as counted and included non-metadata comparison body text in a metadata assertion. The corrected checks verify the intended content and actual glyph sizes. No runtime changes were made to conceal these measurement errors.

## Upgrade and remaining limitations

- Existing **undated fallback sessions are discarded** because their age cannot be proven. Select the original workbook(s) again once. Successfully saved v175 fallback records retain timestamps; reloads and transfers do not reset their retention period. The expiry applies to retained binaries; it does not promise forced erasure of an already open in-memory workbook at a timer boundary.
- **NOT RUN here:** macOS Chrome `file://` import/persistence/filter/new-tab/PDF acceptance. The supplied v174 Mac reports include partial manual startup/import screenshots and a separate successful localhost continuation; those do not certify the final v175 direct-file workflow. No automation restriction or browser security setting was bypassed. See [Mac retest](Mac-Retest-v175.md).
- The supplied Mac test scope is Chrome only. Installed Edge and Windows compatibility are not certified. Cloud runs use desktop Linux Chromium with local HTTP serving.
- No real 24-hour wait, genuine previous-month workbook reconciliation, cold native-browser restart, Excel recalculation/Power Query refresh, PDF viewer activation/copy/search or PDF accessibility certification is claimed. Controlled identical snapshot files validate restoration only, not historical activity.
- Original broad client-specific PDF text-shift reports remain subject to direct-file/viewer retesting. Changed roles and tested print geometry pass; this does not establish every client/viewer layout.
- Mobile, tablet and PowerPoint are excluded. No new whole-app audit or unrelated redesign is included.
