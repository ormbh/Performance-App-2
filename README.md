# Performance App v142

[Download app — v142 ZIP](https://github.com/ormbh/Performance-App-2/raw/refs/heads/main/Performance-App-v142.zip) · [Verification](Saytara-Verification-v142.md) · [Design standard — Revision 17](Design-Standard/TEC-Apple-Inspired-Design-Standard-Revision-17.md) · [Download standard ZIP](https://github.com/ormbh/Performance-App-2/raw/refs/heads/main/TEC-Design-Standard-Revision-17.zip)

Monthly PDF filenames now group the Arabic report title and selected scope together, followed by the English report month/year and extension: **التقرير_الشهري_للأداء_مكتب_خطة_دبي_Sep_26.pdf**. Multiple choices use the first selected name only, without **+N**. A partial unit takes priority over a partial sector; full/unrestricted scope is omitted. The date comes from the report.

The format is **التقرير_الشهري_للأداء[_scope]_Mmm_yy.pdf**. Ordinary Unicode text keeps Arabic in its natural order. No hidden direction controls are added because Chromium replaces them with underscores. The operating system controls filename alignment.

Monthly dashboard dropdowns, scope summaries and PDF headers retain **first selected name +N** for partial selections and **الكل** for full/unrestricted selections. Other reports' filenames, source data, filters, calculations and output layouts retain their existing behavior.

Verification: twelve filename cases, seven browser/PDF checks and seven extracted-package checks pass. An actual PDF download retains the approved compact scope in its native header. Only the filename function and its generated runtime bundle changed among app assets. See verification for practical limits.

Extract the whole ZIP and open index.html with its assets folder beside it. App/PDF assets are bundled locally. Select your workbook; processing remains on your device. QA uses an illustrative fixture and managed Chromium over local HTTP. Native Windows Explorer, Windows file-origin execution and physical printers were not tested for this change.

Previous: [v141 ZIP](https://github.com/ormbh/Performance-App-2/raw/refs/heads/main/Performance-App-v141.zip) · [v141 verification](Saytara-Verification-v141.md) · [Historical Revision 16](Design-Standard/TEC-Apple-Inspired-Design-Standard-Revision-16.md). Earlier releases are preserved.
