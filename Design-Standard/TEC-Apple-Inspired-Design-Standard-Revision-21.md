# TEC Apple-Inspired Design Principles

**Revision 21 · 13 October 2026 · Performance App v154**

The approved monthly dashboard establishes a reusable visual language for the TEC app. Apply its hierarchy, typography, surfaces, spacing, controls and alignment to equivalent roles across pages. Preserve the distinct purpose, content and calculations of each page.

This document consolidates approved rules through Performance App v154, including unified status appearances and agenda quarter-chart interactions and export totals. It records the approved implementation; the document itself does not change the app. The proposed additional-status disclosure and top follow-up shortcut are excluded. The separate entity-report redesign remains a concept.

## 1. The approach

1. **Lead with the information.** Make the page purpose, selected scope and primary values easy to find. Let secondary details remain secondary.
2. **Use consistent roles.** The same kind of title, label, value, table, action or status should receive the same visual treatment across the app.
3. **Keep the compact hierarchy.** Place metric names above figures and changes below. Use whitespace and shared alignment to connect related information.
4. **Remove repetition.** Omit explanatory subtitles beneath titles. Keep the report date, necessary units, field labels and actual record notes.
5. **Use restrained surfaces.** Prefer Paper cards on Linen, fine separators and modest corners. Avoid decorative layers and excessive nesting.
6. **Make color meaningful.** Keep brand roles and status mappings stable. A color must not imply a different metric, status or performance judgment.
7. **Keep behavior predictable.** Use the same navigation, filters, menu behavior and action hierarchy on equivalent pages.
8. **Design for the reading context.** Reflow the live app for a phone; compose PDF output using its own approved geometry and type scale.
9. **Preserve data truth.** Styling must not change scope, formulas, denominators, recorded notes, source identities or the meaning of missing values.
10. **Verify the result.** Inspect the real render and the requested interactions. Match claims to the checks actually performed.

The latest user instruction overrides this document. Page-specific rules below take precedence over general patterns. Historical proposals and screenshots do not override later approvals.

## 2. Screen typography

Sizes are CSS pixels at 100% browser zoom. Use the supplied font assets and regular weight unless Bold is explicitly specified. Treat font family names as roles mapped to the existing project assets.

| Role | Size | Font | Color / scope |
| --- | --- | --- | --- |
| Page title | 38px | DIN Next Arabic Regular | Charcoal |
| Search-home title | 36px | DIN Next Arabic Regular | Charcoal |
| Portfolio / major section heading | 30px | DIN Next Arabic Regular | Charcoal |
| Card / table-section title | 28px | DIN Next Arabic Regular | Charcoal |
| Main card total | 40px | DIN Next LT Arabic Regular | Charcoal unless a status meaning applies |
| Agenda status and strategy primary figures | 34px | DIN Next LT Arabic Regular | Approved figure/status color |
| Secondary figures, including special-project totals and statuses | 28px | DIN Next LT Arabic Regular | Approved figure/status color |
| Strategy registered denominator | 28px | DIN Next LT Arabic Regular | Charcoal |
| Subgroup names, e.g. للقيادة / للأمانة العامة | 18px | Dubai Regular | Charcoal |
| Agenda category names | 18px | Dubai Regular | Ink |
| Dashboard metric/status/total labels and strategy metric names | 16px | Dubai Regular | Ink; existing source-report legends retain their own roles |
| Table column headings | 18px | Dubai Bold | Ink |
| Table content, names and actual notes | 16px | Dubai Regular | Ink |
| Status badge text | 16px | Dubai Regular | Approved badge treatment |
| Actions, navigation and input values | 16px | Dubai Regular | According to component state |
| Completion caption and percentage | 14px | Dubai Regular | Ink; directly adjacent |
| Important supporting body explanations | 14px | Dubai Regular | Ink; no title subtitles |
| Change arrows and differences | 15px | Dubai Regular | Taupe, with meaning-based exceptions |
| Minor metadata | 14px | Dubai Regular | Taupe |
| Filter / input labels | 12px | Dubai Regular | Taupe |

Do not apply a blanket font size to all text or table descendants. Retain separately approved chart annotations and report-specific roles. Do not shrink table text to force a fit. The former oversized side-by-side metric-label concept is superseded by the compact hierarchy above.

## 3. Color roles

