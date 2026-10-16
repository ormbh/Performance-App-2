# TEC Desktop Design Principles

**Revision 38 · 16 October 2026 · Performance App v174**

## 1. Scope, authority and change control

- Desktop is the sole interface design and testing target. Existing responsive code stays in place; mobile and tablet optimization/testing are outside scope.
- PDF is the sole report export format. PowerPoint controls, generation paths and export assets are excluded from the delivered runtime.
- Current explicit user instructions override historical documents and generic skills. Do not infer approval from a previous developer-written claim.
- A calculation, eligibility, data-quality or source-label correction does not authorize a visual redesign. Approval for one page or chart does not extend to another.
- Reuse equivalent component roles while preserving each page’s purpose, source scope and approved chart type. Illustrate a new visual direction and obtain approval before implementation.
- Distinguish an agreed requirement, proposed decision, intentional exception and verified implementation. Documentation is not proof that a component passes.
- Preserve source identities, raw values, meaningful notes, filters, denominators and calculations. Separate genuine zero, missing and unavailable states.
- Use one shared component/token implementation for equivalent roles. Preserve readable Arabic/RTL, mixed-script isolation, keyboard access and visible focus.

Revision 36 approval: the owner approved the revised text-only sticky navigation illustration and explicitly approved the complete consolidated audit corrections on 16 October 2026. The grid shortcut appears only on search home and opens the monthly report. Existing chart types and visual roles are retained.

Revision 37 approval: the owner explicitly approved the revised four project filters, five entity filters, contents restricted to the three formal reports, and desktop/PDF-only scope. Correct moving logos and broken navigation without changing approved chart designs. These rules supersede the older eight/three filter inventories and portfolio/entity contents clauses.

Approval references: the owner’s explicit approval of the six-part desktop/PDF consistency package in this conversation (16 October 2026) controls Revision 35. Monthly strip geometry is the inspected pre-v166/v165 reference (9px desktop / 1.6mm PDF), not the later counted-strip change. The three detailed report chart types remain as previously approved. Historical Revision 30 claims of approval for counted monthly bars are superseded. Approved monthly legislation composition and all data contracts remain in force.

Revision 38 approval: the owner approved the complete v173 audit correction package and reviewed projects/entities compositions. The **التقرير الشهري** page is the visual baseline for desktop dashboard/workspace pages; **تقرير الأجندة السنوية** is the baseline for formal reports. The approved baseline overrides an older conflicting implementation, but does not change source definitions or authorize an unrelated chart redesign. Portfolio retains count-scaled month bars with quarter/year totals, budget physically right and deadlines left; entities uses one comparable domain-stack panel followed by domain-specific record tables. No generic **نظرة عامة** or contents block is added.

### Revision 38 resolved layout decisions

- **R01 — precedence:** use the two named baseline pages, the role tables below and explicit page exceptions. Passing calculations or an unchanged previous PDF does not establish layout compliance.
- **R02 — requester labels:** preserve the monthly baseline's 16px requester/subgroup labels as an explicit monthly exception. The general 18px subgroup-name role remains for its other approved contexts.
- **R03 — spacing:** the base scale remains 4 / 8 / 12 / 16 / 24 / 32 / 48px. Existing approved baseline components may retain 20px internal groups and 28px count-end reserves where required by chart geometry. These are named component exceptions, not new general spacing values.
- **R04 — chart interaction:** proportional marks retain exact data geometry. Tiny segments are not independent undersized action targets. Use a minimum-44px whole-domain/row activation and readable exact-status drill controls. Counts that do not fit stay represented in visible aggregate status totals and exact record views; do not stretch marks, shrink figures or create overlapping hit areas. For an entity domain stack, the whole-domain control exposes every exact source-status count in its accessible name. Activate it, then select the source status in the existing detail filter to display the exact domain/status total and matching records. Global aggregate totals alone do not satisfy this requirement.
- **R05 — legend scope:** monthly keeps its existing compact key; the three formal reports keep workflow definitions. Portfolio and entity use one compact related-chart key with status totals and accessible source definitions. Do not add duplicate or unrelated legends, and do not merge source statuses that share an appearance.
- **R06 — repeated PDF context:** ordinary special-project detail pages have no repeated administrative group title/count strips; native-PDF inspection verifies the existing section heading appears once per group. Preserve the initial section heading and essential project identity/status/progress on genuine long-record continuations; do not remove these legitimate identity headers.
- **R07 — file setup hierarchy:** previous/current comparison file-card titles use the shared 28px Charcoal card-title role; their source filenames remain meaningful upload context. App navigation, controls and drill commands are screen-only unless the exported PDF contains a real verified destination. Comparison PDFs retain measures/explanations and omit dead app commands (C27).
- **R08 — blank chart categories:** retain every contributing row and its blank raw category. A chart-only contextual label **قطاع المصدر فارغ** may identify that aggregate; make its missing-category meaning explicit, retain exact records and keep the original record field empty. This does not create a recorded sector or suppress an otherwise nonzero group.
- Equivalent dialogs use 28px Charcoal titles, shared 44px controls and the shared focus/state system. Selected filter values retain a coherent 72px peer row, compact first-name/additional-count display and full names in the selector/accessibility label. Their full values must never become clipped data or lost scope.
- Desktop entity records use progressive browsing, with continuous ordinals from the full scoped/domain order; full PDF includes every matching row. Domain-specific progress/date fields and meaningful notes remain intact. Ordinal columns reserve at least 4-digit space, remain no-wrap and isolate numerals on screen and in PDF.
- Full-PDF record tables use a comfortable 3.5mm vertical / 2mm horizontal cell role; explicitly selected compact portfolio record tables and compact chart/history tables use 2mm / 1.5mm. The monthly baseline retains 3.5mm on both axes as a named exception. Ordinal cells reserve width independently instead of shrinking text.
- Full-PDF primary totals use 28pt and secondary summary figures 20pt. Formal-report figure roles remain separately specified. Preserve 12pt source table text and source-driven pagination instead of reducing type to force a page count.

## 2. Typography and role precedence

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

General type roles apply unless a component has an explicit exception below. Chart axes, definitions and PDF typography have separately specified roles; never apply a blanket font-size override to all descendants.

## 3. Color, status, missing values and progress

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

Use these pairings without new unapproved tints or blanket opacity. **One status uses the same fill, readable ink and border across badges, chart marks, legends, native PDFs.** The badge appearance is the reference; the former separate chart-status palette is superseded. For example, **جاهز للعرض is Teal everywhere**, and work/review uses Mist with Teal ink and borders. Give Paper and pale chart marks a visible boundary so they do not disappear into the canvas. Keep status names and exact values available; color is never the only identifier.

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

