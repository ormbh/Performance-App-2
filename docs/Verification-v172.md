# Performance App v172 — desktop audit corrections

16 October 2026 · Design Principles Revision 36

**Verdict: focused desktop and native-PDF checks pass, with the compatibility/source limits below.** This release implements the complete app correction list approved after the consolidated audit, including the approved navigation revision. It is not a certification of every operational workbook or browser.

## Implemented

- Sticky text-only navigation on loaded workspaces, with the named monthly-report link, active-page indication and exactly three report-dropdown destinations. Original four-square shortcut appears only on search home and opens monthly. Official fonts, logo, palette and approved chart designs remain.
- Existing PDF actions align with applicable filters. Page-specific filters/settings and report links remain. Section links focus their destination below the sticky header. Modified clicks retain explicit new-tab behavior and source transfer.
- Agenda, legislation and budget-project count metrics share their named-record eligibility across totals, supporting status/category/quarter counts, denominator, exact drills and uploaded comparison snapshots. Special-project requester classification remains explicit yes versus all others. Raw rows remain imported for data review.
- Documented financial and council-register scope differences remain. A financial-scope annotation appears on monthly screen/PDF when unnamed financial rows contribute. Original workbook formulas are not modified by the application.
- Unsupported legacy aggregate detail changes are unavailable with a reason; uploaded prior workbooks are recalculated under the current definitions. Valid unrelated history remains.
- All six monthly card navigation-reference footers, including plain captions/arrows, are omitted from PDF; screen links remain. Legitimate internal PDF contents links remain.
- Council tables combine quarters into one logical table per year within each existing follow-up/other-record population. Six columns, continuous numbering, conditional decision metadata and source row order remain.
- Special-project fitting metadata fields/cards remain together. Long cards repeat their real project identity only when meaningful content continues; empty trailing decoration cannot produce a stray repeated heading. Font sizes and source text are preserved.
- Missing-status council diagnostics identify actual affected source records. Diagnostic field names use actual imported headings. Source values and statuses are not silently corrected.
- Entity page uses shared desktop gutters/Linen canvas, aligned filter label/value roles, whole-count chart ticks and common reset wording. Generated monthly zeros share the existing formatter on screen and PDF.

## Verification

The source was the previously supplied anonymized/dummy workbook with its saved report cutoff. The original workbook bytes were checked and preserved. Existing independently derived source rowsets were reused and adjusted only for the approved named-record eligibility; no replacement workbook data was invented for the source reconciliation.

- Independent source-key comparisons cover the affected metric families and preserved council/special/KPI rules.
- Desktop routes checked at1280,1440 and1920px: monthly, portfolio, entities, agenda, council, special projects, data checks, comparison, results, upload and search.
- Effective status badge fonts/colors, official192px logos, copyright footer, absence of Harvey balls, original9px monthly strips and no added in-bar monthly numerals checked.
- Actual filter open/union selection/reset, report dropdown routes/keyboard/Escape/outside click, sticky positioning and contents focus offsets checked.
- Six actual count drills checked through normal clicks and Ctrl-click new tabs against exact metric counts. Controlled department-transfer plus status-change cases reconcile incoming/outgoing effects without residuals. Pending comparison intent and uploaded source survive reload.
- Actual native PDF scenarios cover populated monthly, agenda, special projects, council, portfolio, entity and data checks; empty monthly/agenda/special/council; a deliberately long synthetic special-project narrative; and a monthly PDF from the exact extracted release ZIP.
- Checked page plans versus actual page count, approved full-PDF/A4-landscape profiles, bounds/glyphs, absence of blank/footer-only pages, cover exclusion from numbering and content numbering/copyright. All special-project metadata field associations were checked against physical page plans. Rendered page overviews and affected Arabic layouts/continuations were inspected.
-203 native internal PDF link annotations across the affected report outputs resolve to existing named destinations. No external URI navigation was introduced.
- Clean runtime ZIP has23files, no workbook/test/audit folders/PPT modules. Each extracted runtime hash matches its release manifest. Exact extracted bundle exercised under a local test server; no unexpected external runtime requests or JavaScript errors occurred.
- Bundle generation check and JavaScript syntax validation completed. An initial drill-test property error was corrected from `total` to the actual search API's `counts.all`; those12UI tests were rerun successfully. Initial named-link resolver syntax was corrected to use PDF named destinations; no application change was needed for either harness correction.

## Recorded limits

- User target is desktop Chrome/Edge opening extracted `index.html`. Managed Chromium here blocks `file://` before application loading with an administrator-policy error. Actual Chrome/Edge local-file compatibility remains **not run**; keep normal security settings. Local-server Chromium checks do not certify that target environment.
- No genuine prior-month dummy workbook was provided. Controlled movements validate logic; they do not certify operational month-to-month figures.
- Uploaded source workbook formulas/caches and auxiliary formula errors are retained unchanged. Corrected app counts can intentionally differ from old mold summary formulas that use another eligibility rule. Excel recalculation and Power Query refresh were not executed.
- No mobile/tablet, PowerPoint or screen-reader certification is claimed.

Runtime file inventory and SHA256 are in [release.json](release.json). Current requirements are in [TEC-Design-Principles.md](TEC-Design-Principles.md). No source workbook, workbook-derived screenshots or private audit data are included in this repository update.
