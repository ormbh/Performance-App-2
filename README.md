# Performance App v141

[Download app — v141 ZIP](https://github.com/ormbh/Performance-App-2/raw/refs/heads/main/Performance-App-v141.zip) · [Illustrative PDF](Monthly-Filters-v141/ILLUSTRATIVE-Continuous-Monthly-v141.pdf) · [Verification](Saytara-Verification-v141.md) · [Design standard — Revision 16](Design-Standard/TEC-Apple-Inspired-Design-Standard-Revision-16.md) · [Download standard ZIP](https://github.com/ormbh/Performance-App-2/raw/refs/heads/main/TEC-Design-Standard-Revision-16.zip)

Monthly dropdown values, scope summary and PDF headers now show the **first selected name +N** for partial selections. A single choice shows its name; full and unrestricted selections show **الكل**, without a number. Selection order is preserved. Removing the first choice promotes the next remaining choice. Source alias grouping and exact selected values retain their definitions.

Monthly PDFs download as **التقرير_الشهري_للأداء_Mmm_yy[_scope].pdf**, using the report date. A partial unit selection takes priority over a partial sector selection. Multiple choices add the first name and **_+N**; all-selected/unrestricted fields add no suffix. Example: **التقرير_الشهري_للأداء_Sep_26_مكتب_خطة_دبي_+3.pdf**. The visible report title and other reports' filenames retain their rules.

The offline **تنزيل PDF** workflow remains. Monthly output defaults to one continuous page with A4 portrait selectable; agenda, council and HH use A4 landscape, and other reports A4 portrait. Approved fonts, data formulas, cards, report date, first-page scope and copyright/page-number footer remain.

Verification passes 67 browser/PDF checks, nine filter edge cases, eleven filename cases and seven extracted-package checks. Scope/counts/followups match v140 in five selected scopes. Actual continuous and A4 downloads were inspected. See verification for full scope and limits.

Extract the whole ZIP and open index.html with its assets folder beside it. App/PDF assets are bundled locally. Select your workbook; processing remains on your device. QA uses an illustrative fixture and managed Chromium over local HTTP; the user's Windows file-origin environment and physical printers were not tested.

Previous: [v140 ZIP](https://github.com/ormbh/Performance-App-2/raw/refs/heads/main/Performance-App-v140.zip) · [v140 verification](Saytara-Verification-v140.md) · [Historical Revision 15](Design-Standard/TEC-Apple-Inspired-Design-Standard-Revision-15.md). Earlier releases are preserved.
