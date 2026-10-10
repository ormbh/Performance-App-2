# Saytara v123 verification — TEC Apple-inspired implementation

Review date: **11 October 2026 (Asia/Dubai)**. Source reporting cutoff: **30 September 2026**.

**Verdict: PASS with source limitations.**

## Implemented scope

The approved monthly and projects illustrations are implemented as live, workbook-driven interfaces, including their native browser report/print views. Search home/results and local workbook upload use the same TEC design method. The uploaded workbook is preserved. Attached-document instructions were not treated as additional user authorisation.

- Exact TEC palette, logo, Dubai body font and DIN Arabic headings are retained. The page uses linen `#EFEBE7`, paper cards `#FCFBFB`, consistent 12px screen card corners, restrained depth, clear controls and visible keyboard focus.
- Monthly executive portfolios remain on the physical right, projects on the left. Strategy stays below legislation in the executive column. The cutoff and scope appear below the screen title.
- Projects have three paired rows: finance right/schedule left, status right/manager portfolios left, priority counts right/budget left, followed by the full-width five-column follow-up table. The extra five-card summary is removed.
- Both tables use plain names in neutral `#4F4E4E`, weight 400. Status labels retain meaning: completed green `#01831E`, unfinished late red `#C00000`, frozen taupe/stone, cancelled charcoal and transferred grey. Completed legislation after its deadline is green and remains distinct from unfinished overdue work.
- Follow-up order is **late → frozen → cancelled → transferred**, stable within each group. Frozen uses the display label «مجمّد» without rewriting source values. Projects qualify when frozen, cancelled or transferred, or unfinished active/not-started with a valid source deadline before cutoff. Comments alone and future not-started projects do not qualify. Each project appears once.
- Completion bars and valid previous-report ↑/↓ remain. Empty/missing status and H/M/L visual groups are omitted while records remain in totals and source review. Zero completion remains distinct from missing completion. Empty notes are hidden only in mobile cards; meaningful notes remain complete.
- Legends are omitted when the same parts are already identified by direct labels. Wording uses «الأجندة المعتمدة», «المواضيع المستجدة» and «الموازنة المعتمدة». The legislation subtitle is «مراجعة التشريعات ومتابعة الإنجاز»; its SLC explanation appears once at the bottom.
- Search keeps suggestions, tabs, exact filter semantics, sorting, pagination and exports. Upload keeps keyboard selection, drag/drop, error recovery, current-file retention and local processing. No new upload service or file format is introduced.

## Source and data checks

GitHub baseline: **Performance-App-v122.zip**, SHA-256 `79700f71e47f0a1e320bdf700f82ec143c46c407da76381ad62d1a4a83800640`.

Authoritative user source: **Saytara_2026_Mold_v2.xlsx**, SHA-256 `1638e2d9e194c21d8d8e258a2bcad7c121cbeb9a4f529f90cea632f212cc66f2`. Source and QA workbooks are unchanged and excluded from the release.

| Check | Outcome and evidence |
| --- | --- |
| Workbook/model regression | PASS: 56 scoped project/monthly comparisons match v122 for all non-follow-up metrics, money, progress coverage, source cutoff and native history differences. Only the authorised portfolio follow-up model changes; the other 14 model modules are byte-identical. |
| Arithmetic and cohort reconciliation | PASS: 13 existing project arithmetic checks and 10 focused project contract checks. Manager ranking, financial cohort denominators, schedule grouping and reconciliation remain native. |
| Deadline/follow-up boundaries | PASS: 20 cases cover valid/invalid/missing dates, cutoff boundaries, unfinished overdue work, completed-after-deadline exclusion, uncommented frozen/cancelled/transferred inclusion, classification and stable order. |
| Scoped table consistency | PASS: 10 final scope checks confirm both tables derive the qualifying records without changing unrelated dashboard totals. |
| Actual source limitations | PASS with limits: the supplied mold has no eligible named projects, so its project total remains 0. Missing project names and financial fields are not replaced with examples or zero assumptions. Native legislation figures 152/28 and KPI coverage 39/54 are preserved. |
| Comparison integrity | PASS: exact unique-key matching and period confirmation remain required. Test snapshots have 607 exact matches; 65 Council missing keys per period remain quarantined. No Council movement is invented. |
| Follow-up progression | PASS: confirmed test pair gives monthly ↑2; a separate browser-only reduced population verifies ↓1. Embedded, unconfirmed, invalid-period, missing-key, duplicate-key and unavailable-metric comparisons suppress this derived follow-up arrow. No operational previous report was supplied. |
| Rounding and semantics | PASS: native averages are unchanged; screen and print display 83.2%/87.8% in the illustrative fixture. Zero, missing and unavailable comparison remain distinct. |

