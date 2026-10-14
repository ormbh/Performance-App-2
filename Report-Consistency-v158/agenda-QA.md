# Agenda export correction — v158

Final rebuilt-bundle verification: PASS, 56 checks. Uses the existing explicitly illustrative workbook; no source data is changed.

- Removed the additional exported status-by-quarter count matrices. Exact interactive disclosures remain available on screen.
- The all-scope native PDF now has 14 physical pages (cover + 13 content pages), down from 16. The filtered emerging-only PDF has 3 physical pages, down from 4. Counts are content-driven rather than hardcoded.
- Charts, aggregate status totals and the original detailed legend stay together on physical page 2. Cover remains full-bleed without footer; content numbering excludes the cover.
- Every source topic record remains present in the actual native PDF: 117 all-scope; 2 in the selected entity scope.
- Native editable PPTX has no additional count-matrix slides: 15 slides/2 charts all-scope, 4 slides/1 chart filtered. Every original topic table row remains.
- PPTX table styling uses Linen headers, Ink labels, Paper body and bottom-only fine dividers. No zebra rows or vertical table frame.
- Desktop/phone layout, quarter selection, exact interactive details, native chart operations and source immutability pass.

Native PDF pages 2 and 3 were rendered and visually inspected. The final export confirms the inherited even-row seams are gone: Paper rows use only fine horizontal dividers beneath a uniform Linen header. Deadline headings stay on one line, and status badges remain readable. Charts and the original detailed legend stay together. Actual Office rendering is unavailable, so PPTX verification covers its native structures, values and style XML rather than a claimed Office visual pass.

Machine-readable evidence and actual PDFs/PPTX are in this folder. Runtime bundle hashes are recorded in evidence.json.