| Token | Hex | Role |
| --- | --- | --- |
| Charcoal | `#333333` | Headings and default figures |
| Ink | `#4F4E4E` | Table text, metric names, essential labels and explanations |
| Taupe | `#756B5F` | Minor metadata, neutral changes, field boundaries and allocation bar fills |
| Teal | `#115E67` | Primary actions, selected navigation, focus, spending and measurement bars |
| Burgundy | `#651D32` | Frozen/held statuses, cancelled accents, existing destructive/error treatments |
| Grey | `#808080` | Existing large or decorative elements |
| Stone | `#ABA394` | Existing non-status category and decorative roles; no longer the ready-status identity |
| Silver | `#C8C7C7` | Unclassified segments, dividers and disabled borders |
| Linen | `#EFEBE7` | Page canvas, table headers, quiet category boxes and bar tracks |
| Paper | `#FCFBFB` | Cards, table body, fields and text on filled controls/badges |
| Sand | `#E7E0D3` | Card borders and existing quiet/pressed surfaces |
| Mist | `#D9E1E2` | Existing accent and work/review/measured badge surfaces |
| Completed Green | `#01831E` | Completed values and favorable changes |
| Late Red | `#C00000` | Late values and adverse changes |

Use these pairings without new unapproved tints or blanket opacity. **One status uses the same fill, readable ink and border across badges, chart marks, legends, native PDFs and PowerPoint exports.** The badge appearance is the reference; the former separate chart-status palette is superseded. For example, **جاهز للعرض is Teal everywhere**, and work/review uses Mist with Teal ink and borders. Give Paper and pale chart marks a visible boundary so they do not disappear into the canvas. Keep status names and exact values available; color is never the only identifier.

| Status appearance: badge / chart mark / legend swatch | Ink on the fill | Fill / border |
| --- | --- | --- |
| منجز | Paper | Green / Green |
| متأخر | Paper | Red / Red |
| مجمّد / معلّق | Paper | Burgundy / Burgundy |
| ملغى | Burgundy | Sand / Burgundy |
| منقول | Teal | Paper / Teal |
| قيد العمل / قيد التطوير / قيد الإجراء / قيد المراجعة | Teal | Mist / Teal |
| جاهز للعرض | Paper | Teal / Teal |
| لم يبدأ | Paper | Ink / Ink |
| مقاس | Teal | Mist / Teal |
| غير مقاس / لا ينطبق | Paper | Ink / Ink |
| Unknown / missing | Ink | Paper / Silver |

Aliases share appearance only. Do not merge their source statuses or rename records. Resolve supported presentation aliases through the shared status helper, including frozen/held Arabic labels. A colored fill must not be reused as text if that makes a pale label unreadable. Plain status names and counts remain Ink except the explicitly approved completed Green and late Red emphasis. Financial allocations, spending, measurement coverage, source quantities and change arrows retain their independent meanings; a status-color update must not recolor them.

Use the same appearance mapping when generating native chart fills, marker borders, in-mark labels, legend swatches and export chart series. Verify both effective browser styles and generated export colors. Preserve chart data, status order and exact totals while changing presentation.

## 4. Layout, spacing and component geometry

Use the spacing scale **4 / 8 / 12 / 16 / 24 / 32 / 48px**. Preserve approved component-specific exceptions.

| Area / component | Standard |
| --- | --- |
| Page gutters | 48px desktop, 32px tablet, 16px phone; fluid width |
| Main columns | 24px gap |
| Stacked cards | 16px gap |
| Cards | Paper; 1px Sand border; 18px corners; 24px desktop / 16px phone padding |
| Table cells | 16px padding; content-driven height; approximately 1.6 Arabic line-height; fine Linen row dividers |
| Action buttons | Minimum 44px height; 16px horizontal padding; 8px icon/text gap; 8px corners; no shadow |
| Icon buttons | Minimum 44 × 44px target; 20px icon; 8px corners |
| Inputs | Minimum 44px height; 12px horizontal padding; 8px corners |
| Core report filters | Minimum 72px height; 8px vertical / 12px horizontal padding; 4px label/value gap; 1px Taupe boundary |
| Status badges | 6px vertical / 12px horizontal padding; 8px corners; natural height; 1px border; no shadow |
| Metric changes | One aligned 24px comparison row where needed; each change stays with its own figure |
| Completion caption | Label and percentage share a baseline, with an 8px gap |

