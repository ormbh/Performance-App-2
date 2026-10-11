# TEC Apple-Inspired Design standard

Consolidated typography, action controls, status badges, layout and report rules. This is a design specification; it does not change the app or source data. The monthly page is the first implementation and review target at 100% browser zoom.

The typography and status colors below preserve the latest approved choices. An asterisk (*) identifies a new default for a previously unspecified detail. These defaults are ready for review in the monthly page; they are not presented as earlier approvals or as official TEC brand rules.

All listed fonts use the actual supplied **Regular (400)** face. DIN Next Arabic and DIN Next LT Arabic are distinct supplied font families.

## Master component table

For text-only rows, “Inherited” means the text follows the surrounding surface; it does not create a separate box. Taupe text must remain on Paper for readable contrast. A dash means no separate border or fill.

| Element | Font / screen size | Text | Background | Border |
| --- | --- | --- | --- | --- |
| Page title | DIN Next Arabic Regular / 36px | Charcoal #333333 | Inherited | — |
| Portfolio heading | DIN Next Arabic Regular / 28px | Charcoal #333333 | Inherited | — |
| Card / table-section title | DIN Next Arabic Regular / 26px | Charcoal #333333 | Paper #FCFBFB | — |
| Main figures | DIN Next LT Arabic Regular / 34–40px | Charcoal #333333, with defined status exceptions | Paper #FCFBFB | — |
| Secondary figures* | DIN Next LT Arabic Regular / 28px | Charcoal #333333, with defined status exceptions | Paper #FCFBFB | — |
| Table column headings* | Dubai Regular / 18px | Ink #4F4E4E | Linen #EFEBE7 | Sand #E7E0D3 bottom divider |
| Table content, names and notes | Dubai Regular / 18px | Taupe #756B5F | Paper #FCFBFB | Linen #EFEBE7 row dividers |
| Important labels and explanations | Dubai Regular / 12px | Taupe #756B5F | Paper #FCFBFB | — |
| Change arrows and differences | Dubai Regular / 15px | Ink #4F4E4E, with meaning-based exceptions | Inherited | — |
| Minor metadata | Dubai Regular / 14px | Ink #4F4E4E | Inherited | — |
| Primary action button* | Dubai Regular / 16px | Paper #FCFBFB | Teal #115E67 | Teal #115E67 |
| Secondary action button* | Dubai Regular / 16px | Teal #115E67 | Paper #FCFBFB | Teal #115E67 |
| Text action / action link* | Dubai Regular / 16px | Teal #115E67 | Transparent | — |
| Destructive action button, when present* | Dubai Regular / 16px | Paper #FCFBFB | Burgundy #651D32 | Burgundy #651D32 |
| Icon button* | Existing icon family / 20px icon | Ink #4F4E4E | Paper #FCFBFB | Taupe #756B5F |
| Filter / input value* | Dubai Regular / 16px | Ink #4F4E4E | Paper #FCFBFB | Taupe #756B5F |
| Filter / input label | Dubai Regular / 12px | Taupe #756B5F | Paper #FCFBFB | — |
| Inactive navigation tab* | Dubai Regular / 16px | Ink #4F4E4E | Sand #E7E0D3 | Sand #E7E0D3 |
| Selected navigation tab* | Dubai Regular / 16px | Teal #115E67 | Paper #FCFBFB | 2px Teal #115E67 selected marker |
| Disabled action button* | Dubai Regular / 16px | Ink #4F4E4E | Linen #EFEBE7 | Silver #C8C7C7 |
| متأخر badge | Dubai Regular / 18px | Paper #FCFBFB | Red #C00000 | Red #C00000 |
| مجمّد / معلّق badge | Dubai Regular / 18px | Paper #FCFBFB | Burgundy #651D32 | Burgundy #651D32 |
| ملغى badge | Dubai Regular / 18px | Burgundy #651D32 | Sand #E7E0D3 | Burgundy #651D32 |
| منقول badge | Dubai Regular / 18px | Teal #115E67 | Paper #FCFBFB | Teal #115E67 |
| منجز badge | Dubai Regular / 18px | Paper #FCFBFB | Green #01831E | Green #01831E |
| قيد العمل / قيد التطوير / قيد الإجراء badge | Dubai Regular / 18px | Teal #115E67 | Mist #D9E1E2 | Teal #115E67 |
| قيد المراجعة badge | Dubai Regular / 18px | Teal #115E67 | Mist #D9E1E2 | Teal #115E67 |
| جاهز للعرض badge | Dubai Regular / 18px | Paper #FCFBFB | Teal #115E67 | Teal #115E67 |
| لم يبدأ badge | Dubai Regular / 18px | Paper #FCFBFB | Ink #4F4E4E | Ink #4F4E4E |
| مقاس badge | Dubai Regular / 18px | Teal #115E67 | Mist #D9E1E2 | Teal #115E67 |
| غير مقاس / لا ينطبق badge | Dubai Regular / 18px | Paper #FCFBFB | Ink #4F4E4E | Ink #4F4E4E |

