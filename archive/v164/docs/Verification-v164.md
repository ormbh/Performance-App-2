# Performance App v164 — PDF compatibility fix

14 October 2026 · TEC design principles Revision 28 retained

The native PDF exporter now supports the legacy Office square bullet U+F0A7 that caused `Unsupported glyph in approved PDF font: U+F0A7`. It uses a licensed, embedded square-symbol fallback for that character and Unicode U+25AA. Source text, selectable Unicode, original DIN/Dubai font files, report calculations and report design are preserved.

Browser print measurement uses the identical embedded square outlines and advances. Distinct glyph IDs preserve both Unicode characters when they occur in one PDF. The PDF engine URL now follows the application build number so the browser loads the corrected engine after updating. Dependencies remain pinned and integrity checked; the build uses a writable temporary npm cache.

## Verification

- Reproduced the exact reported U+F0A7 failure in v163 using controlled source text.
- Actual v164 native PDF exports pass for council decisions, agenda, special projects and the shared general-report path.
- Council long-text case retains all 24 latest-decision paragraphs and 18 notes paragraphs, with exactly 21 legacy and 21 Unicode square bullets across page breaks. Source data is unchanged.
- Ordinary council PDF selectable text is identical to the v163 baseline.
- The clean 26-file runtime produces an actual PDF download from the app UI and requests the versioned v164 PDF engine without external runtime dependencies.
- Original four Arabic font checksums and application CSS match v163. Browser measurements retain the original Arabic/Latin widths across font weights; square advances match the native PDF metrics. Unknown private-use characters remain explicit export errors rather than being silently removed.
- Reviewed rendered square bullets, Arabic wrapping and continuation pages. Build freshness and JavaScript syntax checks pass.

Machine-readable evidence: [PDF checks](checks/pdf-glyphs.json), [reproduction](checks/regression-baseline.json), [clean UI download](checks/clean-download.json), [code review](checks/code-review.json), [visual review](checks/visual-review.json). Preview: [Arabic council table with square bullets](previews/pdf-square-bullets.png).

## Scope and limits

Tests used `ILLUSTRATIVE-monthly-preview.xlsx` (672 records), SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`, plus explicitly controlled in-memory text. The source workbook was not edited. This validates the reported character failure; the user's production workbook was not available for a new reconciliation. No source figures, eligibility or date cutoffs were changed.

Native Office rendering and cold file:// opening were not rerun for this PDF-only fix. The minimal runtime was exercised over local HTTP in managed Chromium. Previous broader report verification remains in [v163 documentation](../archive/v163/docs/Verification-v163.md); those checks are not represented as newly rerun.
