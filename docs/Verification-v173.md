# v173 — desktop consistency corrections

This release implements the owner's post-v172 approval: four main portfolio filters, five main entity filters, contents only on the three formal reports, stable workspace logos and functional section navigation. It preserves the existing metric definitions and chart designs. Design Principles Revision 37 supersedes conflicting earlier filter/contents inventories.

## Delivered changes

- Portfolio and its formatted report: sector, organizational unit, concerned entity and project manager. Removed filter dimensions remain useful chart/record dimensions; old routes cannot silently reactivate invisible page constraints.
- Entity report: the same four fields plus domain. PM uses the source project-manager field, without substituting a coordinator. Main filter matching, previous/current rows, URL state, exact drills, reset and printed scope share that basis. Concerned-entity selection stays distinct from contributor context.
- No contents blocks on portfolio/entity screen or PDF. Existing meaningful summaries, sections and chart-specific legends remain; generic overview headings are absent. The three formal reports retain working contents and internal PDF destinations.
- Stable 192px workspace logo at physical right/top, including results; intrinsic image dimensions reserve its aspect ratio before loading. The centered search landing and landscape covers retain their approved compositions. Results logo uses the shared monthly destination.
- Bare local section fragments no longer enter the app route parser. Existing formal-report jumps retain scroll/focus behavior. Unavailable local destinations keep the current page and report their unavailable scope.
- Direct main filters have consistent reset captions and no obsolete disclosure controls. Comparison's extra filter-card padding was removed so its PDF action aligns with its fields, using the shared desktop gutters.

## Source and method

Used the unchanged supplied dummy `Performance_2026_Mold_v4.xlsx`, cutoff 30 September 2026; SHA-256 `5de17c2ba49534dccbab911d4cd7ada234786b7fb03209bfc9b8cf5a9acb41a5`. These are test records, not operational figures. The original workbook was not changed. No Excel recalculation or Power Query refresh is claimed.

Reused v172's verified source memberships, calculation definitions, financial/council scope exceptions, formal-report geometry and existing test helpers. Unfiltered monthly totals, every metric's exact source rowset and financial values agree with that baseline. New entity tests independently calculate field unions, intersections, blank selections and empty selections from source rows. A controlled PM transfer verifies previous/current scope without claiming a real historical movement.

## Checks and evidence

- Focused source/UI/PDF suite: **249 checks passed**, including 13 native PDF scenarios (seven populated workspaces, a filtered entity view and five empty report/workspace views).
- Navigation/roles supplement: **32 checks passed**. Actual global navigation, report dropdowns, monthly footer destinations, project list/record links and a Ctrl-open entity drill were activated. New-tab PM/domain scope remains intact.
- Extracted-package suite: **101 checks passed** on the initial candidate. A final comparison alignment check then found padding offsetting the PDF button; it was corrected, not waived.
- Final affected-control suite: **14 checks passed** against the corrected extracted package, including comparison alignment/bounds, monthly follow-up row/column parity, project PM selection/reset, entity historical scope and unconfirmed-date fallback.
- Final release suite: **28 checks passed**, including final ZIP/inventory hashes and actual packaged monthly, comparison and A4-landscape agenda downloads.
- Desktop widths: 1280, 1440 and 1920 CSS pixels. Logo x/y/width/height were checked after images loaded; at 1440px all workspace logos use x=1200px, y=105px, width=192px. No mobile/tablet tests.
- PDF checks cover final page count/profile, glyph bounds, horizontal overflow, blank/footer-only pages, working internal destinations, record order and screen-only command removal. Empty views omit empty contents/record groups. Formal covers remain outside content-page numbering.
- Formal-report text regression compared every page: agenda 14, council 31 and special projects 70 pages preserve v172 text, type sizes and positions. The final packaged agenda was compared again on every page. Existing formal chart types and record sequence are retained.
- Monthly strips retain the approved 9px desktop / 1.6mm PDF treatment without added in-bar counts. Card references remain screen-only; the documented financial-scope note remains in PDF. Approved fonts, colors, badges and the offline PDF core are retained.

## PDF alignment report: not reproduced

The owner reported shifting text throughout the monthly PDF and other reports. Checks therefore cover title/logo placement, card title/total roles, status labels/figures and follow-up table content/order. Native text advances were compared with the final browser print layout; the largest measured monthly width difference was below **0.04pt**. Sampled print/native renders agree after the documented paper inset. The six monthly cards retain title-right/total-left roles, and follow-up rows/columns match.

This does **not** establish that the owner's reported issue is fixed. No broad PDF alignment or font redesign was applied without reproducing the defect. Paper margins, pagination, approved PDF type roles and the approved monthly date-bearing title intentionally differ from desktop pixel coordinates. A user-environment example may still reveal a discrepancy absent from these tests. Copied/extracted Arabic text reading order is not separately certified.

## Compatibility limits

Native downloads and extracted runtime were tested in desktop Chromium under a local test server. Direct `file://` navigation was attempted in an independent context accepting local resources, but the managed browser rejected it before application load with `ERR_BLOCKED_BY_ADMINISTRATOR`. Actual extracted-file Chrome/Edge compatibility remains **not run**; this is an environment limitation, not a passing application test. No browser-policy bypass or user security-setting change is recommended.

No genuine previous-month workbook was supplied, so real month-to-month movements are not certified. Existing unaffected source/metric contracts reuse v172 evidence; this is a focused regression release, not a claim of another complete application audit.

## Artifact

`Performance-App-v173.zip` contains 23 runtime files, with no workbooks, CSVs, tests, audit screenshots or PowerPoint exports. The exact checksum, byte count and runtime-file inventory are in [release.json](release.json). Full PDF is retained for other pages; only agenda, council decisions and special projects use A4 landscape.
