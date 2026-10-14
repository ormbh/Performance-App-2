# Performance App v130 verification

**Verdict: PASS for the approved design and tested workflows.**

Verified 11 October 2026 against the approved TEC Apple-inspired Design Standard Revision 5. Baseline: Performance App v129. Tests exercised the assembled application, without injecting substitute CSS or application modules. Browser: Chromium 151.0.7922.173 on managed Linux, device scale 1 and normal browser zoom.

## Implemented contract

- DIN Regular page/portfolio/card titles at 38/30/28px; DIN LT Regular figures at 34–40px. Dubai Regular table names, notes and statuses at 16px; Dubai Bold column headings at 18px. Neutral source names, approved status fills, 14px retained body explanations and 15px changes.
- Generic subtitles removed beneath page, portfolio, section, card and table titles. Actual source notes, field/status labels, source caveats, required report dates and meaningful definitions retained. SLC definition appears once with «مقارنة:».
- Shared date-only report mastheads, official logo, three plain primary navigation links, application menu and grouped print actions. All remaining utility/report destinations stay available through the menu.
- Separate sector/unit/entity controls and retained project extra filters. Field reset preserves the workbook, cutoff date, comparison context and saved view/display/print preferences. Mobile fields use a native modal sheet with live selections, inert background and explicit forward/reverse Tab cycling.
- Google-like search, six-column results table, native source details/CSV/all-match printing and approved upload panel. Copyright-only screen footer.
- Native A4/A3 printing with one first-page title containing the actual cutoff date and logo; no continuation report mastheads. Table headings repeat. Every footer contains only copyright and generated page X of Y. Printed filter fields are hidden while their selected scope and actual row entity names remain.

## Source and calculation regression

The frozen **illustrative** fixture has SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`, cutoff 30/09/2026. It is excluded from the release.

| Verification | Result |
| --- | --- |
| 672 canonical records, 672 distinct keys and 46 blank-unit rows | Identical to v129 |
| Monthly figures, budget, KPI denominators/averages and historical context | Identical to v129 |
| 16 model/report source files | Byte-identical to v129 |
| 29 core model/library/font/image files plus 3 icons | Byte-identical to v129 |
| Monthly screen/print follow-up eligibility | Same 8 source keys |
| Project table/report membership | Same 84 keys/cohorts |
| Project type / union within type / intersection with priority | 59 / 84 / 67 source rows |
| Scope reset / genuine empty unit selection | Restores 84 / empty count uses dash |
| Search table, CSV and print for «استراتيجي 006» | Same 4 keys and order |

Real source 0% progress remains 0%. Missing/unknown statuses remain distinct. Display changes do not create data or historical deltas.

## Screen and interaction checks

202 visual/computed-style checks across 28 captures passed, including monthly widths 1920/1440/1024/700/600/390 and representative project/search/upload/entity/comparison/check/report routes on desktop and mobile. A final focused check also confirms diagnostic table sheet names use 16px Dubai Regular. Screenshots use native CSS pixels; no whole-page scaling substitutes for the approved font sizes.

21 interaction checks passed: outside/Escape menu dismissal; menu arrows/Home/End and focus restoration; live filter selection/search; 3 core plus 5 additional project fields; reset preservation; mobile inert background and Tab cycling; upload Enter/Space selection, valid picker and drag/drop, invalid replacement recovery; shared mastheads and single print actions; Google-like search and results. No uncaught browser errors or whole-document horizontal overflow were observed in the tested layouts.

## Native PDF checks

12 native print flows passed exact first-title/logo/scope/footer checks and footer geometry on every generated page. Print scale: title 24pt, source table/status 13.5pt, footer 10.5pt, with the separately approved DIN figure and section scales. No forced shrink-to-fit page count.

| Illustrated report | Native pages |
| --- | --- |
| Monthly A4 / A3 | 4 / 2 |
| Projects A4 / A3 | 7 / 4 |
| Project browser report A4 | 7 |
| Search matches A4 | 2 |
| Entities A4 | 47 |
| Agenda / council A4 | 16 / 32 |
| Special projects report A4 | 72 |
| Comparison / checks A4 | 1 / 29 |

These are fixture-specific page counts, not targets for operational data. Existing per-record report pagination is retained where applicable. Native browser headers/footers were suppressed even when enabled; approved status fills remained visible with background graphics disabled. A synthetic unusually tall table row continued across 16 pages without losing any of its 100 test phrases, with repeated column headings. Source record order and source notes were preserved.

The 12-flow print gate used CSS SHA-256 `31825307fd3ff5bb6382f3c78595548c2cfa0952171686eaced8682a0d49fbad`. The final release adds only a screen-media regular-weight rule for diagnostic sheet names; print rules are unchanged. Final JavaScript SHA-256: `29d66f62af07ee77ef080aabd36a381421fc1197574261db758e179e092f30f1`. Final CSS SHA-256: `a3a374fb86d1b99f0733a96d70f7e24c914e6adbea89e3bedccf27a4b22bc79a`.

## Release and reproducibility

`python tools/build-bundles.py --check` verifies all 58 CSS and 48 JavaScript sources match the served bundles. `node --check assets/js/app-bundle.js` passes. Readable sources, local fonts/images/libraries and this audit are included. `SHA256SUMS` and `release-manifest.json` identify release contents. No source workbook, uploaded operational PDF, illustrative workbook or browser storage is bundled.

## Practical limits

The operational workbook shown in the user's screenshots was not provided. Numerical regression therefore applies to the illustrative fixture, not unseen operational numbers. The app reads cached Excel formula results; it does not refresh formulas or Power Query. Existing editable PowerPoint/workbook export pipelines were retained, not redesigned or newly reconciled. Native Windows file opening, physical printing and a full accessibility certification were not tested. Page-margin counters were verified in Chromium 151; other browser engines can differ. Browser file-origin notes/settings can vary when the extracted folder moves, so retain the prior folder until existing notes/settings are checked.
