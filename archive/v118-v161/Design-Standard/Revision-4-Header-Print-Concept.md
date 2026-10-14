# TEC Apple-Inspired Design — revised header and print concept

**Revision 4 concept, 11 October 2026.** This revision follows the latest header,
navigation and printing corrections. It supersedes the corresponding Revision 3
proposals; approved fonts, exact colors, status treatments, figures, source notes
and filtering meanings remain unchanged. The app release is unchanged.

## Updated setup

| Component | Previous proposal | Revised concept |
| --- | --- | --- |
| Screen title block | Title, cutoff and full scope text | Title and cutoff date only. No explanatory note, scope line or current-data marker in this block. |
| Navigation | Filled tabs with icons; separate application menu and actions rows | Quiet text links in one compact row, a Teal underline for the current page, one application menu and print controls at the opposite end. |
| Filters | Core fields inside another bordered panel | Keep the visible core fields as a simple row below navigation. Scope belongs here; extras retain their project-specific disclosure. |
| First printed header | Preview label above title; date/scope below | Title and date in one title: «التقرير الشهري للأداء والتنفيذ - لتاريخ 30/09/2026». No notes above or below; keep the official logo. |
| Later printed pages | Compact repeated report title, logo, date and scope | No continuation report header. Begin with the relevant section or repeated table column headings. |
| Print footer | Report context, calculation date, page count and legal line | Copyright/legal line and page numbers only. No report title, date, scope, filename or extra note. |
| Screen footer | File, calculation date and legal metadata | Copyright/legal line only in this concept. Page numbering belongs to print. |

## Retained sizing and colors

| Element | Font | Size | Treatment |
| --- | --- | --- | --- |
| Screen page title | DIN Next Arabic Regular | 38px | Charcoal #333333 |
| Screen cutoff date | Dubai Regular | 14px | Ink #4F4E4E |
| Primary navigation | Dubai Regular | 16px | Ink; current page Teal #115E67 with 2px underline |
| Report logo | Official supplied TEC asset | 192px desktop; 144px mobile | Preserve proportions |
| Print action | Dubai Regular | 16px; minimum 44px target | Paper #FCFBFB on Teal |
| Optional print settings | Dubai Regular | 16px; minimum 44px target | Teal on Paper |
| Application menu icon | Existing outline SVG | 20px in 44px control | Existing palette and accessible name |
| Filter field | Dubai Regular | Label 12px / value 16px; minimum 72px | Paper, Taupe #756B5F boundary; Teal boundary on hover |
| First printed title | DIN Next Arabic Regular | 24pt | Charcoal |
| Date inside printed title | DIN Next Arabic Regular | 24pt | Charcoal; date isolated in left-to-right order |
| Printed section title | DIN Next Arabic Regular | 16pt | Charcoal; this is content, not a continuation report header |
| Printed table heading | Dubai Bold | 13.5pt | Ink on Linen #EFEBE7 |
| Printed names, notes and badges | Dubai Regular | 13.5pt | Approved neutral names and status treatments |
| Printed copyright and page count | Dubai Regular | 10.5pt | Ink |

Screen gutters retain 48px desktop, 32px tablet and 16px mobile. Tables retain
natural wrapping and approximately 1.6 line spacing. Print retains A4 landscape,
10mm outer margins and content-driven pagination.

Navigation and actions reflow onto separate rows below 700px. The five additional
project fields use three desktop columns, two columns at 600–1023px, one mobile
column and 16px gaps. Core filter fields retain their approved responsive layout.
Menus and filter popups stay within the available viewport.

## Rules for this concept

1. Keep only the date beneath the screen title. Remove explanatory header notes
   and the current-data indicator from this visible header.
2. Give navigation a clear current-page marker without surrounding every link
   with a filled box or repeating unnecessary icons.
3. Keep primary destinations visible; the application menu retains the other
   existing destinations and eligible actions.
4. Place task actions together, with one primary print action and optional
   settings. Maintain 44px targets and visible keyboard focus. Menus close on
   outside click or Escape; keyboard dismissal returns focus to the trigger.
   Menu arrow keys, Home and End navigate items. Mobile sheets contain focus,
   preserve selections when dismissed and restore focus to their live trigger.
5. Keep filter scope with the filters. Removing scope from the title never
   clears selections or changes report membership.
6. Keep the first printed header to the official logo and one report title with
   its cutoff: «التقرير الشهري للأداء والتنفيذ - لتاريخ 30/09/2026». The latest
   clarification removes all notes above and below. Do not print a separate
   date line or sector/unit/entity scope line in this header; filters still apply.
7. Remove the report masthead from every later printed page. Keep repeated table
   column headings and relevant section titles readable.
8. Keep only the exact copyright/legal line and generated page numbering in the
   print footer. Reserve sufficient footer space; never overlap table rows.
9. Keep source notes, SLC definitions and interpretive caveats in the report body.
   Footer simplification does not authorize dropping source information.
10. Hide the entity filter field and selected value in print while preserving
    its effect on the exported dataset. Entity names in actual table content stay.
11. Keep native approved print sizes. Add pages when content requires them rather
    than applying a whole-page shrink factor.
12. Review the concept at native size before applying it to the working app.

## Comparison scope

The “before” panels show the previous Revision 3 concept. The “after” panels show
this Revision 4 concept using the same supplied assets and frozen illustrative
records. The three-page PDF demonstrates selected overview components and eight
table records; it is not the complete operational export or a target page count.
