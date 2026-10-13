# Performance App v151 — layout verification

355 focused checks passed: 324 across all, mixed-entity, approved-only, emerging-only and empty scopes, plus 31 for long Arabic topic/entity text. Screen checks cover 1440, 768 and 390px. Deadline headers remain on one line within their column at desktop/tablet widths and in native PDFs, retaining the approved type size. Phone cards remain within the viewport. Long source text wraps without omissions.

The complete cover title/entity/period group is centered on both axes within 0.5 CSS pixels; actual native PDF glyphs retain the full reporting year 2026. Saved user title overrides are preserved. Approved and emerging titles share the same heading font/size, with quarter/count context below. Empty approved table sections and their jump links are absent. Source counts 117/10/4/2/0, exact row keys, bar values, filtered category visibility, full-page cover, cover-free footer numbering and chart/definitions placement remain correct.

Source model modules and agenda-matrix.js match v150 byte-for-byte. Bundle consistency, JavaScript syntax, offline native export, ZIP CRC and every extracted manifest hash pass. The source workbook is illustrative and unchanged (SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`). No workbook or QA PDF is bundled.

The vertical-quarter illustration is separate and uses the user's supplied screenshot values, not the illustrative workbook. It has not been applied to the app. Browser checks use local HTTP because managed Chromium blocks direct file:// launch; cold Windows launch and physical printing were not tested.
