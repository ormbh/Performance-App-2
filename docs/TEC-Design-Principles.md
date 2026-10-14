# TEC Apple-Inspired Design Principles

**Revision 28 · 14 October 2026 · Performance App v163**

The approved monthly dashboard establishes a reusable visual language for the TEC app. Apply its hierarchy, typography, surfaces, spacing, controls and alignment to equivalent roles across pages. Preserve the distinct purpose, content and calculations of each page.

This document consolidates approved rules for Performance App v163. Agenda and special-project reports use one page composition, contents/navigation, table-column sequence, record numbering, cover-title pattern, final notes/recommendations and compact legend treatment. **المستجدات التفصيلية** exists only in special projects. Preserve each report’s source fields, eligibility, chart orientation, status definitions and calculations. Council extends the same visual roles through its explicit six-column and issuing-body contract below. These are requirements; Verification-v163.md establishes what was actually tested. The rejected additional-status disclosure and top follow-up shortcut remain excluded; the separate entity-report redesign remains a concept.

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

The latest user instruction overrides this document. Revision 28 extends the shared report treatment to council decisions, with dynamic issuing-body charts and the approved six-column table, and omits each blank decision-reference field. Revision 27 removes the separate HH overview, repeated detail-card group/number strip and duplicate yes/no leadership field, and aligns the leadership badge across screen and export. Revision 26 supersedes the former prohibition on agenda contents, the differing screen/PDF section sequence, the first-after-cover chart page, separate notes layouts and legend sizes, and table column order. Revision 25’s removal of added agenda count-matrix pages and the HH main-list PM column remains applicable. Monthly legislation aggregation, numeric progress without circular indicators, zero-as-dash, missing-as-blank, shared status colors, HH visibility and endpoint totals remain unchanged.

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

Aliases share appearance only. Do not merge their source statuses or rename records. Resolve supported presentation aliases through the shared status helper, including frozen/held Arabic labels. A colored fill must not be reused as text if that makes a pale label unreadable. Plain status names and counts use Ink except **منجز** in Completed Green, **متأخر** in Late Red and **جاهز للعرض** in Teal. These plain-text roles apply across dashboard metrics, report cards, tables, legends and chart summaries. Text inside a filled badge or chart segment follows that fill’s readable-ink role: Paper on Teal, Green and Red; Teal on Mist. Do not put Teal text directly on a Teal segment. Financial allocations, spending, measurement coverage, source quantities and change arrows retain their independent meanings; a status-color update must not recolor them.

Use the same appearance mapping when generating native chart fills, marker borders, in-mark labels, legend swatches and export chart series. Verify both effective browser styles and generated export colors. Preserve chart data, status order and exact totals while changing presentation.

### Numeric zero, missing values and provenance

- Across dashboard, search/results, cards, tables, charts and exports, render a true numeric zero as **–**. A zero percentage displays **–**, without a percent sign. A chart’s visible zero tick also uses **–**; its numeric baseline remains zero. Retain existing suppression of unchanged comparison arrows and empty status groups.
- Apply the formatter at the presentation boundary. Preserve raw numeric values, denominators, sorting, filtering, scale geometry, formula inputs, accessible numeric values and machine-readable source exports. Do not replace zeros embedded in dates, identifiers, version numbers or narrative source text, or corrupt numeric input values.
- Render generated missing-value placeholders such as **غير مسجل / غير مسجلة** as an empty value, preserving the field’s label and source association where the field remains. Retain the distinction between missing and a real zero internally. Do not erase substantive source notes or invent a value from a blank.
- Omit the source filename field, including **Source.Name / ملف المصدر**, from user-facing report cards and their rendered exports. Keep provenance in the raw record and audit machinery. This does not remove the upload control’s chosen-file confirmation or rewrite source identities.
- Recorded status and recorded progress are separate source fields. Do not infer **منجز** from 100% progress, force completed records to 100%, or derive an unrecorded status from the absence of a value.

### Recorded progress without circular indicators

- Remove Harvey balls, pie-like progress markers and circular progress indicators across app pages, search/results, cards, details, report tables and printed/PDF output. Remove the indicator's unused spacing as well.
- Keep the recorded progress as a readable numeric percentage in its existing field and preserve the field label. Use **–** for a true numeric zero and an empty value for missing progress; do not turn missing progress into zero or infer a percentage from status.
- Preserve the original source progress, precision, sorting, filters, calculations and machine-readable values. The removal changes presentation only.
- Retain approved linear completion bars, stacked status distributions and their captions. Do not replace the removed circles with a new symbol, graphic or duplicate progress value.

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

