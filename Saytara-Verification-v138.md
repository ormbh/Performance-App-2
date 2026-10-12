# Performance App v138 — offline PDF verification

12 October 2026. **Verdict: PASS for the tested direct-download workflows and approved output rules.**

The app now uses **تنزيل PDF** and **إعدادات PDF**. Report buttons download a native PDF through the locally bundled engine. No download calls `window.print`, opens a print dialog, uses a CDN or sends workbook data to an external service. Original source models, TEC fonts, approved visual rules and Office exports remain intact.

## Actual-button exports

Chromium 151, 1440px desktop, frozen illustrative workbook: **307 checks passed**, with no browser runtime errors or external requests. PDFs were downloaded using the actual app button, then parsed and rendered through MuPDF. These page counts belong to this fixture; operational reports paginate according to their actual scope and content.

| Export | Format | Fixture pages |
| --- | --- | ---: |
| Monthly, all scope | Continuous 297 × 622mm | 1 |
| Monthly, filtered scope | Continuous 297mm width, measured height | 1 |
| Monthly, A4 option | A4 portrait | 3 |
| Agenda | A4 landscape | 16 |
| Council | A4 landscape | 30 |
| HH | A4 landscape | 71 |
| Projects dashboard | A4 portrait | 6 |
| Entities | A4 portrait | 34 |
| Comparison, current-file state | A4 portrait | 1 |
| Search results | A4 portrait | 2 |

The ten cases contain 165 native PDF pages. An independent review checked page geometry, text/font/color/vector/image fingerprints and actual source content, with readable renderings and comparisons to the approved baseline. No out-of-page text, footer collision, missing font programs, replacement characters or unexpected body raster images remain. Table heads repeat on continuation pages. Nearby section headings, table heads and first rows stay together; fitting monthly cards stay whole while retaining the paired portfolios.

The continuous page fills its whole perimeter with Linen **#EFEBE7**. Content uses the approved 281mm width and 8mm top/side insets. The bottom reserve is 16mm; copyright glyph bounds are **8.93mm** above the physical bottom edge. The actual title/date and official logo appear once. Every page has only copyright and actual page X/Y in its footer. Generic A4 output retains the approved paper dimensions, 10mm content insets and independent print typography.

All source titles in the agenda and council body survive the export: 117 agenda titles/IDs and 164 council titles/IDs. HH retains all 62 project titles in its main table and detail cards; each full normalized title occurs twice as expected. Entities retain all 343 source titles in this fixture. Monthly numeric, date and source-ID tokens match the canonical v137 content exactly.

## Cold download and recovery

A separate **54-check robustness pass** verified:

- An immediate first download in a fresh context, before the local engine or measurement cache existed: one continuous page, with screen controls restored.
- Rapid repeated actions: exactly one download, visible spinner, disabled control and `aria-busy`, then normal controls restored.
- Missing local engine: no damaged download, actionable extraction/retry message, source/scope unchanged, clean recovery and successful retry after the resource became available.
- Checks: 23 A4 portrait pages; projects report opened through the real menu: 8 A4 portrait pages. Native text remains inside page bounds and copyright appears on every page.
- 390px download controls and the retained mobile layout.

The engine itself passed network-disabled native font, shaping and symbol probes. It embeds original TEC font outlines and a licensed symbol-only fallback for missing arrows/Harvey progress symbols. Arabic body text, headings, mixed SLC captions, figures and charts remain native PDF content. Only the original official logo is an image. Its bundled PDF bytes match the original logo asset exactly.

The four TEC fonts are unchanged. The supplied legacy DIN face lacks contextual-layout tables; a shaping-only supplement derives joining from its own presentation-form glyph map. A 60-line width comparison with Chromium's original fonts differs by at most **0.001167 CSS px**. All eight native corpus PDFs opened, rendered and extracted through MuPDF and Poppler. Ordinary Arabic words and status labels remain selectable Unicode. Highly marked Arabic can have reader-dependent combining-mark extraction order; identical raw extraction bytes across PDF readers are not claimed.

## Source regression and native print defect

Four matched continuous/A4 contexts, each with full and filtered scope, preserve all **672 illustrative source records**, 37 full-scope / 22 filtered metrics and eight / one follow-up keys. Values, bars, null/zero distinctions, notes, SLC captions and cleanup state match v137. **44 protected assets, 15 model modules, 11 report/PowerPoint files, 41 other original JavaScript modules and all 65 original CSS sources** are byte-identical.

The earlier v137 bug was reproduced from ordinary screen media: native printing could capture an unmeasured 80mm page before layout preparation completed. Earlier settled-output checks did not cover that timing case. v138 validates fonts/images and full layout before publishing a continuous measurement; native print without a ready matching cache safely uses A4. Direct download awaits its own complete prepared document and does not depend on native print-preview timing.

## Release bindings and limits

| Runtime asset | SHA-256 |
| --- | --- |
| `assets/js/app-bundle.js` | `5a34e9cfbd62ad909effddfa841d0633db594cc46956b076d68ef76caff2591c` |
| `assets/js/lib/offline-pdf-engine.js` | `8038eaa52e8aa4693e6f4d9141f51edfaf78be42621384e608ddfc81d5cb2528` |
| `assets/css/print-measure-bundle.css` | `1305fa85010c66e8d39da391c07205cb78f1ee6ad1b11e9b543aed3a8a6b57b6` |
| `assets/css/app-bundle.css` | `2eeb64c7f2f8db5f42facec0573d027eb9a3529ade05bf84858132d9e76ecdea` |

Reproducible bundle generation and JavaScript syntax checks pass. The release manifest covers every packaged file except itself. The final ZIP is checked for exact file membership, CRC integrity, manifest hashes and correspondence with these tested runtime assets before publication. QA fixtures, workbooks and sample PDFs are excluded from the app ZIP; readable source, licenses and provenance are included.

The operational workbook shown in the user's screenshots was not supplied. All populated verification figures are illustrative. Managed Chromium blocks direct `file://` navigation by administrator policy, so app route and extracted-package browser checks use local HTTP; native Windows file launching was **not run**. Physical printing, native Office editing, every PDF viewer and formal accessibility certification were not tested. No server is part of the delivered app: all required libraries, WASM, font bytes and the original logo are local assets.

Historical verification files retain their release scopes and do not establish these v138 results.
