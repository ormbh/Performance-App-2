# HH illustration revision 3 — focused QA

**Verdict: PASS for the requested R3 chart changes.** No unresolved defects were found in this focused review. This is an illustrative report review, not approval of production data or proposed status wording.

| Check | Result | Evidence |
|---|---|---|
| Source version and reporting period | PASS | The illustrative workbook and source-model SHA-256 values still match `source-review.json`. The reporting label remains 30/09/2026; no current-date recalculation was performed. |
| Source preservation | PASS | R3 `data.js` is byte-identical to R2. All 62 keys and all 12 retained item fields exactly match the corresponding source-model records. The illustration uses a projection of the fuller parser model. |
| Cohort scope and blank treatment | PASS | Leadership is the 24 rows marked نعم. TEC contains all 38 other rows, including both blank leadership flags. The cohorts are disjoint and complete. There are no blank sectors; the one blank status remains in حالات أخرى. |
| Record, row and status reconciliation | PASS | Leadership sector totals are 1 + 6 + 15 + 2 = 24; TEC totals are 11 + 3 + 8 + 9 + 1 + 6 = 38. Combined total: 62. Leadership statuses: 12 development + 12 completed. TEC: 3 review + 23 development + 11 completed + 1 other. |
| Empty sector rows | PASS | Only 4 leadership rows and 6 TEC rows render in the unfiltered view. No zero-count sector rows render in the tested filtered views. Source sector and status ordering is preserved. |
| Empty cohorts and filters | PASS | Leadership-only, TEC-only, sectors with no leadership projects, a single office, a combined sector selection intersected with leadership, no-result scope and reset were checked at all four viewport widths. Empty cohorts disappear; a sole remaining cohort fills the grid width. Empty scopes show the empty state. Displayed keys and totals match an independent source filter. |
| Total at actual bar endpoint | PASS | Every tested row places its total 8 CSS px after the actual filled left edge, within rounding tolerance. Every total stays inside its row and card. This was checked at 1600, 1280, 390 and 320 px, for all tested scopes, and in the print DOM. |
| Segment numbers and status labels | PASS | Segment counts are inside their bars, equal the source counts and retain proportional widths. There are no `.segment-keys` elements or individual status labels under the bars. Cohort status totals and the detailed legend remain visible. |
| Responsive HTML and visual quality | PASS | No document overflow or JavaScript errors at 1600, 1280, 390 or 320 px. Delivered desktop chart and fresh 1280/320 px chart captures were visually inspected for Arabic, wrapping and geometry. |
| Actual PDF | PASS | All 3 current PDF pages were independently rendered and visually inspected. Page 2 has the same 4/6 rows, 24/38 totals, in-bar values, status summaries and five legend definitions. Measured vector gaps at row ends are 7.69–8.44 CSS px after PDF rounding. No clipping or overlap was found. |
| PDF image provenance and fonts | PASS | `print-1.png`, `print-2.png` and `print-3.png` are pixel-identical to fresh renders of the current PDF at 1.5×. PDF fonts are embedded subsets or self-contained Type3 glyphs with ToUnicode maps. Arabic shaping appears correct; LiberationSans is used for demonstration arrows. |
| Historical comparison, query refresh and editability | NOT RUN / outside scope | No historical comparison, recalculation, Power Query refresh, PowerPoint editing or Excel editing was requested or performed. No accessibility certification is implied. |

`qa-evidence.json` contains the browser geometry, independent scoped counts, file hashes and actual-PDF observations. The 864 passing assertions are repetitions of these focused R3 checks across rows, widths and scopes, not the earlier broad application test suite. Application, repository and source files were not edited during QA.
