# TEC design comparison — current and new

Visual previews of the current v128 monthly page and proposed TEC Apple-Inspired Design standard. The app, workbook data and calculations are unchanged. Both monthly versions use the same illustrative fixture values.

Download **[TEC-Design-Comparison.zip](TEC-Design-Comparison.zip)**, extract it and open **[index.html](index.html)**. Open PNGs at 100% and PDFs at actual size: GitHub thumbnails and fitted images scale the previews down.

## Paired comparison sheets

Current appears on the left and the proposed standard on the right.

| Preview | What it shows |
| --- | --- |
| [Action-button states](TEC-Controls-Current-New.png) | Default, hover, pressed, focus, disabled and loading; secondary, destructive, icon and text actions. |
| [Inputs, filters and navigation](TEC-Inputs-Current-New.png) | Field boundaries, focus, errors, disabled states and selected tabs. |
| [Typography and figure colors](TEC-Typography-Current-New.png) | Actual fonts and sizes, neutral table text and status color exceptions. |
| [Spacing](TEC-Spacing-Current-New.png) | Card padding, table row spacing and aligned change arrows. |
| [Current and new print](TEC-Print-Current-New.png) | Native PDF appearance and content-driven pagination. |
| [Page versus print — table detail](TEC-Page-Print-Table-Detail.png) | A closer look at screen and print table readability. |

## Full monthly page and native PDFs

| Format | Current | Proposed |
| --- | --- | --- |
| Desktop screenshot, 1920px viewport | [Current PNG](TEC-Monthly-Page-Current.png) | [New PNG](TEC-Monthly-Page-New.png) |
| Monthly HTML snapshot | [Current HTML](monthly-current.html) | [New HTML](monthly-new.html) |
| Native print PDF | [Current PDF — 2 pages](TEC-Monthly-Print-Current.pdf) | [New PDF — 4 pages](TEC-Monthly-Print-New.pdf) |
| Mobile screenshot, 390px viewport | — | [New mobile PNG](TEC-Monthly-Page-New-Mobile.png) |

The monthly HTML files are visual snapshots without the app’s operational JavaScript. The proposed print separates the budget section and uses additional pages to retain readable text; the monthly screen composition stays unchanged. This fixture’s page count is a review result, not a fixed report limit.

The images were rendered at **100% CSS scale, device scale factor 1**. Use 100% browser zoom to inspect the HTML. A physical print size and a screen pixel size are distinct; inspect the PDF at actual size rather than comparing scaled thumbnails.

## Live control specimens

- [Standalone action controls](controls.html) — paired static state specimens using the actual v128 CSS cascade and proposed tokens.
- [Inputs and live interactions](inputs.html) — try menu dismissal, keyboard navigation, selected tabs and loading.

Current generic loading, destructive-button and search-field validation treatments are marked as undefined where the shared current component has no dedicated treatment; the previews do not invent a legacy state.

## Proposed screen and print scale

All proposed faces are supplied **Regular (400)**: DIN Next Arabic for headings, DIN Next LT Arabic for figures, Dubai for table and supporting text.

| Role | Screen | Print |
| --- | --- | --- |
| Page title | 36px | 24pt |
| Portfolio heading | 28px | 18pt |
| Card / section title | 26px | 16pt |
| Main figures | 34–40px | 24–28pt |
| Secondary figures | 28px | 20pt |
| Table headings, content, names, notes and status labels | 18px | 13.5pt |
| Change arrows and differences | 15px | 11pt |
| Minor metadata | 14px | 10.5pt |
| Important labels and explanations | 12px | 9pt |
| Action / field values | 16px; minimum 44px control | Operational controls hidden |

Spacing uses proposed 4 / 8 / 12 / 16 / 24 / 32 / 48px defaults; cards retain 18px corners. Desktop card padding is 24px, mobile padding 16px. Table cells use 16px padding and approximately 1.6 line spacing. The full standard identifies previously approved choices and new defaults separately.

## Verification and limits

- Supplied source font files and browser font loading verified; exact TEC palette used.
- Proposed controls tested for outside-click dismissal, Escape and focus return, menu arrow keys, selected navigation, fixed-width loading and duplicate-action prevention.
- Icon pressed state tested with mouse-down and **keyboard Space with the pointer away**: Ink on Sand, Taupe border, **6.32:1 contrast**. Keyboard focus retains Ink on Paper with a 2px Teal ring and 2px gap.
- Chromium desktop at 1920px and proposed mobile at 390px reviewed. Native PDFs and their rendered pages reviewed. Windows and the Windows print dialog were not run.
- Native PDFs embed DIN / Dubai as Type3 glyph fonts. Some extracted Unicode text is incomplete; change arrows use a Liberation Serif fallback. Source fonts and CSS font loading were verified. This is not a claim that every PDF glyph has complete searchable Unicode mapping.

These are illustrative comparisons and targeted checks, not an official TEC brand manual or a full accessibility certification. No app implementation or data reconciliation is claimed by this preview pack.

## Full standard and earlier previews

- [Consolidated design standard](../Design-Standard/README.md)
- [All supplied font previews](../Font-Previews/README.md)
- [Text colors and exact TEC palette](../Color-Previews/README.md)
- [All approved status badges](../Status-Previews/README.md)

These relative links target sibling folders in the repository. When viewing only an extracted comparison folder, open the corresponding repository pages for the full standard and earlier previews.
