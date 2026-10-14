# Saytara v126 — monthly density and priority chart verification

**Verdict: PASS for the focused layout corrections and tested states.**

This release follows the approved TEC Apple-Inspired Design and the current
monthly-dashboard standard. It addresses the two requested areas: priority-chart
scrollbars and excess spacing in monthly cards, plus an existing project-print
pagination defect discovered during verification.

## Changes and evidence

The priority chart region had 1–2 pixels of vertical overflow from the axis
numerals. Its horizontal scrolling also enabled vertical scrolling, exposing a
scrollbar on platforms that paint one. Increased axis line spacing and a small
screen-only bottom inset give the font room without hiding or clipping content.

The colored priority segments already used correct common scales. Unused track
backgrounds are now transparent so a small total no longer resembles a full-width
bar. Missing-budget coverage remains written beside the actual values; missing
values do not become plotted amounts. Numeric scales and calculations are unchanged.

Monthly cards have smaller gaps between headers, metrics and supporting notes.
Existing total change controls sit beside their values on larger screens, and
agenda subtotal changes share their value row. Text sizes, content, colors and
keyboard actions are retained. On narrow screens the total controls retain room
to stack. These density adjustments are screen-only.

The review also reproduced a masthead-only opening page in comfortable A4 project
reports with partial budget data. The complete v125 bundle produced identical
opening-page pixels, confirming that this defect predated the release. A narrowly
scoped print rule now lets a long finance card continue across pages; its financial
blocks, calendar groups and table rows keep their existing keep-together rules.
The finance-right / schedule-left composition is retained. Other project print
sizes and densities retain their existing rules.

| Monthly card | v125 height | v126 height | Reduction |
| --- | ---: | ---: | ---: |
| Annual agenda | 410 px | 322 px | 88 px |
| Council decisions | 343 px | 291 px | 52 px |
| Legislation | 414 px | 356 px | 58 px |
| Special projects | 416 px | 354 px | 62 px |
| Strategic-budget projects | 932 px | 864 px | 68 px |

These measurements are from the same illustrative workbook with native embedded
history at 1920/1500/1024px, comparing complete generated bundles. They describe
layout density, not the user's operational figures. Card heights vary with source
content, scope and history.

## Verification

- Priority checks passed across 36 states: full and partial budgets, widths
  1920/1500/1024/390px, device scale factors 1 and 1.25, CSS zoom at 125%, and
  A4/A3 print with both project density settings. Screen regions have no vertical
  scroll range. Both mobile chart regions retain keyboard horizontal scrolling.
- Segment widths match an independent Excel-derived oracle and the common axis
  within 0.2 CSS pixels. Partial coverage captions remain visible. All eight
  affected priority print pages were rendered and visually inspected.
- Monthly checks passed across 20 viewport/history states, including embedded
  history, a separately supplied previous fixture, unavailable history, partial
  source data and an explicitly labeled arrow-markup stress case. The uninjected
  built app matches the measured final layout. Values, models, typography and
  arrow facts are preserved. Moved controls support keyboard activation and retain
  target sizes of at least 28px.
- Monthly print text and geometry match v125. A4 remains two pages and A3 one;
  all three monthly pages were rendered and visually inspected.
- A separate independent review passed 12 monthly and 10 priority/report states,
  verified the actual DIN Next Arabic/Dubai font resolution, and inspected 11
  rendered PDF pages before the targeted pagination correction. The pagination
  follow-up checks full/partial budgets with and without separate previous-file
  history. Numeric source tokens, fonts and text sizes remain intact; the opening
  page now includes the paired report content in the affected A4 states.
- Final saved-code pagination checks passed all four comfortable A4 cases in two
  independent runs. Every printed business-number token matches the pre-fix
  baseline after accounting for the per-page copyright year. All eight affected
  first/second pages were visually inspected. Twelve A3/A4 compact cases remain
  identical in text and rendered pixels. Final priority scales and captions still
  pass. Partial-budget continuation pages can remain sparse because each financial
  block stays intact; this is a targeted opening-page fix, not a full pagination
  redesign.
- Strategy remains physically below legislation. Completed legislation remains
  green `#01831E`, including completion after its deadline; late remains red
  `#C00000`. Approved section positions, terminology and table rules are retained.
- The v125 contrast fixes remain in place: TEC ink on linen, 6.993:1, for the
  monthly legislation note and screen project comparison note.
- All 51 JavaScript files, including 15 model modules, are byte-identical to v125.
  Fonts, logos and brand assets are unchanged. Only two source CSS files, the
  generated CSS bundle, build/cache version and release documentation changed.
  Bundles match their 50 CSS and 47 JavaScript source files.
- Release packaging verifies the clean-extracted file set and every manifest
  SHA-256 hash. QA fixtures and operational workbooks are excluded.

Evidence is retained outside the app under `/workspace/saytara-work/qa-v126`:
`priority-implemented-evidence.json`, `monthly-density-evidence.json`,
`monthly-density-review.md`, `source-integrity-evidence.json`, rendered screen
crops and print pages, independent review and pagination follow-up records, plus
package and GitHub download integrity records. The focused chart/density evidence
precedes the additional print-only finance correction; its follow-up records the
final bundle and affected print states.

Final CSS bundle SHA-256: `c30537ce3a56db786e97fea150b323a2f6276be41a7c7beee819d7697771177e`.
Final JavaScript bundle SHA-256: `1516e7aca83caeb3ca09d7c251563a5984c08c47f09ba23aefb4c4d75ebca140`.

## Scope and limits

These are targeted TEC design, Saytara QA and dashboard-accessibility checks in
managed Linux Chromium, not formal accessibility or Apple certification. Main
skill instructions and approved assets were available. Linked skill reference
pages that were previously provider-unreadable remain a recorded limit.

The original mold and its title-required formulas are unchanged, as requested.
Its operational title columns are blank, leaving title-required totals at zero
while some native subgroup/status formulas count unnamed rows. The operational
`TEC Performance Report Sep2026_v2.xlsx` shown in screenshots was not uploaded;
production totals are not verified. Populated checks use illustrative QA sources.

Native Windows file protocol, native Windows scrollbar painting, screen-reader
and native browser zoom checks were not run. Device-scale and CSS-zoom simulations
are separate checks. No Excel recalculation, Power Query refresh or native
PowerPoint verification was performed. Earlier audits describe their own releases;
this report covers the v126 layout corrections.
