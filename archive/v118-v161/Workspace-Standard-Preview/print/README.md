# TEC printing component proposal — illustrative specimen

This is a review artifact for the proposed shared print header/footer setup. It does not update the app or implement a live report exporter.

Public-safe review artifacts:

- `TEC-Print-Before-After.png`: first-page header, continuation header and footer at the same native PDF scale. The before panels come from v129's explicitly illustrative monthly export, not the user's supplied production PDF.
- `TEC-Shared-Print-Proposal.pdf`: three A4-landscape component pages.
- `TEC-Shared-Print-Proposal-Page-1.png` through `-Page-3.png`: rendered copies of every proposed PDF page.

Page 1 demonstrates selected overview components, the first-page title/logo/context and reserved footer. It explicitly does not represent the complete monthly overview. Pages 2–3 demonstrate two continued follow-up-table pages containing the eight frozen illustrative rows, unchanged and in the source-established group order. The three-page specimen is not a complete export and is not a claim that the user's supplied five-page report can be reduced to three pages.

The first-page title uses DIN Next Arabic Regular 24 pt and a 38 mm official TEC logo. Continuation pages use DIN Next Arabic Regular 16 pt document context, Dubai Regular 10.5 pt date/sector/unit, and a 30 mm logo. Continuation context sits outside the table header. Table headings repeat on both table pages and use Dubai Bold 13.5 pt; body/names/notes/status badges remain Dubai Regular 13.5 pt. Supporting labels are at least 9 pt, figures retain approved roles, and quarter secondary values use DIN Next LT Arabic Regular 20 pt. Footer context, date, page numbering and legal text use Dubai Regular 10.5 pt.

The printed field for entity selection is absent; sector/unit context remains. Footer source filenames remain screen-only. Actual entity names in report content would remain visible when present; hiding the field must not reset scope.

The outer PDF margin remains 10 mm on A4 landscape. Header and footer reservations are inside that usable area. The HTML review pages deliberately use explicit page prototypes and a static `page X of 3` value: later implementation must obtain page count from the actual renderer, paginate dynamic content and repeat context automatically. There is no fixed shrink factor or fixed target page count.

The existing canonical proposal uses a `طباعة التقرير` primary action and optional adjacent `إعدادات الطباعة` secondary action. Settings use the existing live/save-preferences flow; the print action opens native print directly without adding a required confirmation.

## Verification

`print-proposal-verification.json` records the final native Chromium render. All four supplied font faces loaded. Effective style sizes matched the proposal. The PDF has three A4-landscape pages, all content spans remain inside the usable 10 mm-margin area, and no body/row/heading intersects a footer. All eight frozen row keys are unchanged and ordered identically to v129's illustrative fixture. Every final page and the comparison image were visually inspected for Arabic shaping, badge identity, wrapping, clipping and header/footer continuity.

The frozen illustrative workbook hash is `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`; its extracted review data are in `frozen-illustrative-print-data.json`. Only illustrative names/notes and values are used in public-safe artifacts. Internal supplied-production-PDF renders and text outside this directory must not be included in a public preview package.

Regeneration scripts `freeze-fixture.py`, `build-proposal.py`, `render-proposal.py` and `build-comparison.py` use the bundled `../assets/fonts` and `../assets/img` resources for preview rendering; fixture extraction itself references the existing local v129 app and review workspace. They are audit tools, not an app build change. Dynamic live-export behavior, production-workbook reconciliation, native Windows rendering of this proposal and PDF accessibility certification were not run.

The portable HTML specimen uses bundled local assets. By default it opens for review without invoking print. Adding `?autoprint=1` waits for the supplied fonts and official-logo images to finish loading, then opens native printing. Its illustrative/component-specimen labels remain visible. This convenience does not add a live app export implementation.
