# Performance App

[Download the current app — v175](https://github.com/ormbh/Performance-App-2/raw/refs/heads/main/Performance-App-v175.zip)

[Download v175 with optional local HTTP launcher](https://github.com/ormbh/Performance-App-2/raw/refs/heads/main/Performance-App-v175-Local-HTTP.zip) · [Mac HTTP instructions and verification](docs/Local-HTTP-v175.md)

Extract the complete ZIP and open `index.html` in desktop Chrome. Keep all 23 runtime files together. No workbook, sample data, tests or audit folders are bundled.

This release restores labeled record counts in formal PDF contents, corrects the specified monthly/comparison PDF text sizes and enforces the existing 24-hour binary-retention rule in shared and tab-only storage. Calculations, source scope, navigation and approved chart designs remain unchanged. Design Principles Revision 39 clarifies these existing requirements.

Older undated fallback sessions are cleared because their retention age cannot be established; select the workbook again once. Reloads and tab transfers preserve the saved timestamp.

Focused desktop HTTP tests and actual native PDF exports pass, including the exact final package. Direct-file operation on the user's Mac remains only partially evidenced by the supplied v174 startup/import screenshots; v175 Mac direct-file retesting remains open. The supplied Mac test scope is Chrome only; Edge compatibility is unverified. See the verification report for exact coverage and limitations.

Desktop/PDF only. Full PDF for other pages; A4 landscape for agenda, council decisions and special projects. No mobile/tablet or PowerPoint testing.

[Verification](docs/Verification-v175.md) · [Design principles](docs/TEC-Design-Principles.md) · [Mac retest](docs/Mac-Retest-v175.md) · [Release inventory](docs/release.json)
