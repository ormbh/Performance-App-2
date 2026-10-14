# Monthly PDF filename verification — v142

Twelve filename cases, seven candidate browser/PDF checks and seven extracted-package checks pass. Monthly downloads group Arabic title and first selected scope, then the report-date suffix `Mmm_yy.pdf`. No additional-selection count is generated in the filename. Screen/PDF-header counters remain unchanged.

`browser-bidi-probe.json` records actual suggested filenames after Chromium sanitizes hidden direction controls. The release uses ordinary Unicode without those controls. `source-audit.json` confirms the isolated filename change; `release-evidence.json` binds the ZIP and extracted runtime to the tested candidate.

Managed Chromium over local HTTP; illustrative workbook. Native Windows filename rendering remains unverified. See [verification](../Saytara-Verification-v142.md) for scope and limits. No operational workbook is included.