### Shared agenda and special-project report presentation

Apply consistency to the entire report page and its output, including the following equivalent roles. Use shared components and scoped semantic styles instead of independent visual variants for agenda and HH. A common style does not require identical content, identical columns or a new chart type.

| Equivalent role | Common presentation and behavior |
| --- | --- |
| Report heading and navigation | One hierarchy, logo, action sizes and PDF action. Default titles are **مستجدات الأجندة السنوية {year}** and **مستجدات المشاريع الخاصة {year}**, with the same January-to-cutoff-month period format from the report date. Preserve deliberate custom titles/periods. Selected entity appears beneath the title; covers center title/entity/period together. |
| Scope and report controls | Matching direct filter fields, label/value type, surfaces, borders, spacing, scope summary and control alignment. Use a common utility/disclosure pattern for report editing. Keep each report's eligible options, requester/leadership semantics, editor fields and save behavior. |
| Report contents and section navigation | One compact contents component on each screen, using 16px links with 44px targets and visibly labeled record counts. Links follow rendered section order and include populated final notes/recommendations. PDF has a contents page after its cover, using actual displayed page numbers and working internal destinations. Do not print screen-only return controls. |
| Cards and chart panels | Paper surfaces, Sand outlines, 18px corners, 24px padding (16px on phones), corresponding title/total alignment and content-driven height. Hide empty data groups; a remaining group uses the available width. Remove redundant outer framing around agenda's screen chart panels, preserving its title and grand total. |
| Charts | Matching status palette, figure fonts, axis/annotation hierarchy and aggregate status-summary roles: 16px labels beside 28px figures, with common spacing and baselines. PDF uses 16pt chart/panel headings, 20pt category totals, 10.5pt aggregate labels and 12pt aggregate figures; use 12pt in-bar figures only where they fit legibly. Keep vertical quarter columns for agenda and horizontal sector bars for HH; retain each chart's source scope and scale. |
| Detailed legends | Below the charts, use a 20px heading, 16px labels, 14px definition text, 10px bordered swatches, 16px padding/gaps and modest label/body separation. PDF uses a 12pt heading, readable 10.5pt labels/definitions, 2mm swatches and compact padding/gaps. Retain every definition and give recovered space to the charts. Keep chart/legend together. |
| Section and table headings | Use 30px major headings, 28px table-section titles and 14px counts, with 32px major separation and 16px heading/content spacing. Keep headings with their following content and preserve the category/quarter labels and counts that identify agenda records. |
| Record tables | The same header surface, text roles, row separators, cell padding, status badges, numeric alignment and link/focus treatment. Long topic/project and entity text receives sufficient width and wraps naturally. |
| Record detail content | Only special projects has **المستجدات التفصيلية**. Preserve meaningful populated source details and the project manager there. Match card identities and ordering to the main table. Keep record numbers in the table and internal link mapping; omit the repeated section-title/number strip from individual detail cards. Use the same 28px titles, 12px field labels, 16px content, status palette and numeric-progress roles; omit source filenames and circular indicators. |
| Responsive behavior | Reflow equivalent controls and summary panels together. Use one common title/total role at narrow widths; avoid separate per-report size variants. Mobile records use a Paper card with 18px corners and 16px padding: title first, sequence and field-label metadata at 12px, and all actual field values at readable 16px. Omit zebra bands and nested field boxes. |
| Print/PDF | Shared A4 landscape geometry, typography, table-header treatment, footer roles and continuation rules. Covers are print-only in the workspace and full bleed in output, with the title, applicable selected entity and period centered together. Preserve report-specific titles, section order and content; remove unused space when content is removed. |

### Shared notes, empty states and links

