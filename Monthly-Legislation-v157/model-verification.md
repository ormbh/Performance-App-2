# v157 legislation model verification

PASS: 34 focused browser model checks. See `evidence.json`.

The existing illustrative workbook loads through v156, then the final v157 `rules.js` and `comparison.js` sources are injected into the browser. This isolates model changes and preserves a before/after comparison of every existing metric and normalized source record. This is not the final bundled UI/export verification; the independent v157 QA run covers that integration.

The source fixture has 191 legislation records: 180 completed (152 on time + 28 overrun), 11 in progress, of which 2 late. A separate explicitly synthetic model exercises the approved 183 / 178 / 5 / 2 example and +17 / +14 / +1 changes. No illustration figures enter production code.

The `legDone` predicate combines existing on-time and overrun membership with a per-record OR, leaving the source-specific predicates available. Generic drilldown and comparison descriptors inherit the new metric. `legProgress` remains the existing source-defined inclusive in-progress count. `legLate` remains unchanged; projection flags identify cases where the nested-subset presentation is not supported by the records.

Historical completion derives from both recorded prior SLC components for every selected sector/unit row. Missing, quarantined, negative, fractional, or impossible components cannot create an arrow. The derived prior in-progress count also validates each row before summation. Existing entity scope and prior-workbook availability restrictions are retained. The snapshot schema and loader, persisted workbook bytes and raw source records are unchanged; no new saved field is required.
