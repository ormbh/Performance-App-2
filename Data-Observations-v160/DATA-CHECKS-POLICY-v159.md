# Data observation policy — v159

Approved 14 October 2026. An observation should identify an actionable source inconsistency, an unresolved identity or a classification that affects reliable reporting. Valid source situations and calculation explanations do not automatically become correction tasks.

| Rule | Treatment |
| --- | --- |
| Sector or department outside the approved organisation registry | Warning, with original value and source row retained. |
| Department paired with the wrong approved sector | Warning showing the expected sector and recorded pair. The approved registry governs validation; the workbook is not corrected automatically. |
| Populated controlled value outside its applicable LOV | Warning. Includes status, entity, priority, type, month, year and completion percentages where defined by the schema. Numeric zero is a populated value. |
| Approved legacy organisation alias | Accepted using the existing bounded alias registry; no fuzzy spelling match or source rewrite. |
| Completion outside 0–100% | One specific range warning instead of a duplicate generic membership warning. |
| Active with 0% | Valid; no observation. |
| Repeated title alone | No observation. Confirmed duplicate matching keys remain flagged. |
| Blank leadership flag | Valid TEC membership; no observation. A nonblank value outside YesNo is still flagged. |
| Valid future completion date | No observation solely because its year differs from the reporting year. Invalid/missing dates retain relevant checks. |
| Blank decision follow-up requirement | Flag only if a recorded status, positive numeric progress, follow-up letter date or reply date provides follow-up evidence. Request review, not automatic inclusion. |
| Negative unallocated budget | Informational finance review: may be a settlement or an allocation overrun. Preserve its original value and inclusion in totals. |
| Partial historical status block | Keep the existing comparison eligibility/quality safeguards, without a source correction observation merely for an incomplete subset. Invalid historical totals and ambiguous snapshots remain actionable. |
| Missing/duplicate matching keys | Keep, preserving every source row and existing comparison quarantine. |
| Meeting year/date conflict | Keep for source review. Do not infer the correct year automatically. |
| Completed below 100% | Keep for source review. Status and percentage are not rewritten. |
| Result without a target / zero with unspecified measurement state | Keep the actionable missing-classification review and existing metric eligibility. |

Blank values are not invalid LOV values by themselves. Required/missing-field checks depend on source semantics. If no approved list can be loaded and no defaults exist, retain the loader's list-availability observation rather than inventing accepted values. Free-text titles, notes and IDs are not LOV fields.

The on-screen data-notes page and CSV export use the same revised issue list. Diagnostic evidence retains literal source values even where the app's numeric display uses a dash for zero.