- Put report-level **ملاحظات** and **توصيات** at the end in both reports. Use stacked Paper cards, right-aligned Charcoal headings and 16px Ink body text. On screen and in PDF, add one contents destination when either is populated; remove the destination and cards when both are empty. Native PowerPoint uses separate page entries for populated notes and recommendations in both reports. Preserve record-specific narrative in its special-project detail card.
- A zero-result scope shows one report-level empty state. Hide contents, summary cards, invalid completion strips, charts, legends and empty record sections. Preserve the active filters and reset action.
- Use **الإجمالي حسب الحالة** visibly beneath both chart types. The shared standalone status colors remain in force. Use **مشاريع القيادة** consistently in charts, filters and detail badges.
- PDF contents uses actual page references determined from final pagination. Screen counts remain explicitly labeled as record counts. Contents and project-detail links must resolve to real destinations; never imply a printed record count is a page number.
- Preserve custom cover text and full selected entity scope. Default year and period follow the report date, never the download date. Cover text is centered horizontally and vertically as one group.

Agenda and special projects use the same summary lead: report-category title physically right and scoped overall total physically left, with الإجمالي beneath the number. The special-project summary is the title/total followed by its two nonempty cohort charts and detailed legend, on screen and in PDF. Remove the separate four-metric overview and its completion strips from these report pages. This does not change the monthly dashboard or source calculations.

Use the screen and PDF scales defined in this document independently. Match equivalent labels, figures and baselines rather than copying a page's pixel coordinates onto a differently shaped chart. Keep visible keyboard focus and semantic headings, table headers and field associations.

For both reports, use a Linen table header with Ink headings and a Paper body with fine Linen row separators. Avoid a second report-specific stripe or border style. Keep numeric values directionally isolated and dates readable. Do not reduce font size or truncate source text to fit columns. Keep **موعد الإنجاز** on one line while allocating enough width to the topic and entity fields; preserve the approved agenda column meanings.

Common RTL table sequence is **م، الموضوع/المشروع، الجهة المعنية، الحالة، نسبة الإنجاز where recorded, موعد الإنجاز**. Agenda has five columns without an invented completion-percentage field; HH has six. Preserve quarter/date meanings and actual source progress. Keep the HH main-list PM column omitted, while retaining its populated detail field. Use the same header styles, content alignment, readable wrapping and sufficient deadline width.

Report order is **contents → charts and compact legend → record tables → applicable detailed updates → notes and recommendations**; the PDF cover comes first. Detailed updates appear only in special projects. The agenda record order is approved quarter groups, emerging topics, then other/unclassified topics if present, matching its chart/navigation category order. HH main rows follow ongoing then completed groups, preserving source status/end-date order within each group; detail cards use that same order. Number table records continuously within each filtered report and preserve that identity in internal HH card links; do not repeat visible record numbers in each detail-card header. Do not add exact-count print matrices, source-note appendices or invented record fields.

## 6. Metric cards and alignment

- Keep the card title and total visually distinct. Preserve the approved physical positions and the total label beneath its number.
- Place short metric/status names above figures; place changes directly below those figures. Align the first label lines, numeric baselines and comparison rows across peers.
- Use shared row sizing when one Arabic label wraps. Avoid arbitrary offsets applied to individual labels. Maintain logical label/value relationships when columns reflow.
- Retain 18px subgroup names with 28px subgroup figures. Do not enlarge subgroup names to card-title size.
- Preserve the strategy's three metric roles: measured/registered, average measured results and average approved targets. Keep 16px names, 34px primary figures and the 28px registered denominator. Keep meaningful changes aligned on a shared row.
- An increase arrow means a numeric increase; its color conveys an agreed performance meaning. Neutral totals and spending changes stay Taupe. Completed increases are Green; increases in late items are Red. Hide unchanged/unavailable comparisons according to the existing eligibility rules.
- Where the existing SLC breakdown is still presented outside the monthly card, retain the exact captions **منجز ضمن موعد SLC** and **منجز بعد موعد SLC**, rendered with isolated Latin and Arabic runs. Preserve the approved visual order: SLC at the physical left, the Arabic phrase to its right. Keep the caption, figure and change aligned. Positive changes for completed-after-SLC items are Green, including both arrow and number. The monthly card uses the combined **منجز** figure specified in section 8; this does not rename source keys or change other reports.

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
| Legislation | Completed within SLC deadline + completed after SLC deadline | All legislation in scope; beneath one Green/Linen completion bar |
| Special projects | Completed in each requester subgroup | Full subgroup total; beneath each subgroup bar |
| Budgeted projects | Completed budgeted projects | All budgeted projects in scope; new Green/Linen bar after statuses and before quarters |

