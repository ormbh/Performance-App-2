# Performance App v130 — actual app previews

Captured from the assembled app in Chromium 151 at 100% browser zoom and device scale 1. **All report content is illustrative.** No uploaded operational PDF or source workbook is published. The illustrative workbook is excluded from the app ZIP. Images may appear reduced in a document viewer; open the original image to inspect its native pixels.

[Download v130 ZIP](https://github.com/ormbh/Performance-App-2/raw/refs/heads/main/Performance-App-v130.zip) · [Approved standard](../Design-Standard/TEC-Apple-Inspired-Design-Standard-Revision-5.md) · [Verification](../Saytara-Verification-v130.md)

| Area | Before — v129 | After — v130 |
| --- | --- | --- |
| Monthly header, navigation, print actions and filters | [Native desktop image](monthly-before-v129.png) | [Native desktop image](monthly-desktop.png) |
| Projects header, navigation and core filters | [Native desktop image](projects-before-v129.png) | [Native desktop image](projects-desktop.png) |

Both comparisons use the same 1920px viewport and illustrative source. Version 129 remains available as an earlier release.

| Current app area | Preview |
| --- | --- |
| Monthly dashboard, full content | [Full page](monthly-full-page.png) |
| Monthly mobile header/cards | [390px viewport](monthly-mobile.png) |
| Monthly mobile follow-up rows | [Readable reflow](monthly-followup-mobile.png) |
| Projects mobile | [390px viewport](projects-mobile.png) |
| Search home | [Google-like layout](search-home.png) |
| Search results | [Six-column table](search-results.png) · [Mobile table](search-results-mobile.png) |
| Upload | [Approved panel](upload.png) |
| Entities | [Shared header](entities-header.png) |
| Monthly native A4 printing | [Illustrative four-page PDF](ILLUSTRATIVE-monthly-A4.pdf) |

## Final applied sizes

| Role | Screen | Print |
| --- | --- | --- |
| Page title | DIN Arabic Regular 38px | First report title, including actual cutoff date: 24pt |
| Portfolio / card heading | DIN Arabic Regular 30 / 28px | 18 / 16pt |
| Main figures | DIN LT Arabic Regular 34–40px | 24–28pt |
| Table content, names, notes, status text | Dubai Regular 16px | 13.5pt |
| Table column headings | Dubai Bold 18px | 13.5pt |
| Change arrows | Dubai Regular 15px | 11pt |
| Retained body explanations | Dubai Regular 14px | 9pt |
| Copyright / pages | Dubai Regular 14px on screen | 10.5pt |

Subtitles beneath titles are removed. Screen report headers show only the date below the title. Primary navigation uses plain links with an active underline, and the application menu retains all utility destinations. Filters and actions use approved field/button states, readable labels and minimum 44px action targets. Project additional fields preserve selections when closed. Outside click and Escape close menus; mobile filter sheets keep keyboard focus inside.

Print has one first-page title containing the date and official logo. Later pages have no report masthead. Table headings repeat; every footer has copyright and actual page X of Y only. Printed entity filter fields are omitted while scope still determines exported rows.

## Verification

202 screen checks plus 2 focused final font checks and 21 interaction checks passed. The 12-flow native print gate passed; a separate populated comparison check also passed using the existing explicitly illustrative previous/current workbook pair. Its large page count reflects the unchanged detailed comparison report. The final extracted ZIP passes a real upload/search/details/mobile/print smoke check and all 146 manifest-file hashes.

[Release integrity](release-integrity.json) · [Clean extraction checks](clean-extraction-checks.json) · [Original source identity](source-identity.json) · [Final font checks](final-font-checks.json)

The managed browser blocks direct file:// navigation, so that mode is recorded as unrun; app behavior was verified through a local HTTP origin. Native Windows opening and physical printing were not tested. Numerical verification uses illustrative data, not the operational workbook shown in the user's screenshots.
