# Data observation policy — v160

Approved 14 October 2026. Retains the rules in [v159](DATA-CHECKS-POLICY-v159.md) and adds the following warnings to the data-notes page and CSV export.

| Check | Scope and treatment |
| --- | --- |
| Project end date before start date | Secretariat projects use valid numeric Excel dates. Special projects use recorded start/end month and year. Warn only when the end date is definitely earlier. Same-day/same-month periods are allowed. Month-only formats retain their precision; missing or ambiguous dates are not guessed. |
| Numbers stored as text | Applies to schema numeric amounts, percentages, progress and year fields. Recognises zero, negative values, grouped decimals, scientific notation, percentages, Arabic/Persian digits and accounting parentheses. Warn with the original field, source row and literal value. Formatting alone does not convert a text cell into a numeric value. |

A numeric identifier in an ID field, a number in narrative text or a nonnumeric placeholder is not mislabeled as a numeric-text observation. Valid numeric cells and genuine numeric zero are not flagged as text. Recognised percentage text is compared with the approved percentage list without rewriting it, so a valid listed value receives its storage-type warning rather than an incorrect out-of-list warning.

The application never reverses dates, converts cells or changes record values automatically. All calculation definitions, reporting scope and comparison safeguards remain unchanged.