Aliases listed together share a treatment. Each rendered item retains its own applicable source-backed label.

## Button, field and badge geometry

| Component | Size / padding | Corners / depth |
| --- | --- | --- |
| Action buttons* | Minimum 44px height; 16px horizontal padding; natural width; 8px icon/text gap | 8px radius; 1px border where listed; no shadow |
| Icon buttons* | Minimum 44 × 44px hit area; 20px icon | 8px radius; 1px border; no shadow |
| Inputs, filters and tabs* | Minimum 44px height; 12px horizontal padding; expand for the label/value | 8px radius; 1px control border where listed |
| Status badges | 6px vertical / 12px horizontal padding; natural width; 18px text at 1.6 line-height | 8px radius; 1px border; no shadow; no fixed height |
| Cards | 24px padding on desktop / 16px on mobile* | Preserve 18px corners; Paper surface; 1px Sand border; restrained existing depth |
| Table cells* | 16px vertical / 16px horizontal padding; content-driven row height | Fine Linen dividers; no heavy grid or nested boxes |

Status badges are informational. An actual drilldown action has a separately accessible hit area and interaction behavior; badge appearance alone does not imply a button.

## Interaction states

These are defaults (*) to apply and verify consistently:

| State | Treatment / behavior |
| --- | --- |
| Primary / destructive hover | Paper text on Charcoal #333333, with a matching Charcoal border |
| Primary / destructive pressed | Paper text on Ink #4F4E4E, with a matching Ink border |
| Secondary / icon hover | Mist #D9E1E2 surface; preserve a readable foreground and visible control border |
| Filter / input hover | Retain the Paper #FCFBFB surface; use a Teal #115E67 border; keep Taupe labels on Paper |
| Secondary pressed | Sand #E7E0D3 surface; Teal text and border |
| Icon pressed | Sand #E7E0D3 surface; Ink #4F4E4E icon and Taupe #756B5F border, including keyboard Space without hover |
| Keyboard focus | Visible 2px Teal #115E67 ring, separated from the control by a 2px gap; retain the normal component colors |
| Disabled | Ink on Linen with a Silver border; actually disabled; no hover or repeated action; do not dim text with blanket opacity |
| Loading | Preserve button width and label; add a clearly labeled progress indicator; prevent duplicate submissions |
| Field validation error | Burgundy #651D32 border and concise Burgundy text on Paper; retain the entered value |
| Menu / dropdown | Close on outside click or Escape; support keyboard navigation; return focus to the trigger after keyboard dismissal |
| Text action hover / focus | Underline; retain Teal text and visible keyboard focus |
| Selected tab / current page | Teal text and a 2px Teal marker on Paper; expose the correct selected/current state to assistive technology |
| Clickable table name | Retain Taupe, Dubai Regular 18px; use underline/focus to reveal the action without changing the agreed name color or weight |
| Informational badge | Preserve its status treatment; no action-style hover or loading state |

