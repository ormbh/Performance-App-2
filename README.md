# Performance App

[Download the current app — v169](https://github.com/ormbh/Performance-App-2/raw/refs/heads/main/Performance-App-v169.zip)

Extract the ZIP and open **index.html**. Keep **assets** and **manifest.webmanifest** beside it, then select your report workbook. No workbook is bundled.

Monthly comparisons now explain the exact +/− metric, department transfers, status/value changes and unresolved matches. Drill-downs stay in the same tab by default, with explicit new-tab support. Supported browser storage retains a versioned binary workbook pair locally; older tabs identify newer versions. Screen and native PDF share selected content, periods, scope and row order.

[Implemented comparison and native PDF](docs/comparison/README.md) · [Verification](docs/Verification-v169.md) · [Design principles](docs/TEC-Design-Principles.md) · [Earlier releases](archive/README.md)

Hosted Chromium was verified. The managed test browser blocks direct-file navigation, so direct-file and other-browser behavior remain unverified here. Blocked/quota-limited storage shows an explicit fallback message.
