# Continuous monthly preview — independent review

**PASS.** The actual native PDF is one continuous page, nominally **210 × 634 mm** (Chromium output **209.89 × 633.90 mm**). It preserves the v135 reference content and type scale.

| Check | Result |
|---|---|
| Full page and four overlapping readable native render crops | PASS — no clipped cards, rows or overlapping text |
| Projects on the left; executive portfolio on the right | PASS |
| Complete eight follow-up records, including names and notes | PASS |
| SLC captions; removal of the three strategy explanatory notes | PASS |
| One official logo/header; copyright and page1of1 footer | PASS |
| Native typeface names and sizes | Same as reference; title24pt, table12pt, tableheads13.5pt, footer10.5pt |
| Font embedding | EightType3 embedded glyph programs and twoType0 embeddedfontprograms |
| Page width / actual footer collision | No text outsidepage and no footer collision; **28.43pt** clear belowbody |
| Native visible body versus the three-page v135 reference | Exact bodytext-line/fontmultiset equality after excluding footers and the single repeated continuation tableheader |

All **37 metrics** and **8 source follow-up keys** remain unchanged in the parent/browser evidence. The independent native comparison finds **no missing or added visible body content**. Footer counters change appropriately from three numberedpages to one.

PDF SHA-256: `0216f2bcda2f84fab47efb655998da4a22c73c9ec45d5c70844336c833047871`  
Reference SHA-256: `1f33e4b923d141e107d93f9d084d2ce988a03c31bf4a53f6f55b554679db482e`

[Machine-readable review](Independent-Preview-Review.json) records exact dimensions, fonts, geometry, source scope and comparison method. Additional detailed evidence is stored in `independent-review/` and `independent-text-review/`.

This is a **concept preview**, using the unchanged frozen illustrative workbook, not a change to the app's A4 print setup. No app or workbook was edited. Hardware printing and formal PDF accessibility certification were not tested.
