# Performance App v147 — focused verification

**تعريفات مستويات الإنجاز** now immediately follows the agenda chart and precedes the record tables on screen and in PDF reading order. The content appears once. Existing definitions, source calculations, legend, status colors and chart geometry are preserved. The strategy metric label is **المؤشرات المعتمدة / المؤشرات المقاسة**, with approved count at the right and measured count at the left; the coverage bar still calculates measured divided by total.

Screen checks passed at 1440, 768, 390 and 320px: chart → definitions → tables, one definition block, all 117 illustrative records retained, no horizontal document overflow or runtime errors. Desktop and phone output was visually inspected.

Actual native PDF downloads were checked for all records, a selected entity, sparse results, empty results and a long title. Both charts remain together. Definitions appear next, before any record table; they continue on the next page when they do not fit below the chart. PDF definitions use three columns matching the desktop grid. Fonts and margins are retained rather than shrinking the content. Exact record order and complete definitions are preserved. A4 landscape dimensions, footer clearance and first-page header behavior pass. Empty results exercise definitions fitting below the chart on page 1.

The strategy caption and count positions were checked on screen and in an actual native monthly PDF: approved 54 is on the right, measured 39 on the left, with existing typography and coverage 39÷54 preserved. The monthly PDF remains one continuous page.

Bundle consistency and JavaScript syntax pass. All model modules match v146. ZIP CRC, membership and every manifest hash are verified on fresh extraction. No workbook or QA data is included in the app.

This is a focused placement and label alignment check using the frozen illustrative workbook (SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`), not an operational-data audit. Earlier v146 verification remains historical. Tests use local HTTP because managed Chromium blocks direct file:// launch; Windows launch and physical printing were not tested.
