# TEC Apple-Inspired Design standard

Approved typography, controls, status badges, layout, header, navigation, bars and print rules. **Revision 11 — 12 October 2026; continuous monthly PDF and roomier digital spacing approved.** This consolidates the supplied standard and all subsequent approved amendments, including **18px Dubai Regular subgroup names and agenda category labels**, the updated Ink/Taupe text roles and solid financial bars.

**Implementation: Performance App v136.** The monthly report defaults to a continuous digital PDF with a 260mm page width, content-measured height and 12mm margins. A4 portrait remains selectable for monthly paper printing. Agenda, council and HH paper reports retain A4 landscape; all other paper views retain A4 portrait. A3 remains unavailable. Monthly short value/status labels and strategy metric names stay 16px on screen; SLC captions and the earlier caption corrections remain approved. Fonts, colors, source scope and calculations are unchanged. Browser, source and native PDF checks pass for the tested workflows; see VERIFICATION-v136.md for evidence and limits. Earlier verification files describe their own releases.

The monthly page establishes the shared standard at **100% browser zoom**. Screen typography uses 38px page titles (36px on the search home), 30px portfolio headings, 28px card titles, 16px table content and badges, and 18px Dubai Bold table headings. Retain the compact card grouping: 18px subgroup names, 16px monthly status labels above their figures, and change arrows below their own values. The card-header total label retains its position beneath the main total. **Remove explanatory labels and subtitles beneath all page, portfolio, section, card and table titles**, including search and upload titles. Retain the required screen report date as secondary metadata.

Print keeps its independent approved scale: table body, names, notes and in-table badges use **12pt**; table headings and badges outside tables use **13.5pt**. Screen size amendments do not automatically enlarge print. Updated text-color roles and solid financial-bar presentation apply to screen and print, except where a component has its own specified treatment, such as status badges, controls and the print footer.

Use the supplied **Regular (400)** faces for headings, figures, body text and controls. **Table column headings use the supplied Dubai Bold (700)** face. DIN Next Arabic and DIN Next LT Arabic are distinct supplied font families.

## Latest approved amendments

**Continuous monthly PDF:** use one custom digital page by default, with a 260mm width, 12mm margins and a 236mm content width. Measure the complete report after print fonts and images are ready; its height grows with the content. Preserve projects physically left, executive portfolios physically right and full-width followups below both. Use one report masthead and one legal/page-number footer. Keep all approved print font sizes; do not fit the document with zoom, font shrink or a fixed height.

**Digital spacing:** use 5mm padding inside monthly cards and the followup card, a 6mm portfolio-column gap, 4mm between stacked cards, 3mm beneath card headings, 2.5mm above metric rows and bars, and 3mm table-cell padding. Put the followup section 7mm below the summary. Preserve natural wrapping and the label/value/change associations. These spacings apply to the continuous digital format; screen and A4 paper spacing retain their approved profiles.

**Monthly format control:** the primary action reads **طباعة / حفظ PDF**. Under **إعدادات الطباعة**, show the **تنسيق التقرير** dropdown with **PDF متصل — صفحة واحدة** and **A4 عمودي — للطباعة**. The continuous format is the default when no current format preference is saved; retain a user's selected A4 preference. For the continuous format, choose Save as PDF in the browser dialog; select A4 for physical paper printing.

**Continuous height limit:** if the measured digital page would exceed 5080mm, automatically use A4 portrait pages for that print session and show an explanatory toast. Preserve every record, note, value and filter; keep the saved format preference unchanged. Do not truncate the report, clamp it to the limit or shrink text. Ordinary continuous reports remain one page; this fallback applies only to an unusually long report.

**Monthly A4 composition:** the selectable paper mode preserves projects left, executive portfolios right and full-width followups below both. Keep approved print fonts and use natural pagination. A fitting card moves whole if the remaining page space is insufficient; a taller card may continue readably. Do not promise a fixed A4 page count. The continuous digital mode supplies the approved single-page output by extending its page height.

**Strategy card notes:** remove the visible coverage/unmeasured-count caption, result-count caption and target-count caption on screen and in print (for example «تغطية القياس 72.2% · 15 غير مقاس», «متوسط نتائج 39 مؤشراً مقاساً», «متوسط 49 مستهدفاً مسجلاً»). Remove their empty spacing. Keep primary values, denominator, measurement bar, meaningful source availability explanations and valid changes. Align the retained changes on their own shared row when metrics appear side by side.

**SLC visual order:** retain the exact logical labels **SLC منجز ضمن موعد** and **SLC منجز بعد موعد**. Visually place the Latin prefix first at the physical left, with the Arabic phrase to its right; isolate each language run so bidirectional text cannot move SLC to the end. Align first caption lines and numeric/change rows. Below 600px, reflow the legislation metrics into two columns rather than squeezing four 16px captions; a single visible metric uses the full width. Print keeps its four status columns when all four categories are present and its 9pt label scale.

**Dashboard metric names:** monthly short value/status labels and strategy metric names use 16px Dubai Regular Ink on screen. Agenda category labels and subgroup names remain 18px; badges remain 16px. Retained explanations/metadata remain 14px. The independent print scale is unchanged. This is a monthly/dashboard role amendment, not a blanket resize of source-report legends or supporting labels.

**Legislation captions:** display **SLC منجز ضمن موعد** and **SLC منجز بعد موعد**. Remove the repeated comparison paragraph from the monthly screen and both output formats. Preserve the source fields, disjoint timing cohorts, status colors and formulas.

**Paper and orientation:** physical paper modes remain A4 only: agenda, council and HH use landscape; every other paper view, including the selectable monthly paper mode, uses portrait. A3 remains removed. The continuous monthly digital PDF is a separate custom-size format, not an A3 paper option. Keep the approved print scale in both digital and paper output. A4 cards reflow to the paper width and stay together when they fit.

The retained typography amendment increases only **الأجندة المعتمدة** and **المواضيع المستجدة** category labels from 14px to **18px Dubai Regular Ink** on screen. Their figures remain 28px and changes 15px. Print retains 9pt labels, 20pt figures and 11pt changes. Monthly short value/status labels and strategy names now use 16px. Supporting body explanations and minor metadata retain 14px. Other report/legend roles retain their separately specified sizes. The search-home title also moves 4px upward from v132; its 36px size and the logo, search-field and action positions stay unchanged.

