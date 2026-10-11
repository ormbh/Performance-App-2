# Independent search and upload preview review

**Verdict: PASS for the isolated visual previews against TEC Apple-Inspired Design, Revision 2.** Reviewed 11 October 2026. This verdict covers the supplied previews, not implementation of the standard in the working app.

## Baseline and source fidelity

- Independently compared the unpacked app with `Performance-App-v128.zip`. `index.html`, `assets/css/app-bundle.css` and `assets/js/app-bundle.js` match the release ZIP byte-for-byte by SHA-256. Before captures use the actual current app.
- Search Before and After use the same `ILLUSTRATIVE-monthly-preview.xlsx` fixture and query `استراتيجي 006`. The four record models match, including their keys, titles, statuses and progress. The renderer also asserts unchanged table text. This fixture is illustrative, not a live reporting snapshot.
- The no-match model remains zero; its approved presentation is **–**. Valid source-backed 0% completion remains visible.
- Upload Before and After retain the initial no-data state, source text, existing Excel workflow and privacy statement. Renderer assertions and final bundle hashes confirm that the preview work did not change application files or calculations.

## Typography and components

- Computed browser styles and the rendered screens confirm 38px DIN Next Arabic Regular page titles, 28px DIN card/empty-state titles, 34px DIN Next LT Arabic Regular search counts, 14px Dubai Regular supporting explanations and 16px Dubai Regular controls.
- Search table headers use supplied Dubai Bold at 18px, Ink on Linen. Names, notes and table content use Dubai Regular at 16px, neutral Taupe on Paper, with approximately 1.6 line spacing. An independent scan found no incorrect visible table leaf sizes or weights.
- Frozen and completed badges use the approved Burgundy and Green treatments at 18px. Names remain regular and neutral; match underlines preserve their text color. Remaining status mappings were checked in the proposal CSS but were not all present in the four-row rendered sample.
- Primary, secondary and icon controls use the approved palette and minimum 44px targets. The mobile menu is 44 × 44px with a 20px icon. The actual sort select is 44px high. Disabled CSV uses Ink on Linen with a Silver border and opacity 1. Scope labels use 12px Dubai Regular Taupe on Paper.
- Actual DIN and Dubai font faces load. Table headers use the supplied Bold face; regular text is not synthetically bolded.

## Logo, layout and mobile

- The supplied TEC logo retains its proportions. Independently measured Upload After at a 1920px viewport: logo 164 × 52.609px at y24, with clear space inside its header. Final upload evidence also records intrinsic dimensions and desktop/mobile bounds.
- Native desktop and 390px mobile renders were visually inspected. Main panels, Arabic wrapping, controls, empty states and results remain readable without overall horizontal overflow.
- Independently opened all three proposed frozen search HTML snapshots at 390px after the CSS-only reflow correction. Each document has a 390px scroll width; result rows retain 16px content and 18px labels without requiring the removed app scripts.
- Independently ran the actual app at 390px with the proposal CSS in browser memory and checked effective background inheritance: names and source details in all four stacked records use Taupe on Paper, including the title cells. The same check passes in the frozen results snapshot. The former Linen title-cell inheritance is corrected.
- Frozen upload Before/After were also opened independently: their desktop font roles and logo bounds match native evidence. Task comparison sheets keep Before physically left and After right without clipping the main panels.

## Verification limits

The gallery has its own working preview controls. Individual HTML snapshots are visual illustrations with application scripts removed; they do not provide live search or upload. Automated upload evidence records native file-picker pointer/Enter/Space, invalid-file feedback and loading guards in isolated browser pages. This review does not certify all parser cases, screen-reader behavior, complete accessibility conformance, Windows browser print output, or implementation in the working application. No print redesign or new app release is part of this preview task.

