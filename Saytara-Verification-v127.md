# Saytara v127 — monthly reference implementation and legislation status display

**Verdict: PASS for the reference implementation and tested source states.**

The monthly dashboard was rebuilt from the actual HTML/CSS source of the user’s
attached reference, rather than applying density adjustments to the legacy page.
The reference image is 2880 × 4772 pixels, rendered at 1440 CSS pixels/DPR 2.
Its SHA-256 is `fda6577d2c84651356c8bc9986f39c98a8dcfee03a5383d8076f27cf09029e09`.

The live implementation follows its masthead, physical title-left/logo-right
placement, monthly/projects tabs, three open scope filters, two portfolio columns,
rounded cards, separate quarter boxes, strategy below legislation, financial
ledger and full-width follow-up table. Search, upload, reports, comparisons,
source details and print settings remain available from compact controls.

The user explicitly retained the earlier exceptions to the literal image:
completed statuses are green `#01831E`, late statuses red `#C00000`, item names
neutral `#4F4E4E` at weight 400, and empty status/priority groups hidden. Follow-ups
keep late → frozen → cancelled → transferred ordering, stable within each group.
Agenda wording is الأجندة المعتمدة and المواضيع المستجدة. The approved-budget
heading omits the internal revised suffix. There are no repeated bar legends
where the values above already identify the segments. Small neutral labels use
approved TEC ink on linen for 6.99:1 contrast; frozen pills retain taupe on paper.

## Legislation and progression

Late legislation appears beside the other status metrics and contributes a red
segment to the bar on screen and in native A4/A3 monthly exports. `legPending`
counts titled, in-progress records that are not late; its drilldown selects that
same cohort. Existing workbook metrics, including `legProgress`, remain intact.
The illustrative QA example reconciles as 152 on time + 28 completed after the
deadline + 9 nonlate pending + 2 late = 191; the original in-progress count is 11.
Both completed categories remain green. The SLC explanation appears once below.

Change controls sit below associated values, with isolated ↑/↓ direction and
amount, without moving their numeric columns or overlapping bars. Changes use
comparable source values only. Uploaded previous workbooks use the exact same
item-level pending metric. Embedded pending history requires complete, valid
components, compatible scope and cutoff, and consistent current cohort membership;
missing, conflicting or ambiguous history does not generate an arrow. Overlapping
source statuses retain their values and receive an explanation instead of a
misleading double-counted status bar.

## Verification

- 86 meaningful model checks passed: unchanged existing metrics across the
  illustrative and adverse sources/scopes, exact pending-drill membership,
  embedded and uploaded prior values, missing titles/columns, date mismatches,
  partial or conflicting history, and overlapping status guards.
- 81 independent screen checks passed, plus 12 complete style states across
  1440/1920/1024/390px and unavailable/embedded/uploaded history. No body overflow,
  bar/value or arrow/value overlap, runtime error or external request was found.
  The history fixture displays 28 valid arrows; unavailable history displays none.
- Keyboard and route checks passed for the native sector/unit/entity selectors,
  unions and dependent units, Escape, reset focus, utility/report menus, source
  details, print settings and no-source recovery. Pending and late drills select
  exactly 9 and 2 matching illustrative records respectively.
- Native A4/A3 exports passed metric, segment-width, color, row-order, text and
  page-bound checks. All five resulting PDF pages were rendered and visually
  inspected: populated A4 two pages, populated A3 one page, and the supplied
  blank-title mold one page in either size. A4 summary spacing was reduced by
  approximately 7mm using whitespace only, preserving fonts and the existing
  source-comparison warning rather than stranding strategy on another page.
- Local fonts/logo and the literal layout source were checked against the reference.
  Paired special-group amounts, bars and captions stay aligned when only one
  group has a genuine subtotal or status change; wrapped legislation labels
  also share their amount baseline. This was checked separately after the full
  independent screen gate. Native print styles remain identical after this
  screen-only alignment adjustment. No unavailable arrow or placeholder history
  is fabricated.


The exact reference geometry is matched where applicable: at 1440 CSS pixels,
canvas x52/width1336; columns x52 and x731/width657 with a 22px gap; first cards
y392.5; 18px card radii, 25px/26px padding, 23px headings and 39px totals. The
reference header, logo, tabs, filters and print control match within 0.1px. Card
heights vary with the confirmed exceptions, source text and valid history; this
is not a claim of identical pixels to an illustration with different visible
statuses and data. Small labels changed only to approved contrast pairings.

The full screenshot shipped alongside the release is generated by the actual
v127 app using an explicitly illustrative QA workbook with native embedded
history. It is visual evidence, not the user’s operational workbook.

Only `rules.js` changed among the 15 model modules, adding the pending metric and
its guards; the other 14, all fonts/images, and all project/search/upload source
styles are unchanged from v126. The focused project priority scale/scrollbar and
comfortable-A4 pagination fixes from v126 are retained.

## Source and practical limits

The attached Saytara_2026_Mold_v2.xlsx remains unchanged. Its operational title
columns are blank. The user’s title-required formula preference is preserved;
nonempty status cells do not create titled operational records. The operational
TEC Performance Report Sep2026_v2.xlsx shown in screenshots was not supplied,
so its displayed numbers have not been reconciled to the original source. QA
workbooks and test code are excluded from the app package.

Verification used managed Linux Chromium and native text/vector PDFs. Windows
Chrome/file-protocol rendering, native browser zoom, screen-reader certification,
Excel recalculation/Power Query and native PowerPoint checks were not run. Some
linked skill resources were provider-unreadable; available main TEC Apple-inspired,
Saytara QA, analysis and accessibility instructions and the latest user rules
were applied. No source workbook edits, live publication/deployment of a website,
or invented production history are included.

## Release integrity

The ZIP contains a SHA-256 manifest for every delivered file except the manifest
itself. Clean extraction, the complete file set, all hashes, bundle rebuild
checks and build marker 127 were verified. The standalone audit, application ZIP
and illustrative live-app preview are recorded in the repository SHA256SUMS.
Downloaded GitHub artifacts were verified against the locally reviewed release.