Taupe control borders are chosen as a readable boundary on Paper. Stone #ABA394 and Silver #C8C7C7 remain suitable for nonessential separators, chart marks and disabled boundaries rather than as the sole visible boundary of an active input.

## Complete formatting and content rules

1. **Fonts and hierarchy.** Use DIN Next Arabic Regular for headings, DIN Next LT Arabic Regular for main/secondary figures, and Dubai Regular for tables, labels, notes, metadata, controls and status badges. Use the supplied font files; do not simulate bold or substitute Apple system fonts. English table names also use Dubai Regular.
2. **Screen sizes.** Retain 36px page titles, 28px portfolio headings, 26px card titles, 34–40px main figures, 18px table content and badges, 12px important labels/explanations, 15px changes, and 14px metadata. New 28px secondary figures and 16px controls are defaults for the previously unspecified roles. Do not shrink the agreed table text to fit content.
3. **Text color roles.** Names and notes stay neutral Taupe and regular weight. Table headers use Ink on Linen. Taupe labels use Paper backgrounds. Main figures default to Charcoal; completed figures use Green #01831E and late figures use Red #C00000 where those status meanings apply. The Paper text inside filled badges is a separate treatment from figure color.
4. **Palette.** Use the exact existing TEC colors and the agreed green/red status exceptions. Paper #FCFBFB is the card/table surface; Linen #EFEBE7 is the page/table-header surface; Sand #E7E0D3 is a quiet grouping/border tone; Mist #D9E1E2 is an accent surface. Stone #ABA394, Silver #C8C7C7 and Grey #808080 serve appropriate chart/decorative roles, not small regular body-text roles. Grey may be used for large or decorative elements. No new colors or undocumented tints.
5. **Arabic and mixed text.** Use approximately 1.6 line-height for table text, natural Arabic wrapping, comfortable padding and top/middle alignment appropriate to the content. Preserve source names. Keep English identifiers, dates, values, fractions, percentages and currency units in their correct reading order. Align numeric columns consistently.
6. **Badge identity.** Use the final badge mapping in the master table, including frozen as a solid Burgundy badge and cancelled as Burgundy on Sand. Keep badges visually distinct from ordinary table text. Preserve the actual source-backed status label; styling aliases do not create combined labels or new business categories.
7. **Completion and lateness.** Late unfinished work is always red. Completed legislation is green for both completion within the deadline and completion after the deadline; completion after the deadline does not become unfinished-late work.
8. **Legislation composition.** Place late legislation beside the other statuses and include it in the bar. Split pending items into late and remaining pending so each item appears once. Keep the SLC definition once below the status area: **مقارنة: تاريخ الإنجاز الفعلي بالموعد المعتمد لدى SLC**.
9. **Follow-up tables.** Show only items requiring follow-up. For projects, include unfinished overdue projects with a valid deadline, frozen, cancelled and transferred items, with or without comments. Keep the group order **late → frozen → cancelled → transferred**, and stable source order within each group. Names remain neutral and regular. Preserve the agreed columns and omit the removed delay-reason column.
10. **Zero and missing values.** Show true zero counts and zero table values as **–**. Hide empty status and H/M/L groups. Keep meaningful chart-axis zero baselines and source-backed 0% completion captions where required. Missing or invalid values remain distinct from true zero; use **غير متاح** where a dash would be ambiguous. Do not turn missing financial/progress data into zero.
11. **Progression arrows.** Use source-backed comparisons only. Put 15px arrows/differences directly below their corresponding value, on aligned baselines, reserving a single 24px comparison line where needed*. ↑ means a numeric increase and ↓ a decrease. Green/red describes whether the change is favorable/adverse; use Ink for neutral changes such as a total or spend increase without an agreed performance meaning. A decline in late items is favorable; an increase is adverse. Hide unchanged or unavailable comparisons.
12. **Charts and legends.** Use flat bars, clear direct labels, visible values/units and comparable scales. Add a legend only when the series/category labels above or beside the bar do not already identify its colors. Distinguish category counts, average completion and budget shares; do not interchange these measures. Preserve financial source scope, valid denominators and category meaning.
13. **Layout and spacing.** Use a consistent 4 / 8 / 12 / 16 / 24 / 32 / 48px spacing scale*. Retain the widened fluid layout: 48px desktop gutters, 32px tablet gutters and 16px mobile gutters, subject to available screen width. Use 24px between main columns and 16px between stacked cards*. Keep cards as tall as their content requires; avoid large empty areas and decorative status sidebars.
14. **Monthly composition.** Preserve the approved two-column monthly composition: project portfolio physically left, executive-follow-up portfolio physically right, with strategy below legislation. Remove **سيطرة · لوحة المتابعة الشهرية** from displayed branding. Remove the extra **لم يبدأ 7 / منقول 2** line in the monthly projects card. Keep the official TEC logo and approved proportions/clear space.
15. **Projects composition.** Preserve the agreed physical pairings: quarters/months left and budget right; manager follow-up left and status summary right; budget by priority/type left and project count by priority/type right. Put the full-width follow-up table below these panels. Expand priority charts to their populated rows rather than putting them inside small scrolling panes.
16. **Terminology.** Use **الأجندة المعتمدة**, **المواضيع المستجدة**, and **الموازنة المعتمدة**. Do not add **(المعدلة)** to the displayed budget title. Keep the SLC explanation below and a concise legislation-review description above.
17. **Responsive behavior.** Reflow cards and controls on narrow screens while preserving readable type. Adapt tables to a readable mobile presentation; do not squeeze them into tiny text. Keep the overall page within the viewport; use deliberate table scrolling only when required for a wide data table. Priority charts expand with their visible categories.
18. **Controls and accessibility.** Use one clear primary action per task, predictable button/field states, visible selected tabs and focus, keyboard-accessible menus, explicit labels for icon buttons, text alongside status colors, and reduced-motion support. Keep drilldowns and full-report actions available without adding visual clutter or exposing internal implementation details in product flows.
19. **Print and exports.** Use the separate print scale below, repeat table headers, preserve Arabic direction and badge identity, and keep individual rows together where possible. Add pages to accommodate content instead of shrinking the entire report. Hide navigation, filters, menus and operational buttons. Preserve scope/date and the official logo. Keep template/report data rules unchanged.
20. **Verification and rollout.** Establish this standard on the monthly page first. Review its header, cards, controls, table and interactions at **100% browser zoom**, then inspect the actual PDF at readable size. Verify source totals, previous/current comparison keys, missing values, fonts, colors, wrapping, mobile behavior and exports before reusing the standard on projects, search, uploads and other pages. Visual polish must not change calculations or source meaning.