## 4. Desktop geometry and controls

Use the spacing scale **4 / 8 / 12 / 16 / 24 / 32 / 48px**. Desktop gutters are 48px, main-column gaps 24px and stacked-card gaps 16px. Paper cards have 1px Sand borders, 18px corners and 24px padding. Height follows content; do not stretch unrelated cards to create symmetry.

| Component | Standard |
|---|---|
| Action buttons | Minimum 44px height; 16px horizontal padding; 8px icon/text gap; 8px corners; no shadow |
| Icon buttons | Minimum 44 × 44px target; 20px icon |
| Inputs | Minimum 44px height; 12px horizontal padding; 8px corners |
| Core report filters | Minimum 72px height; 8px vertical / 12px horizontal padding; 4px label/value gap; 1px Taupe border |
| Execution-status badges | 16px Dubai Regular; 6px vertical / 12px horizontal padding; 8px corners; 1px border; no shadow |
| Leadership classification badge | 16px Dubai Regular, Mist/Teal, existing pill shape; 13.5pt outside-table PDF role |
| Table cells | 16px padding, content-driven height, approximately 1.6 Arabic line-height, fine Linen separators |
| Informational changes | Compact 24px visual row, each change attached to its own figure |
| Interactive changes | At least 44 × 44px reserved target with compact numeral line; no overlapping hit areas or negative-margin expansion |
| Completion captions | Label and percentage on one baseline with 8px gap |

Primary actions are Teal/Paper; hover Charcoal/Paper; pressed Ink/Paper. Secondary actions are Paper/Teal with Teal borders; hover Mist and pressed Sand. Disabled actions use Ink/Linen/Silver without blanket opacity. Loading preserves width and label, communicates busy state and prevents duplicate activation. Keyboard focus uses a 2px Teal outline with 2px offset.

Small text on Linen uses Ink where Taupe/Linen fails 4.5:1 normal-text contrast (measured approximately 4.40:1). Keep Taupe’s other approved roles where contrast is sufficient; do not introduce unapproved colors.

## 5. Header, navigation, menu, filters and PDF actions

### Header and navigation

- Retain the supplied official logo, aspect ratio and colors. The shared desktop workspace uses the existing 192px logo at the physical right, title/context at the left, and 32px/48px top/side insets. Anchor the logo at the same top/right position on all workspace routes, including search results; do not vertically center it against different title heights. Search home and landscape covers retain their separately approved compositions.
- Use the page title and applicable source/report cutoff; do not substitute the download date. Avoid duplicate titles and explanatory subtitles. Preserve necessary units, dates, field labels and actual notes.
- Use one slim sticky text navigation above the masthead on loaded desktop workspaces, including results, comparison, checks and upload. Keep Paper background, subtle Sand separator, no enclosing capsule and no grid/hamburger icon. The masthead and filters scroll normally.
- Primary links follow RTL reading order: **البحث في الأداء، التقرير الشهري، محفظة المشاريع، تقرير الجهات، التقارير، المقارنة الشهرية**. The separated utility group contains **ملاحظات البيانات، رفع ملف التقرير**. Preserve every existing destination and necessary page command.
- **التقارير** opens exactly three text-only destinations in this order: **تقرير الأجندة السنوية، تقرير قرارات المجالس، تقرير المشاريع الخاصة**. Keep a small dropdown arrow; no item icons. The active destination has Teal text and a restrained 2px underline. Navigation uses 16px Dubai and targets at least 44px; the approved header height is 72px.
- Preserve real route URLs and inherited scope, same-tab default, Ctrl/middle-click source transfer, dropdown arrow/Home/End navigation, Escape/outside-click dismissal and focus restoration. Offset section/focus destinations beneath the sticky bar. Logo navigation remains monthly after loading and upload before loading.
- Search home retains its centered logo/title/field composition and 36px title. Center the **original four-square button + بحث في التقرير + عرض جميع النتائج** beneath the field. The 44×44px four-square shortcut has no visible caption or tooltip, has the accessible name **التقرير الشهري**, and opens that page. It appears nowhere else. Do not put the global header on search home.
- Align existing PDF/task actions at physical left beside the direct filter fields, with scope/reset below. Preserve all page-specific filters, settings/editor commands and source behavior. Pages without those filters keep a consistent left task-action group. Shared navigation is screen-only.

### Filters

- Place direct labeled fields below navigation, then the selected-scope summary and applicable **مسح التصفية**. Do not add an outer filter card. Preserve approved page-specific filter sets, with four main portfolio fields and five main entity fields as specified below. Directly visible fields must not retain contradictory hidden/disclosure states or redundant collapse controls.
- Labels use 12px Dubai Regular; selected values 16px. One choice shows its name; partial multiple choice shows the first selected visible name **+N**; all/unrestricted shows **الكل**. Retain selection chronology and directional isolation. Full checked values remain accessible in the selector.
- Same-field choices are unions; different fields intersect. Preserve dependent options, exact tokens, explicitly blank selections and inherited drill scope. Stale selections never silently become unrestricted.
- Comparison file setup and diagnostic severity controls retain their task-specific semantics while sharing control colors, geometry, focus and readable labels.

### PDF button

- Use **تنزيل PDF**, with one 20px download icon and the primary-action treatment, in the shared left task-action group. Download directly through the bundled offline engine; no browser print dialog or network is required.
- Place applicable **إعدادات PDF** beside it as a secondary action. Monthly settings retain calculation-date controls; portfolio settings retain spacing controls. Neither offers obsolete paper-format choices.
- Keep button width and label during loading, expose busy state, prevent duplicate activation, restore focus after completion and show a truthful error if export fails.

### Search and results

- Shared prompt: **ابحث عن بند أو مشروع أو مسؤول**; number search remains supported and named accessibly. Use one functional search-submit icon.
- Default result fields are **البند، الحالة / التقدم، التوقيت، الوحدة التنظيمية**; retain saved/custom columns and full details. Export all matching rows independently of the visible result page.
- Matched text uses Mist behind Ink, regular weight. Result titles have the existing detail arrow and hover/focus underline; no permanent underline across the entire title.

## 6. Report composition, legends, tables and empty states