Group with proximity and whitespace before adding another container. Keep cards as tall as their content requires. Align corresponding metric rows within a group; do not stretch unrelated cards to create artificial symmetry.

Status badges are informational unless an existing action explicitly makes them interactive. An interactive badge or drilldown still needs an accessible action target and clear behavior.

Use a 2px Teal focus ring with a 2px offset. Primary actions use Paper text on Charcoal for hover and Paper on Ink when pressed. Disabled actions use Ink text, a Linen fill and a Silver border without blanket opacity. Loading preserves the button's width and label, exposes its busy state and prevents duplicate activation.

## 5. Titles, navigation and filters

- Use the approved logo, title and required report date. Remove repeated explanatory labels beneath page, section, portfolio, card and table titles, including search and upload titles, and remove their reserved spacing.
- Keep the search title at 36px between the approved logo and search-field positions, with the approved upward placement. Reuse that search composition; do not shift the logo or field to compensate for title spacing.
- Search home places the application menu beside **بحث في التقرير**, with the menu, search action and **عرض جميع النتائج** centered together beneath the field, without separate monthly/project links. Other pages show **Search + the current destination**, with remaining destinations in the menu. Keep agenda, council and HH report destinations available from every page's menu.
- Mark the current destination with a 2px Teal underline, using a transparent background. Maintain at least 44px link targets.
- Separate navigation from task actions by position and spacing. Reflow the toolbar below 700px. Use a Teal primary action and a Paper/Teal secondary action where applicable.
- Place applicable core filters below navigation as separate fields, with the scope summary beneath. Keep their field labels. Avoid an extra enclosing filter panel.
- For the approved monthly scope pattern, a partial selection shows the first selected visible name and **+N** additional choices. One choice shows its name alone. Full selection or an unrestricted field shows **الكل**, without a count. Preserve selection order and directional isolation.
- Reuse that scope-summary pattern for equivalent multi-select components when authorized to standardize them. Preserve existing page-specific selection semantics and do not imply that every report has already been migrated.
- Keep full checked values accessible in the dropdown. A display count is not a record count. Preserve unions within a field, intersections across fields, dependent options and source-token distinctions. Never treat a stale selection as “all.”

### Search and results

- Use **ابحث عن بند أو مشروع أو مسؤول** as the shared search prompt. Keep number search available and included in the accessible name. Preserve the approved home logo, 36px title, field positions and upward title adjustment.
- Default results show **البند**, **الحالة / التقدم**, **التوقيت** and **الوحدة التنظيمية**. Preserve saved column choices; owner and narrative columns remain available through customization. Preserve full organizational context in record details and applicable PDF cells.
- Use a compact results toolbar with the result count, filtering and sorting. On phones, keep sorting visible and put column customization, CSV and PDF under the options control. Use one functional search-submit icon.
- Present every selected result field in readable stacked rows on phones. Preserve 16px Dubai Regular content, status meanings, timing labels, result ranges and pagination. Do not shrink text to fit desktop columns or silently omit a customized field.
- Distinguish matched text with Mist **#D9E1E2** behind Ink **#4F4E4E**, regular weight. Result titles have a detail arrow and a hover/focus underline; avoid a permanent underline across the whole title.
- Search dropdowns and applicable screen/PDF scope summaries use the first selected visible name **+N** rule, or **الكل** for all/unrestricted. Keep selection chronology and inherited dashboard drill scope intact.
- Keep keyboard access, 44px controls, Escape behavior and focus restoration. Export all matching rows independently of the visible screen page. Search PDF remains A4 portrait with its own print scale and full selected output fields.

## 6. Metric cards and alignment

