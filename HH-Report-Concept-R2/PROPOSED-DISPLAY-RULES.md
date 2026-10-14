# HH revision 2 and shared display rules

**Illustration for review · 14 October 2026.** The working application remains v154. This document records the latest requested design for later implementation; it does not claim an app-wide rollout.

## Shared presentation

- Show zero numeric results as **–**, including a zero percentage without an extra percent sign. Preserve the underlying numeric zero, scale geometry, calculations, sorting and accessible numeric values. Do not replace digits inside dates, identifiers or narrative text.
- Show generated missing-value placeholders such as **غير مسجل / غير مسجلة** as an empty value. Preserve missing-state information and source records internally; a blank is not a zero.
- Use **TEC Teal #115E67** for plain **جاهز للعرض** labels and numbers, alongside green completed and red late labels/numbers. Keep white text on a teal badge or bar for contrast.
- Omit the source filename from report cards and exports. Keep raw provenance available internally. Other meaningful populated fields remain.
- Apply these presentation rules consistently across dashboard, search/results, report cards, tables, charts and exports when implementation is authorized.

## HH chart composition

- Leadership is **only** records explicitly marked **نعم**. TEC / general-secretariat is **every other record, including blank**, per the user's clarification.
- The illustrative source reconciles as **24 leadership + 38 TEC = 62**. The two blank requester records remain in TEC.
- Keep the existing sector breakdown in two equal panels, leadership physically on the right and TEC on the left. The unrestricted panels share a count scale from zero to 15.
- Show segment counts inside the bars with readable contrast. Short status names below each row disambiguate statuses that share the same approved fill. Full names and descriptions appear in the detailed legend.
- Keep the common sector rows aligned across populated panels. A zero row has no bar and shows a dash. A completely empty cohort panel hides; the populated cohort takes the available width.
- Show totals by status beneath each chart. Keep the shared detailed **تعريفات مستويات الإنجاز** legend beneath both charts, together on the PDF content page.

## Source and illustration limits

Source: the existing `ILLUSTRATIVE-monthly-preview.xlsx` fixture, reference date **30/09/2026**, workbook SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`. The displayed period remains report metadata rather than an implicit source-date filter.

Leadership: development **12**, completed **12**. TEC: review **3**, development **23**, completed **11**, other **1**. Overall completion remains **23/62 = 37.1%**; the leadership rate remains **12/24 = 50%**.

The fixture contains no HH records with **جاهز للعرض**. Its new plain-label/number treatment is therefore shown in a separate, explicitly labeled design example, excluded from report totals. HH has no approved workflow definition prose in the current source; the illustrated detailed legend is proposed wording based on its recorded statuses, without importing agenda council-approval definitions.

The PDF is a static design review, generated from the concept HTML. Native in-app PDF integration and a complete export of every project are outside this illustration.