- Equivalent desktop report roles share surfaces, title/total alignment, controls, contents, links and spacing. Category title is physically right; scoped overall total physically left, with **الإجمالي** beneath it.
- Agenda and HH sequence: **contents → charts/status totals/detailed legend → record tables → applicable detailed updates → notes/recommendations**. Only special projects has **المستجدات التفصيلية**. Council’s explicit sequence is in section 8.
- **محتويات التقرير is reserved for agenda, council decisions and special projects only**, on screen and in PDF. Portfolio, entity, monthly and other pages have no report-contents block or dependent return-to-contents controls. Preserve meaningful sections and specifically approved summaries; do not blanket-add **نظرة عامة** headings or legends. Legends belong only to the approved charts they explain.
- Contents links in the three formal reports follow rendered order with labeled record counts. PDF contents uses actual final content-page numbers and valid internal destinations. Screen-only return controls do not print.
- Status totals belong directly below each corresponding chart. Detailed **تعريفات مستويات الإنجاز** belongs below the related chart group (after the full-width unassigned council box), before record tables. Monthly uses its separate compact key after the summary columns and before follow-up rows. Do not duplicate keys on each bar.
- Detailed desktop legends: 20px heading, 16px labels, 14px definitions, 10px bordered swatches, 16px padding/gaps. PDF: 12pt heading, 10.5pt labels/definitions, 2mm swatches. Preserve report-specific definitions. Keep charts and legends together when they fit; readability and complete content take priority over a fixed page count.
- Main desktop table headings: 18px Dubai Bold; content: 16px Dubai Regular. Linen header, Paper body, fine Linen separators. Allow natural wrapping; never shrink/truncate source text to force a fit. Keep **موعد الإنجاز** on one line.
- Common RTL sequence: **م، الموضوع/المشروع، الجهة المعنية، الحالة، نسبة الإنجاز where recorded، موعد الإنجاز**. Agenda has five columns; HH six. Do not invent a progress field for agenda. Keep the HH main-list project-manager column omitted; retain its meaningful detail field. Council uses its explicit six columns.
- Number records continuously within the filtered report, preserving link identities. Agenda groups approved quarters, emerging then other topics; HH lists ongoing then completed in approved source/status/date order, with details in the same order.
- HH project detail identity shows leadership classification once as **مشاريع القيادة**; omit repeated section/number strips and raw نعم/لا metadata. Preserve meaningful source details, including project manager. Hide source filenames and circular progress markers.
- Put populated report notes/recommendations at the end in stacked Paper cards. Keep meaningful source narrative intact. Omit empty cards and their contents links.
- A zero-result scope retains filters/scope/reset and shows one meaningful empty state. Hide empty contents, charts, legends, sections and invalid completion strips. A remaining chart uses available width. Never add empty alignment rows, count-matrix PDF pages or source-note appendices.

## 7. Bars, chart semantics and metric alignment

Preserve the existing physical title/total positions and metric name/value/change order. Names sit above figures; changes below their own figures. Align peers through shared rows, not arbitrary offsets. Numeric increase arrows express direction; color expresses the agreed performance meaning. Neutral totals/spending remain neutral; completed increases Green and late increases Red. Preserve valid history; hide unavailable/unchanged comparisons without inventing zeros.

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
- Native PDF always includes aggregate totals by status below each chart, independent of screen quarter selection. Keep charts, totals and the compact full definitions together after the contents when they fit at the approved readable sizes; otherwise continue without clipping. Use the recovered legend space for the plot; do not clip text or distort marks. Cover has no footer; displayed numbering starts with contents as page 1.
- Put each nonzero status count inside its segment only when the supplied DIN numeral fits legibly with padding. Measure both available height and width at the actual rendered size. Screen in-bar figures are at least 16 CSS pixels; use approximately 12pt for in-bar figures in A4 PDF. Keep readable ink from the shared status mapping.
- Preserve exact proportional segment geometry and the common count scale. Never inflate a small segment, alter the denominator, overlap labels, merge statuses or shrink numerals below their readable role just to show every in-bar count. Increase usable plot height and recover whitespace where appropriate; re-evaluate fit after desktop resizing or filter changes.
- Small counts that do not fit remain available through each quarter’s accessible description, explicit quarter activation and expandable on-screen exact count details. Do not insert these count matrices as separate printed/PDF tables or appendix pages. Keep the approved chart, aggregate status totals, detailed definitions and original agenda record tables in the export. Omitted in-bar labels must not change segment geometry, source counts or available interactive detail.
- Keep axis/quarter labels at approximately 9pt and above-bar quarter totals at 16pt in A4 landscape PDF. Status-summary labels use 10.5pt and values 12pt. Verify short, dense, filtered, single-category and undated layouts with the actual downloaded PDF.

### Special-project charts and cards

- Detail cards show each project heading without a repeated group-title/number strip. Show the group heading once above its cards. Keep the leadership classification once as an outlined **مشاريع القيادة** badge beside the project identity, with the same Teal border/ink and Mist fill on screen and in PDF. Omit the duplicate raw **مشاريع القيادة: نعم/لا** metadata field; preserve its source value, filters and cohort membership. 

- Split the same active source scope into two disjoint cohorts: **مشاريع القيادة** includes only records explicitly marked **نعم**; **مشاريع الأمانة العامة** (TEC) includes every other record, including blank leadership classification. Do not drop unclassified records. The two cohort totals must reconcile to the scoped project total.
- On a wide screen, place leadership physically right and TEC physically left in equal-width panels. Hide an empty cohort panel and let the populated panel use the available width. If both are empty, use the existing report-level empty state rather than rendering empty charts or legends.
- Group each cohort by the existing sector field in stable source/approved order. Hide a sector row when its count is zero **within that cohort**, independently of the other chart. Keep heights content-driven; do not add blank rows to align panels.
- Use horizontal stacked count bars that extend leftward from the RTL zero baseline. Both visible cohorts share one zero-based whole-count scale, derived from the largest visible sector total. Recompute it from the active source scope; do not fix it to illustrative counts. Preserve each status segment’s exact count and order.
- Put counts inside status segments only where they fit legibly, using the shared fill/ink/border mapping. Retain exact small values in accessible descriptions and readable exported detail when a label cannot fit. Keep bars proportional; do not stretch a one-project segment to create room for text.
- Put each row’s total immediately beyond its actual filled-bar endpoint, with a readable gap and reserved edge clearance. In RTL this is to the left of the filled bar, not in a fixed far-left total column. Prevent clipping at the maximum row.
- Remove the short status labels beneath individual bars. Retain **totals by status beneath each cohort chart**, within the same filter scope, and the shared detailed **تعريفات مستويات الإنجاز** below the pair. These totals reconcile to each cohort total. Use completed Green, late Red and ready Teal for plain status labels/counts.
- Preserve the approved HH-specific legend wording and mark source-unclassified/other states honestly. Do not import agenda council-approval definitions as if they were HH business rules. Use the same source-derived status meaning in cards, bars, legend and exports.
- Keep the two populated charts, their aggregate status totals and detailed legend together on the HH summary PDF content page when they fit. Use the landscape report profile, readable native text/vector marks and content-driven continuation for unusually long scopes; never clip rows or force a fixed page count.
- Use the common contents and section sequence in HH, with actual PDF page references and internal links. Omit the separate four-metric overview and its completion strips from both screen and native PDF; retain the scoped title/overall-total lead above the cohort charts. Keep main list and populated detail sections in matching order, with table numbering preserved in internal card identities. The only extra structural section is **المستجدات التفصيلية**, split into ongoing and completed when populated. Screen return controls do not print.
- Use the six-column main list specified in section 5, without a project-manager column. Keep project title, recorded status/progress and meaningful populated source details in cards. Hide source filenames through the presentation layer only. The displayed reporting period remains report metadata unless an existing explicit date filter applies; redesign does not silently remove projects based on project start/end dates.