The budgeted-project denominator includes statuses absent from headline figures. Its Linen remainder means all not completed. Keep the existing headline composition without adding the rejected extra-status disclosure.

A valid zero numerator over a positive denominator keeps its zero completion geometry and displays **–** as the percentage value, with no percent sign. This presentation does not make a zero equivalent to missing data. Missing, nonfinite, negative or impossible values and zero denominators produce no completion bar/caption. Suppress a distribution caption if its bar is invalid. For legislation, show the completion bar/caption only when the completed cohorts are valid and non-overlapping and their aggregate lies within the full eligible total; do not double count overlapping source records or repair invalid data by clamping a figure. Do not apply these completion captions to financial or strategy measurement bars.

Financial bars stay solid even when some source values are unavailable. Remove hatching, completeness markers and repeated availability notes such as **قيم متاحة: 59 من 61**. Do not replace them with a new marker, note or tooltip. Missing values must still retain their source semantics and calculation eligibility.

### Agenda quarter charts and totals

- Use vertical stacked quarter columns with exact topic counts. Approved agenda stays physically right and emerging topics left. Use a shared zero-based whole-count axis across visible categories, with one count above each quarter and no percentage or quarter/total ratio captions.
- Hide empty categories. Preserve the union and source order of active quarters, the explicit undated group and any additional eligible category. A category’s missing intersection with another active quarter is a true zero and displays a dash.
- Under each chart, show **الإجمالي حسب الحالة** and that category’s totals by status across all its quarters within the active filters. These status totals must sum to the category total. Do not use the first quarter as the default summary.
- No quarter is selected on initial render or after a filter change. Hover and keyboard focus do not replace the totals. Clicking a quarter, or activating it with Enter/Space, shows only its status values with its quarter name; omit ratios and percentages. Clicking that quarter again or pressing Escape restores totals; clicking outside a quarter restores totals.
- Remove persistent and hover outlines around bars. Keep a visible keyboard-only focus cue. Arrow keys move focus without changing the status summary. Retain accessible names and the expandable underlying count table.
- Keep the original **تعريفات مستويات الإنجاز** below the charts without rewriting its definitions. Swatches match the shared status appearance. Standalone completed labels/counts use Green, late uses Red and ready uses Teal; other plain status text remains Ink.
- Native PDF always includes aggregate totals by status below each chart, independent of screen quarter selection. Keep charts, totals and the compact full definitions on one summary page after the contents. Use the recovered legend space for the plot; do not clip text or distort marks. Cover has no footer; displayed numbering starts with contents as page 1.
- Put each nonzero status count inside its segment only when the supplied DIN numeral fits legibly with padding. Measure both available height and width at the actual rendered size. Screen in-bar figures are at least 16 CSS pixels; use approximately 12pt for in-bar figures in A4 PDF. Keep readable ink from the shared status mapping.
- Preserve exact proportional segment geometry and the common count scale. Never inflate a small segment, alter the denominator, overlap labels, merge statuses or shrink numerals below their readable role just to show every in-bar count. Increase usable plot height and recover whitespace where appropriate; re-evaluate fit after reflow or filter changes.
- Small counts that do not fit remain available through each quarter’s accessible description, explicit quarter activation and expandable on-screen exact count details. Do not insert these count matrices as separate printed/PDF tables or appendix pages. Keep the approved chart, aggregate status totals, detailed definitions and original agenda record tables in the export. Omitted in-bar labels must not change segment geometry, source counts or available interactive detail.
- Keep axis/quarter labels at approximately 9pt and above-bar quarter totals at 16pt in A4 landscape PDF. Status-summary labels use 10.5pt and values 12pt. Verify short, dense, filtered, single-category and undated layouts with the actual downloaded PDF.

### HH special-project charts and cards

- Detail cards show each project heading without a repeated group-title/number strip. Show the group heading once above its cards. Keep the leadership classification once as an outlined **مشاريع القيادة** badge beside the project identity, with the same Teal border/ink and Mist fill on screen and in PDF. Omit the duplicate raw **مشاريع القيادة: نعم/لا** metadata field; preserve its source value, filters and cohort membership. Native PowerPoint follows the same visible treatment.

