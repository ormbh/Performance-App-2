# Performance App v135 verification

**Verdict: PASS for the approved design and tested workflows.**

This correction uses the supplied monthly layout reference and subsequent 16px/SLC/strategy-note instructions. The released v134 ZIP is the immutable before baseline. Its broad workflow/print audit remains historical; these checks cover the changed monthly screen/print composition and shared caption helper.

| Requested change | Verified result |
| --- | --- |
| Monthly print keeps paired portfolios | A4 portrait, 10mm margins, projects physically left/executive right; two 93mm columns and 4mm gap. Followups span the full 190mm width below both. A single portfolio uses full width. |
| Readable pagination | All card/figure/table font sizes retained. No page zoom or scale-to-fit. Cards fitting a page move whole when remaining space is insufficient; oversized content can continue. The illustrative before report has 4 pages; after has 3. This is not a fixed production page-count promise. |
| Financial values | Labels wrap above their amounts within the two allocation columns. Complete numeric strings remain visible; no leading digits lost. |
| Monthly metric/status and strategy names | 16px Dubai Regular Ink on screen. Agenda category/subgroup names remain 18px, supporting explanations 14px, differences 15px and table text 16px. Independent print labels remain 9pt; table body/badges 12pt and heads 13.5pt Bold. |
| SLC order and alignment | Exact logical labels retained. Latin SLC appears first at physical left, with isolated RTL Arabic to its right. First lines and figures align. Below 600px, legislation uses two metric columns; a single metric uses full width. |
| Strategy notes | Coverage/unmeasured-count, result-count and target-count captions removed screen/print. Primary values, denominator, measurement bar, valid changes and meaningful missing-source explanations remain. No empty note containers are retained. |
| Strategy alignment | 52px desktop label reserve fits two 16px lines. All three main values and the retained changes align when side by side. Print preserves shared value/change rows. |
| Header/footer and other reports | First title/logo and inline cutoff retained; no continuation masthead. Footer copyright/pages only. Other report layouts/orientations and controls are unchanged. |

Actual native screens were inspected at 320,390,599,1000,1120,1440 and1920px. The SLC/mobile review passed without document or visible text overflow. The paired monthly candidate passed 17 checks: all 35 numeric metric strings complete in the native PDF, unchanged fonts, source membership and follow-up identities. All three final PDF pages have correct A4 dimensions and copyright/page footers, with no outside-page text or body/footer collision.

Source regression passes: all 672 illustrative records, monthly counts/KPI/budget/changes, screen/print values, bar quantities and eight follow-up identities match v134. Fifteen model modules and 34 protected assets remain byte-identical. Missing and zero progress are still distinct. No workbook is changed.

| Final asset | SHA-256 |
| --- | --- |
| assets/css/app-bundle.css | `09a75135d9ad0ecc924b8478d70612a57250e15a1a16e34de2133f0eb017b8a6` |
| assets/js/app-bundle.js | `d86285126e10ed1172620f93b4a37a593a3077757459091192301fa7dee486c8` |

The app is packaged with local fonts, readable sources, the updated Revision 10 standard and an integrity manifest. A fresh extraction is checked before release. The comparison gallery and PDFs use the same explicitly illustrative workbook before/after; no operational workbook or user screenshot is published. Generated QA evidence and workbooks are excluded from the app ZIP.

These targeted browser/PDF checks are not reconciliation of the user's unavailable operational workbook. Native Windows file opening, hardware printing and formal accessibility certification are not claimed. Previous v134 verification describes that version's broader baseline, not the corrected monthly arrangement.

Rebuild: `python tools/build-bundles.py`; check: `python tools/build-bundles.py --check`.