- Keep the card title and total visually distinct. Preserve the approved physical positions and the total label beneath its number.
- Place short metric/status names above figures; place changes directly below those figures. Align the first label lines, numeric baselines and comparison rows across peers.
- Use shared row sizing when one Arabic label wraps. Avoid arbitrary offsets applied to individual labels. Maintain logical label/value relationships when columns reflow.
- Retain 18px subgroup names with 28px subgroup figures. Do not enlarge subgroup names to card-title size.
- Preserve the strategy's three metric roles: measured/registered, average measured results and average approved targets. Keep 16px names, 34px primary figures and the 28px registered denominator. Keep meaningful changes aligned on a shared row.
- An increase arrow means a numeric increase; its color conveys an agreed performance meaning. Neutral totals and spending changes stay Taupe. Completed increases are Green; increases in late items are Red. Hide unchanged/unavailable comparisons according to the existing eligibility rules.
- Use the exact SLC captions **منجز ضمن موعد SLC** and **منجز بعد موعد SLC**, rendered through the existing component with isolated Latin and Arabic runs. Preserve the approved visual order: SLC at the physical left, the Arabic phrase to its right. Keep the caption, figure and change aligned. Positive changes for completed-after-SLC items are Green, including both arrow and number.

## 7. Bars and completion captions

| Bar | Meaning | Treatment |
| --- | --- | --- |
| Completion | Completed / full eligible total | Green on Linen; remainder means not completed |
| Status distribution | Disjoint statuses sharing one total | Shared status fill / ink / border mapping from section 3, matching badges and exports |
| Allocation | Source-defined allocation ratio | Solid Taupe; retain approved budget denominator |
| Spending | Source-defined invoice-spending ratio | Solid Teal; retain approved budget denominator |
| Strategy measurement | Measured / registered indicators | Solid Teal on Linen; not a completion or finance measure |

Preserve scales and zero baselines. Use a shared scale where rows are intended to be compared; project count/money bars retain their existing zero-to-largest-row scale. Do not stack overlapping statuses or calculate a percentage from only the visible headline categories.

For the approved monthly completion captions, show only **نسبة المنجز** directly beside the percentage beneath the bar, right aligned. Use at most one decimal place, for example **نسبة المنجز 11.9%**. Isolate the numeric percentage as LTR. Screen uses 14px Dubai Regular Ink; PDF uses 9pt with a 2mm gap.

| Monthly card | Completion numerator | Denominator / placement |
| --- | --- | --- |
| Annual agenda | Completed agenda items | All agenda items in scope; beneath status bar |
| Council decisions | Completed decisions | All decisions in follow-up scope, including missing statuses; beneath status bar |
| Legislation | Completed within SLC deadline + completed after SLC deadline | All legislation in scope; beneath valid disjoint status bar |
| Special projects | Completed in each requester subgroup | Full subgroup total; beneath each subgroup bar |
| Budgeted projects | Completed budgeted projects | All budgeted projects in scope; new Green/Linen bar after statuses and before quarters |

The budgeted-project denominator includes statuses absent from headline figures. Its Linen remainder means all not completed. Keep the existing headline composition without adding the rejected extra-status disclosure.

A valid zero numerator over a positive denominator shows **0%**. Preserve existing count/table conventions that display a true zero as **–**; this presentation does not make a zero equivalent to missing data. Missing, nonfinite, negative or impossible values and zero denominators produce no completion bar/caption. Suppress a distribution caption if its bar is invalid; suppress legislation distribution and caption if cohorts overlap. Do not apply these completion captions to financial or strategy measurement bars.

Financial bars stay solid even when some source values are unavailable. Remove hatching, completeness markers and repeated availability notes such as **قيم متاحة: 59 من 61**. Do not replace them with a new marker, note or tooltip. Missing values must still retain their source semantics and calculation eligibility.

### Agenda quarter charts and totals

- Use vertical stacked quarter columns with exact topic counts. Approved agenda stays physically right and emerging topics left. Use a shared zero-based whole-count axis across visible categories, with one count above each quarter and no percentage or quarter/total ratio captions.
- Hide empty categories. Preserve the union and source order of active quarters, the explicit undated group and any additional eligible category. A category’s missing intersection with another active quarter is a true zero and displays a dash.
- Under each chart, show **الإجمالي حسب الحالة** and that category’s totals by status across all its quarters within the active filters. These status totals must sum to the category total. Do not use the first quarter as the default summary.
- No quarter is selected on initial render or after a filter change. Hover and keyboard focus do not replace the totals. Clicking a quarter, or activating it with Enter/Space, shows only its status values with its quarter name; omit ratios and percentages. Clicking that quarter again or pressing Escape restores totals; clicking outside a quarter restores totals.
- Remove persistent and hover outlines around bars. Keep a visible keyboard-only focus cue. Arrow keys move focus without changing the status summary. Retain accessible names and the expandable underlying count table.
- Keep the original **تعريفات مستويات الإنجاز** below the charts, with swatches matching the shared status appearance. Only completed and late standalone status counts/text use Green and Red; neutral labels stay readable.
- Native PDF always includes aggregate totals by status below each chart, even when a quarter is currently active on screen. Keep charts, status totals and full definitions together on the first content page after the cover. Recover whitespace before reducing chart space; do not shrink the page or clip labels/definitions to force a fit.
- Keep chart labels at 9pt and quarter counts at 16pt in A4 landscape PDF. Status-summary labels use 10.5pt and values 12pt. Verify short, dense, filtered, single-category and undated layouts with the actual downloaded PDF.