All supporting text in this table uses the supplied Dubai Regular face; numeric figures use DIN Next LT Arabic Regular. The latest **18px** subgroup-name approval replaces the earlier **28px proposal**.

| Element | Example / placement | Approved screen size | Font | Default text color |
| --- | --- | --- | --- | --- |
| Special-project subgroup names | للقيادة / للأمانة العامة | **18px** | Dubai Regular | Charcoal #333333 |
| Agenda category labels | الأجندة المعتمدة / المواضيع المستجدة | **18px** | Dubai Regular | Ink #4F4E4E |
| Special-project subgroup totals | 24 / 36 | 28px | DIN Next LT Arabic Regular | Charcoal #333333 |
| Special-project status figures | 12 / 10 / 26 | 28px | DIN Next LT Arabic Regular | Charcoal #333333, with status exceptions |
| Agenda status figures | 43 / 16 / 58 | 34px | DIN Next LT Arabic Regular | Charcoal #333333, with status exceptions |
| Monthly dashboard short value/status labels | الإجمالي / منجز / قيد العمل; retain compact grouping | **16px** | Dubai Regular | **Ink #4F4E4E** |
| Monthly strategy metric names | Names above their respective values | **16px** | Dubai Regular | **Ink #4F4E4E** |
| Strategy primary figures | 39 / 83.2% / 87.8% | 34px | DIN Next LT Arabic Regular | Charcoal #333333 |
| Strategy registered denominator | 54 in the measured/registered pair | 28px | DIN Next LT Arabic Regular | Charcoal #333333 |
| Table content, names and actual notes | Neutral, regular weight | **16px** | Dubai Regular | **Ink #4F4E4E** |
| Status badge text | Informational status treatment | 16px | Dubai Regular | Approved status palette below |
| Table column headings | Column labels | 18px | Dubai Bold | Ink #4F4E4E |
| Important labels and retained explanations | Useful body guidance, units and definitions | **14px** | Dubai Regular | **Ink #4F4E4E** |
| Change arrows and differences | Below the corresponding value | **15px** | Dubai Regular | **Taupe #756B5F**, with meaning-based performance exceptions |
| Minor metadata | Screen date, secondary detail, empty-note placeholder | **14px** | Dubai Regular | **Taupe #756B5F** |
| Financial bars with partial numeric coverage | Allocation/spending ratios and subtotals | Solid fill | Existing chart treatment | Allocation Taupe #756B5F; spending Teal #115E67 |
| Financial hatching, completeness markers and numeric availability notes | Including قيم متاحة: 59 من 61 | **Removed on screen and in print** | Not rendered | No replacement marker or note |
| Explanatory labels/subtitles beneath titles | Repeated title descriptions | Removed | Not rendered | — |

The 14px explanation scale applies to retained definitions, useful source caveats and body guidance. Keep actual notes in the table, field labels, value/status labels, units and meaningful calculation definitions. The financial numeric-availability-note removal is the specific exception described in the bar rules below; it does not remove actual recorded notes or essential metric definitions.

An empty-note placeholder is secondary metadata at 14px Taupe; actual recorded table notes remain 16px Ink. Remove the redundant **جميع بنود المتابعة** label above the full follow-up table; keep its item count, status counts and **عرض جميع البنود** action.

## Monthly card grouping and alignment

| Area | Approved arrangement |
| --- | --- |
| Card header | Card title 28px DIN Next Arabic; main total retains 40px DIN Next LT Arabic; short total label 16px Dubai Ink beneath the total |
| Special projects | Two subgroup blocks, with 18px Dubai subgroup names and 28px totals; retain two status columns within each subgroup |
| Agenda | Retain the approved/new-item breakdown: category labels 18px Dubai Ink with 28px figures; retain three status columns with 16px labels above 34px figures |
| Value labels | Keep 16px monthly status labels close to their values, above the numeric row; retain the header total label beneath its value; do not use the rejected oversized side-by-side labels |
| Changes | 15px differences directly below their own figures; align corresponding values and comparison rows across adjacent groups |
| Completion bars | Preserve the shared bar baseline across the two special-project subgroups, including when a comparison is absent |
| Strategy | Keep measured/registered at physical right, average results in the middle and average targets at left; retain three distinct measures |
| Strategy alignment | 16px metric names above the figures, shared primary-value row; reserve 52px for two 16px label lines on desktop, and align retained changes below the appropriate values; preserve percentage units and the 28px registered denominator |
| Narrow screens | Reflow groups and metrics while preserving their approved font sizes and meaningful label/value associations |

Use shared layout rows for alignment rather than aligning text to the outer card box. Keep the compact arrangement and content-driven height; the 18px subgroup-name change does not expand the labels to figure size or move them into widely separated pairs.

## Master component table

For text-only rows, “Inherited” means the text follows the surrounding surface; it does not create a separate box. Card, table and field supporting text retains the specified Paper surface. Secondary page metadata follows its inherited surface; do not add a separate box beneath the date. A dash means no separate border or fill.