## 8. Council decisions report

- Apply the shared report typography, spacing, status appearances, surfaces, controls, contents, return links, notes and export conventions. Preserve council-specific source eligibility and meanings; the agenda and special-project reports establish visual roles, not council business rules.
- Reading order is **contents → title/overall total, issuing-body charts and compact detailed legend → القرارات التي تتطلب المتابعة → قرارات أخرى مسجلة when populated → report notes/recommendations**. The full-bleed PDF cover precedes contents, centers the report title, selected entity and period together, has no footer, and is omitted from the screen workspace. Keep a neutral separate table when source columns make follow-up classification unavailable. Do not add decision detail cards, source-note appendices or boxes.
- Use the source-defined follow-up scope for chart totals: titled decisions eligible under the complete shared 2026 rule in section 10, including qualifying closed/cancelled records. Completed, development/review, late and residual statuses retain their existing disjoint source definitions. Late is not included again in progress for council decisions. Keep other recorded decisions in their table; do not silently drop them or label all of them closed/cancelled.
- Show one nonempty chart panel per named issuing body. **المجلس التنفيذي** is first, physically right; **مجلس الشؤون الاستراتيجية** is second, physically left. Other populated named bodies follow. Place **قرارات دون جهة إصدار محددة** in a separate full-width box below all named charts, spanning both columns. Keep its title and overall total in the shared card header, and arrange its populated status bars in two columns on wide screens, in source status order. Do not assign those decisions to either main council. Hide the box when empty; keep it when it is the only populated group. A lone named panel without an unassigned group fills the available width.
- Each named panel shows its issuing-body title and total, then horizontal count bars for its actual statuses in approved source order. The unassigned box retains those exact status counts and bars without repeating the named panels’ axis. Keep one physical bar-length-per-count scale across named plots and the unassigned box at the same viewport or exported size; a full-width container must not double the visual value of its bars. Use one common zero-based whole-count scale across all visible panels, recalculated from the active scope. Put exact counts inside marks where legible, with readable shared ink; use an adjacent count for a mark too short to hold its number. Never enlarge a bar to fit a label. Hide zero rows and empty panels. Status labels and explicit counts keep the chart understandable without relying on color. All issuer-panel totals and status rows must reconcile to the eligible overall total.
- Place one compact **تعريفات مستويات الإنجاز** beneath the charts, using the shared swatches, title and definition typography. Describe recorded council statuses without inventing approval or deadline rules. Keep charts, the unassigned box and legend together in ordinary A4 output when they fit; paginate additional bodies or unusually tall status groups at readable sizes, retaining the unassigned box after the named charts and before detail tables. Preserve fully readable source labels and do not clip or shrink text to force a page count. The absence of a source status is not evidence of completion.
- Exact RTL table order is **م ← الموضوع ← القرار الأخير ← الجهة المعنية ← الحالة ← ملاحظات**. Use the shared table appearance, readable Arabic text and natural wrapping; allocate the greatest width to the latest-decision narrative. There is no separate decision-number, issuing-body or meeting-date column. Do not add a completion percentage or project-manager field.
- Inside **القرار الأخير**, place a secondary metadata line above the full decision text in this order: **رقم القرار: … · صادر عن: … · تاريخ الاجتماع: …**. Omit each empty field together with its label and separator. If all metadata is empty, omit the metadata line. Omit an empty narrative; if both metadata and narrative are empty, leave the cell empty. Retain an available reference even when the narrative is empty. Never infer a missing date or decision number.
- Use **م** for continuous sequential numbering across the rendered filtered report, with the follow-up table first and other recorded decisions next. Preserve source decision numbers and record identities separately. Use one logical table per meeting year within each existing follow-up/other-record population. Keep rows in quarter/date order without separate quarter tables, quarter headings or an added quarter column. Retain year-only and undated records in their applicable final sequence; never invent a quarter. Repeat column headings only on physical PDF continuation.
- Preserve the complete recorded **الموضوع**, **القرار الأخير** and **ملاحظات**. Keep meaningful notes in their table column instead of duplicating a source-notes appendix. Missing table values remain empty; a genuine numeric zero displays **–** at the presentation boundary. Identifiers, dates and narrative text retain their source characters.
- Reporting period is cover context, not a new meeting-date filter. Preserve the existing entity, sector, department and follow-up filter semantics. **تاريخ الاجتماع** means meeting date; a reply date is not a completion deadline. Displayed dates and grouped dates must come from the same source values.
- PDF contents follows final pagination, with real page references and destinations. Repeat the six column headings on continuation pages, preserve complete long text, and keep headings with the following content. The cover is unnumbered; copyright and page 1 start on physical page 2. Desktop and native PDF must use the same scoped records, chart model, labels and section order.

## 9. Page-specific presentation contracts

### Monthly detail composition

These are monthly-report rules, not required content for every dashboard.

- **Agenda categories:** two separate equal Linen boxes, **الأجندة المعتمدة** right and **المواضيع المستجدة** left. Use a 12px screen gap, 9px radius and 8px vertical / 14px horizontal padding. Preserve 18px names, 28px figures and their individual changes. PDF uses equal boxes with a 3mm gap and existing print typography.
- **Budget order:** approved budget first; invoice spending, its change and Teal bar next; allocated/unallocated amounts and Taupe bar below. Omit the visible **الإنفاق … من الموازنة المعتمدة** caption, retaining the calculation and accessible bar meaning.
- **Quarter annotation:** show only **مشاريع 2027: N** when the filtered valid-2027 count is positive. Otherwise omit the line and spacing. Keep the separate quarter reference year. The rule is specifically 2027; do not silently roll it forward.
- **Strategy cleanup:** remove **مؤشرات الأداء** and the three repeated coverage/result-count/target-count notes. Keep primary values, the denominator, measurement bar and valid metric changes. A valid nonzero total-count change remains neutral and unlabeled in the card header.
- **Legislation card:** use the approved two-column composition described below. Omit the repeated explanation comparing actual completion with the SLC deadline; retain the source timing definitions and SLC details wherever they remain relevant outside this card.
- **PDF-only exclusions:** omit the missing-requester note, such as **جهة الطلب غير مسجلة: 2 · مشمولة في الإجمالي**, and the specified prior-project-status completeness explanation. Keep their screen diagnostics, source totals, comparison eligibility and unrelated output warnings intact.

