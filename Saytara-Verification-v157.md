# Performance App v157 — approved monthly legislation card

## Applied behavior

The monthly dashboard and native continuous/A4 PDF now show **منجز** as one aggregate of the existing completed SLC cohorts, beside **قيد العمل**. The late subset appears beneath in progress as **منها متأخر**, with its eligible change; it is never added a second time to the total. The completion strip is Green/Linen and uses completed records over the full selected legislation total, with **نسبة المنجز** beside the percentage.

The new `legDone` metric uses an exact per-record union and supplies matching drilldowns and comparison details. Existing source fields, SLC metrics and status meanings are retained. Sector/unit/entity filters continue to use the established scope rules. Historical changes require valid comparable values; missing, quarantined or contradictory saved components do not become zero or fabricated deltas.

Empty status groups retain the existing suppression behavior. True zero remains a dash; missing values retain their source meaning. Invalid numerator/denominator or overlapping completed/in-progress categories suppress the bar and caption. Where late is not a subset of in progress, it is shown separately as **متأخر**, preserving existing source diagnostics instead of falsely labelling it **منها**.

## Source and validation

Used the existing illustrative workbook, cutoff 30 September 2026, SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. Its actual legislation counts are 191 total, 180 completed (152 within SLC + 28 after SLC), 11 in progress including 2 late, with 94.2% completion. Source bytes and parsed records remain unchanged.

The approved screenshot case is tested separately as clearly labelled controlled input: 183 total, 178 completed, 5 in progress including 2 late, 97.3% completion. A valid supplied prior case yields +17 total, +14 completed, +3 in progress and +1 late; unavailable history yields no change arrow. No screenshot values are hardcoded into production code or written into the source workbook.

- **166 independent checks passed on the final bundled app:** 125 real-fixture checks and 41 controlled/edge-case checks. No runtime or external-network errors were observed.
- Verified exact completed/in-progress/late drilldown keys, multi-select scope, empty scopes, historical eligibility, zero/missing/invalid values, late-subset fallback and overlap suppression in app and print.
- Five other monthly card texts and the follow-up record order remain unchanged against v156. Underlying current source metrics retain their previous values.
- Visually inspected RTL desktop and phone rendering across 320–1440px: completed physically right, in progress left, late beneath in progress, aligned values and correct Green/Red typography.
- Generated and inspected actual native PDF downloads. The real fixture produces one continuous page and three A4 pages; the approved-example-only A4 report produces one page. Checked proportional bars, text bounds, scope, numeric values, source invariance and follow-up order. These are fixture page counts, not fixed app limits.
- An additional 34 focused model checks and 37 screen checks supported implementation. The model checks used source-module injection; the independent 166-check run above verifies the actual final bundle.
- Release packaging checks JavaScript syntax, generated bundles, ZIP CRC, extracted file hashes, immutable v156 archive and identical Revision 24 principle copies. No source workbook or test output is bundled in the app.

## Limits

These checks use the existing illustrative fixture and controlled scenarios, not a production-data audit. Chromium loaded local assets with outside requests blocked. Cold file-URL startup, native mobile hardware and screen-reader certification were not separately tested. No workbook refresh, Excel recalculation or historical-data reconstruction was performed. PowerPoint was outside this monthly-dashboard/PDF change.

Revision 24 updates the downloadable skill/principles package; it does not claim to update a separately cloud-installed skill.