## Proposed print scale (*)

These are readable starting values for the monthly print layout. They require inspection of the actual rendered PDF before becoming the print implementation standard. Page count follows the content.

| Element | Font | Print size |
| --- | --- | --- |
| Page title | DIN Next Arabic Regular | 24pt |
| Portfolio headings | DIN Next Arabic Regular | 18pt |
| Card / table-section titles | DIN Next Arabic Regular | 16pt |
| Main figures | DIN Next LT Arabic Regular | 24–28pt |
| Secondary figures | DIN Next LT Arabic Regular | 20pt |
| Table headings/content and status badges | Dubai Regular | 13.5pt |
| Important labels and explanations | Dubai Regular | 9pt |
| Change arrows and differences | Dubai Regular | 11pt |
| Minor metadata | Dubai Regular | 10.5pt |

Use A4 landscape with 10mm margins as a starting print default*. Larger paper remains an export option for wider reports. Avoid forced two-page output or a fixed whole-page shrink factor. If an unusually tall row cannot fit a page, allow a readable continuation instead of clipping it.

## Related previews

- [Typography colors and exact TEC palette](../Color-Previews/README.md)
- [Actual bundled font samples](../Font-Previews/README.md)
- [Latest status badge preview](../Status-Previews/README.md)

This specification consolidates approved choices and names the remaining defaults. It is not a claim that the app already implements the standard, an official TEC brand manual, or an accessibility certification.