Remove unused spacing with removed content. These exceptions do not authorize removing actual table notes, units, essential source caveats or metric definitions elsewhere.

### Project portfolio

- Apply the approved complete-page composition to **محفظة المشاريع**, including its formatted report and native full PDF print. Default the report name to **مستجدات محفظة المشاريع** plus the source reporting year, preserving custom report title and period. Keep the actual cutoff distinct from the displayed reporting period.
- Show the overall scoped project total prominently with **الإجمالي** beneath. The compact summary distinguishes completed-project count/share, mean recorded progress and follow-up count. Do not equate recorded progress with status completion, money or a budget-weighted average.
- Show exactly four main filters directly on the portfolio page and formatted report, in RTL order: **القطاع، الوحدة التنظيمية، الجهة المعنية، مدير المشروع**. Type, priority, quarter and status remain meaningful chart/record dimensions, rather than additional hidden page constraints. Old routes must not silently reinstate removed main-filter constraints. Preserve within-field unions, cross-field intersections, dependent options, exact record identity, selected scope, return navigation and current record details. Compact selected values use the first visible name plus the additional-choice count; full values remain available in the selector and accessible name. Never turn a stale or explicitly blank selection into an unrestricted field. The concerned entity for this budget portfolio is the General Secretariat under the existing parent mapping; sector and unit remain separately labeled context. Include all selected portfolio filters and the actual cutoff in PDF scope.
- Keep budget physically right and deadlines left on a desktop. Show full headline amounts with explicit AED units; retain allocation, invoice spending and recorded work value as separate measures with their existing eligible denominators. Missing finance remains unavailable, zero remains zero internally, negative recorded amounts remain signed and overspending is not clamped away.
- Use count-scaled month bars on one zero-based scale across displayed years, with explicit quarter/year totals. Keep active source years separate and retain undated records when present. Hide wholly empty groups. The mean recorded percentage stays in its own labeled column and is not used as count-bar geometry.
- Keep counts inside a bar when they fit at the approved type size; put the total at the end of a count bar. Tiny values retain proportional widths and exact accessible values. A single count mark uses an adjacent value when its in-bar label does not fit; small stacked segments remain represented in the visible aggregate status totals and exact-record drilldowns. Do not imply that every tiny segment has a visible individual label. Never stretch a segment or shrink type to simulate a fit. Re-evaluate fitting after fonts load, resizing and PDF layout.
- Show recorded status distributions on common count and money scales with a separate recorded-progress column. Include a neutral **حالات أخرى** category when unknown/missing statuses are present. A derived late condition overlaps recorded open statuses and must not be added to their disjoint grand total. Individual missing source fields remain empty.
- Use one compact portfolio-specific status-definition legend. Reuse approved badge/mark/swatch appearances; completed plain labels and counts are Green. Standardize the source Frozen display as **مجمّد** while preserving raw source values, stored filter tokens and old-link compatibility. Do not add a ready-for-presentation status to a portfolio whose source does not define it.
- Preserve the existing manager follow-up ranking: half the unfinished-count share plus half the unfinished-budget share. It describes follow-up volume, not employee performance. Preserve its source coverage rules and separate completed comparison group. Priority/type charts use true intersections, source order and separate count/money scales.
- Standardize leading record columns as **م ← المشروع ← الجهة المعنية ← الحالة ← نسبة الإنجاز ← موعد الإنجاز**. The follow-up table appends **ملاحظات**. Use the same table component for the main list, embedded follow-up and matching drilldowns. Keep the deadline heading on one line, continuous numbering within the displayed scoped list, full notes and exact project links. The displayed ordinal is separate from the immutable source key/reference. Sector/unit remain labeled context beneath the entity; type, priority and populated PM remain beneath project identity. Preserve all existing financial fields and populated notes in the record view. On desktops, retain a real table in a focusable horizontal-scroll region; do not combine the generic stacked-record layout with table columns. Preserve empty cells, including blank notes, without placeholder text or loss of column alignment.
- Keep quiet explicit screen report/list links. Portfolio has no contents block. Place populated report notes and recommendations at the end; hide empty editorial and follow-up sections. Do not introduce **المستجدات التفصيلية** outside special projects.
- Screen and PDF share the scoped model, section sequence, legend, column order, names and source text. Use full PDF print with readable type, correct page numbers and copyright; continuation at the technical height limit repeats table headings. Portfolio has neither a contents block nor an agenda-style cover. Portfolio numbering starts on its first content page. Do not enforce a fixed page count or claim PDF parity from screen captures. Exclude screen-only navigation references, captions and arrows from PDFs; retain genuine internal PDF contents destinations.
- Route financial values through one strict decimal reader. Reject malformed/non-decimal numeric text as unavailable; preserve valid decimal numeric text and its existing data-quality observation. Do not silently change the deliberate difference between named-project portfolio finance and monthly all-row source sums. Keep relevant diagnostics and test these distinct populations explicitly. Recalculate financial history from uploaded previous records with the same reader. Saved aggregate financial deltas require the explicit compatible numeric-contract marker; otherwise show an unavailable comparison with its reason, preserving valid nonfinancial history.
- Never replace an incomplete operational workbook with illustrative records. Label published example screenshots/PDFs and record the actual source identity and cutoff in QA evidence. A populated example validates behavior and layout, not the current operational totals. Verify the exact delivered app and PDF after final edits.

### Entity report

