# Performance App v152 — focused verification

The search landing-page menu now appears beside **بحث في التقرير**. The menu, search and **عرض جميع النتائج** controls form one centered RTL row. This release changes only the home composition and home-menu placement, plus generated bundles and release metadata.

## Passed

- Actual generated bundle, without source injection, checked at 1440×1000, 768×1024, 390×844, 320×640 and 390×400.
- Menu is physically right of search, with browse on the left. The entire group is centered within 1 CSS pixel; all three vertical centers align within 1 CSS pixel.
- Original logo, title and search-field coordinates and dimensions remain within 1 CSS pixel of v151 across all five viewports.
- All three controls retain at least 44×44px targets; no document overflow. Narrow-phone spacing keeps them in one row.
- The opened menu stays inside the visible viewport; long menus scroll on short screens. All ten menu entries remain available.
- ArrowDown opens and focuses the first menu item; Home/End navigation, Escape with focus restoration, click toggle and outside click work.
- Query search and browse-all still navigate to results. The results page retains its own header menu. Existing autocomplete was dismissed with Escape before activating the search button.
- No browser JavaScript errors. Source-to-bundle consistency and JavaScript syntax checks passed.
- Desktop, phone and short-viewport screenshots visually inspected. ZIP CRC and fresh-extraction manifest hashes verified during packaging.

## Scope

Fixture: ILLUSTRATIVE-monthly-preview.xlsx (SHA-256 4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08).

The fixture is illustrative. These are focused search-layout and navigation checks, not a new source-data or PDF audit. Report models, agenda chart source and export logic remain byte-identical to v151. Browser validation used a local loopback server; this is not a new cold file:// or native-device validation.

The revised vertical-quarter chart is a separate review illustration. It uses counts, omits percentages and selected-quarter ratios, and restores the original definition legend. It is not applied to this app.
