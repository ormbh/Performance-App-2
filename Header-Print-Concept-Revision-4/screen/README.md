# Revised screen header concept

This is an isolated review prototype. It does not change the v129 app.

| Part | Revision 3 | Revised concept |
|---|---|---|
| Title metadata | Date plus sector, unit and entity copy | Cutoff date only, 14px Dubai Ink |
| Header | Title and logo plus data-current label | 38px DIN title physically left; official logo physically right; no note or data-current label |
| Navigation | Filled tabs with icons in a separate row | 16px Dubai text links, active Teal underline, 44px targets; app grid at the right edge |
| Printing actions | Separate action row | Primary print and named settings at the opposite edge of the navigation row |
| Core filters | Nested panel around all fields | Three separate 72px fields in a quiet row, outside the header |
| Scope and extra filters | Scope adjacent to print controls and repeated below filters | Scope summary and projects extra-filter disclosure below the core filters |

- Approved fonts, font sizes, palette, logo proportions and field recipes remain unchanged.
- No filled navigation tabs or redundant navigation icons.
- Desktop gutters: 48px. Tablet gutters: 32px. Mobile gutters: 16px. Mobile text retains readable sizes and reflows.
- Additional project filters retain 16px gaps: three desktop columns, two columns at 600–1023px, and one mobile column. Navigation and actions reflow below 700px to prevent overlap.
- The screen footer shows copyright only. It follows the content and stays clear of the report.
- Menu closes on outside click and Escape. Escape restores focus to the trigger; menu arrow keys/Home/End navigate.
- Mobile filter sheet contains focus and keeps selections on dismissal.
- Search navigation preserves the already approved Google-style search layout.
- `concept.html?view=projects` and `concept.html?view=monthly` show the two report headers.
- Boards compare the previous Revision 3 proposal against this revised proposal at the same native CSS scale, not against a modified app.
- Blank cards show alignment only. Filter options and dates are illustrative; no business calculations are added.