- Use **تقرير الجهات**, with exactly five direct main filters in RTL order: **القطاع، الوحدة التنظيمية، الجهة المعنية، مدير المشروع، المجال**. Show readable selected scope and the source calculation cutoff. The entity filter uses the recorded concerned entity; contributor relationships remain contextual information and exact relationship drilldowns, rather than a sixth main filter. PM uses the actual project-manager field; never substitute an agenda/council coordinator. Apply the same scope to current/previous rows, comparison, totals, charts, records, URL state, reset and PDF. Preserve within-field unions, cross-field intersections, exact contributor dictionary matching and ambiguous contribution text without inferred ownership.
- Derive screen and native PDF from one scoped renderer: one scope/context presentation, approved summary values without a generic overview heading, one common-scale domain status-stack panel and compact totals/key, grouped main records, then preserved timing/relationship and comparison context. Keep the nonempty follow-up list available through its exact-count drill without duplicating long records on the overview. Focused drills show their own exact records; print the active domain/status/query and refresh print content on live query changes.
- Keep approved agenda, **المواضيع المستجدة**, other agenda when present, all recorded council decisions and special projects separate, in the same chart/table sequence. Entity council totals include all recorded rows; the council report's eligible follow-up denominator remains distinct and explicitly explained. Do not add budget, legislation or KPI populations without validated entity relationships and metric contracts.
- Show each recorded-status distribution once, using one count scale, the shared palette and readable in-bar counts where they fit. For the approved composed domain stacks, a tiny segment keeps its exact proportional width; the compact key retains visible status totals, the whole-domain control exposes its exact domain-specific source-status values, and the existing domain → status-filter → matching-record view shows the exact selected count. This explicitly supersedes the older requirement to place an outside label beside every tiny stacked segment; neither global aggregates nor color alone replace exact domain/status access. Standalone tiny count bars retain an adjacent exact count when their in-bar label cannot fit. Outside labels must not change bar proportions. Missing status rows remain in totals and neutral distributions; individual missing fields stay blank. Real zero displays as a dash.
- Keep date-based lateness separate from recorded status. A ready topic remains **جاهز للعرض** after a passed plan. Use neutral wording **تجاوز الموعد المخطط · موعد العرض غير مسجل** without asserting booking failure. Council meeting dates are not follow-up deadlines. The 30-day window includes the reference day.
- Use leading columns **م، الموضوع/المشروع، الجهة المعنية، الحالة**, adding recorded progress only where that source field exists, then applicable follow-up dates and full populated notes. Contributions remain labeled entity context. Omit each blank decision-reference field. Keep filenames and repeated administrative source references out of report rows. Number the grouped main list continuously.
- Keep full source notes with their field labels in main/focused record tables. The priority table gives its alert reason without duplicating long source notes. Preserve exact single-record links, keyboard focus and comparison setup. Desktop tables remain real tables; any necessary local scroll region has a descriptive accessible name and keyboard access.
- Primary/contributor counts can overlap. Count a source row once in the selected entity scope; entity subtotals cannot be summed into a grand total or presented as a performance ranking. State the relationship basis and preserve it in drilldowns.
- Empty scopes retain filters and scope but show one meaningful empty state. Hide empty summary, contents, charts, legends, follow-up and record groups. Explain missing names separately from a genuine zero workload. The special-project detail model uses the same named-record eligibility guard instead of treating fallback titles as source names.
- Native entity output uses full PDF print. Retain the same content and reading order, full scope, 12pt table text, readable badges, repeated headings, complete long-note continuation, sequential page totals and copyright. Include full section headings and count labels when continuing an oversized row; do not create a gap-only page. Keep fitting chart/legend groups together and allow content-driven continuation for larger scopes.
- Preserve valid comparison definitions and unavailable-history explanations. Do not invent historical arrows or add empty comparison cards. Existing comparison-specific record views retain their purpose.

### Monthly summaries and links

- Preserve the two portfolio columns: **محفظة المشاريع** physically left and **محافظ المتابعة التنفيذية** physically right. Retain their established card order; the separate legislation review plate does not reorder the production report. Use content-driven cards and the approved screen/PDF typography rather than copying illustration canvas dimensions.
- Special-project leadership is an explicit **نعم**. TEC includes every remaining record, including an empty leadership classification, as in the detailed special-project report. Within either cohort, completed, ready, late, known work and other are disjoint. **قيد العمل** includes only recorded review/development statuses; missing or unrecognized statuses remain in neutral **حالات أخرى** and the full total. Hide empty cohort/status groups without changing source data or counts.
- Recalculate historical comparisons using the same cohort and status definitions whenever previous records exist. Embedded summaries calculated under incompatible definitions cannot support corrected subgroup/work changes: leave those changes unavailable with a truthful reason. Retain independently valid comparisons, including an unchanged overall-total comparison. Do not turn missing historical buckets into zero or fabricate the difference caused by a definition correction.
- Monthly status distributions retain the pre-v166 thin-strip treatment: 9px high with 5px corners on desktop; 1.6mm high with 1mm corners in PDF. No in-bar numerals. Keep exact proportional status widths, the existing metric values and accessible descriptions. This does not change the counted charts in the three detailed reports.
- Apply Green to completed labels and values, Teal to ready labels and values, and Red to late labels and values in both screen and actual PDF output. Work labels remain neutral; work bars use Mist with Teal border/ink. Other uses Paper with a Silver border. Text inside filled Green/Teal marks uses Paper.
- Use one compact shared color key in the approved order: late, completed, ready, work, other. The common colors do not redefine portfolio-specific status semantics; legislation lateness remains a subset of work. Keep the key in full PDF print, after the summary columns and before follow-up rows.
- Put **الإجمالي** beneath the primary total in screen and PDF. A true numeric zero displays **–**; a missing numeric value is blank and retains its unavailable semantics. Leave missing follow-up notes blank; preserve all supplied note text.
- Give each summary a quiet explicit footer link. Special projects, agenda, council and budget projects open their existing formatted reports; legislation and strategy open their existing detailed record views. Preserve sector/unit/entity scope and clear unrelated report-local filters. Count/status actions retain their exact matching-record drilldowns. The complete summary footer is screen-only: omit its link, plain reference caption, arrow and divider from PDF. A non-clickable caption is still navigation content. Preserve genuine internal PDF contents links.
- Preserve source-derived figures, valid metric changes, units, independent KPI means and all approved diagnostic exceptions. Illustration values are examples, never runtime constants. Budget headline categories do not authorize adding the rejected extra-status disclosure; completion still uses every scoped budget project.
- PDF output must retain the shared legend and applicable source notes. Keep fitting cards together, permit readable continuation and repeat table headings as needed. Do not remove content or shrink type to force a fixed page count. Verify the actual full PDF files against the screen and uploaded workbook.

Agenda missing-status information uses **بدون حالة معتمدة: N** beneath the strip in both desktop and PDF. Do not promote it to a PDF-only peer metric or use a different PDF label. Keep council’s existing missing-status footer and follow-up scope note.


### Monthly legislation

