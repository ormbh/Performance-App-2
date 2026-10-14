# Performance App v166 — approved monthly report

14 October 2026 · TEC design principles Revision 30

## Implemented

The approved monthly overview, council/budget/strategy treatment and legislation composition now run on live workbook data. The project column stays physically left and executive portfolios right. Agenda/council status bars contain readable counts, with tiny values retained separately. A compact common color key follows the summaries. Completed, ready and late labels and values use Green, Teal and Red consistently on screen and in PDF. Main total captions sit below values. Missing numeric values and follow-up notes stay blank; real zero stays a dash.

Special-project leadership requires explicit yes. Every remaining classification belongs to TEC, including blank values. Work counts only recorded review/development statuses; other and ready stay separate. The fixture reconciles 24 leadership + 38 TEC = 62; TEC 11 done + 26 work + 1 other = 38. Uploaded previous records are recalculated with the same definitions; incompatible embedded summaries cannot create fabricated cohort/work changes. The independently valid overall change +7 is preserved.

The existing approved legislation meaning remains: late is a subset of work and counted once. Its actual fixture values are 191 total, 180 done, 11 work including 2 late, 94.2% completion. The illustration’s 183 example is not an application constant. Budget headline categories, independent KPI result/target means, eligibility and all other source definitions remain intact.

Quiet footer links open the corresponding formatted report or existing detailed record view while retaining sector/unit/entity scope. Unrelated destination-local filters reset. Numeric actions retain exact-record drilldowns. Native PDF footer captions are references, not links into an absent local app.

## Verification

- **355 independent data/runtime assertions**, on the populated attachment and anonymized fixture, plus 53 final-runtime assertions after the final JavaScript caption change. Exact metric membership, six filter scenarios, empty/cohort/status edge cases, zero/missing behavior and previous-record/legacy-history comparisons pass. Source workbook bytes remain unchanged.
- **256 browser navigation assertions**, followed by 30 checks on final JavaScript: four formatted routes, scoped URLs, stale-filter reset, keyboard/Ctrl/middle activation, source transfer, focus and browser Back; metric drilldowns retain their records.
- **28 final screen checks** at 1560, 1440, 768, 390 and 320px. No page overflow, aligned status figures despite Arabic wrapping, readable measured bar labels and 44px footer actions.
- **222 final PDF assertions across nine actual downloads**, with independent visual inspection. Full fixture and attachment: one continuous 297 × 753mm page or four A4 portrait 210 × 297mm pages. Filtered: one A4 page. Controlled long notes: seven readable pages with source identifiers at the start and repeated table headings. Empty scope: one page. Pagination follows content and retains approved font sizes.
- Native exports preserve every tested metric, all eight follow-up records, supplied notes, both U+F0A7/U+25AA square glyphs, shared legend, scope, page numbers and copyright. Fitting summary cards remain whole. No orphan follow-up border appears on the preceding summary page. Applicable comparison notes remain even without follow-up records.
- Build freshness and JavaScript syntax pass. Final PDF and screen evidence identifies the exact delivered runtime hashes. The bundled PDF engine, original Arabic fonts and council full-width unassigned box remain unchanged.

The supplied workbook is populated and dated 30 September 2026; it is not asserted to be the latest operational dataset. No workbook recalculation, Power Query refresh or Office visual rendering was performed. This is not an accessibility certification. Cold file:// opening was attempted but managed Chromium rejected navigation with ERR_BLOCKED_BY_ADMINISTRATOR before app code ran; clean-runtime verification used local HTTP. The existing nonstandard seven-status council height guard remains outside this monthly change.

## Evidence and delivery

- [Data](checks/data.json) · [Final data smoke](checks/data-final.json)
- [Navigation](checks/navigation.json) · [Final navigation smoke](checks/navigation-final.json)
- [Screen](checks/screen.json) · [Actual PDF](checks/pdf.json) · [PDF review](monthly/PDF-verification.md)
- [Actual screen](previews/monthly-screen.png) · [A4 page 1](previews/monthly-a4-page-1.png) · [A4 page 2](previews/monthly-a4-page-2.png)
- [Illustrative A4 PDF](monthly/monthly-illustrative-a4.pdf) · [Continuous PDF](monthly/monthly-illustrative-continuous.pdf)
- [Release hashes](release.json)

Clean app package: exactly 26 runtime files, no workbook, audit artifacts, source modules or development folders. Readable source and historical releases are archived separately. Public screenshots/PDF examples use anonymized fixture data only.
