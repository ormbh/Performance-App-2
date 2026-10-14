# Agenda / special-project consistency — final v158 QA

**PASS: 249 checks (129 UI + 120 native HH PDF), no runtime errors or external network requests.**

Verified the final built app at 1440, 768, 390 and 320px: equivalent typography, gutters, panel and legend styling, table/record-card roles, labelled mobile fields, title-first record order, 72px filters, phone filter dialog/Escape, report editors, partial selections (first name +1), all selections (الكل), and reset. Normalized source records remain identical to the prior workbook baseline and unchanged by interactions.

Actual downloaded HH PDFs: all 62 projects produce 71 physical pages; the selected police entity’s 2 projects produce 6 physical pages. Both preserve exact project keys and recorded percentages in main list/detail cards. The main list contains six columns without PM, while every recorded PM value remains in its matching detailed card. Table headings are 13.5pt on Linen and body text 12pt on Paper. Visually checked the final main-list page: no former header vertical seams or alternating outlined rows.

Chart panels and full definitions remain together on physical page 2, with native vector charts. The cover fills landscape A4 and centers title/entity/date as a group. Selected entity appears on the cover only when selected. The cover has no page number or copyright; content-page numbering excludes the cover and starts on physical page 2. Every actual PDF text span stays within page bounds.

Zero-count HH appendices and their contents links are omitted. The filtered report ends with its second real project card, without an empty completed-project page. Interactive return-navigation links do not print. The obsolete duplicate overview and circular indicators remain absent from the PDFs.

Final evidence includes runtime hashes matching the browser’s actual loaded JS/CSS and native-print CSS. See `FINAL-EVIDENCE.json`, `ui-evidence.json`, `pdf-evidence.json`, actual PDFs and screenshots in this directory. Agenda PDF verification is maintained by the separate agenda export QA task. This audit does not claim actual Office rendering or a redesign of unrelated pages.
