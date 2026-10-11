# Performance App v128 — monthly sizing, interactions and native print

**Verdict: PASS for the monthly refinements and tested source states.**

The approved TEC Apple-inspired monthly direction is retained. The latest eight
refinements govern this update: fluid width at normal browser zoom, removal of
the obsolete monthly eyebrow, removal of the supplemental not-started/transferred
row from the monthly strategic-project card, outside-click utility-menu dismissal,
zero metrics displayed as a dash, “مقارنة:” in the single bottom SLC explanation,
and a native print view that follows the approved design instead of the older
compact report template.

## Screen and interaction

The fixed 1440px maximum is removed from the monthly canvas and aligned legal
footer. At 1920 CSS pixels and browser scale 1, content is 1824px wide with 48px
side gutters, compared with 1336px in v127. At 1440 it is 1344/48px, at 1024
960/32px, and at 390 358/16px. A 32px desktop top inset replaces 40px.
Approved TEC DIN/Dubai fonts, numeric hierarchy, card radius, spacing and arrow
alignment are retained; widening does not magnify the text.

The hamburger closes in place when clicking or moving keyboard focus outside it.
This avoids a redraw that could interrupt the clicked filter or control. Nested
reports, route actions, Escape focus and native mobile touch remain functional.
Zero metric counts, quarter values and the empty follow-up count display `-`;
genuine completion captions retain their source percentage, including 0%.
This is a presentation change only; accessible zero/missing semantics,
source counts and chart baselines are preserved. The removed extra row does not
remove transferred records from follow-up tables or change the source total.

## Native print

The native monthly template now uses the approved TEC masthead, warm rounded
cards, two portfolio columns, separate quarter boxes, budget ledger and neutral
follow-up table. Legacy RAG edges and the duplicate strategy total are removed.
Totals use 22pt and status values 18pt. Source-backed changes remain in aligned
tracks below their values. The approved budget heading and amount share a row
to fit physical paper without changing either value.

The populated illustrative report occupies two A4 pages: complete summary on
page one, complete follow-up table and source/history warning on page two.
The populated A3 report also uses two pages so the table stays intact and
readable. The tested governance-unit scope fits one A3 page with two follow-up
rows; both A4 and A3 blank-title mold outputs fit one page. A3 continuation
tables repeat compact report/date/TEC context. A single-page A3 guarantee is
not made for every scope or table length.

All nine final PDF pages were visually inspected, including the separate
background-graphics-off A4 output. Green, red, taupe, teal and linen native
fill counts match the background-on output, preserving chart meaning. Every
page contains the official TEC image, native selectable text and vector
drawings. Arabic shaping, 39 / 54 direction, full notes, page boundaries and
source values passed. The current-source outputs checked 37 metric cells and
28 valid arrows each; the governance scope checked 30 cells and 11 arrows;
the mold checked two KPI cells and two valid arrows per output. An independent
print gate passed 52 checks plus visual inspection of those nine pages.
No clipping, overlapping cards, blank page or warning-only page was observed.

## Verification and source scope

Eight sizing cases passed: embedded/no history at 1920/1440/1024/390 CSS
pixels and scale 1, with no body overflow or runtime error and unchanged
source values. Paired special-project values/meters and wrapped legislation
values remain aligned. The original source history produces 28 valid arrows;
unavailable history produces none.

The menu-specific suite passed 28 actual-app checks, including repeated
open/close, outside clicks, clicked filter preservation, Tab exit, nested
reports, routes, Escape focus, settings and mobile touch. An independent
screen gate passed 71 checks spanning width, wording, zero display, menu
interaction, exact status colors, neutral table names/order, arrows and the
uploaded blank-title mold. Nine final rebuilt-bundle checks also passed at
1920 and 390px. No runtime error or unexpected external request
was observed. A local file-protocol browser check was NOT RUN because the
managed Chromium policy returned ERR_BLOCKED_BY_ADMINISTRATOR; it was not
bypassed. Actual bundled application checks used local HTTP.

All 15 model source modules, fonts and images are byte-identical to v127. No
source workbook was modified. The existing source totals, denominators, pending
projection/history guards, filters and follow-up order remain authoritative.
Completed statuses, including completed after deadline, remain green #01831E;
late is red #C00000; table names are neutral #4F4E4E at weight 400; zero/empty
status and priority groups are hidden. Late legislation remains beside the other
statuses and contributes to a disjoint red segment; SLC appears once below.

The supplied blank-title mold is tested separately and retains title-required
formula eligibility. The operational TEC September workbook shown in the user's
screenshots was not supplied; its operational figures cannot be reconciled to
source. Preview image and native PDF use an explicitly illustrative QA workbook
with embedded history, not invented operational history. QA workbooks/scripts
are excluded from the app ZIP.

Managed Linux Chromium is used for browser and native PDF checks. No Windows
Chrome/browser-UI print-dialog or screen-reader certification is claimed. No
Excel recalculation/Power Query or PowerPoint output is included. Linked TEC
skill resources remain provider-unreadable; available main TEC Apple-inspired,
Saytara QA, accessibility and export instructions and current approved assets
were used. The user's latest directions supersede older skill defaults.

## Release integrity

The ZIP is built from the verified v128 source and includes a SHA-256 manifest
for every app file except the manifest itself. A clean extraction verifies
the complete file set, every manifest hash, the v128 build marker and both
generated bundles. Test workbooks, QA scripts and preview PDFs are excluded
from the app ZIP. The native PDF and screen preview are published separately
and explicitly identified as illustrative test data.

GitHub release files and their checksums are verified again after downloading
from the exact published commit. Existing release artifacts are preserved.
Publication and extraction evidence are retained outside the app package.