| Element | Font / screen size | Text | Background | Border |
| --- | --- | --- | --- | --- |
| Page title | DIN Next Arabic Regular / 38px | Charcoal #333333 | Inherited | — |
| Search-home title | DIN Next Arabic Regular / 36px | Charcoal #333333 | Inherited | — |
| Portfolio heading | DIN Next Arabic Regular / 30px | Charcoal #333333 | Inherited | — |
| Card / table-section title | DIN Next Arabic Regular / 28px | Charcoal #333333 | Paper #FCFBFB | — |
| Main figures | DIN Next LT Arabic Regular / 34–40px | Charcoal #333333, with defined status exceptions | Paper #FCFBFB | — |
| Secondary figures, including special-project subgroup totals/status figures | DIN Next LT Arabic Regular / 28px | Charcoal #333333, with defined status exceptions | Paper #FCFBFB | — |
| Special-project subgroup names | Dubai Regular / 18px | Charcoal #333333 | Paper #FCFBFB | — |
| Agenda category labels | Dubai Regular / 18px | Ink #4F4E4E | Linen #EFEBE7 category strip | — |
| Agenda status / strategy primary figures | DIN Next LT Arabic Regular / 34px | Charcoal #333333, with defined status exceptions | Paper #FCFBFB | — |
| Monthly short value/status labels and strategy metric names | Dubai Regular / 16px | Ink #4F4E4E | Paper #FCFBFB | — |
| Table column headings | Dubai Bold / 18px | Ink #4F4E4E | Linen #EFEBE7 | Sand #E7E0D3 bottom divider |
| Table content, names and notes | Dubai Regular / 16px | Ink #4F4E4E | Paper #FCFBFB | Linen #EFEBE7 row dividers |
| Important labels | Dubai Regular / 14px | Ink #4F4E4E | Paper #FCFBFB | — |
| Supporting body explanations; no title subtitles | Dubai Regular / 14px | Ink #4F4E4E | Paper #FCFBFB | — |
| Change arrows and differences | Dubai Regular / 15px | Taupe #756B5F, with meaning-based exceptions | Inherited | — |
| Minor metadata | Dubai Regular / 14px | Taupe #756B5F | Inherited | — |
| Primary action button | Dubai Regular / 16px | Paper #FCFBFB | Teal #115E67 | Teal #115E67 |
| Secondary action button | Dubai Regular / 16px | Teal #115E67 | Paper #FCFBFB | Teal #115E67 |
| Text action / action link | Dubai Regular / 16px | Teal #115E67 | Transparent | — |
| Destructive action button, when present | Dubai Regular / 16px | Paper #FCFBFB | Burgundy #651D32 | Burgundy #651D32 |
| Icon button | Existing icon family / 20px icon | Ink #4F4E4E | Paper #FCFBFB | Taupe #756B5F |
| Filter / input value | Dubai Regular / 16px | Ink #4F4E4E | Paper #FCFBFB | Taupe #756B5F |
| Filter / input label | Dubai Regular / 12px | Taupe #756B5F | Paper #FCFBFB | — |
| Inactive primary navigation link | Dubai Regular / 16px | Ink #4F4E4E | Transparent / inherited | — |
| Current primary navigation link | Dubai Regular / 16px | Teal #115E67 | Transparent / inherited | 2px Teal underline |
| Selected category tab, where applicable | Dubai Regular / 16px | Teal #115E67 | Paper #FCFBFB | 2px Teal selected marker |
| Disabled action button | Dubai Regular / 16px | Ink #4F4E4E | Linen #EFEBE7 | Silver #C8C7C7 |
| متأخر badge | Dubai Regular / 16px | Paper #FCFBFB | Red #C00000 | Red #C00000 |
| مجمّد / معلّق badge | Dubai Regular / 16px | Paper #FCFBFB | Burgundy #651D32 | Burgundy #651D32 |
| ملغى badge | Dubai Regular / 16px | Burgundy #651D32 | Sand #E7E0D3 | Burgundy #651D32 |
| منقول badge | Dubai Regular / 16px | Teal #115E67 | Paper #FCFBFB | Teal #115E67 |
| منجز badge | Dubai Regular / 16px | Paper #FCFBFB | Green #01831E | Green #01831E |
| قيد العمل / قيد التطوير / قيد الإجراء badge | Dubai Regular / 16px | Teal #115E67 | Mist #D9E1E2 | Teal #115E67 |
| قيد المراجعة badge | Dubai Regular / 16px | Teal #115E67 | Mist #D9E1E2 | Teal #115E67 |
| جاهز للعرض badge | Dubai Regular / 16px | Paper #FCFBFB | Teal #115E67 | Teal #115E67 |
| لم يبدأ badge | Dubai Regular / 16px | Paper #FCFBFB | Ink #4F4E4E | Ink #4F4E4E |
| مقاس badge | Dubai Regular / 16px | Teal #115E67 | Mist #D9E1E2 | Teal #115E67 |
| غير مقاس / لا ينطبق badge | Dubai Regular / 16px | Paper #FCFBFB | Ink #4F4E4E | Ink #4F4E4E |

Aliases listed together share a treatment. Each rendered item retains its own applicable source-backed label.

## Exact color palette

| Color | Hex code | Approved role |
| --- | --- | --- |
| Charcoal | #333333 | Headings, default figures, primary/destructive hover |
| Ink | #4F4E4E | Table headings/body/names/notes, short value/status labels, strategy metric names, important explanations and field values |
| Taupe | #756B5F | Secondary metadata, neutral differences, secondary field labels and active field borders; allocation/active chart fills |
| Teal | #115E67 | Primary controls, focus, selected navigation, relevant status treatments, progress accents |
| Burgundy | #651D32 | Frozen badges, cancelled text/borders, destructive actions, validation errors |
| Grey | #808080 | Large or decorative elements |
| Stone | #ABA394 | Chart fills and nonessential detail |
| Silver | #C8C7C7 | Chart fills, dividers, disabled control borders |
| Linen | #EFEBE7 | Page and table-heading surfaces, row dividers, disabled fills |
| Paper | #FCFBFB | Cards, table body, fields, light text in filled badges/buttons |
| Sand | #E7E0D3 | Card borders, quiet grouping surfaces, secondary/icon pressed fills |
| Mist | #D9E1E2 | Accent surfaces, secondary/icon hover, work/review/measured badge fills |
| Completed Green | #01831E | Completed figures/badges and favorable changes |
| Late Red | #C00000 | Late figures/badges and adverse changes |

Green and Red are the approved status exceptions. All other entries retain the existing TEC palette. Use the specified combinations; do not introduce new tints or dim disabled text with blanket opacity.

## Button, field and badge geometry

| Component | Size / padding | Corners / depth |
| --- | --- | --- |
| Action buttons | Minimum 44px height; 16px horizontal padding; natural width; 8px icon/text gap | 8px radius; 1px border where listed; no shadow |
| Icon buttons | Minimum 44 × 44px hit area; 20px icon | 8px radius; 1px border; no shadow |
| Inputs and existing category tabs | Minimum 44px height; 12px horizontal padding; expand with content | 8px radius; 1px boundary where listed |
| Core report filter fields | Minimum 72px height; 8px vertical / 12px horizontal padding; 4px label/value gap | 8px radius; 1px Taupe boundary; no extra enclosing panel |
| Primary navigation links | Minimum 44px hit area; natural text width | No filled tab boxes; current destination has a 2px Teal underline |
| Status badges | 6px vertical / 12px horizontal padding; natural width; 16px text at 1.6 line-height | 8px radius; 1px border; no shadow; no fixed height |
| Cards | 24px padding on desktop / 16px on mobile | Preserve 18px corners; Paper surface; 1px Sand border; restrained existing depth |
| Table cells | 16px vertical / 16px horizontal padding; content-driven row height | Fine Linen dividers; no heavy grid or nested boxes |