- Split the same active source scope into two disjoint cohorts: **مشاريع القيادة** includes only records explicitly marked **نعم**; **مشاريع الأمانة العامة** (TEC) includes every other record, including blank leadership classification. Do not drop unclassified records. The two cohort totals must reconcile to the scoped project total.
- On a wide screen, place leadership physically right and TEC physically left in equal-width panels. Stack them at narrow widths. Hide an empty cohort panel and let the populated panel use the available width. If both are empty, use the existing report-level empty state rather than rendering empty charts or legends.
- Group each cohort by the existing sector field in stable source/approved order. Hide a sector row when its count is zero **within that cohort**, independently of the other chart. Keep heights content-driven; do not add blank rows to align panels.
- Use horizontal stacked count bars that extend leftward from the RTL zero baseline. Both visible cohorts share one zero-based whole-count scale, derived from the largest visible sector total. Recompute it from the active source scope; do not fix it to illustrative counts. Preserve each status segment’s exact count and order.
- Put counts inside status segments only where they fit legibly, using the shared fill/ink/border mapping. Retain exact small values in accessible descriptions and readable exported detail when a label cannot fit. Keep bars proportional; do not stretch a one-project segment to create room for text.
- Put each row’s total immediately beyond its actual filled-bar endpoint, with a readable gap and reserved edge clearance. In RTL this is to the left of the filled bar, not in a fixed far-left total column. Prevent clipping at the maximum row and at phone widths.
- Remove the short status labels beneath individual bars. Retain **totals by status beneath each cohort chart**, within the same filter scope, and the shared detailed **تعريفات مستويات الإنجاز** below the pair. These totals reconcile to each cohort total. Use completed Green, late Red and ready Teal for plain status labels/counts.
- Preserve the approved HH-specific legend wording and mark source-unclassified/other states honestly. Do not import agenda council-approval definitions as if they were HH business rules. Use the same source-derived status meaning in cards, bars, legend and exports.
- Keep the two populated charts, their aggregate status totals and detailed legend together on the HH summary PDF content page when they fit. Use the landscape report profile, readable native text/vector marks and content-driven continuation for unusually long scopes; never clip rows or force a fixed page count.
- Use the common contents and section sequence in HH, with actual PDF page references and internal links. Omit the separate four-metric overview and its completion strips from both screen and native PDF; retain the scoped title/overall-total lead above the cohort charts. Keep main list and populated detail sections in matching order, with table numbering preserved in internal card identities. The only extra structural section is **المستجدات التفصيلية**, split into ongoing and completed when populated. Screen return controls do not print.
- Use the six-column main list specified in section 5, without a project-manager column. Keep project title, recorded status/progress and meaningful populated source details in cards. Hide source filenames through the presentation layer only. The displayed reporting period remains report metadata unless an existing explicit date filter applies; redesign does not silently remove projects based on project start/end dates.

### Council decisions report — approved Revision 28

