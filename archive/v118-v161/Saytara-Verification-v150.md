# Performance App v150 — empty-category verification

The agenda chart omits categories with no source records in the selected scope, including their title/count boxes. A single populated category fills the available chart width on screen and in native PDF. The empty state shows no category boxes or matrices. This changes presentation only: populated-category values, source record keys, source model modules, shared status/quarter ordering, common bar scale and zero dashes are retained.

Focused desktop/phone and actual PDF checks cover all records, emerging-only, approved-only and empty scopes. PDF checks include the inherited full-page cover, absent cover footer, content numbering starting on physical page 2, chart/definitions page, and emerging-topic heading/entity column. The v149 full export and long-text verification remains applicable to unchanged code. The illustrative workbook is unchanged (SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`).

Bundle consistency and JavaScript syntax pass. Source model modules match v149. ZIP CRC, membership and every manifest file hash are verified after fresh extraction. No workbook or QA PDF is bundled. Browser checks use local HTTP because managed Chromium blocks direct file:// launch; cold Windows file-origin launch and physical printing were not tested.