Status badges are informational. Their text uses 16px Dubai Regular, while padding and border remain as listed; their natural height is approximately 40px for a single line. Do not impose a fixed height. An actual drilldown action retains a separately accessible minimum 44px hit area and interaction behavior; badge appearance alone does not imply a button.

## Layout spacing

| Area | Approved spacing |
| --- | --- |
| Spacing scale | 4 / 8 / 12 / 16 / 24 / 32 / 48px |
| Desktop page gutters | 48px each side, fluid content width |
| Tablet page gutters | 32px each side |
| Mobile page gutters | 16px each side |
| Main column gap | 24px |
| Stacked card gap | 16px |
| Card padding | 24px desktop / 16px mobile |
| Table cell padding | 16px vertical / 16px horizontal |
| Arabic table line spacing | Approximately 1.6 |
| Comparison line below values | Reserve one aligned 24px line where comparisons are present |
| Header/navigation | One compact desktop row for navigation and task actions; reflow onto separate rows below 700px |
| Core filter row | Three separate fields below navigation; scope summary below the fields; no extra enclosing panel |
| Additional project fields | 16px gaps; three desktop columns, two at 600–1023px, one below 600px |

Rows and cards expand with their content. Charts show all populated categories without internal vertical scrollbars. Responsive layouts preserve the role sizes and readable wrapping rather than scaling down the entire page.

## Interaction states

Apply and verify these approved states consistently:

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
| Current primary navigation link | Teal text and a 2px Teal underline on the inherited surface; expose the current page to assistive technology |
| Selected category tab, where applicable | Teal text and a 2px Teal marker on Paper; expose the selected state to assistive technology |
| Clickable table name | Retain Ink #4F4E4E, Dubai Regular 16px; use underline/focus to reveal the action without changing the agreed name color or weight |
| Informational badge | Preserve its status treatment; no action-style hover or loading state |

Taupe control borders are chosen as a readable boundary on Paper. Stone #ABA394 and Silver #C8C7C7 remain suitable for nonessential separators, chart marks and disabled boundaries rather than as the sole visible boundary of an active input.

## Approved header, navigation, filters, menus and icons

| Component | Approved setup |
| --- | --- |
| Screen report title | DIN Next Arabic Regular 38px, Charcoal; title physically left and official logo physically right on desktop |
| Screen title metadata | Required cutoff date only beneath the title, Dubai Regular 14px Taupe #756B5F; no explanatory subtitle, scope line, preview note or current-data marker |
| Logo | Official supplied TEC asset; 192px desktop / 144px mobile report logo, preserved proportions and clear space |
| Primary navigation | Plain 16px Dubai links: البحث plus the current page only; search home has the menu only, search results have one current Search link; every other destination remains in the menu. Teal current-page underline; no filled boxes or redundant destination icons |
| Application menu | One existing 20px grid icon in a 44px control, named صفحات التطبيق; include three direct report links (agenda, council and HH) on every loaded page, including search; retain other existing destinations and eligible actions |
| Task actions | Monthly primary طباعة / حفظ PDF; other reports retain طباعة التقرير. Optional إعدادات الطباعة secondary action, grouped opposite navigation on desktop |
| Core filters | Sector → unit → entity in physical RTL order where applicable; separate fields below navigation; 12px labels and 16px values |
| Scope summary | 14px Ink below the filter fields; retain the active scope and update it when selections change |
| Additional project filters | Type, priority, completion quarter, status and manager under المزيد من التصفية; collapse preserves selections |
| Filter option search | Search available options without discarding selected values hidden by the search; native labelled checkboxes, 16px text and 44px rows |
| Selection behavior | Live update; OR within a field and AND across fields; empty selection is unrestricted; preserve source option scope, aliases and existing dependent-field validation |
| Filter reset | مسح التصفية clears filter fields only; retains the workbook, cutoff, notes, comparisons and print/display preferences |
| App/command menu | Paper surface, Sand border, 12px corners, 8px padding; 320px preferred width; 44px rows and viewport clamping |
| Checkbox filter popup | Paper surface, Taupe border, 12px corners; 320–400px preferred width; readable option area within the viewport |
| Menu dismissal | Outside click or Escape closes; keyboard dismissal returns focus to the trigger; outside click allows the clicked control to receive focus |
| Menu keyboard behavior | Enter/Space open; Up/Down and Home/End navigate command items; use real links for destinations; retain modified-click/new-tab behavior |
| Mobile filter sheet | Paper, 18px top corners and 16px padding; modal focus containment and inert background; close, تم and Escape preserve selections and restore focus |
| Print settings dialog | Paper/Sand, 18px corners; 28px DIN title with no subtitle; 16px fields / 12px field labels; 44px close target; Escape and focus restoration. Monthly تنسيق التقرير offers PDF متصل — صفحة واحدة and A4 عمودي — للطباعة |
| Definitions disclosure | Keep exact definitions and caveats in the report body; 16px named trigger, 20px directional chevron, 44px target and 14px Ink body text |
| Screen footer | Exact organisation/copyright legal line only; no source filename, calculation date, report title or extra note; no fixed footer covering content |
| Search and upload | Preserve the Google-style search and upload interactions. Search-home title 36px, raised 4px from its v132 position; preserve logo, field and action positions on desktop/mobile. This approved positioning amendment supersedes the prior optical-centering position. Home navigation is menu-only. Remove title subtitles |

Only one nonmodal popup is open at a time. Opening a modal closes other popups.
Keep menus/popups within the viewport. Responsive dismissal restores focus to a
live trigger. Closing any filter disclosure or sheet never clears selections.
Primary navigation does not silently transfer or reset unrelated page filters.