- Keep **التشريعات** at the card’s physical right and the full scoped total at the physical left, with **الإجمالي** and its eligible change beneath the total. Use the shared monthly card type, spacing, surface and change roles rather than reproducing the illustration’s enlarged review canvas.
- Show two peer metric columns: **منجز** on the right and **قيد العمل** on the left. **منجز** is the aggregate of the existing completed-within-SLC and completed-after-SLC cohorts. Keep the label, count and favorable completed change Green; retain the existing source-backed unfavorable-change treatment when completion decreases. This combines their monthly presentation without altering either source cohort, calculation key or other report’s breakdown.
- **قيد العمل** retains its existing source-defined count, including unfinished late items. Within that column, place the secondary line **منها متأخر** with its count and eligible change in Red. Late is a subset of in-progress work, never a third peer bucket added again to the card total or bar. Do not infer unfinished lateness from a completed-after-SLC record.
- Keep real zero values as **–**, generated missing values blank and existing empty-metric suppression. Hide an empty late subset and its unused spacing; never turn a missing late value into zero. Maintain readable label/value relationships and isolate signed changes and percentages for RTL.
- Below the metrics, use one Green completion strip on a Linen track. Its numerator is the combined completed count; its denominator is **all legislation in the active source scope**, including records omitted from headline figures. The Linen remainder means not completed, not a separately derived status. Omit separate SLC segments and a red late segment from this completion strip.
- Beneath the strip, show only **نسبة المنجز** directly beside the percentage, right aligned on a shared baseline, rounded to at most one decimal place. Retain the shared 14px screen / 9pt PDF caption roles and their approved gap. Do not add the illustration’s review label or explanatory footnote to the production card.
- All values, proportions and deltas come from the uploaded report and active filters. The approved illustration’s 183 total, 178 completed, 5 in progress and 2 late are an example, not application constants. Preserve sector, unit, entity and inherited drilldown scope; an aggregate completed drilldown returns the exact union of the two completed cohorts, an in-progress drilldown returns its full source group, and late returns only its subset.
- Apply existing historical-comparison eligibility to the combined completed figure. Show a combined change only when both constituent comparisons are valid for the same current/previous source scope; never treat an unavailable historical cohort as zero or add a partial change. Keep total, in-progress and late changes tied to their own valid source histories. Suppress zero or unavailable changes under the existing rules; do not infer a new in-progress change from the illustration’s other figures.
- Preserve all source identities, status/timing fields, historical keys and existing diagnostics. Do not force completed plus in-progress to equal the card total when the source has other or incomplete classifications. Validate the aggregate and denominator before drawing a bar; retain existing unavailable/invalid-state behavior instead of inventing records, a status, a remainder count or an apparently reconciled history.
- Use the same metric meaning, order, nesting, colors, values, scope and completion denominator on desktop and full PDF print. Preserve the existing print scale; inspect the real exported text and bar geometry rather than relying only on a browser preview.

## 10. Comparison and source-data contracts

### Monthly changes and session retention

- Compare exact approved identities across both complete snapshots before applying scope. Preserve raw typed keys. Changes to sector/title/source-name key components must never be silently paired. Flag exact partial-key candidates as unresolved diagnostics; one-sided keys establish source presence, not proof of new, cancelled or completed work. Retain missing/duplicate-key quarantine and missing-table safeguards.
- Reuse one source-field change detector for comparison and entity history. Compare relevant non-calculated source fields, including notes, managers and narrative updates. Keep recalculated timing distinct from a source-cell edit.
- A monthly +/− opens its exact metric and inherited scope in the same tab, focuses the explanation and highlights relevant changed fields. Keep both incoming and outgoing contributors, including offsetting movements. Other edits and unchanged records remain available separately. Preserve the drill intent through file setup, reload and return navigation.
- Use a domain/metric table in monthly order for the comparison overview. Do not combine projects, decisions, indicators and money into a primary grand total. Approved agenda and emerging topics remain separate. Keep independent financial/measurement measures and the established legislation, council and cohort definitions.
- Use the RTL detail sequence **م ← الموضوع / المشروع ← سبب التغير ← السابق ← الحالي ← الأثر على المقياس**. Full before/after source information is available on demand. Technical provenance is secondary. Any necessary local desktop table scroll region remains keyboard-accessible and named.
- Counts reconcile previous + incoming − outgoing + unresolved residual = current. Money uses amount contributions in the same currency/population. Rate/average changes are non-additive: show coverage and the matching measured cohort rather than fabricated per-record count contributions. Ignore only floating-point residual noise within a documented machine-precision bound. Missing source/required fields are unavailable, not zero. Display zero as a dash and retain approved status colors.
- Attribute the same records to each affected organizational level using the metric's eligibility before and after. A transfer plus status change must not subtract from a status the old unit never held. Do not sum sector/unit/entity levels or overlapping memberships into a disjoint total.
- Default shared drill navigation to the same tab. Keep explicit new-tab activation and modified clicks. Successful supported storage retains the validated binary workbook pair locally through a small session reference and a version. New tabs retain the requested pair/version; older tabs announce a newer version and update explicitly. Never silently mix snapshots.
- Validate storage write/read, retain honest blocked/quota fallback messages and stage replacements. Do not label live files saved unless verified. Keep any prior retained version available for explicit recovery; do not silently restore it as the newly selected pair. Offer session ending and local-file removal. Binary sessions expire after 24 hours and expired records are cleaned on the next successful app start; tab closure alone is not a guaranteed deletion event. No workbook data is sent to a service.
- Export the selected comparison view, period, entity/organizational scope, query context, changed fields and row sequence from the same model. Use native selectable text/vector PDF, readable full-PDF columns and, at the technical height limit, repeated table headers and existing long-row continuation. Draw legend swatches; do not insert unsupported decorative font glyphs. Verify affected shared exports and record the direct-file/browser limitations actually encountered.

### Council follow-up eligibility: approved 2026 mold

- Use one shared source-grounded eligibility predicate in monthly counts, council summaries/charts/tables, drilldowns, comparisons and exports. A nonblank subject is required after Excel TRIM/NBSP handling.
- Include «رسالة رسمية» and «بريد من الوحدة التنظيمية» without a year condition. Include «مغلق (لا يتطلب متابعة)» and «ملغي» only when the follow-up letter date is in 2026, the decision letter reference contains the text 2026, or the meeting-year field equals 2026 after trimming. Numeric Excel dates use their calendar year; textual dates use the mold's contains-2026 test. Meeting date is not an additional eligibility field. Count each source record once.
- Blank or unsupported follow-up values are outside this performance population; preserve them in the source/register and data-quality review. Closed/cancelled follow-up is not proof of completed execution. Preserve the independently recorded status; it cannot override eligibility.
- This rule explicitly targets 2026, matching the approved mold. Never silently substitute the current date or comparison snapshot's year.
- Apply the same rule to both comparison source snapshots. Legacy embedded monthly totals cannot prove the previous month was recomputed under the new rule; retain that limitation.
- If an alternative eligibility column is missing and a closed/cancelled record has no known positive year witness, report the metric unavailable rather than silently excluding an ambiguous record. Default letter/email records need no year witness.
- Preserve the intentionally broader entity register and the council report's other-records section. Distinguish these full source populations from follow-up performance metrics; do not discard source records to make totals match.
- Anonymized subjects intentionally removed by the owner are not a workbook defect. Preserve originals and validate with separate, explicitly synthetic names/controlled cases. Do not publish supplied or synthetic workbooks in the runtime ZIP. Distinguish formula inspection/independent calculation from actual Excel recalculation and Power Query refresh.
- Keep the approved visual composition, fonts, colors and six council columns. Verify the current PDF profiles in section 11; no historical format requirement overrides them.

