# Font engine verification

Verified bundle SHA256: `8038eaa52e8aa4693e6f4d9141f51edfaf78be42621384e608ddfc81d5cb2528`.

The independent browser probe loads the bundle, places Chromium offline, and creates native PDF documents for the original DIN, DIN LT, Dubai Regular and Dubai Bold faces. All eight corpus PDFs opened, rendered and extracted text through MuPDF and Poppler. The production default leaves the optional ActualText layer disabled. Runtime request capture recorded zero requests after initialization began, including fonts and WASM.

The 60-line width proof compares the engine with Chromium using the exact supplied font bytes at 32 CSS px / 24 PDF points. It includes monthly title/card/portfolio text, Arabic ligatures, diacritics, SLC mixed labels, dates, ratios, percentages and numeric figures. The maximum measured difference was **0.001166993 CSS px**. Native specimen and browser specimen confirm corrected joining for the legacy DIN face. The earlier isolated/reversed DIN output was an actual defect and is superseded by the shaping-only supplement.

Native specimens have Type0 embedded fonts and zero text images. Ordinary Arabic keywords such as الإجمالي, الموازنة, الأمانة and الأداء are preserved by the ToUnicode mappings. The Dubai status مجمّد extracts correctly in MuPDF. Poppler adds bidi controls and sometimes groups combining marks separately; highly marked Arabic can have reader-dependent extraction order. Exact raw-text byte equality across readers is not a release claim.

The original DIN/Dubai font files retain their exact bytes; no app font files or source data were changed. The engine build was repeated with the same pinned dependencies and produced the same bundle hash. The licenses/provenance include the symbol-only OFL subset and scoped dependency notices.

Actual managed Chromium `file://` navigation was blocked by administrator policy, so that launch mode was **not run**. The network-disabled browser proof establishes no runtime font/WASM/library fetch; it does not override that policy restriction. Application route/layout/source and download-button verification are recorded separately by the parent QA scripts.

Evidence:

- `evidence.json`: eight native PDF corpus outcomes and network capture.
- `width-evidence.json`: all 60 exact-font advance comparisons.
- `browser-font-comparison.png`: Chromium render of the supplied fonts.
- `tec-din-native.png`: corrected native legacy DIN specimen.
- `keyword-evidence.json`: raw MuPDF/Poppler extraction, including the reader-dependent mark behavior.

The final symbol fallback now includes all audited source arrows and all five Harvey progress forms. `symbol-evidence.json` verifies every declared subset character and native MuPDF/Poppler extraction across all four TEC font aliases. The subset remains LiberationSerif-derived under the retained OFL license; no extra font family was added.