- Apply the shared report typography, spacing, status appearances, surfaces, controls, contents, return links, notes and export conventions. Preserve council-specific source eligibility and meanings; the agenda and special-project reports establish visual roles, not council business rules.
- Reading order is **contents → title/overall total, issuing-body charts and compact detailed legend → القرارات التي تتطلب المتابعة → قرارات أخرى مسجلة when populated → report notes/recommendations**. The full-bleed PDF cover precedes contents, centers the report title, selected entity and period together, has no footer, and is omitted from the screen workspace. Keep a neutral separate table when source columns make follow-up classification unavailable. Do not add decision detail cards, source-note appendices or boxes.
- Use the source-defined follow-up scope for chart totals: titled decisions requiring **رسالة رسمية** or **بريد من الوحدة التنظيمية**. Completed, development/review, late and residual statuses retain their existing disjoint source definitions. Late is not included again in progress for council decisions. Keep other recorded decisions in their table; do not silently drop them or label all of them closed/cancelled.
- Show one nonempty chart panel per issuing body. **المجلس التنفيذي** is first, physically right; **مجلس الشؤون الاستراتيجية** is second, physically left. Other populated named bodies follow, then **قرارات دون جهة إصدار محددة** for blank issuing-body values. Do not assign those decisions to either main council. A lone panel fills the available width; narrow screens stack the panels in the same reading order.
- Each panel shows its issuing-body title and total, then horizontal count bars for its actual statuses in approved source order. Use one common zero-based whole-count scale across all visible panels, recalculated from the active scope. Put exact counts inside marks where legible, with readable shared ink; use an adjacent count for a mark too short to hold its number. Never enlarge a bar to fit a label. Hide zero rows and empty panels. Status labels and explicit counts keep the chart understandable without relying on color. All issuer-panel totals and status rows must reconcile to the eligible overall total.
- Place one compact **تعريفات مستويات الإنجاز** beneath the charts, using the shared swatches, title and definition typography. Describe recorded council statuses without inventing approval or deadline rules. Keep charts and legend together in ordinary A4 output; paginate additional bodies at readable sizes and keep source labels fully readable. The absence of a source status is not evidence of completion.
- Exact RTL table order is **م ← الموضوع ← القرار الأخير ← الجهة المعنية ← الحالة ← ملاحظات**. Use the shared table appearance, readable Arabic text and natural wrapping; allocate the greatest width to the latest-decision narrative. There is no separate decision-number, issuing-body or meeting-date column. Do not add a completion percentage or project-manager field.
- Inside **القرار الأخير**, place a secondary metadata line above the full decision text in this order: **رقم القرار: … · صادر عن: … · تاريخ الاجتماع: …**. Omit each empty field together with its label and separator. If all metadata is empty, omit the metadata line. Omit an empty narrative; if both metadata and narrative are empty, leave the cell empty. Retain an available reference even when the narrative is empty. Never infer a missing date or decision number.
- Use **م** for continuous sequential numbering across the rendered filtered report, with the follow-up table first and other recorded decisions next. Preserve source decision numbers and record identities separately. Group the tables by meeting year then quarter, ordering valid meeting dates chronologically within each group. Retain year-only and undated groups at the end of their applicable sequence; do not invent a quarter.
- Preserve the complete recorded **الموضوع**, **القرار الأخير** and **ملاحظات**. Keep meaningful notes in their table column instead of duplicating a source-notes appendix. Missing table values remain empty; a genuine numeric zero displays **–** at the presentation boundary. Identifiers, dates and narrative text retain their source characters.
- Reporting period is cover context, not a new meeting-date filter. Preserve the existing entity, sector, department and follow-up filter semantics. **تاريخ الاجتماع** means meeting date; a reply date is not a completion deadline. Displayed dates and grouped dates must come from the same source values.
- PDF contents follows final pagination, with real page references and destinations. Repeat the six column headings on continuation pages, preserve complete long text, and keep headings with the following content. The cover is unnumbered; copyright and page 1 start on physical page 2. Screen, native PDF and native PowerPoint must use the same scoped records, chart model, labels and section order.

## 8. Approved monthly composition details

These are monthly-report rules, not required content for every dashboard.

- **Agenda categories:** two separate equal Linen boxes, **الأجندة المعتمدة** right and **المواضيع المستجدة** left. Use a 12px screen gap, 9px radius and 8px vertical / 14px horizontal padding. Preserve 18px names, 28px figures and their individual changes. PDF uses equal boxes with a 3mm gap and existing print typography.
- **Budget order:** approved budget first; invoice spending, its change and Teal bar next; allocated/unallocated amounts and Taupe bar below. Omit the visible **الإنفاق … من الموازنة المعتمدة** caption, retaining the calculation and accessible bar meaning.
- **Quarter annotation:** show only **مشاريع 2027: N** when the filtered valid-2027 count is positive. Otherwise omit the line and spacing. Keep the separate quarter reference year. The rule is specifically 2027; do not silently roll it forward.
- **Strategy cleanup:** remove **مؤشرات الأداء** and the three repeated coverage/result-count/target-count notes. Keep primary values, the denominator, measurement bar and valid metric changes. A valid nonzero total-count change remains neutral and unlabeled in the card header.
- **Legislation card:** use the approved two-column composition described below. Omit the repeated explanation comparing actual completion with the SLC deadline; retain the source timing definitions and SLC details wherever they remain relevant outside this card.
- **PDF-only exclusions:** omit the missing-requester note, such as **جهة الطلب غير مسجلة: 2 · مشمولة في الإجمالي**, and the specified prior-project-status completeness explanation. Keep their screen diagnostics, source totals, comparison eligibility and unrelated output warnings intact.

Remove unused spacing with removed content. These exceptions do not authorize removing actual table notes, units, essential source caveats or metric definitions elsewhere.

### Monthly legislation card — approved Revision 24

