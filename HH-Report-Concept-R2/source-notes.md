# HH concept r2 source review

This is a read-only source audit for illustration. No application files were edited. The source is the existing ILLUSTRATIVE workbook and its HH source-model; counts are demonstration data, not operational reporting.

- Latest user instruction: blank requester belongs to TEC. 62 total = 24 leadership (نعم) + 38 TEC/general-secretariat (all values other than نعم). This overrides the existing app exact-no cohort (36 لا plus 2 blank). Do not add a separate unclassified-note display.
- Leadership: review 0, development 12, done 12, other 0. TEC: review 3, development 23, done 11, other 1. The two blank-lead rows are included within TEC (review1, done1; both in التنمية المستدامة).
- Workbook WorkStatus order: متأخر → قيد المراجعة → قيد التطوير → منجز. HH model appends حالات أخرى for residual values, including the one blank status. Zero statuses/bars are omitted in the current chart.
- Ready (جاهز للعرض) exists only in AgendaStatus, not WorkStatus; it has no HH rows in this fixture. Illustrate its teal label/number as an app-wide treatment separately if needed.
- No HH workflow prose definitions found in the app or fixture. Agenda council-approval definitions are agenda-specific. JSON includes proposed HH legend wording explicitly grounded in recorded source status.
- Existing shared palette: review/development #D9E1E2 with #115E67 ink/border; done #01831E with warm-white ink; late #C00000 with warm-white ink; ready #115E67 with warm-white ink; other warm-white with #C8C7C7 border and #4F4E4E ink.
- Current HH report counts قيد العمل as review + development (+ other named active/late statuses if present): 38. Global specialProgress is total minus done and late: 39, including blank status. Keep the current report definition unless intentionally changed.

## Presentation-only scope

Exact numeric zero metrics already use hyphen through metricText/displayNumber; remaining exceptions are local percent formatters or calls to fmtNum/fmtN. Do not rewrite raw source values, status categories, filter values, dates, identifiers, axis baseline zero, chart geometry or machine-readable numeric accessibility attributes. Do not apply the zero rule to digits embedded in descriptive source text.

Blank only generated missing-value placeholders at rendering boundaries. Retain independent missing-state metadata and explanatory/grouping labels where necessary for understanding counts. tableCellText already blanks placeholders and dashes for follow-up tables, so use caution: routing a newly formatted zero dash through it would erase that zero representation. Remove Source.Name from displayed project card fields only.

The JSON provides exact per-sector distributions in the workbook LOV order, colors, record references and formatter audit locations. It is the authoritative evidence file for this concept revision.
