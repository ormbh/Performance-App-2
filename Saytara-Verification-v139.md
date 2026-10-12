# Performance App v139 verification

Date: 12 October 2026. Target: Revision 14, restored PDF header and strategy badge removal.

## Change and result

The strategy card no longer shows **مؤشرات الأداء** on screen or in the exported report. Main values, the coverage bar and valid count/average differences remain. A nonzero registered-total difference keeps its neutral header position and accessible context without a decorative tag.

First-page PDF headers retain the official TEC logo and the complete display title with its actual cutoff date. A compact **القطاع / الوحدة التنظيمية** line uses the active organizational selections, or the all-sectors/all-units values. It uses 10.5pt Dubai Regular Ink beneath the 24pt DIN title. Multi-selects use the existing readable source aliases. Each route uses its own filters; monthly-driven search restrictions remain combined with search facets. Entity/checks views do not acquire unrelated dashboard selections. Entity filter values remain omitted from the header while their effect on records remains intact. Custom report titles use the complete display title, without filename truncation.

A reproduced v138 boundary defect could discard both title and date when browser font Range rectangles extended above the header, even though their baseline and visible glyphs fitted. v139 assigns first-header text by its baseline, retaining clipping and normal table-row bounds. Tests using the same supplied DIN glyphs with enlarged ascent/descent reproduce the prior omission and pass with v139 in continuous and A4 downloads. This proves the boundary defect and correction; the user's exact Windows font metrics were not captured.

The final visible line can extend a fraction of a pixel beyond its element. Export height now includes that measured line, preventing a footer-only trailing comparison page without dropping its final definition label.

## Actual downloads

**355 checks pass**, with zero failures or browser errors, across ten cases and 165 pages. Tests activate **تنزيل PDF** and inspect the downloaded bytes. They do not substitute a browser screenshot or print emulation for the direct-download result. The title/date and organizational scope appear once. Text remains selectable; approved DIN and Dubai fonts are embedded, values/keys remain unchanged, no text lies outside pages, and the footer keeps copyright and generated page counts. All runtime requests stay local and `window.print` is not invoked.

| Case | Pages | First page size, mm |
| --- | --- | --- |
| monthly-continuous | 1 | [297.0, 629.0] |
| monthly-filtered | 1 | [297.0, 342.0] |
| monthly-a4 | 3 | [210.0, 297.0] |
| reports-agenda | 16 | [297.0, 210.0] |
| reports-council | 30 | [297.0, 210.0] |
| reports-hh | 71 | [297.0, 210.0] |
| projects | 6 | [210.0, 297.0] |
| entities | 34 | [210.0, 297.0] |
| comparison | 1 | [210.0, 297.0] |
| results | 2 | [210.0, 297.0] |

The monthly full report remains one continuous page; the A4 choice remains three pages for this illustrative fixture. Agenda, council and HH retain A4 landscape; other A4 reports retain portrait. Continuous output retains the full Linen surface, 8mm reading insets and the footer reserve. The standard card/table sizes are unchanged.

Five additional actual-download regression cases verify the title/date under native and larger font metrics, including selected sector/unit context and both continuous/A4 painting paths. The collected title Range still starts at -10px in the enlarged-metrics cases, so the original failure condition remains exercised. All five preserve the title/date, source keys and clean export cleanup.

## Final extracted package

The freshly extracted ZIP passes **143 acceptance checks**, including native file-input upload, actual menu navigation, cold continuous download, selectable A4 monthly download and landscape agenda download. All **178 manifest entries** match the packaged files. Source keys/date/scope are retained, font/figure/header/footers and download cleanup pass, and no runtime or remote-request errors occur. These checks use the extracted release, not the development folder.

Independent visual review passes the requested first-page header, filtered sector/unit/entity cases, removed strategy badge and retained figures/differences in continuous and A4 formats. Full monthly numeric/date/ID tokens match v138; all 165 final pages pass the native bounds/footer gate. See [independent review](Offline-PDF-v139/INDEPENDENT-VERIFICATION.md).

## Source and filter regression

All **12 monthly scope/format cases** match v138 for scoped metrics, bars, differences and follow-up keys: continuous/A4 × all, sector+unit, multi-select, explicit blank unit, reset/all and entity scope. All **672 full source records** have the same digest, including 502 null and 27 numeric-zero progress values. Full scope retains 37 print metric entries and eight follow-up keys. Entity filtering changes the data normally while its header field stays omitted.

All **15 header routing cases** pass, including independent projects/report/comparison filters, search drill-plus-facet restrictions, blank selections, alias deduplication and full display titles. All 44 protected assets and 15 model modules are identical to v138.

The badge-free total-difference renderer passes an explicitly synthetic nonzero-difference test. The existing dashboard model does not supply `kpiTotal` in its historical `cur` snapshot, so native `D.change('kpiTotal')` currently returns `none`; that pre-existing behavior is identical in v138/v139 and is not redefined by this presentation update. Measured-count and average-result differences retain their existing behavior.

## Supplemental mobile and native-print checks

**59 checks pass** with no runtime errors. At 390px, the strategy tag is absent, labels remain 16px and figure alignment passes. Prepared Chromium native print-to-PDF produces one continuous page and three A4 portrait pages, with the first title/date/scope, eight original follow-up keys and copyright/page-only footer intact. This separately checks the optional CSS-print path; it does not replace the actual app-button download tests above.

Headless Control+P exposes no preview UI, so native output was generated after real preflight through Chromium print-to-PDF. Original-font computed roles and rendered sizes/visuals were checked. Chromium's Type3 font family naming/color and exact ligature extraction are not asserted. Neither path certifies a physical printer or the user's Windows installation.

## Runtime bindings

| Runtime asset | SHA-256 |
| --- | --- |
| `assets/js/app-bundle.js` | `515087e6b5297af85610f87a7a37a6dbcb7b95048ae6663dea3fbc1f2e9147dd` |
| `assets/css/app-bundle.css` | `c5dca03eb8791f003de61a1519e27d76557ec23f0eafb24d40c4cf7ab43347d4` |
| `assets/css/print-measure-bundle.css` | `b9c76b378417f9c84f09cfc9dd29252c0086172b37bff0eacc0bdd93f0163cd8` |
| `assets/js/lib/offline-pdf-engine.js` | `8038eaa52e8aa4693e6f4d9141f51edfaf78be42621384e608ddfc81d5cb2528` |

Readable source remains packaged. All prior calculation models, report/Office templates, original stylesheets, font bytes, logo and bundled PDF engine are unchanged. The build adds the specific exported-header stylesheet and updates the header/badge/renderer sources and generated bundles. A release manifest covers every packaged file except itself; the ZIP is checked for CRC, exact file membership and all manifest hashes before publication.

## Scope and limits

The frozen workbook is explicitly illustrative (SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`). It contains 672 records and cutoff 30/09/2026; it is excluded from the app package. No operational workbook from the user's screenshots was supplied or published.

Validation uses managed Chromium on Linux and local HTTP. Managed browser policy blocks direct file navigation; Windows file launching, the user's exact browser/font environment, physical printers and native Office editing were not run. The app and PDF engine remain fully bundled for offline use; no remote rendering service is introduced. Earlier release checks remain historical evidence for their own versions.
