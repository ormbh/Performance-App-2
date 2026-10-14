# Portfolio audit and proposed implementation checklist

**Review only · 15 October 2026 (Dubai) · current runtime v166.** No application, source workbook, release ZIP or approved-principles change is included.

## Source basis and correction

The supplied `Saytara_2026_Mold_v2.xlsx` has 84 raw rows on `مشاريع_الأمانة`, with populated status/type/priority/date/progress fields but **no project titles, manager names or financial values**. The current app correctly reports zero eligible named projects and warns about the 84 untitled rows. The source uses a fixed 30 September 2026 cutoff; it is not established as the latest operational source.

An initial browser reconciliation incorrectly retained an already-loaded illustration workbook. Those attachment claims were discarded. A fresh, isolated browser context subsequently waited for the exact uploaded file identity and matched the source completeness against independent openpyxl and XLSX XML inspection. This correction supersedes the earlier progress update describing populated source reconciliation.

| Input | SHA-256 | Verified role |
| --- | --- | --- |
| Supplied workbook | `1638e2d9e194c21d8d8e258a2bcad7c121cbeb9a4f529f90cea632f212cc66f2` | Source-completeness audit; zero named projects and no financial values |
| Generated illustrative workbook | `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08` | Populated behavior, layout and export examples; synthetic names and amounts |
| Unchanged v166 ZIP | `de52212e47f5848ac405d94f28e77eb190b903dedf51b6452748ceef7848ac74` | Exact released runtime baseline |

All populated illustration figures are **examples**, not verified current reporting totals. No workbook save, Office recalculation, Power Query refresh or historical-snapshot reconciliation was performed.

## Membership, totals, statuses and filters

The generated fixture has 84 named projects: completed 10, active 61, not started 7, frozen 3, transferred 2 and cancelled 1. Its six follow-up projects are frozen/cancelled/transferred. The monthly example's eight follow-ups include two legislation items, so the scope difference is expected.

Completed-project share is 10/84 = 11.9%; mean recorded progress is 38.9%. Neither is a spending measure or a budget-weighted average. The example approved budget is AED 58,275,000; allocation is 46,620,000, unallocated is 11,655,000, invoice spending is 20,396,250 and recorded work value is 23,018,125. Those independent measures must keep their own denominators and labels.

The example deadlines include 81 projects in 2026 and three in 2027. Preserve year identity, active quarters/months and undated records when present. Do not infer status from a recorded percentage or add calculated lateness to disjoint recorded-status totals.

The data audit completed 84 assertions: 82 passed and two controlled consistency cases failed. The failures are proposed corrections, not concealed passes. Eleven fixture filter cases covered unions and intersections for sector, unit, entity, type, priority, status, year/quarter and manager. Portfolio/report record identities and order reconcile. A status click opens the exact matching records, return navigation works, and the report command preserves active scope.

Budget projects belong to **الأمانة العامة للمجلس التنفيذي** under the existing approved parent mapping; there is no separate source entity column. Keep sector and organizational unit distinct from entity. Choosing another entity excludes these projects; a union including the General Secretariat includes them. Project-specific filters are additional portfolio/report scope and must not silently be applied to the monthly page.

## Data findings

| Finding | Evidence and proposed treatment |
| --- | --- |
| Incomplete operational source | Supply project names and intended financial fields before operational totals can be reconciled. Keep the current untitled-record diagnostics; do not substitute example values. |
| Inconsistent invalid-number parsing | A controlled `0x10` amount is rejected by the portfolio but interpreted as 16 by monthly/legacy financial parsing, producing 1,200.50 versus 1,216.50. Reuse one strict decimal reader and compatible eligibility rules. This case is not present in the available attachment. |
| Incomplete unknown-status bar | A controlled month with one completed and two unknown records retains total three, but draws only the completed third while describing a 100% distribution. Keep unknown records neutral and include their segment/count, without classifying them as active. Records are retained; this is a chart/wording problem. |
| Frozen terminology | Portfolio uses مجمّد while other views use معلق for the same source Frozen group. Use one approved display term and appearance while retaining raw values and filter identities. |
| Deliberately different money populations | Portfolio money includes named projects; monthly source formulas include monetary rows without a title. Controlled named 100 plus unnamed 900 yields 100 versus 1,000 with diagnostics. Preserve and explain the defined populations rather than forcing artificial agreement. |