| Icon purpose | Existing glyph | Size / label |
| --- | --- | --- |
| Application destinations | Grid | 20px in 44px control; صفحات التطبيق |
| Print report | Printer | 20px beside monthly طباعة / حفظ PDF or other-report طباعة التقرير |
| Print settings | Chevron | 20px beside إعدادات الطباعة |
| Filter/disclosure open or close | Chevron down/up | 20px; expose expanded state |
| Close dialog/popup | X | 20px in 44px control; explicit accessible name |
| Search | Search | 20px workspace icon; preserve the approved search-pill glyph |
| Upload/change file | Upload/document | 20px with visible action text |
| Export/download | Download | 20px; identify the file format in the action label |
| Data observations | Warning | 20px with a descriptive action label and source count |

Reuse the existing outline SVG family and stroke character. Do not add emoji,
another icon font or a mixed filled/outline set. Mirror only genuinely directional
navigation, never printer, grid, document or upload icons, or numeric/time axes.

## Complete formatting and content rules

1. **Fonts and hierarchy.** Use DIN Next Arabic Regular for headings, DIN Next LT Arabic Regular for main/secondary figures, Dubai Bold for table column headings, and Dubai Regular for table content, labels, notes, metadata, controls and status badges. Use the supplied font files; do not simulate bold or substitute Apple system fonts. English table names also use Dubai Regular.
2. **Screen sizes.** Use 38px page titles (36px on the search home), 30px portfolio headings, 28px card titles, 34–40px main figures, 28px secondary figures, 18px Dubai Bold table headings, 16px Dubai Regular table content/names/notes, 16px status badge text, 18px Dubai subgroup names, 16px monthly short value/status labels, 16px monthly strategy metric names, 14px important labels and meaningful supporting body explanations, 15px changes, 14px metadata and 16px control values. Agenda category labels use 18px Dubai Regular Ink; their figures remain 28px. Special-project subgroup totals and status figures use 28px; agenda status and strategy primary figures use 34px; the strategy registered denominator stays 28px. Do not shrink the agreed table text to fit content. Filter labels retain 12px; their values use 16px.
3. **Text color roles.** Table content, names and actual notes use neutral Ink #4F4E4E and regular weight. Table headers use Dubai Bold, Ink on Linen. Monthly short value/status labels and strategy metric names use 16px Dubai Regular Ink. Other important labels and essential explanations retain 14px Dubai Regular Ink. Secondary metadata and neutral differences use Taupe #756B5F. Subgroup names use 18px Dubai Regular Charcoal. Card/table/field secondary text retains the specified Paper surface; screen date metadata follows the inherited page surface. Secondary filter labels retain their separately approved 12px treatment. Main figures default to Charcoal; completed figures use Green #01831E and late figures use Red #C00000 where those status meanings apply. The Paper text inside filled badges is a separate treatment from figure color.
4. **Palette.** Use the exact existing TEC colors and the agreed green/red status exceptions. Paper #FCFBFB is the card/table surface; Linen #EFEBE7 is the page/table-header surface; Sand #E7E0D3 is a quiet grouping/border tone; Mist #D9E1E2 is an accent surface. Stone #ABA394, Silver #C8C7C7 and Grey #808080 serve appropriate chart/decorative roles, not small regular body-text roles. Grey may be used for large or decorative elements. No new colors or undocumented tints.
5. **Arabic and mixed text.** Use approximately 1.6 line-height for table text, natural Arabic wrapping, comfortable padding and top/middle alignment appropriate to the content. Preserve source names. Keep English identifiers, dates, values, fractions, percentages and currency units in their correct reading order. Align numeric columns consistently.
6. **Badge identity.** Use the final badge mapping in the master table, including frozen as a solid Burgundy badge and cancelled as Burgundy on Sand. Keep badges visually distinct from ordinary table text. Preserve the actual source-backed status label; styling aliases do not create combined labels or new business categories.
7. **Completion and lateness.** Late unfinished work is always red. Completed legislation is green for both completion within the deadline and completion after the deadline; completion after the deadline does not become unfinished-late work.
8. **Legislation composition.** Place late legislation beside the other statuses and include it in the bar. Split pending items into late and remaining pending so each item appears once. Use the generated captions **SLC منجز ضمن موعد** and **SLC منجز بعد موعد**, isolating the Latin SLC run in Arabic layout. Remove the repeated **مقارنة: تاريخ الإنجاز الفعلي بالموعد المعتمد لدى SLC** paragraph on screen and in print. The applicable SLC date fields, actual source notes and timing calculations remain unchanged.
9. **Follow-up tables.** Show only items requiring follow-up. For projects, include unfinished overdue projects with a valid deadline, frozen, cancelled and transferred items, with or without comments. Keep the group order **late → frozen → cancelled → transferred**, and stable source order within each group. Names remain neutral and regular. Preserve the agreed columns and omit the removed delay-reason column.
10. **Zero and missing values.** Show true zero counts and zero table values as **–**. Hide empty status and H/M/L groups. Keep meaningful chart-axis zero baselines and source-backed 0% completion captions where required. Missing or invalid values remain distinct from true zero; use **غير متاح** where a dash would be ambiguous. Do not turn missing financial/progress data into zero.
11. **Progression arrows.** Use source-backed comparisons only. Put 15px arrows/differences directly below their corresponding value, on aligned baselines, reserving a single 24px comparison line where needed. ↑ means a numeric increase and ↓ a decrease. Green/red describes whether the change is favorable/adverse; use Taupe #756B5F for neutral changes such as a total or spend increase without an agreed performance meaning. A decline in late items is favorable; an increase is adverse. Hide unchanged or unavailable comparisons.
12. **Charts and legends.** Use flat bars, clear direct labels, visible values/units and comparable scales. Add a legend only when the series/category labels above or beside the bar do not already identify its colors. Distinguish category counts, average completion and budget shares; do not interchange these measures. Preserve financial source scope, valid denominators and category meaning. Financial bars use solid fills on screen and in print; remove diagonal hatching, numeric completeness markers and repeated numeric availability notes without changing calculations or replacing the removed treatment with another marker or note.
13. **Layout and spacing.** Use a consistent 4 / 8 / 12 / 16 / 24 / 32 / 48px spacing scale. Retain the widened fluid layout: 48px desktop gutters, 32px tablet gutters and 16px mobile gutters, subject to available screen width. Use 24px between main columns and 16px between stacked cards. Keep cards as tall as their content requires; avoid large empty areas and decorative status sidebars.
14. **Monthly composition.** Preserve the approved two-column monthly composition: project portfolio physically left, executive-follow-up portfolio physically right, with strategy below legislation. Remove **سيطرة · لوحة المتابعة الشهرية** from displayed branding. Remove the extra **لم يبدأ 7 / منقول 2** line in the monthly projects card. Keep the official TEC logo and approved proportions/clear space.
15. **Projects composition.** Preserve the agreed physical pairings: quarters/months left and budget right; manager follow-up left and status summary right; budget by priority/type left and project count by priority/type right. Put the full-width follow-up table below these panels. Expand priority charts to their populated rows rather than putting them inside small scrolling panes.
16. **Terminology.** Use **الأجندة المعتمدة**, **المواضيع المستجدة**, and **الموازنة المعتمدة**. Do not add **(المعدلة)** to the displayed budget title. The legislation timing labels identify SLC directly; omit the repeated SLC comparison paragraph. Remove the generic legislation-review subtitle beneath its title.
17. **Responsive behavior.** Reflow cards and controls on narrow screens while preserving readable type. Adapt tables to a readable mobile presentation; do not squeeze them into tiny text. Keep the overall page within the viewport; use deliberate table scrolling only when required for a wide data table. Priority charts expand with their visible categories.
18. **Controls and accessibility.** Use one clear primary action per task, predictable button/field states, visible selected tabs and focus, keyboard-accessible menus, explicit labels for icon buttons, text alongside status colors, and reduced-motion support. Keep drilldowns and full-report actions available without adding visual clutter or exposing internal implementation details in product flows.
19. **Print and exports.** Use the separate print scale below, preserve Arabic direction and badge identity, and keep all source content. The default continuous monthly PDF grows its custom page height and uses one header/footer; its unusually long-report fallback uses A4 portrait pages. A4 paper modes add pages and repeat table column headings instead of shrinking the report; keep individual rows together when possible. The first printed header contains the official logo and report title with its source cutoff in the same title; for the monthly report use **التقرير الشهري للأداء والتنفيذ - لتاريخ 30/09/2026**, replacing the example date with the actual cutoff. No notes, separate date line, scope line or explanatory subtitle surround this title. Later printed pages have no repeated report title, logo, date or scope masthead; relevant section headings and table column headings remain. Footers contain the exact copyright/legal line and generated page numbering only. Hide navigation, menus, filters, operational controls and the entity filter's selected-value field while preserving all selections' effect on the exported dataset. Actual entity names and source notes in table content remain. Keep template/report data rules unchanged.
20. **Title labels and subtitles.** Remove explanatory labels and subtitles beneath every page, portfolio, section, card and table title across monthly, projects, search, upload, other pages and print. Remove the repeated agenda subtitle **الأجندة المعتمدة والمواضيع المستجدة**, follow-up subtitle **البنود التي تستدعي المتابعة ضمن نطاق التقرير**, and redundant full-table label **جميع بنود المتابعة**. Keep the agenda breakdown labels **الأجندة المعتمدة** and **المواضيع المستجدة** with their values. Preserve required screen date metadata, actual notes in the **الملاحظات** column, field labels, status/value labels, counts, currency/percentage units, meaningful definitions and source caveats. Retained explanations belong beside the relevant content or in a definitions disclosure, not as title subtitles. Do not leave empty subtitle elements or their reserved spacing.
21. **Navigation and filters.** Apply the approved shared setup above: quiet text navigation, current-page underline, one app menu, grouped task actions and separate core filters. Keep scope with filters rather than in the title block. Preserve keyboard behavior, live selections and existing search/upload functions.
22. **Footer.** The screen footer contains the exact copyright/legal line only. Each output footer contains that legal line and generated **صفحة X من Y** only: once on the ordinary one-page continuous monthly PDF, and once per page in A4 output. Remove source filename, calculation date, report title, scope and extra notes from footers. Required definitions and source caveats stay in the report body, subject to the specific removal of financial numeric-availability notes.
23. **Verification and rollout.** Establish this standard on the monthly page first. Review its header, cards, controls, table and interactions at **100% browser zoom**, then inspect the actual PDF at readable size. Verify source totals, previous/current comparison keys, missing values, fonts, colors, wrapping, mobile behavior and exports before reusing the standard on projects, search, uploads and other pages. Visual polish must not change calculations or source meaning.