- Keep **التشريعات** at the card’s physical right and the full scoped total at the physical left, with **الإجمالي** and its eligible change beneath the total. Use the shared monthly card type, spacing, surface and change roles rather than reproducing the illustration’s enlarged review canvas.
- Show two peer metric columns: **منجز** on the right and **قيد العمل** on the left. **منجز** is the aggregate of the existing completed-within-SLC and completed-after-SLC cohorts. Keep the label, count and favorable completed change Green; retain the existing source-backed unfavorable-change treatment when completion decreases. This combines their monthly presentation without altering either source cohort, calculation key or other report’s breakdown.
- **قيد العمل** retains its existing source-defined count, including unfinished late items. Within that column, place the secondary line **منها متأخر** with its count and eligible change in Red. Late is a subset of in-progress work, never a third peer bucket added again to the card total or bar. Do not infer unfinished lateness from a completed-after-SLC record.
- Keep real zero values as **–**, generated missing values blank and existing empty-metric suppression. Hide an empty late subset and its unused spacing; never turn a missing late value into zero. Maintain readable label/value relationships and isolate signed changes and percentages for RTL.
- Below the metrics, use one Green completion strip on a Linen track. Its numerator is the combined completed count; its denominator is **all legislation in the active source scope**, including records omitted from headline figures. The Linen remainder means not completed, not a separately derived status. Omit separate SLC segments and a red late segment from this completion strip.
- Beneath the strip, show only **نسبة المنجز** directly beside the percentage, right aligned on a shared baseline, rounded to at most one decimal place. Retain the shared 14px screen / 9pt PDF caption roles and their approved gap. Do not add the illustration’s review label or explanatory footnote to the production card.
- All values, proportions and deltas come from the uploaded report and active filters. The approved illustration’s 183 total, 178 completed, 5 in progress and 2 late are an example, not application constants. Preserve sector, unit, entity and inherited drilldown scope; an aggregate completed drilldown returns the exact union of the two completed cohorts, an in-progress drilldown returns its full source group, and late returns only its subset.
- Apply existing historical-comparison eligibility to the combined completed figure. Show a combined change only when both constituent comparisons are valid for the same current/previous source scope; never treat an unavailable historical cohort as zero or add a partial change. Keep total, in-progress and late changes tied to their own valid source histories. Suppress zero or unavailable changes under the existing rules; do not infer a new in-progress change from the illustration’s other figures.
- Preserve all source identities, status/timing fields, historical keys and existing diagnostics. Do not force completed plus in-progress to equal the card total when the source has other or incomplete classifications. Validate the aggregate and denominator before drawing a bar; retain existing unavailable/invalid-state behavior instead of inventing records, a status, a remainder count or an apparently reconciled history.
- Use the same metric meaning, order, nesting, colors, values, scope and completion denominator on screen, continuous PDF and A4 PDF. Reflow naturally on phones without shrinking type. In A4, keep a fitting card together and preserve the existing print scale; inspect the real exported text and bar geometry rather than relying only on a browser preview.

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
- **Agenda, council and HH covers:** full-bleed A4 landscape image with the report title, selected entity (when selected) and source report period centered horizontally and vertically. Keep agenda's month-to-month year format. No footer or page number on the cover. Start copyright and content-page numbering on physical page 2, excluding the cover from the total. Covers do not duplicate the screen workspace. Agenda retains its entity column, category titles and topic counts in the detail tables and omits empty category sections and the source-notes appendix.
- **Continuation:** no repeated report masthead. Repeat table column headings across continuation pages and keep section headings with following content. Omit empty sections and their contents entries. Preserve working PDF contents/project destinations while omitting screen-only return controls. Never insert separate agenda count-matrix pages.
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

**Source basis:** the user’s latest council approval, exact six-column order and empty decision-reference omission, together with the user’s 14 October 2026 approval to apply all consistency recommendations, align table-column order and cover naming, keep detailed updates only for special projects, and reduce legends to enlarge charts. Revision 26 incorporates that approved reading order, contents and link behavior. Retain the prior approved monthly legislation card, no Harvey balls, status palette, source-grounded bars, exact filter semantics and all data-quality checks from v159/v160. Current implementation evidence belongs in **Verification-v163.md**; documentation alone is not a validation pass. Historical standards remain provenance and do not override this revision.