## 8. Approved monthly composition details

These are monthly-report rules, not required content for every dashboard.

- **Agenda categories:** two separate equal Linen boxes, **الأجندة المعتمدة** right and **المواضيع المستجدة** left. Use a 12px screen gap, 9px radius and 8px vertical / 14px horizontal padding. Preserve 18px names, 28px figures and their individual changes. PDF uses equal boxes with a 3mm gap and existing print typography.
- **Budget order:** approved budget first; invoice spending, its change and Teal bar next; allocated/unallocated amounts and Taupe bar below. Omit the visible **الإنفاق … من الموازنة المعتمدة** caption, retaining the calculation and accessible bar meaning.
- **Quarter annotation:** show only **مشاريع 2027: N** when the filtered valid-2027 count is positive. Otherwise omit the line and spacing. Keep the separate quarter reference year. The rule is specifically 2027; do not silently roll it forward.
- **Strategy cleanup:** remove **مؤشرات الأداء** and the three repeated coverage/result-count/target-count notes. Keep primary values, the denominator, measurement bar and valid metric changes. A valid nonzero total-count change remains neutral and unlabeled in the card header.
- **Legislation cleanup:** omit the repeated explanation comparing actual completion with the SLC deadline. Preserve the source timing definitions and the approved SLC caption rendering.
- **PDF-only exclusions:** omit the missing-requester note, such as **جهة الطلب غير مسجلة: 2 · مشمولة في الإجمالي**, and the specified prior-project-status completeness explanation. Keep their screen diagnostics, source totals, comparison eligibility and unrelated output warnings intact.

Remove unused spacing with removed content. These exceptions do not authorize removing actual table notes, units, essential source caveats or metric definitions elsewhere.

## 9. Phone, RTL and accessibility

- Reflow the live interface; preserve the approved text sizes. Let controls and labels wrap before squeezing them. Keep the whole page within the viewport, with deliberate local scrolling only where a data table requires it.
- Retain two equal agenda category boxes on phone widths. Allow names to wrap and reserve equal label height so figures and changes align.
- Below 600px, legislation metrics use two columns; a single visible metric uses the full width. Other cards follow their own approved responsive structure.
- Use RTL structure with isolated LTR dates, ratios, percentages, signed changes and identifiers. Preserve real reading order and intended physical positions rather than mechanically mirroring everything.
- Maintain visible focus, keyboard access, concise accessible names, selected states, dialog Escape behavior and focus restoration. Do not make hover the only route to necessary information.
- Keep accessible bar meanings and underlying values even where a specific repeated visible note was removed. Do not recreate the removed financial-availability annotation through an added tooltip.
- Check text contrast using the approved palette, include text with status colors and respect reduced motion. Document actual checks; do not claim certification from appearance.

## 10. PDF and paper profiles

The primary report action is **تنزيل PDF**, with **إعدادات PDF** where applicable. Use the bundled offline export engine, embedded fonts, Arabic text and vector graphics. Internet access and the browser print dialog are not prerequisites for download.

| Document | Output profile |
| --- | --- |
| Monthly report, default digital output | One continuous custom page: 297mm wide, measured content height |
| Monthly selected paper mode / height-limit fallback | A4 portrait |
| Agenda, council and HH reports | A4 landscape, 297 × 210mm |
| Projects, entity, comparison, search results and other paper exports | A4 portrait, 210 × 297mm |

No A3. Preserve report-specific templates; these PDF rules do not redefine workbook sheet layouts or PowerPoint slides.

