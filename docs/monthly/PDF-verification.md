# v166 monthly screen/PDF verification

**PASS — 222 automated checks and visual inspection of the actual rendered pages.** Tested the clean 26-file runtime, using the real download control. Final loaded asset hashes exactly match the release candidate.

The full illustrative workbook and supplied populated workbook both export to one continuous page at **297 × 753 mm**, or **four A4 portrait pages at 210 × 297 mm**. The tested sector/unit-filtered report is one A4 page or a **297 × 213 mm** continuous page. Pagination follows content; fonts are not reduced to force a page count.

## Coverage

Nine actual native PDF downloads:

- Illustrative full scope, continuous and A4.
- Illustrative sector/unit filter, continuous and A4.
- Supplied workbook full scope, continuous and A4, plus filtered A4.
- Controlled oversized-note A4 case, seven pages, including both `U+F0A7` and `U+25AA`.
- Empty-scope A4 case, one page.

Every displayed metric matches the screen and remains present in its mapped native PDF rectangle. The corrected special-project cohort is 24 leadership + 38 TEC = 62; TEC shows 11 completed, 26 known in-progress and one other. Source totals remain dynamic. The actual legislation card is 191 total / 180 completed / 11 in progress, including two late, with 94.2% completion; the separate 183 example is not hardcoded.

Completed, ready and late labels and values use the same approved colors. Main total captions are below their numbers. Visible numbers inside the agenda/council bars fit and are retained in native PDF text. The tiny unclassified council segment keeps its separate visible value. The compact shared legend appears exactly once, including A4, and is omitted for an entirely empty scope.

Projects remain physically left and executive portfolios right. Each fitting summary card stays whole. All eight follow-up records are retained once; supplied notes remain, absent notes are blank, and continuation pages repeat the table heading. Oversized note rows begin with their project identity and status at the top. The legacy square glyph and Unicode square both render and survive text extraction, alongside every controlled start/middle/end marker.

The previously observed orphan follow-up border no longer appears at the bottom of the summary page. Comparison source notes remain in actual PDFs even when the selected scope has no follow-up rows. The existing approved PDF-only omission of the missing-requester diagnostic remains. Page numbers and copyright are correct on every tested page. Native text stays inside the physical page boundaries. There are no browser errors or external network requests, and both input workbook byte hashes are unchanged.

Screen overflow checks passed at desktop and widths 768, 390 and 320 pixels. This verifies the tested layouts; it is not a general accessibility certification. App footer navigation is covered by the separate navigation QA; PDF footer labels are report references rather than live routes into a local app.

## Evidence and privacy

- `public-evidence.json` contains only assertions, aggregate export metadata and asset hashes. This is safe to publish with the release.
- `evidence.json`, attachment PDF files, geometry and extracted text are local QA evidence and may contain source record content. Do not publish these attachment artifacts.
- `fixture-full-a4-page-1.png` through `fixture-full-a4-page-4.png` and `fixture-full-continuous-part-1.png` through `fixture-full-continuous-part-4.png` are actual rendered illustrative outputs suitable for publication.
- All four full-scope A4 pages and all continuous crops were visually reviewed, along with the filtered, empty and long-note continuation pages. The final screen-only CSS refinement was rechecked through actual downloads on the final hashes.

The supplied workbook carries a 30 September 2026 reporting cutoff; this verification does not assert it is the latest operational dataset. No workbook recalculation, Power Query refresh or Office rendering was performed. Values are read through the application's validated source model.

## Final runtime hashes

- `assets/js/app-bundle.js`: `51ab13e0d1908b59bdd4d9e5be738815bd69336bce513468b85fe2a99e543bdd`
- `assets/css/app-bundle.css`: `14b0cb32e88a853d1c6c52d548a87af5b579584da9b95549faae54552f2ddeb6`
- `assets/css/print-measure-bundle.css`: `6e18d22b7682cd9e4d73f51e67e175aaf250f40dd8235090e49c520a8390644a`
- `assets/js/lib/offline-pdf-engine.js`: `647b32e4d4481fbc4df6edfa77ac71853131448ea4602d6b054f713ef6ee7069`
