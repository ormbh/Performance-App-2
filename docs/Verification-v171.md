# Performance App v171 — Desktop/PDF consistency verification

**16 October 2026 · Design principles Revision 35 · PASS with the limits below**

The approved desktop consistency package is implemented. The full monthly report keeps its established composition, with the pre-v166 thin status strips restored. Source data, eligibility, metric definitions and the three detailed report chart types are preserved.

## What changed

- Consolidated principles into one current desktop/PDF standard with explicit approval precedence, component exceptions, menu order, icon policy, export profiles, legend placement, footer rules and verification requirements. Removed superseded device/PowerPoint/portrait-format requirements from the active standard.
- Shared workspace logo/title hierarchy and navigation/PDF-action grouping; entity, comparison and checks titles use the same masthead. The approved centered search-home composition stays intact.
- All ten menu destinations use text labels, in the agreed order. The trigger retains the grid icon. Page utilities are separated. Current destination, keyboard navigation, Escape/focus restoration and primary PDF actions retain shared behavior.
- Monthly strips are 9px high on desktop and 1.6mm in PDF, without in-strip numerals. Exact proportions and accessible counts remain. Missing agenda status appears as the same neutral footer on screen and PDF, instead of a PDF-only extra metric.
- Entity main tables use 18px Dubai Bold headings/16px Dubai Regular data; comparison section headings use 28px. Actionable changes and affected links reserve 44px targets. Checks cards/controls/selected colors align with the shared standard. Leadership classification keeps its pill shape, now 16px desktop/13.5pt PDF. Small Taupe-on-Linen metadata uses existing Ink where needed for contrast.
- Removed PowerPoint controls/generation paths and the three unused runtime export assets. Existing responsive code remains; no mobile/tablet work was performed.
- Full PDF print is used for monthly, portfolio, entity, comparison, results and checks. Agenda, council decisions and special projects retain A4 landscape covers/contents/tables. Old portrait choices/fallbacks are removed.
- Native PDF preparation uses a fresh complete clone after export preparation; first-click downloads do not depend on background warm-up. Very long reports continue at the same full width and readable scale at the engine's 5080mm physical height limit, with safe text boundaries and repeated table headings.
- Removed the redundant follow-up empty card when the entire monthly scope is empty. Populated report content and valid existing follow-up behavior remain.

## Verification performed

**406 focused checks passed**: 310 baseline/model/desktop/native-output regressions, 50 additional desktop/filter/sequence/empty-state checks, and 46 checks against the exact extracted clean ZIP.

- Reused existing illustrative and controlled synthetic fixtures; no supplied workbook was modified or bundled. All source items, monthly metrics and agenda/HH/council models agree with v170 on the same fixture. Rules/loader/comparison/entity calculation modules and the three chart renderers are byte-identical to v170.
- Desktop header geometry was checked at 1280/1920px and monthly layout at 1280/1440/1920px. Menu order, icon consistency, Escape/focus, filter multi-select display, real same-field union/cross-field intersection/reset, PDF states and local table naming pass.
- Exact collected screen/native-PDF record sequence agrees for the three landscape reports. Controlled monthly council completion 44→45 opens the exact same-tab metric and one contributing record; the binary pair and intent survive reload.
- 19 native PDF downloads / 47 pages were generated, rasterized and reviewed through page contact sheets and readable samples. Text/glyph bounds, approved dimensions, complete visible content, no horizontal overflow, no blank/footer-only pages, empty sections and landscape cover-excluded numbering pass.
- Large unfiltered entity and search exports each exercised full-width continuation. Monthly missing-status and final zero-result cases were exported separately. Final desktop metadata checks found no small Taupe-on-Linen pairing in the inspected eight populated workspaces.
- Final build/bundle consistency and JavaScript syntax checks pass. The extracted ZIP matches all 23 runtime file hashes. No unexpected external requests or browser runtime exceptions were recorded.

## PDF samples checked

| Output | Pages | Profile |
|---|---:|---|
| Monthly populated / missing-status / empty |1 each|Full PDF print|
| Data checks, selected worksheet |1|Full PDF print|
| Agenda, selected unit |6|A4 landscape|
| Special projects, selected unit |11|A4 landscape|
| Council decisions, selected unit |9|A4 landscape|
| Each landscape report with an empty scope |2 each|Unnumbered cover + meaningful empty-state content page|
| Entity, all entities |2|Full-width continuation; no portrait fallback|
| Portfolio |1|Full PDF print|
| Search, all matches |2|Full-width continuation|
| Comparison overview / exact metric detail |1 each|Full PDF print|
| Entity, empty |1|Full PDF print|

Counts are fixture-specific; they are not fixed report page counts. Some outputs were repeated against the final package, producing the total above.

## Remaining limits and scope

Hosted/local-HTTP **desktop Chromium** was verified. Other browsers and direct-file execution were not certified. Mobile/tablet and PowerPoint tests are intentionally excluded. The fixtures are illustrative/synthetic; no operational figures are certified by this visual change. Native Excel recalculation and Power Query refresh were not run.

Runtime ZIP: **23 files · 7,022,742 bytes**. No workbook, source tree, QA folder or PowerPoint template/font-export asset is included.

SHA-256: `a200d1a6d6c576071080f00f6b54d8bf2184b78377451b41ecd65ef6fd14beb8`
