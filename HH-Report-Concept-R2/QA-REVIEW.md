# HH illustration revision 2 — QA review

**Verdict: PASS for the revised illustrative HTML and three-page PDF.** All 75 focused browser checks pass. Desktop, mobile and all actual PDF page renders were visually inspected. No unresolved defect was found in the requested changes.

Reviewed 14 October 2026 using the Saytara QA skill. The source is illustrative, and the report remains a design review; this verdict does not certify operational reporting or official workflow definitions.

## Source and scope

- Source: `../monthly-apple-preview/ILLUSTRATIVE-monthly-preview.xlsx`, as audited in `source-review.json`, and the unchanged HH source payload `data.js` from the previous concept.
- `data.js` is byte-identical to the previous concept. SHA-256: `9509c7419a7112facfa83d28222ee9c7294a05915833ff08bcb57e312d0a951d`.
- Reporting label: **حتى تاريخ 30/09/2026**. This remains a displayed period, not a new historical recalculation or Power Query refresh.
- Latest requested cohort rule: `t.lead === 'نعم'` is leadership; every other value, including the two blanks, is TEC/general secretariat. No separate unclassified cohort is displayed.
- Grain: 62 source rows with 62 distinct parsed keys. Cohorts cover all keys exactly once: leadership **24**, TEC **38**. Source values were not rewritten.
- Summary: **23 done + 38 working + 1 other = 62**. Leadership: development **12**, done **12**. TEC: review **3**, development **23**, done **11**, other **1**.

## Verified changes

| Check | Result and evidence |
| --- | --- |
| Source filename removal | PASS — all 62 actual detail cards exclude `Source.Name`, the displayed source-file label, and raw source filenames. Raw payload remains unchanged. The PDF detail also excludes the filename. |
| Zero and missing display | PASS — zero detail percentages display `–` while the numeric accessibility value remains `0`. Empty summary count/percentage use `–`. Generated `غير مسجل`, `غير مسجلة`, `غير متوفر` and `غير متوفرة` become blank; none appear in the 62 actual detail cards. The intentionally labelled before/after design example still shows its input. |
| Ready styling | PASS — the sample `جاهز للعرض` label and count both compute to teal `#115E67`; its filled bar has a contrasting number inside. The source contains no ready HH rows. Sample **8** is explicitly outside report data. |
| Cohort charts | PASS — every nonzero sector/status segment and all subtotals match `source-review.json`; both panels use common maximum **15**, six aligned source-order sector rows, and dashes for zero sector totals. Empty cohort panels disappear under cohort filtering. |
| Bar numbers | PASS — every displayed segment count stays inside its segment at viewport widths **1440, 1280, 1200, 390 and 320 px**. PDF bar geometry also passes and is visually legible. |
| Detailed legend | PASS — sits below both charts, in source status order, with recorded-status descriptions. The PDF marks the descriptions as proposed wording. These are not certified official workflow definitions. |
| Responsive layout | PASS — no page-level horizontal overflow at the five tested widths. At 390 and 320 px, the long first selection is truncated and **+1** stays visible within the filter control. The projects table retains its own intended horizontal scrolling region. |
| Cohort filters and reset | PASS — leadership selects exactly the 24 audited keys; TEC selects all 38 audited keys, including blanks; an empty scope removes panels and shows the empty state; reset returns all 62. |
| JavaScript | PASS — no page errors during the reviewed scenarios. |
| Arabic and visual output | PASS — inspected desktop charts and detail, 320 px charts, the mobile multi-selection control, and all three actual PDF renders. No observed clipping, overlap, broken Arabic shaping or RTL ordering defect. |
| HTML–PDF consistency | PASS — PDF uses the current HTML/CSS/JS/data hashes, the same 24/38 split and sector counts, the matching detail sample and display rules. Chart and detail PDF pages have zero embedded images and contain native browser text/vector output. This does not imply PowerPoint editability. |

## Evidence

- `qa-review-evidence.json`: 75 browser assertions and segment bounds at each tested width.
- `qa-review-probe.py`: reproducible focused browser checks.
- `qa-pdf-evidence.json`: independent final PDF/hash/input checks.
- `print-evidence.json`: PDF generation, proportional bars, page bounds, font and DOM-clone evidence.
- `qa-charts-desktop.png`, `qa-detail-desktop.png`, `qa-display-rules.png`, `qa-charts-mobile-320.png`, `qa-charts-mobile-390.png`, `qa-filter-mobile-320.png`, `qa-filter-mobile-390.png`: actual browser captures.
- `print-1.png`, `print-2.png`, `print-3.png`: actual final PDF renders, generated from the delivered PDF using PyMuPDF and visually inspected.
- `TEC_HH_Report_Review_R2.pdf`: three A4 landscape pages; SHA-256 `4496bb878326982a5b39c99ad67ffcc49f79fd37f976238d0643adb4699a8b4e`.

## Not run / not applicable

- No fresh workbook refresh, formula recalculation, historical snapshot comparison or independent full workbook audit was performed in this revision; the previously validated source fixture and its source-review audit are the baseline.
- No PowerPoint or modified Excel deliverable is supplied in this revision; their editability was not tested.
- Visual/geometry checks are not an accessibility certification. Font evidence records Chromium's embedded Type3 glyph subsets and TrueType subsets; no original full font is required to render the PDF.
