# v130 bar meanings and proposed clarification

Read-only audit of actual source in `/workspace/saytara-work/Performance-App-v130`. No app source changed. The uploaded screen crops are references, not a complete source workbook.

| Visible bar | Actual meaning / denominator | Current fill(s) | Suggested concept |
|---|---|---|---|
| Special projects, each leadership / secretariat subgroup | Number classified completed ÷ that subgroup’s total. Screenshot: 12 / 24 = 50%; 10 / 36 = 27.8%. It does not average individual project progress. | Completed Green `#01831E`; remaining Linen `#EFEBE7` | Keep fraction or percentage with a concise `نسبة المنجز` metric label; no explanatory paragraph. |
| Annual agenda status strip | Each disjoint category count ÷ agenda total. Screenshot: 43 completed + 16 ready + 58 in work = 117. A red late segment appears only when > 0; uncategorized residual is Silver. | Green `#01831E`; ready Stone `#ABA394`; work Taupe `#756B5F`; late Red `#C00000`; residual Silver `#C8C7C7` | Keep status values above; these act as the legend. Retain a short visible missing-status note only when residual > 0. |
| Council decisions status strip | Each status count ÷ council **follow-up population**, not every council record in the source. Screenshot: 38 completed + 31 in work + 1 without approved status = 70. The small silver section is that one record. | Green `#01831E`, Taupe `#756B5F`, late Red `#C00000`, Silver `#C8C7C7` | Preserve `بدون حالة معتمدة: 1`. Do not remove a real scope / missing-data qualification as decorative repetition. |
| Legislation status strip | Each disjoint category ÷ legislation total. Screenshot: 152 on-time completion + 28 after-deadline completion + 9 pending + 2 late = 191. Late is excluded from pending. | Both completion groups Green `#01831E` with Paper `#FCFBFB` divider; pending Taupe `#756B5F`; late Red `#C00000`; residual Silver `#C8C7C7` | Keep separate status figures and thin divider. Date-derived late cohort never double counts pending; malformed overlapping statuses suppress the bar rather than invent a reconciliation. |
| Monthly allocated budget strip | Sum allocated ÷ approved budget. The remaining track represents the unfilled approved-budget fraction; it is not a project-status category. | Taupe `#756B5F` on Linen `#EFEBE7` | Add / retain a short `المخصص من الموازنة` percentage if clarification is needed. Do not color allocation Green. |
| Monthly invoices-spending strip | Sum invoice spending ÷ approved budget. Screenshot: 24,123,730 / 75,750,000 ≈ 31.8%. Does not measure completion. | Teal `#115E67` on Linen `#EFEBE7` | Existing `الإنفاق 31.8% من الموازنة المعتمدة` is meaningful denominator information. Keep concise. |
| KPI measured / registered strip | Measured indicator count ÷ registered indicator count; e.g. 39 / 54 = 72.2%. Does not compare average results with targets. | Teal `#115E67` on Linen `#EFEBE7` | Keep measured / registered fraction. The derived coverage percentage can be omitted if it repeats the fraction, but missing / unmeasured meaning must remain discoverable. |
| Project status table count bars | Relative count for each status on a single shared **0–largest-status-count** scale. Full length is the largest row count, not 100% of all projects. | Completed Green `#01831E`; other count bars Teal `#115E67`; Linen track | Keep numbers and shared scale. Do not call these completion percentages. |
| Project status table budget bars | Sum valid approved-budget values for the row; common **0–largest-status-budget** scale, displayed in AED / thousand AED / million AED as the column heading indicates. | Taupe `#756B5F`; partial aggregates hatch Stone `#ABA394` / Sand `#E7E0D3`; Linen track | Keep money unit at column heading. A partial-data marker must remain tied to the value. |
| Project average progress strips | Unweighted arithmetic mean of valid source percentages in range 0–100, among projects that supply one. These do not derive from status. | Teal `#115E67` on Linen `#EFEBE7` | Keep percentage and a short partial-data cue only when coverage is incomplete. |
| Project financial panels | Allocated, invoices spent, or value of completed works ÷ approved budget **within the matched valid project cohort for that panel**. Cohorts may differ. | Allocation / work-value Taupe `#756B5F`; invoices Teal `#115E67`; remaining Linen `#EFEBE7` | Retain matched denominator / cohort information. Work value, invoice spending and project completion are different metrics. |

