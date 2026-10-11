# Preview verification

Result: **PASS for this isolated illustrative comparison.** App implementation and production workbook reconciliation are outside this preview scope.

The two monthly versions use the same frozen illustrative workbook. Their source model and screen text were compared before the proposed CSS was applied. Current v128 CSS and JavaScript hashes remain unchanged.

| Check | Result |
| --- | --- |
| Actual supplied fonts loaded | PASS: DIN Next Arabic Regular, DIN Next LT Arabic Regular, Dubai Regular; current specimens also use the existing Dubai Bold face where applicable |
| Screen typography | PASS: page36px, portfolio28px, card26px, main40px, status34px, secondary28px, table18px, changes15px, labels12px, metadata14px; proposed weights400 |
| Table roles | PASS: Ink headings on Linen; Taupe body/names/notes on Paper; names Regular |
| Empty groups / zeros | PASS in fixture: empty statuses hidden; zero quarter counts use dashes; meaningful completion percentages retained |
| Legislation composition | PASS: late2 + remaining pending9 + on-time152 + after-deadline28 = total191; late in status row and bar; SLC explanation below |
| Portfolio totals | PASS: agenda117, councils70, legislation191, special projects62, strategic projects84 |
| Follow-up table | PASS:8rows, ordered2late →3frozen →1cancelled →2transferred; stable fixture order within groups |
| Native print | PASS:4new pages; table text13.5pt; no text below9pt; intact rows, repeated table headers, no page-boundary clipping |
| Control interactions | PASS in standalone specimen: outside click/Escape close menus; arrow navigation and keyboard focus return; loading width retained and repeated action prevented |
| Icon keyboard press | PASS: Ink on Sand, Taupe border; Space tested without pointer hover;6.32:1 text/background contrast |
| Desktop/mobile geometry | PASS in Chromium:1920px desktop and390px mobile; no overall page overflow; mobile table text remains18px |
| Visual inspection | PASS: all paired sheets, full monthly screenshots and every current/new PDF page reviewed |

New print pagination keeps readable type and intact cards; the first summary page therefore has unused space. This is a content result, not a required four-page limit.

DIN Next LT Arabic is explicitly embedded in the PDF. DIN Next Arabic and Dubai export as Type3 glyph fonts; browser font-loading/CSS evidence and visual review establish their source identity. Some extracted Unicode is incomplete. Only arrow symbols use a Liberation Serif fallback. These checks do not claim full accessibility certification, complete PDF text mapping, or verification of Windows browser/print behavior.

Evidence: monthly-preview-evidence.json, sheets-evidence.json, controls-evidence.json and frozen-illustrative-data.json.