## Approved print header, pagination and footer

| Element | Approved printed treatment |
| --- | --- |
| First-page masthead | Official logo approximately 38mm wide and a single 24pt DIN report title including the actual cutoff date |
| Monthly title format | التقرير الشهري للأداء والتنفيذ - لتاريخ 30/09/2026; substitute the actual source-backed report date |
| Notes around the title | None above or below; no separate date/scope line or explanatory subtitle |
| Later-page masthead | None in paginated A4 output; the ordinary continuous monthly PDF has only one page/header |
| Continued content | In A4 output, relevant section titles and repeated 13.5pt Dubai Bold table column headings remain; continuous content stays on its measured page |
| Footer | Exact organisation/copyright legal line and renderer-generated صفحة X من Y only; Dubai Regular 10.5pt Ink. One footer for ordinary continuous monthly output; one per page for A4 output |
| Footer reserve | Reserve clearance within the active format: 12mm margins for continuous monthly output, 10mm for A4. Content and table rows never overlap the footer |
| Entity filter | Control, label and selected value hidden; selected scope still filters the exported records and figures |
| Report membership | Preserve all selected filters, source records and row order; hiding scope text does not reset selections |
| Explanations | Preserve actual table notes, SLC source-date fields and source/history caveats in the report body; omit generic title subtitles |
| Pagination | Continuous monthly: one measured-height page within the 5080mm limit; otherwise A4 portrait with a toast. A4: content-driven page count, fitting rows/cards kept together and readable continuation for unusually tall content |

Page numbers and totals come from the export renderer, not fixed specimen counts.
Browser-generated URL/date/title headers and footers are excluded from the final
report so that the printed footer contains only the required copyright and pages.