### Count populations, diagnostics and semantic pagination

- Named-record count metrics use the same nonblank-title eligibility for total, status/category/quarter breakdown, percentage denominator, source-key drill, comparison snapshot and export. Retain all source rows for data review; do not invent names or remove intentionally anonymized rows from the imported source. Special requester subgroups follow the existing explicit-yes/otherwise-TEC rule.
- Financial monthly sums deliberately retain all valid financial source rows; named-project portfolio finance retains its separate scope. Council follow-up and the broader recorded register retain their approved distinction. Explain these exceptions rather than forcing totals equal.
- Legacy embedded supporting counts do not prove compatible named-record eligibility. Mark affected changes unavailable with an explanation unless a compatible contract is recorded; uploaded previous workbooks are recomputed using the current predicates. Never present a definition change as monthly activity.
- Diagnostics name the actual imported heading, preserve exact source row/key, and identify the demonstrated cause. Missing/unsupported execution status is not a missing-title defect. Keep review observations distinct from automatic corrections.
- Use the shared true-zero formatter and **مسح التصفية** for equivalent reset actions. Missing values remain empty; source narratives, dates and identifiers are untouched.
- Entity workspace uses the same 48px desktop gutters and approved Linen canvas. Record-count chart ticks are whole numbers on a common zero-based scale; proportions and counts remain exact.
- In PDF, keep every fitting metadata field label with its value. Keep headings with following content and repeat table headings on continuation. Long source content may continue at readable type sizes; preserve record identity/context. Check semantic associations in actual page plans and rendered output, not only numeric bounds.

## 11. PDF profiles, footer and output verification

| Page/report | Only permitted export treatment |
|---|---|
| Agenda, council decisions, special projects | A4 landscape, 297 × 210mm |
| Monthly, portfolio, entity, comparison, search results, data checks and other pages | Full PDF print: 297mm wide, measured content height |

- No A4 portrait format choice/fallback, A3, or PowerPoint export. Full print retains all selected content. If content exceeds the engine’s 5080mm physical page-height limit, continue at the same full width and readable scale with text-safe boundaries/repeated table headings; do not silently switch to A4, clip, shrink or require dropping records.
- Embed supplied fonts and render native Arabic text/vector graphics through the bundled offline engine. Draw swatches rather than inserting unsupported decorative/private-use font glyphs. Verify real downloaded files; browser screenshots alone do not establish PDF correctness.
- Full PDF uses the existing full-width monthly profile: 8mm top/side inset, reserved footer clearance and content-derived height measured after fonts/images settle. Other pages retain their own content composition and PDF type roles. Landscape reports use 10mm margins outside full-bleed covers.
- Landscape covers use the approved full-bleed image and logos. Center title, applicable selected entity and period together horizontally/vertically. No border, footer or number on the cover. Physical page two begins **page 1**; the displayed total excludes the cover.
- Desktop footer contains copyright only. PDF footer contains copyright and page numbering only. Never emit blank/footer-only pages. Keep footer clearance independent of content measurement.
- First PDF header uses approved logo/title/source date and applicable scope. Monthly title includes **- لتاريخ DD/MM/YYYY**, with sector/unit scope; entity still filters its data but is omitted from that header. Do not repeat the masthead on continuation pages.
- Keep headings with following content. Repeat table headings on continuation; preserve complete long notes and internal contents/record destinations. Hide empty sections and their contents entries. No forced page count.
- PDF type roles are independent of desktop CSS: first title 24pt; portfolio heading 18pt; card/table-section 16pt; main figures 24–28pt; secondary figures 20pt; table headings 13.5pt Dubai Bold; data/notes/in-table badges 12pt; outside-table badges 13.5pt; standard metric/caption 9pt; changes 11pt; metadata/copyright/page numbers 10.5pt. Detailed chart/legend annotations use the explicit chart roles in section 7.
- Monthly filenames remain **TEC_Monthly_Mmm_yy[_EnglishScope].pdf**, using source date, approved English mappings and first partial unit (otherwise sector), without +N or hidden bidi controls. Preserve other report naming rules.

## 12. Acceptance, evidence and maintenance

- Inspect the desktop renders and interactions changed by the work. Test filters/reset, unions/intersections, exact drill landing, meaningful selected states, keyboard/focus, long Arabic/mixed text, zero/missing values and empty scopes.
- Reconcile affected calculations and source record sets against the verified baseline/independent fixtures. A visual change must not alter metric definitions, source notes or comparison populations.
- Inspect actual PDFs for content/order/scope parity, readable fonts, status colors, clipping, complete records, full-height continuation, landscape pagination, cover exclusion and working destinations. Detect footer-only pages by meaningful body content, not merely nonempty extracted text.
- Test shared-component regressions with focused existing fixtures; do not repeatedly rerun unrelated application/source audits. No mobile/tablet or PowerPoint tests.
- Record exact runtime hashes, source fixture identity, passed/failed/not-run checks and limitations. Do not describe synthetic data as operational figures, formula inspection as Excel recalculation, or code inspection as a visual pass.
- Test actual link activation, resulting route, settled scroll position, focus, back/forward and scoped/new-tab destinations. Destination existence alone does not establish working navigation. Bare local section fragments must never be parsed as app routes.
- Compare logo x/y/width/height across desktop routes after images load. Compare native PDF text geometry with its final browser print layout, allowing only the documented paper margins and type roles; do not claim desktop/PDF pixel equality or a reported alignment bug fixed without reproducing it.
- Current release implementation evidence belongs in **Verification-v174.md**. Historical verification files remain provenance; they do not establish a current pass.

## 13. Historical provenance

Revisions 24–34 remain available in prior release archives. Their approved source/metric contracts are retained above; superseded device/export rules and the unapproved counted-monthly-strip claim are not active requirements. Revision 36 adds the explicitly approved complete audit corrections and revised desktop navigation. Revision 37 records the subsequent filter/contents decisions and actual-interaction verification requirements. Revision 38 records approval of the full v173 layout audit corrections and the reviewed projects/entities compositions, with the monthly and agenda visual baselines and explicit role exceptions above. Other visual directions still require illustration and approval.