- **Monthly first header:** logo and report title including **- لتاريخ DD/MM/YYYY**, followed by the restored sector/unit scope. Use the report date and actual selected scope. Entity selection still filters the data but its field is omitted from the exported header.
- **Agenda cover:** full-bleed A4 landscape image with title, selected entity (when selected) and month-to-month year centered horizontally and vertically. No footer or page number on the cover. Start copyright and content-page numbering on physical page 2, excluding the cover from the total. Keep the entity column, category titles and topic counts in the detail tables; omit empty category sections and the source-notes appendix.
- **Continuation:** no repeated report masthead. Repeat table column headings in multipage tables where needed.
- **Footer:** copyright and page numbers only.
- **Continuous monthly:** full-page Linen, including margins, with Paper cards. Use 8mm top/side insets and 16mm bottom reserve; 281mm content width; 8mm column gap; 6mm card padding and stacked-card gap; 3.5mm table-cell padding. Projects stay physically left, executive portfolios right, with full-width follow-ups below. A single portfolio fills the content width. Measure height after fonts/images are ready and include footer clearance. Do not derive height from the viewport.
- **A4:** 10mm margins. Monthly A4 preserves its two portfolio columns with a 4mm gap; other portrait reports retain their own flow. Keep fitting cards/rows together; allow readable continuation when content exceeds a page. Never force a fixed page count by clipping or shrinking the report.
- **Height limit:** a monthly page above 5080mm falls back to A4 portrait with an explanation; preserve all content and the selected scope. Do not overwrite the saved continuous-format preference.

| PDF role | Font | Size |
| --- | --- | --- |
| First report title including date | DIN Next Arabic Regular | 24pt |
| First-page sector/unit scope | Dubai Regular | 10.5pt |
| Portfolio headings | DIN Next Arabic Regular | 18pt |
| Card/table-section titles | DIN Next Arabic Regular | 16pt |
| Main figures | DIN Next LT Arabic Regular | 24–28pt, according to existing role |
| Secondary figures | DIN Next LT Arabic Regular | 20pt |
| Table headings | Dubai Bold | 13.5pt |
| Table content, notes and in-table badges | Dubai Regular | 12pt |
| Badges outside tables | Dubai Regular | 13.5pt |
| Metric labels, completion captions and retained explanations | Dubai Regular | 9pt |
| Changes | Dubai Regular | 11pt |
| Permitted metadata and copyright/page numbers | Dubai Regular | 10.5pt |

Screen-size changes do not automatically resize PDF text. Validate both profiles using the actual downloaded files.

Monthly filenames use **TEC_Monthly_Mmm_yy[_EnglishScope].pdf**, with the report date. Prefer a partial unit scope, otherwise a partial sector; use the first selected name without **+N**. Omit full/unrestricted scopes. Use the supplied official English mapping, remove terminal **Department** or **Section**, retain **Office** and **Sector**, convert **&** to **and**, and use ASCII underscores without hidden direction controls. Other report filename rules remain independent.

## 11. Applying and maintaining the standard

Map each existing page element to a shared role before editing. Reuse components and tokens; avoid a new set of local overrides for every page. Keep dashboard labels, source-report legends, table text and PDF text separately scoped.

For a new direction, illustrate first. For approved implementation, continue without repeating approval requests. A review finding does not authorize an additional control or a metric change. Keep the rejected extra-status disclosure and top follow-up shortcut out of the standard.

Verify relevant desktop, tablet, phone and export states; long Arabic/mixed-script labels; selected scope; zeros/missing values; actual source totals and denominators; and interactions changed by the work. Record passes and remaining limitations accurately. A documents-only update does not establish that every app page has already been migrated or newly tested.

**Source basis:** the latest user instructions of 13 October 2026 for v154 and earlier approved decisions. The new status palette and agenda behavior supersede conflicting earlier chart/selection rules. Historical reference: the [Revision 19 design standard](https://raw.githubusercontent.com/ormbh/Performance-App-2/286a705e3fb5ab61c748e472833817f7b73908a4/Design-Standard/TEC-Apple-Inspired-Design-Standard-Revision-19.md), interpreted with later instructions taking precedence. The official filename registry remains in the [v144 app package](https://raw.githubusercontent.com/ormbh/Performance-App-2/286a705e3fb5ab61c748e472833817f7b73908a4/Performance-App-v144.zip). These links provide provenance; the bundled skill and principles are readable offline.