The legal line is **الأمانة العامة للمجلس التنفيذي لإمارة دبي · حقوق النشر © 2026 · جميع الحقوق محفوظة**.
Use the applicable copyright year without changing the organisation or legal wording.

## Compliance corrections retained from v134

- Primary hover uses Paper on Charcoal; pressed uses Paper on Ink. Filters retain Paper with Teal boundaries on hover/press. Disabled controls use Ink/Linen/Silver, without blanket dimming; labelled core multi-select fields meet the 72px minimum.
- The PowerPoint command retains its label and width while loading, shows a labelled 20px progress indicator, blocks duplicate actions and respects reduced-motion preferences. Native PowerPoint templates and business/export logic are retained.
- Native browser/PDF status charts use the approved chart palette, separate from badge colors: completed Green, late Red, active/review Taupe, ready/not-started Stone, unclassified Silver, frozen/cancelled Burgundy and transferred Teal. Non-status issuer/sector charts retain an explicit Teal accent. Stone/Silver segment labels use Charcoal; dark fills use Paper. Agenda and council numeric chart labels use DIN Next LT Arabic Regular at their established chart scales.
- HH secondary progress figures use DIN Next LT Arabic Regular, 28px on screen and 20pt in print, in a 92px ring that accommodates 100%. Completed counts and completion ratios use the approved Green. Summary panels use Paper/Sand, 18px corners and 24px desktop/16px mobile padding without decorative status stripes. The native print summary SVG follows the same font/color/surface roles, keeps status bars flat and square, and omits redundant period/filter-context subtitles. Source scales and values remain unchanged.
- Print hides task-page duplicate logos, menus, search/upload controls and checks-only filters/actions. Actual source values, sheet names, notes and counts remain.
- Source tables retain regular weight on mobile, including first-column source names/indices. Checks result/severity badges use 16px Dubai Regular on screen and 12pt in print. Plot quantities retain their established annotation sizes, with DIN Next LT Arabic Regular figures.
- Fit-sized comparison cards stay together. Record/section headings stay with their opening content; initial table headings stay with the first row. Individual source captions stay with their filename/row. Checks result/severity badges use the approved 12pt Regular table scale and wrap naturally. Oversized rows/cards continue readably, without global font shrink or a fixed page count.

## Approved output formats and A4 paper orientation

The monthly digital format and physical paper modes are separate choices. The continuous monthly PDF is the default for digital reading; it is not an A3 option and does not change the approved A4 orientation of other documents.

| Document / export | Format / orientation | Page dimensions (width × height) |
| --- | --- | --- |
| Monthly dashboard / monthly report — default digital output | Continuous custom PDF | 260mm × measured content height; 12mm margins; 236mm content width |
| Monthly dashboard / monthly report — selected paper mode or height-limit fallback | A4 portrait | 210 × 297mm |
| Annual agenda — dedicated view and agenda report | A4 landscape | 297 × 210mm |
| Council decisions — dedicated view and council report | A4 landscape | 297 × 210mm |
| HH / leadership report | A4 landscape | 297 × 210mm |
| Projects portfolio and project report | A4 portrait | 210 × 297mm |
| Entity report | A4 portrait | 210 × 297mm |
| Monthly comparison | A4 portrait | 210 × 297mm |
| Search results | A4 portrait | 210 × 297mm |
| All remaining printable pages / exports | A4 portrait | 210 × 297mm |

**Continuous monthly geometry:** 260mm custom page width, 12mm margins on every side and 236mm content width. With both portfolios present, use two 115mm columns with a 6mm gap; a single remaining portfolio takes the full content width. Projects remain physically left and executive portfolios right. The followup table spans the full width below both. Height is measured from the complete export content after fonts and images are ready, with footer clearance; do not derive it from the browser viewport or a fixed specimen.

| Continuous monthly area | Approved digital spacing |
| --- | --- |
| Portfolio column gap | 6mm |
| Card and followup-card padding | 5mm |
| Stacked card gap | 4mm |
| Space below card heading | 3mm |
| Space above metric rows and bars | 2.5mm |
| Metric horizontal padding | 2.5mm; omit the outer padding at the row's first/last edges |
| Agenda category strip | 2mm vertical / 3mm horizontal padding; 2mm vertical margin |
| Summary-to-followup section gap | 7mm |
| Table cell padding | 3mm vertical / 3mm horizontal |

**Digital height fallback:** a measured page above 5080mm switches automatically to A4 portrait for the current print session and shows an explanatory toast. Retain the selected scope, every source row/note and all values; the saved continuous/A4 preference does not change. This limit does not authorize clipping, truncation or text shrink. Below the limit, the monthly output remains one continuous page with one masthead and footer.

**Physical paper:** A4 only; A3 settings/options remain removed. Use 10mm margins on every side. Landscape provides a nominal 277 × 190mm content area; portrait provides 190 × 277mm, subject to footer clearance. These paper dimensions also apply when a continuous monthly report needs the unusually long-report fallback.

**Monthly A4 composition:** preserve two portfolio columns, projects physically left and executive portfolios physically right, with full-width followups below both. Keep its approved 4mm column gap; a single remaining portfolio occupies the full width. Financial allocation labels may wrap above their amounts within the two project columns to preserve complete numbers. The wider continuous format retains those source associations and its own 6mm gap.

Other portrait document types retain their separate single-column flow by default; reflow summary metrics into a compact grid that fits the paper width. In A4 modes, keep each fitting card/box and row together where possible, repeat table column headings and wrap Arabic naturally. If content is taller than a usable page, allow readable continuation. Add pages as needed; do not shrink the whole report, clip content or force a fixed A4 page count. In continuous monthly mode, extend page height instead. Preserve all source values, notes, table fields, units and selected filters in both formats.

The format follows the document and the monthly format selector. A project report retains A4 portrait; only agenda, council and HH have the landscape paper exception. These rules govern the browser-print/PDF workflow; they do not redefine PowerPoint slides or workbook sheet templates.

The entity report retains A4 portrait. The separate proposed entity-dashboard redesign remains a concept and is not imported into this release; its earlier concept package has no implemented PDF export.

## Approved print scale

Print uses its own approved sizes. The latest subgroup, short-label and strategy-label screen-size amendments do not automatically resize print. Keep the sizes below; use the updated text-color roles and solid financial bars in print as well. Verify the actual rendered PDF after implementation. Continuous monthly height follows the content; A4 page count follows the content.