## Hatched crop and availability note

The cropped “44” bar uses diagonal hatching, not a dashed timeline. In actual code, `.pd-partial` is added to financial aggregate bars when `metric.known < metric.total`; it is not added to progress strips. `قيم متاحة: 59 من 61` means **59 of 61 projects have usable numeric values for that metric**. The other two values are absent / invalid and are excluded from the financial sum, not treated as zero. The bar’s filled length encodes the financial sum; it does **not** encode 59 / 61 data coverage. The exact unit of “44” cannot be proven from the crop, which omits its column heading. In this location the heading often reads `مليون درهم`.

The same `coverage()` note is also used for average progress, where it counts valid progress percentages instead of valid budget values. Coverage counts are per metric, not an overall data-quality score.

### Recommended before / after wording (concept only)

| Before | Proposed after | What remains available |
|---|---|---|
| Hatched money bar + `قيم متاحة: 59 من 61` | Same hatched bar + short cue **`بيانات جزئية · 59/61`** | Focus / hover / tap opens `الموازنة تجمع 59 قيمة رقمية من 61 مشروعاً؛ قيمتان غير متاحتين ولا تُحتسبان صفراً.` |
| Same long explanation on many complete rows | No cue when all values are present | One accessible legend / explanation for the chart. |
| Partial average-progress note | **`بيانات جزئية · 59/61`**, when applicable | `متوسط الإنجاز من نسب 59 مشروعاً من 61؛ النسب غير المتاحة مستبعدة من المتوسط.` |
| Dense explanatory footer lines | One concise chart definition / accessible disclosure | Actual scope, denominator, missing-data, overspend or discrepancy notes remain available. |
| Screen-only tooltip proposed for partial data | Print shows short visible partial-data note at the affected aggregate | No hover dependence in exported PDF. |

Deleting availability semantics altogether would make a partial sum look complete. A visual hatch without an explained meaning is not sufficient. Compact inline cues plus an accessible disclosure are a clearer compromise. Notes that only repeat the title can be removed; notes that change the denominator / completeness cannot simply disappear.

## Color consistency caveat

Monthly status-strip colors and project calendar status-strip colors presently serve chart-series roles and are not identical to status badge surfaces. Project calendar colors are: completed Green `#01831E`, work Taupe `#756B5F`, not-started Burgundy `#651D32`, frozen Stone `#ABA394`, transferred Silver `#C8C7C7`, cancelled Charcoal `#333333`; unknown states are excluded as a named series and retained in the denominator / missing-status footnote. Do not silently recolor these as though they were buttons. A future unification should be shown as a separate chart-palette concept, preserving Green completion and Red lateness.

## Source evidence

- `assets/js/views/dashboard.js:85–109`: guarded ratios, monthly meters and disjoint status distribution; `:142–186`: actual subgroup / money / status call sites.
- `assets/css/tec-apple-monthly.css:3–15`: monthly fills and after-deadline Paper divider.
- `assets/js/views/portfolio-delivery.js:11–15`: money-unit scaling; `:28`: availability wording; `:37–59`: common numeric scales, partial financial bars, progress tracks; `:62–67`: status table / explanatory chart definition; `:112–138`: matched-cohort financial panels.
- `assets/js/model/portfolio-delivery.js:14–16`: strict financial / progress parsing; `:24–29`: metric-specific known counts, sums and unweighted progress; `:94–108`: matched finance cohort denominators and exclusions.
- `assets/css/portfolio-delivery.css:57–91`: plot geometry, diagonal hatch, project chart-series colors; `assets/css/tec-apple-projects.css:4,19–20`: approved Green completion override.

All numbers above are either visible in the supplied screenshots or formulas from app source; this audit does not claim reconciliation against the user’s operational workbook.
