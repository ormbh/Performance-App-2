# Performance App v156 — numeric progress and HH PDF cleanup

## Applied changes

Removed Harvey ball glyphs and circular recorded-progress indicators from app report tables, project cards, entity details, native PDF and HH PowerPoint cards. Numeric percentages remain; zero displays a dash and missing progress remains blank. Status and recorded completion remain separate source fields. Existing linear progress/status bars and charts are retained.

The native HH PDF no longer repeats the combined overview KPI card after the paired chart page. Report contents, both cohort charts, detailed definitions, project tables and detail cards remain. The dashboard screen overview is retained.

The monthly legislation proposal is an illustration only. Its screenshot-derived figures are 183 total, 178 completed and 5 in progress, with 2 late included in progress under the existing calculation. Completion is 97.3%. No in-progress change is invented, and the live monthly SLC composition/calculations are unchanged.

## Verification scope

Used the existing illustrative workbook with cutoff 30 September 2026, SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. This is not a production-workbook reconciliation. Source bytes, exact project keys, raw values and calculated chart totals were preserved.

- Sixteen focused actual-bundle checks passed. All 62 table/card completion values match source, including 55 populated values and seven blanks. True zero, small positive values, decimals, missing and invalid input were checked. No Harvey/ring DOM remains in the checked HH, entities, monthly or results views.
- Desktop, tablet and phone card headers fit at 1440, 768, 390 and 320px. Actual screen/print previews were inspected. No runtime errors were observed.
- Eighteen focused planner checks confirmed only the duplicate native overview is removed; chart, contents, project tables/cards, screen overview and source data are retained. Final native output was checked separately after bundle rebuilding.
- Forty native PDF integration and typography checks passed for source-value parity, no circular operations/glyphs, preserved chart labels and definitions, all-page text bounds, cover/footer behavior, pagination and locally bundled assets. Every emitted percentage was compared against its source key in the actual PDF. All 55 populated table completion values render at 12pt in DINNextLTArabic-Regular and fit their cells. The actual fixture PDF has 72 physical pages; charts and definitions remain together on physical page 2, with the contents retained and no duplicate overview.
- A native 77-slide HH PowerPoint export retains two editable charts and all 55 populated editable completion figures, without circular progress shapes. Native package/data checks passed. Office rendering and interactive editing were unavailable.
- The monthly illustration uses existing Dubai/DIN fonts and approved TEC tokens. Desktop/phone rendering, RTL, no horizontal overflow and the 178/183 percentage were checked. Its numbers are from the user's screenshot, not a newly uploaded workbook.
- JavaScript syntax, generated bundle consistency, ZIP CRC, extracted file hashes, immutable v155 package and synchronized Revision 23 principles are checked during release packaging.

## Limits

Browser checks use Chromium with locally served assets; native mobile hardware, screen-reader certification and cold file-URL startup were not separately tested. PDF uses the app's native offline exporter and embedded fonts. PowerPoint structure/data checks do not substitute for an Office render. No source refresh, historical-data reconstruction, Excel recalculation or production-data audit was performed.

Revision 23 updates the downloadable skill/principles package; it does not claim to update a separately cloud-installed skill.