Populated tests use explicitly synthetic fixtures and the same approved anonymised current/previous illustration pair dated **30/09/2026** and **31/08/2026**. Their names, budgets, notes and historical differences are test examples, not operational records or app defaults. The app starts with local workbook selection and contains no QA datasets.

## Interface and export checks

| Check | Outcome |
| --- | --- |
| Native app and build | PASS: Chromium loads the actual app; all source JavaScript and generated bundles pass syntax checks; 50 CSS and 47 JavaScript modules rebuild consistently. |
| Desktop/tablet/mobile | PASS: 1500, 1024, 768 and 390px affected views retain scope/content, readable controls, correct desktop pairings and no page-level horizontal overflow. Dense tables have labelled local scrolling; mobile follow-up cards retain meaningful notes. |
| Fonts/Arabic | PASS: supplied Dubai and DIN faces resolve; Arabic shaping, RTL and isolated numeric/date fractions were inspected. The pre-existing local-only Ample English heading preference uses its documented Dubai fallback when Ample is not installed; no commercial Ample font is added. |
| Search/upload interaction | PASS: 11 meaningful checks cover explicit/Enter search, suggestion arrows/Escape, tab keyboard focus, filtering/chip/reset, pagination/all-row print, no-match recovery, invalid-file retention, disabled/named loading, keyboard chooser and real drag/drop. No browser runtime errors or external data requests were observed. |
| Screen/print table semantics | PASS: normal-weight neutral names, requested category order, completed green, late red, current figures and valid arrows agree. |
| Browser PDF output | PASS: all 17 pages across six final native files were individually opened and inspected; no clipping, partial rows, blank pages or broken RTL. Projects A4 comfortable/compact: 4/4 pages; A3 comfortable/compact: 3/3. Monthly A4/A3: 2/1. Table headers repeat on continued project pages; A4 header separation, warm surfaces, mobile empty-note handling and the overdue arrow baseline were checked after correction. |
| Accessibility scope | Keyboard/focus, labels, contrast pairings, responsive layout and reduced-motion behavior were inspected. Screen-reader certification and full WCAG conformance were not tested or claimed. |

Print retains complete source notes and chart values; page count follows content and paper/density preferences. Browser testing uses Chromium over local HTTP; Edge, Firefox and Safari were not independently exercised. Direct `file://` smoke testing was not run because managed Chromium blocks that navigation (`ERR_BLOCKED_BY_ADMINISTRATOR`); the policy was not bypassed. Actual local workbook processing and complete local assets were verified over HTTP. PowerPoint authoring/export code is unchanged and was not re-rendered for this styling release. No Excel recalculation or Power Query refresh was performed or claimed. Font licensing provenance remains documented in `FONT-ASSETS.md`.

## Release integrity

The final ZIP is checked by clean extraction, complete file-set and SHA-256 manifest verification, bundle consistency, and an actual app/workbook smoke test. It includes readable source modules, generated bundles and this audit, without workbooks, QA scripts, caches, credentials or synthetic data. The per-file manifest is `release-manifest.json`; package and audit hashes are published in the repository `SHA256SUMS`. Public downloads are checked against those hashes before handoff.