## Whole-page recommendations

| Area | Proposed treatment |
| --- | --- |
| Identity and hierarchy | Consistent default title **مستجدات محفظة المشاريع 2026**, source period/cutoff, obvious overall count with الإجمالي beneath, and existing report options. Preserve custom titles and periods. |
| Navigation | Compact contents in page order; quiet explicit main-list/report links. Preserve active scope, exact record identity and return/focus behavior. |
| Filters | Retain all eight fields and their source-backed union/intersection behavior. The review illustrates direct visibility; changing disclosure placement must not alter filtering. |
| Budget and deadlines | Budget physically right, deadlines left. Full headline financial amounts with AED units. Count-scaled monthly bars on one scale across years, quarter/year totals, and recorded mean progress in its own column. |
| Status chart and legend | Separate count and budget scales; readable count labels; recorded progress remains distinct. Shared fills/ink/borders, completed labels and values Green, late Red where applicable, ready Teal only if supported. One compact portfolio-specific definition legend. |
| Empty and missing values | Hide wholly empty groups; true numeric zero displays a dash; missing values stay blank. No fake minimum bars, invented percentage or default status. |
| Manager analysis | Preserve the top-three follow-up ranking: 50% unfinished-count share and 50% unfinished-budget share. It measures follow-up volume, not employee performance. Preserve the separate completed comparison group when present. |
| Priority and type | Count chart and budget chart remain separate, using actual intersections and independent scales. Preserve source order and neutral unknown groups. |
| Tables | Shared RTL sequence **م، المشروع، الجهة المعنية، الحالة، نسبة الإنجاز، موعد الإنجاز**; follow-up appends ملاحظات. Keep full notes, one-line deadline heading and continuous row numbering. |
| Additional fields | Keep sector/unit and type/priority as labeled context. Preserve populated PM and finance through current record views; retain manager context in operational follow-up. Do not add special-project narrative cards. |
| Additional information | Populated report notes/recommendations at the end, with a contents destination. Hide empty editorial sections. Keep methodology and source diagnostics available. |
| Export | Match data scope, section sequence, table order, naming and status semantics. A cover/contents extension is a proposal, not an existing export defect; keep A4 portrait unless a different geometry is approved. |

The proposed deadline chart changes a **visual encoding**, not a calculation: current one-project and 79-project months have equal-width 100% bars. The illustration gives them proportional lengths on a common count scale. It keeps source-year totals and recorded averages intact.

## Verification completed and remaining

The current v166 UI was inspected with the illustrative fixture at 1440, 390 and 320 pixels. Its existing native portfolio PDF was downloaded and all six A4 portrait pages inspected: text, page boundaries, displayed page sequence and copyright passed. No visible source filename or Harvey-ball indicator was found in the inspected views. These results apply to the example fixture and existing export, not to a newly implemented layout.

The proposed HTML and image plates were separately checked for fonts, RTL alignment, numeric geometry, labels, shared table order, example-data notices, source-derived sample totals and phone containment. See `evidence.json` for the final review checks and limitations.

An eventual implementation must verify the complete operational workbook, all eight filter fields, exact table/report memberships, unknown and missing statuses, malformed numeric text, zero/missing finance, small segments, long Arabic text, keyboard navigation, and fresh native A4 output. Recheck pagination and links after layout changes; do not infer PDF correctness from these screen illustrations. No accessibility certification or new production-PDF pass is claimed here.
