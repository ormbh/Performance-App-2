# Performance App v129 — verification

**Verdict: PASS for the approved design and tested workflows.**

Implementation reference: the user-approved `TEC_Apple-Inspire_ Design_standard.md`,
revision 2, plus the approved Google-like search home, six-column results table
and upload panel. The original standard is included as `DESIGN-STANDARD.md`.
Verification date: 11 October 2026. Baseline: Performance App v128.

## Scope and method

This is the actual bundled application, not a stylesheet-injected mockup.
Chromium on Linux was used at device scale 1 and normal browser zoom. Browser
screens, computed font roles, native interactions and rendered native PDFs were
checked. Desktop and mobile views were reviewed independently for search.

Test workbooks were kept outside the delivered app. The primary fixture was
`ILLUSTRATIVE-monthly-preview.xlsx`, SHA-256
`4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`.
It is explicitly illustrative and contains 672 records. Project regression also
uses the synthetic current/previous QA workbooks retained from the earlier
84-project regression suite. No fixture records are bundled with the app.

## Source regression

- All 29 bundled model, library, font and image files are byte-identical to v128.
- Imported source records, report date, monthly counts, budget, KPI and comparison
  metadata match the same fixture loaded in v128 exactly.
- The project model matches v128: record keys, totals, eligibility and financial
  cohorts, source progress, ranked manager portfolios, follow-up issues and
  priority/type intersections. Historical comparisons retain their definitions.
- Search query `استراتيجي 006` returns the same four source keys in the same order:
  `secretariat-7`, `council-51`, `agenda-7`, `council-7`.
- Count zeros use a dash with accessible zero meaning. Genuine recorded 0%
  completion remains 0%, including in details and PDF. Unavailable values are not
  converted to zero. View changes do not create a source status or comparison.

## Screen and interaction checks

Monthly: 1920, 1440, 1024 and 390px. The approved 38/30/28px DIN heading hierarchy,
DIN LT regular figures, 18px Dubai Bold table headings, 16px regular neutral
names/notes and 15px change arrows are present. Layout fits the viewport; mobile
reflows. Strategy remains below legislation. Empty status groups remain hidden,
legislation lateness is adjacent to the other statuses and included in the bar.
The utility menu dismisses outside or on Escape; Escape restores focus. An empty
follow-up scope shows a dash, while meaningful completion 0% remains visible.

Projects: 1920 and 390px. Paired sections, approved font roles and neutral source
names are preserved. Only populated H/M priority groups appear in the fixture.
Priority charts have no internal vertical scrolling; genuinely wide comparison
and calendar tables retain local horizontal scrolling at readable text sizes.
Follow-up order remains late, frozen, cancelled, transferred. Actual source
notes, chart scales, financial coverage and exception explanations are preserved.

Search: all six columns checked at 1920, 1280 and 390px. Names/values use neutral
Dubai 16px Regular, headers Dubai 18px Bold. No overall mobile overflow; the table
scrolls in a named keyboard-focusable region. Native sorting, column selection,
category tabs, status filters, suggestions, clear-query return, record details,
focus return, menu outside/Escape dismissal and menu arrow keys pass. Browse
shows 672 fixture records in 50-row screen pages; page 2 changes the visible rows.
CSV exports all 672 matches plus its header, rather than only the current page.
No-results export is disabled. Completed-after-deadline legislation remains green;
unfinished late legislation remains red. Search has one 2px teal focus ring.

Upload: actual assembled bundle, no CSS injection. Desktop 1040px panel and 390px
mobile panel, approved title38/dropzone28/support14/control16 sizes, readable
focus, minimum44px targets and local processing pass. Pointer, Enter and Space
open the native chooser. Loading the fixture succeeds. Invalid replacement or
dropped files retain the identical current data object and show an alert. Loading
blocks duplicate reads and disables secondary navigation. Current-file return
and comparison navigation pass. Header/footer use fluid48/32/16px gutters, and
busy controls use the approved Ink/Linen/Silver disabled treatment.

## Browser print and PDF

Monthly native A4/A3 and scoped A3 reports were checked. Text uses the approved
separate print scale: title24pt, portfolio18pt, card16pt, table13.5pt and change11pt.
The full fixture uses four A4 pages or three A3 pages at the readable scale.
Follow-up headings and table headers repeat appropriately; page count follows
content. Rendered pages were visually reviewed for clipping and orphan headings.

A real selected entity scope reduces the monthly fixture's agenda117→4,
council70→3 and special projects62→1. Source hashes remain unchanged. The entity
field, filter label and selected entity value are omitted from print headers;
filtering remains active. Entity names in source table content remain visible.
The same print-only display-scope separation is verified in projects.

Search prints all four matches in two A4 landscape pages, with repeated six-column
headers, 13.5pt regular neutral names/body, 13.5pt Dubai Bold headings, natural
wrapping, unembellished query highlights and a repeated10.5pt footer. Both rendered
pages were reviewed without clipping or overlap; extracted text is within bounds.

Projects native A4 pages were reviewed with the same readable table scale, natural
wrapping, rebalanced chart-table columns, repeated follow-up headers and complete
notes. Project print retains A4/A3 options, 10mm margins and density settings.
The legal footer uses10.5pt rather than the inherited7pt scale. Numeric calendar
labels are kept together; complete year groups may paginate instead of pushing a
blank first page. No text-size reductions or data changes are used to fit pages.

## Release integrity

Readable source modules and their matching local bundles are included. Python
bundle consistency checks and JavaScript syntax checks pass. The release pipeline
checks ZIP integrity, a complete clean extraction and every manifest SHA-256.
The extracted package is browser-smoke-tested with native import, search, details,
monthly/projects typography, mobile fit and current-file navigation. The package
contains no QA workbooks, generated PDFs, CSVs, fixtures or test caches.

## Limits

The operational workbook shown in the user's screenshots was not supplied for
this release. The source-regression verdict applies to the stated QA fixtures,
not unseen production figures. CSV scope/count was checked; this release does
not claim independent field-by-field reconciliation of every exported record.
Browser tests used local HTTP because managed Chromium blocks native file URLs.
Windows/macOS double-click startup, physical printing, screen-reader speech,
Excel recalculation/Power Query refresh and PowerPoint editing were not run.
The unchanged app calculations still read cached Excel formula values. A visual
and keyboard review is not full accessibility certification. Other unrelated
report/export workflows were not newly exhaustively retested.