| Element | Font | Print size |
| --- | --- | --- |
| First printed report title, including cutoff date | DIN Next Arabic Regular | 24pt |
| Portfolio headings | DIN Next Arabic Regular | 18pt |
| Card / table-section titles | DIN Next Arabic Regular | 16pt |
| Main figures | DIN Next LT Arabic Regular | 24–28pt |
| Secondary figures | DIN Next LT Arabic Regular | 20pt |
| Table column headings | Dubai Bold | 13.5pt |
| Table content, names, notes and in-table status badges | Dubai Regular | 12pt (16 CSS px) |
| Status badges outside tables | Dubai Regular | 13.5pt (18 CSS px) |
| Important labels and retained body explanations; no title subtitles | Dubai Regular | 9pt |
| Change arrows and differences | Dubai Regular | 11pt |
| Permitted metadata and copyright/page numbering | Dubai Regular | 10.5pt |
| Entity filter, label and selected-value field | Screen only | Hidden in print |

Use the selected output profile above: continuous monthly PDF with 12mm margins and measured height, or the document-specific A4 orientation with 10mm margins. A3 remains unavailable. Keep these font sizes in both profiles; do not use a fixed whole-page shrink factor. A4 pages accommodate the content with readable continuation for unusually tall rows. Continuous monthly output extends its page height, with the above A4 fallback only when the safe height limit is exceeded.

Entity selection continues to determine the exported rows and figures; hiding its printed field does not reset the selected filter. This rule does not remove entity names where they are part of the report's actual table content.

## Approved bars and data meaning

| Bar / segment | Meaning | Solid fill / code |
| --- | --- | --- |
| Subgroup completion strip | Completed count divided by the eligible subgroup total | Green #01831E on Linen #EFEBE7 |
| Completed status segment | Disjoint completed share of the card total; includes legislation completed after the deadline | Green #01831E |
| Active / pending status segment | Disjoint active or remaining-pending share of the card total | Taupe #756B5F |
| Ready status segment | Ready-for-presentation share of the card total | Stone #ABA394 |
| Late status segment | Unfinished-late share, separated from other pending items | Red #C00000 |
| Unclassified status segment | Source-unclassified share where present | Silver #C8C7C7 |
| Budget / allocation strip | Source-defined allocation share or amount, using its existing denominator/scale | Taupe #756B5F |
| Spending strip | Source-defined spending share or amount, using its existing denominator/scale | Teal #115E67 |
| Strategy measurement strip | Measured indicators divided by registered indicators | Teal #115E67 on Linen #EFEBE7 |
| Unused bar track | Remaining track behind the encoded value | Linen #EFEBE7 |

The ready-status **bar** remains Stone; its separately approved **badge** remains Teal. Do not apply badge fills to bars or change the approved chart category mapping. When the two completed-legislation cohorts share Green, retain their existing Paper separator.

### Financial bars with partial numeric coverage

Use the same solid financial fill for complete and partial numeric coverage, on screen and in print. Remove diagonal hatching, completeness marker bars and repeated financial numeric-availability notes such as **قيم متاحة: 59 من 61** or the previously proposed **بيانات جزئية · 59/61**. Do not replace them with another marker, tooltip or note. Remove the unused note spacing as well.

This is a presentation change. Bar lengths, displayed subtotals, financial ratios, eligible records and all calculations retain their existing source-defined scope. Missing or invalid source values remain excluded where the existing calculation excludes them; do not convert them to zero, estimate values or imply complete source coverage. Retain actual recorded notes, status caveats, currency/percentage units and meaningful denominator/metric definitions. The removal concerns numeric-availability annotations beside financial bars.

Project count/money bars retain the table's shared zero-to-largest-row scale. Progress bars retain valid source progress percentages. A measurement-coverage bar is not a financial completeness marker and remains with its source-backed values and definition.

## Approval and historical previews

Revision 11 is the current approved standard for **Performance App v136**. It adds the default continuous monthly digital PDF, measured page height, roomier digital spacing and an explicit continuous/A4 format choice. It retains Revision 10's paired monthly composition, 16px dashboard labels, strategy-caption removal, isolated SLC captions and approved A4 paper orientations. Search, navigation, status palettes, source text/color roles, solid financial bars and earlier compliance corrections remain approved.

**v136 browser, source and native PDF verification passes for tested workflows.** Its completed screen/mobile, continuous PDF, A4 fallback and source-regression checks are recorded in **VERIFICATION-v136.md**. **Revision 10 / Performance App v135** and **VERIFICATION-v135.md** remain historical references for the previous paired A4 release; earlier standards and verification files retain their own scope.

- [Typography colors and exact TEC palette — historical](https://github.com/ormbh/Performance-App-2/tree/4e235d208f0d7fe155de061ffeeda94ff578909b/Color-Previews)
- [Actual bundled font samples](https://github.com/ormbh/Performance-App-2/tree/4e235d208f0d7fe155de061ffeeda94ff578909b/Font-Previews)
- [Historical status badge preview](https://github.com/ormbh/Performance-App-2/tree/4e235d208f0d7fe155de061ffeeda94ff578909b/Status-Previews)
- [Approved header/navigation/print concept — historical comparison pack](https://github.com/ormbh/Performance-App-2/tree/4e235d208f0d7fe155de061ffeeda94ff578909b/Header-Print-Concept-Revision-4)
- [Compact typography, Ink table text and solid financial-bar comparisons — prior preview](https://github.com/ormbh/Performance-App-2/tree/f8da6bd/Compact-Typography-Concept)

Earlier images may show 18px screen badges, title subtitles, oversized side-by-side labels, 28px subgroup names or hatched financial bars. They do not override this document. The subgroup names in the last compact preview are superseded by the latest **18px** approval. The rejected oversized-label concept is not the approved card arrangement.

This is an app-specific approved standard, not an official TEC brand manual or accessibility certification. Source records, values, calculation definitions and filter behavior remain unchanged. Verification covers the final runtime bundles using the frozen illustrative workbook and actual Chromium screen/PDF output. Native Windows file opening, physical printer output and native Office editing were not tested. Managed Chromium blocks direct file navigation; extracted-package checks used local HTTP.
