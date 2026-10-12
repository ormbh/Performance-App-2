# Saytara verification — v137

**Verdict: PASS for the approved changes and tested workflows.**

The monthly continuous PDF now uses the full TEC Linen surface, including page edges, the column gutter and the footer band. Paper cards retain the approved Sand boundaries. The digital page is 297mm wide with 281mm content, 8mm top/side margins and16mm bottom reserve. The extra 8mm footer band protects a minimum 8mm glyph inset; the final sample's conservative text bounds measure **9.63mm above the physical bottom**. Body and footer have 29.18pt clearance.

Cards and followups use 6mm padding; portfolio columns 8mm gaps, stacked cards 6mm gaps, card headings 4mm bottom spacing, metric rows/bars 3mm top spacing and table cells 3.5mm padding. Portfolio headings align with the cards’ 6mm inner edge. The page grows with all selected content; fonts and data are not scaled. The example is one native page, nominal 297×622mm (actual 297.01×621.96mm).

| Verification gate | Result |
| --- | --- |
| Native full-page layout | PASS:75 actual browser/PDF checks for full and empty continuous reports, page-edge Linen, footer glyph inset, settings persistence/focus/mobile, monthly A4, agenda landscape, projects portrait, source cutoff, copyright and native text bounds. |
| Native surface and A4 regression | PASS:20 independent checks. Graphics ON/OFF produce identical native text/fonts/rendered pixels and source row keys. Linen vector paint encloses the complete MediaBox; physical edge, column-seam and footer-band samples are Linen. All 3 monthly A4 pages match released v136 in dimensions, text, fonts and rendered pixels. |
| Async lifecycle | PASS:22 checks for toolbar and actual print-media entry, delayed fonts/images, pending-callback cleanup, content-height+27mm measurement, safe height fallback, source retention and deferred notice after print exit. |
| Independent full PDF review | PASS:whole final page and readable details; no white band, clipped text or overlaps. SLC order, figures/changes, strategy measures and all 8 followup rows remain aligned and complete. The initial too-close footer finding was corrected and rechecked. Native visible character/font/size/color content and type-size counts match v136. |
| Source regression | PASS:matched continuous and A4 contexts against immutable released v136. All 672 records, KPI/budget/counts/changes, bars, 37 printed metric entries and8followup keys are identical. Null/zero progress remains 502/27. |
| Protected assets/source | PASS:44 protected assets, 15 model modules, 11 report/PPT modules and 50 unmodified JavaScript files are exact matches. Only print-pagination.js changes among JavaScript source files; no calculations, source views, fonts or Office templates change. |
| Extracted-package workflows | PASS:26 checks for actual upload, search/details, report menu, mobile HH, continuous PDF, selected monthly A4 and agenda landscape. No script or asset failures. Final runtime hashes match the tested extraction. |
| Final native PDF binding | PASS:exact exported text, page dimensions and rendered pixels match the independently reviewed final PDF. |
| Direct file navigation / Windows / hardware print | NOT RUN. Managed Chromium blocks direct file navigation; extracted-package checks use local HTTP. Windows dialogs and hardware printers are not available here. No policy bypass was attempted. |
| Native Office editing / accessibility certification | NOT RUN. Office/template assets are retained. Targeted browser keyboard and mobile checks do not constitute formal certification. |

All populated checks use the frozen illustrative workbook `ILLUSTRATIVE-monthly-preview.xlsx`, cutoff 30/09/2026, SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. No operational workbook was supplied. The workbook and test records are excluded from the app ZIP. No Excel formula or Power Query refresh is claimed.

The continuous format remains the default, with selectable A4 portrait for paper. Other document orientations and 10mm A4 margins remain approved. A continuous report exceeding the 5080mm native page limit uses A4 for that session, preserves every record/note and explains the change after print exit. The saved format preference is retained.

Final runtime hashes:

- JavaScript: `19b3f12dcb6c0b0c2c4481134c3290cf0f80b25fc94d8b706136444e8d178d8c`
- CSS: `2eeb64c7f2f8db5f42facec0573d027eb9a3529ade05bf84858132d9e76ecdea`

Build and syntax checks pass for 65 CSS modules and 48 JavaScript modules. Release extraction verifies the complete file set and every manifest hash. Source fields, matching, scope, calculations, status definitions, zero/missing semantics and retained typography remain unchanged. Earlier verification files are historical evidence for their respective releases.
