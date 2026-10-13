# Performance App v149 — agenda corrections

The agenda cover fills the complete 297 × 210mm page using the original image at its natural proportions, cropped to fit. The original paired logos and native title/entity/reporting-period text stay inside safe insets. There is no cover copyright or visible page number. Physical page 2 begins **صفحة 1**; displayed page totals exclude the cover. Later agenda pages retain their 10mm margins and copyright footer.

The emerging-topic section now has its own **المواضيع المستجدة** heading and topic count inside the exported table section. Its table includes **الجهة المعنية**, using each record's source entity. The visible chart scale-range note is removed; internal count scaling and all chart values remain unchanged.

Focused checks cover full, entity-filtered, emerging-only and empty scopes. Actual native PDFs verify cover geometry, image proportions, absent cover footer, content numbering, exact source keys, visible headings/counts/entity values, and the combined chart/definitions page. Desktop and phone checks inspect emerging-topic headings, five-column record associations, zero-dash and status-color behavior, and document overflow. A monthly native PDF regression checks that its continuous-page geometry and existing footer remain unchanged.

The fixture is illustrative, with SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. It includes a natural two-record emerging-only entity scope matching the reported issue. No production-data reconciliation is claimed. Model modules and filter calculations are byte-identical to v148.

Bundle and JavaScript syntax checks pass. The release ZIP is CRC-tested, freshly extracted and checked against every manifest hash. No workbook or QA PDF is bundled. Browser validation uses local HTTP because this managed Chromium blocks direct file:// launch; cold Windows file-origin launch and physical printer output were not tested. Earlier verification documents are historical.
