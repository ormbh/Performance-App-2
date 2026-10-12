# Revision 16 — compact monthly filters and PDF filenames

For the monthly dashboard dropdown values, scope summary and monthly PDF header, use the first selected option's displayed name followed by **+N**, where N is the number of additional distinct visible choices. One selected choice shows its name alone. Preserve actual selection order rather than sorting the selected names by the dropdown order. If the first choice is removed, promote the next remaining choice; a removed and reselected choice goes to the end.

When all available choices are selected, show only **الكل**, with no count. An unrestricted/reset filter also shows **الكل**. Keep each field's label, such as **القطاع** and **الوحدة التنظيمية**. Apply the same format to both continuous and A4 monthly PDF output. The entity filter uses this display on screen but remains excluded from the exported header under the existing scope rule.

Treat the additional count as a display count, not a record count. Group existing source aliases as one choice; retain all exact tokens. Do not claim all-selected when a saved choice is stale or an alias group is only partially selected. Keep the full checked options accessible in the dropdown and preserve its full accessible label. Isolate **+N** for correct Arabic/Latin reading order.

This changes presentation only. Preserve the selected token arrays, unions within fields, intersections across fields, cascaded options, source records, totals, date and PDF profiles. Do not convert an explicit all-selection into an unrestricted filter. Scope formatting on other report types retains its existing behavior.

Monthly PDF filenames use **التقرير_الشهري_للأداء_Mmm_yy.pdf**, using the actual report calculation date for the English three-letter month and two-digit year (for example **Sep_26**, never the computer's download date). Add the selected unit name if its selection is partial; otherwise add a partial sector selection. Use the first selected name plus **_+N** for multiple choices. Omit the suffix for unrestricted/all-selected scope. Replace spaces and unsafe filename characters with underscores, preserve Arabic and keep the extension **.pdf**. Limit unusually long Unicode scope names while preserving the base date and additional-choice count. The visible report title and other report types' naming retain their rules.

Implementation and focused verification: **Performance App v141**, **VERIFICATION-v141.md**. Revision 15 and earlier evidence retain their historical scope.

## Retained Revision 15

### Revision 15 — conditional 2027 annotation, budget order, spending-caption removal and SLC completion changes

Below the strategic-budget project quarter cards, show only **مشاريع 2027: N** when the active filtered report scope contains a positive number of projects with a valid 2027 finish year. Otherwise omit the annotation element and its spacing. Remove **حسب سنة الانتهاء**, the 2026/other-year breakdown, separators and undated-count annotation from this line. Preserve the separate quarter reference-year label. The annotation year is specifically 2027, not an automatically advancing next-year label.

Keep the approved budget total first. Place **المنفق حسب الفواتير**, its amount and valid change, and its solid Teal #115E67 spending bar above the **المخصص / غير المخصص** row and solid Taupe #756B5F allocation bar. Remove the visible dynamic spending-percentage caption, such as **الإنفاق 31.8% من الموازنة المعتمدة**, and its empty spacing. Preserve the spending calculation, approved-budget denominator, bar length and accessible bar label.

For **SLC منجز بعد موعد**, apply the existing completion-change treatment to both the arrow and change number: a valid positive change uses Green #01831E, matching its completed main figure; a negative change retains the existing Red #C00000 treatment. Zero changes stay hidden; unavailable comparisons retain the existing screen explanation and remain omitted in PDF. The main figure remains Green, and the date-based cohorts, timing formulas and isolated SLC caption order remain unchanged.

All Revision 15 refinements apply to screen, continuous PDF and A4 PDF.

Keep scoped totals, quarter values, finish-year classification, date validation, financial values and all source eligibility rules unchanged. Existing record details and diagnostics remain available.

The v140 implementation and focused verification are recorded in **VERIFICATION-v140.md**. Previous release checks retain their historical scope.

## Retained Revision 14 — strategy tag and exported scope header

Remove the strategy card's **مؤشرات الأداء** tag on screen and in both output
formats. Keep a valid nonzero strategy total-count difference as a neutral,
unlabeled change in its card header; zero or unavailable changes stay hidden.
Do not alter the primary strategy values, denominator, measurement bar or valid
metric changes.

Restore the first-page exported report header: the official logo, a 24pt
DIN Next Arabic Regular title with the actual cutoff date, then the active
sector and organisational-unit scope line in 10.5pt Dubai Regular Ink #4F4E4E.
Use existing all-sector/all-unit labels for unrestricted selections. Omit the
entity field, label and selected value from this header; entity selections
continue to filter the exported source records and figures. Repeat neither
the title/date nor this scope line on later pages.

The primary report action remains **تنزيل PDF**, replacing the Print button throughout
the app. It saves locally through a bundled PDF engine, with no print dialog,
CDN or upload service. PDF settings retain the approved continuous/A4 choices
and the current source scope/date. The exporter preserves native text, vector
charts, approved fonts/colors, source calculations and full ordered records.
The monthly continuous page and all A4 orientations retain the Revision 12
profiles below.

The first header contains the logo, title with inline date and the restored
sector/unit scope line. Copyright and actual page counters remain the only
footer fields. Continuous footer text has at least
8mm clearance from the physical bottom edge; its fixed baseline uses an 11mm
inset inside the approved 16mm bottom reserve. Original font bytes stay intact;
the local shaper handles legacy DIN joining and mixed text direction, and a
licensed symbol-only fallback supplies missing change-arrow and Harvey progress glyphs.

Native browser print preparation uses a validated full-report measurement or
safe A4 fallback. It never publishes an unmeasured 80mm custom page. Direct PDF
export is independent of native print timing and browser margin settings.

Final v139 direct-download checks pass; results and practical
limits are recorded in **VERIFICATION-v139.md**. Historical v138 checks
remain in **VERIFICATION-v138.md** and do not establish a v139 pass. Revision
13's download action and settings wording still supersede the earlier
browser-dialog workflow; Revision 14's sector/unit metadata is the explicit
exception to the earlier no-exported-scope-line rule.

---

# TEC Apple-Inspired Design standard

Approved typography, controls, status badges, layout, header, navigation, bars and output rules. **Revision 16 — 12 October 2026; compact monthly filter summaries and scoped PDF filenames approved.** Revision 15’s conditional 2027 annotation, budget order, caption removal and SLC change colors remain approved. It retains Revision 14's strategy tag removal and first-page exported sector/unit scope, Revision 13's offline PDF download and Revision 12's full-page Linen monthly PDF, corrected insets and roomier spacing. This consolidates the supplied standard and all subsequent approved amendments, including **18px Dubai Regular subgroup names and agenda category labels**, the updated Ink/Taupe text roles and solid financial bars.

**Implementation: Performance App v141.** The default continuous monthly digital PDF uses a 297mm page width, content-measured height, an 8mm reading inset with additional bottom footer reserve, and 281mm content width. The continuous page margins are 8mm at the top and sides, and 16mm at the bottom. Linen #EFEBE7 fills the whole page, including its insets; Paper #FCFBFB cards retain their approved borders and text roles. A4 portrait remains selectable for monthly paper printing with its existing 10mm margins. Agenda, council and HH paper reports retain A4 landscape; all other paper views retain A4 portrait. A3 remains unavailable. Monthly labels, SLC captions, fonts, source scope and calculations retain their approved rules, with the Revision 15 presentation refinements above. Current-release verification and practical limits belong in **VERIFICATION-v141.md**. **VERIFICATION-v140.md** records the previous presentation refinements. **VERIFICATION-v139.md**, **VERIFICATION-v138.md**, **VERIFICATION-v137.md** and earlier files describe their historical release scopes; they do not establish a v141 pass.

The monthly page establishes the shared standard at **100% browser zoom**. Screen typography uses 38px page titles (36px on the search home), 30px portfolio headings, 28px card titles, 16px table content and badges, and 18px Dubai Bold table headings. Retain the compact card grouping: 18px subgroup names, 16px monthly status labels above their figures, and change arrows below their own values. The card-header total label retains its position beneath the main total. **Remove explanatory labels and subtitles beneath all page, portfolio, section, card and table titles**, including search and upload titles. Retain the required screen report date as secondary metadata.

Print keeps its independent approved scale: table body, names, notes and in-table badges use **12pt**; table headings and badges outside tables use **13.5pt**. Screen size amendments do not automatically enlarge print. Updated text-color roles and solid financial-bar presentation apply to screen and print, except where a component has its own specified treatment, such as status badges, controls and the print footer.

Use the supplied **Regular (400)** faces for headings, figures, body text and controls. **Table column headings use the supplied Dubai Bold (700)** face. DIN Next Arabic and DIN Next LT Arabic are distinct supplied font families.

## Latest approved amendments

**Strategic-budget project quarters:** show only **مشاريع 2027: N** below the quarter cards when the filtered valid-2027 count is positive; omit the line and its spacing otherwise. Preserve the separate quarter reference-year label, valid finish-year classification and existing quarter values.

**Budget order and spending caption:** keep the approved budget total first, followed by **المنفق حسب الفواتير**, its amount/change and solid Teal spending bar, then the **المخصص / غير المخصص** row and solid Taupe allocation bar. Remove the visible dynamic **الإنفاق … من الموازنة المعتمدة** caption while retaining the calculation, denominator and accessible bar label. Apply the order and caption removal to screen, continuous PDF and A4 PDF.

**SLC completed-after-deadline change:** use the existing completion-change treatment for the arrow and number below **SLC منجز بعد موعد**: positive Green #01831E, negative Red #C00000, zero changes hidden, with the existing unavailable-comparison handling retained. The completed main figure stays Green. Preserve timing cohorts, formulas and isolated SLC captions on screen and in both PDF formats.

**Strategy header tag:** remove **مؤشرات الأداء** from the strategy card on screen and in both output formats, including its reserved spacing. Keep a valid nonzero total-count difference as a neutral, unlabeled header change: 15px Dubai Regular Taupe #756B5F on screen, 11pt Dubai Regular Taupe in output. Hide a zero or unavailable total-count change. Preserve primary values, denominator, measurement bar and valid metric changes.

**Exported header scope:** the first-page header contains the official logo and actual-date report title at 24pt DIN Next Arabic Regular, followed by sector and organisational-unit scope in 10.5pt Dubai Regular Ink #4F4E4E. Use active source-backed selections or the existing all-sector/all-unit labels. Do not include the entity control, label or selected value; its selection still filters the exported report. The header appears only on the first page. This required scope metadata is an explicit exception to generic subtitle removal; screen headers retain their existing date-only metadata rule.

**Continuous monthly PDF:** use one custom digital page by default, with a 297mm width, 281mm content width and an 8mm reading inset plus a reserved bottom footer band. Use actual page margins of 8mm top/left/right and 16mm bottom. Fill the full page and its insets with Linen #EFEBE7, including the print page and body surfaces, so there is no white outer frame. Keep cards Paper #FCFBFB with their approved Sand borders. Measure the complete report after print fonts and images are ready; its height grows with the content. Preserve projects physically left, executive portfolios physically right and full-width followups below both. Use one report masthead and one legal/page-number footer. Keep all approved print font sizes; do not fit the document with zoom, font shrink or a fixed height.

**Continuous footer clearance:** retain the 8mm reading inset and reserve an additional 8mm at the bottom, making the actual bottom page margin 16mm. Direct PDF download uses its fixed 11mm footer-baseline inset within this reserve. Optional native printing retains top-aligned footer margin boxes with 1mm top padding. Keep copyright glyph bounds at least 8mm from the physical bottom edge and keep report content clear of the footer. Page height measurement allows 27mm beyond the complete measured content: 8mm top + 16mm bottom + 3mm rounding/clearance. This changes footer space, not source content or approved print fonts; A4 margins remain 10mm.

**Digital spacing:** use 6mm padding inside monthly cards and the followup card, an 8mm portfolio-column gap, 6mm between stacked cards, 4mm beneath card headings, 3mm above metric rows and bars, and 3.5mm table-cell padding. Give portfolio headings 6mm inline padding to align their text with the cards’ inner edge and 3mm bottom padding. Put the followup section 8mm below the report summary, leave 3mm beneath its heading, and give its status-summary row 3mm above and 4mm below. Preserve natural wrapping and the label/value/change associations. These spacings apply to the continuous digital format; screen and A4 paper spacing retain their approved profiles.

**Monthly format control:** the primary action reads **تنزيل PDF** and uses the existing 20px download glyph. Under **إعدادات PDF**, show the **تنسيق التقرير** dropdown with **PDF متصل — صفحة واحدة** and **A4 عمودي — للطباعة**. The continuous format is the default when no current format preference is saved; retain a user's selected A4 preference. Download either format directly through the bundled local PDF engine. Select A4 for a PDF intended for physical paper printing. No browser print dialog or Background graphics setting is part of the app's PDF download workflow.

**Continuous height limit:** if the measured digital page would exceed 5080mm, automatically use A4 portrait pages for that export and show an explanatory toast. Preserve every record, note, value and filter; keep the saved format preference unchanged. Do not truncate the report, clamp it to the limit or shrink text. Ordinary continuous reports remain one page; this fallback applies only to an unusually long report.

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
| Change arrows and differences | Below the corresponding value; strategy total-count difference is the unlabeled header exception | **15px** | Dubai Regular | **Taupe #756B5F**, with meaning-based performance exceptions |
| Minor metadata | Screen date, secondary detail, empty-note placeholder | **14px** | Dubai Regular | **Taupe #756B5F** |
| Financial bars with partial numeric coverage | Allocation/spending ratios and subtotals | Solid fill | Existing chart treatment | Allocation Taupe #756B5F; spending Teal #115E67 |
| Financial hatching, completeness markers and numeric availability notes | Including قيم متاحة: 59 من 61 | **Removed on screen and in print** | Not rendered | No replacement marker or note |
| Explanatory labels/subtitles beneath titles | Repeated title descriptions | Removed | Not rendered | — |

The 14px explanation scale applies to retained definitions, useful source caveats and body guidance. Keep actual notes in the table, field labels, value/status labels, units and meaningful calculation definitions. The financial numeric-availability-note removal is the specific exception described in the bar rules below; it does not remove actual recorded notes or essential metric definitions.

An empty-note placeholder is secondary metadata at 14px Taupe; actual recorded table notes remain 16px Ink. Remove the redundant **جميع بنود المتابعة** label above the full follow-up table; keep its item count, status counts and **عرض جميع البنود** action.

## Monthly card grouping and alignment

| Area | Approved arrangement |
| --- | --- |
| Card header | Card title 28px DIN Next Arabic; main total retains 40px DIN Next LT Arabic; short total label 16px Dubai Ink beneath the total. Strategy has no مؤشرات الأداء tag; any valid nonzero total-count difference remains neutral and unlabeled in its header |
| Special projects | Two subgroup blocks, with 18px Dubai subgroup names and 28px totals; retain two status columns within each subgroup |
| Agenda | Retain the approved/new-item breakdown: category labels 18px Dubai Ink with 28px figures; retain three status columns with 16px labels above 34px figures |
| Value labels | Keep 16px monthly status labels close to their values, above the numeric row; retain the header total label beneath its value; do not use the rejected oversized side-by-side labels |
| Changes | 15px metric differences directly below their own figures; align corresponding values/comparison rows. SLC completed-after-deadline changes use completion colors for arrow and number: positive Green, negative Red, unchanged/unavailable hidden. Strategy retains its valid nonzero total-count difference as a neutral unlabeled header change |
| Strategic-budget quarters | Conditional مشاريع 2027: N below the quarters only for a positive filtered valid-2027 count; preserve the separate quarter reference-year label |
| Strategic budget | Approved total first; invoice spending amount/change and solid Teal bar next; allocated/unallocated row and solid Taupe allocation bar below. Omit the visible spending-percentage caption; preserve the accessible bar label and ratio |
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
| Screen title metadata | Required cutoff date beneath the title, Dubai Regular 14px Taupe #756B5F; screen scope stays with the filter controls. Omit generic subtitles, preview notes and current-data markers; exported sector/unit metadata follows its separate first-page rule |
| Logo | Official supplied TEC asset; 192px desktop / 144px mobile report logo, preserved proportions and clear space |
| Primary navigation | Plain 16px Dubai links: البحث plus the current page only; search home has the menu only, search results have one current Search link; every other destination remains in the menu. Teal current-page underline; no filled boxes or redundant destination icons |
| Application menu | One existing 20px grid icon in a 44px control, named صفحات التطبيق; include three direct report links (agenda, council and HH) on every loaded page, including search; retain other existing destinations and eligible actions |
| Task actions | تنزيل PDF is the primary report action throughout the app, using a 20px download glyph. Optional إعدادات PDF is the secondary settings action, grouped opposite navigation on desktop. Retain the button label and width during preparation, use a labelled 20px progress indicator, expose aria-busy and block duplicate export actions |
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
| PDF settings dialog | إعدادات PDF; Paper/Sand, 18px corners; 28px DIN title with no subtitle; 16px fields / 12px field labels; 44px close target; Escape and focus restoration. Monthly تنسيق التقرير offers PDF متصل — صفحة واحدة and A4 عمودي — للطباعة |
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
| Download report PDF | Download | 20px beside تنزيل PDF; no Print action button in the app |
| PDF settings | Chevron | 20px beside إعدادات PDF |
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
7. **Completion and lateness.** Late unfinished work is always red. Completed legislation is green for both completion within the deadline and completion after the deadline; completion after the deadline does not become unfinished-late work. For **SLC منجز بعد موعد**, the source-backed change arrow and number use the existing completion treatment: positive Green #01831E, negative Red #C00000, with zero and unavailable changes hidden. Its main figure remains Green in every case.
8. **Legislation composition.** Place late legislation beside the other statuses and include it in the bar. Split pending items into late and remaining pending so each item appears once. Use the generated captions **SLC منجز ضمن موعد** and **SLC منجز بعد موعد**, isolating the Latin SLC run in Arabic layout. Remove the repeated **مقارنة: تاريخ الإنجاز الفعلي بالموعد المعتمد لدى SLC** paragraph on screen and in print. The applicable SLC date fields, actual source notes and timing calculations remain unchanged.
9. **Follow-up tables.** Show only items requiring follow-up. For projects, include unfinished overdue projects with a valid deadline, frozen, cancelled and transferred items, with or without comments. Keep the group order **late → frozen → cancelled → transferred**, and stable source order within each group. Names remain neutral and regular. Preserve the agreed columns and omit the removed delay-reason column.
10. **Zero and missing values.** Show true zero counts and zero table values as **–**. Hide empty status and H/M/L groups. Keep meaningful chart-axis zero baselines and source-backed 0% completion captions where required. Missing or invalid values remain distinct from true zero; use **غير متاح** where a dash would be ambiguous. Do not turn missing financial/progress data into zero.
11. **Progression arrows.** Use source-backed comparisons only. Put 15px metric arrows/differences directly below their corresponding value, on aligned baselines, reserving a single 24px comparison line where needed. The strategy total-count difference is the approved exception: keep a valid nonzero difference neutral and unlabeled in the card header after removing its مؤشرات الأداء tag. ↑ means a numeric increase and ↓ a decrease. Green/red describes whether the change is favorable/adverse; use Taupe #756B5F for neutral changes such as a total or spend increase without an agreed performance meaning. A decline in late items is favorable; an increase is adverse. Hide unchanged or unavailable comparisons.
12. **Charts and legends.** Use flat bars, clear direct labels, visible values/units and comparable scales. Add a legend only when the series/category labels above or beside the bar do not already identify its colors. Distinguish category counts, average completion and budget shares; do not interchange these measures. Preserve financial source scope, valid denominators and category meaning. Financial bars use solid fills on screen and in print; remove diagonal hatching, numeric completeness markers and repeated numeric availability notes without changing calculations or replacing the removed treatment with another marker or note.
13. **Layout and spacing.** Use a consistent 4 / 8 / 12 / 16 / 24 / 32 / 48px spacing scale. Retain the widened fluid layout: 48px desktop gutters, 32px tablet gutters and 16px mobile gutters, subject to available screen width. Use 24px between main columns and 16px between stacked cards. Keep cards as tall as their content requires; avoid large empty areas and decorative status sidebars.
14. **Monthly composition.** Preserve the approved two-column monthly composition: project portfolio physically left, executive-follow-up portfolio physically right, with strategy below legislation. Remove **سيطرة · لوحة المتابعة الشهرية** from displayed branding. Remove the extra **لم يبدأ 7 / منقول 2** line in the monthly projects card. Keep the official TEC logo and approved proportions/clear space.
15. **Projects composition.** Preserve the agreed physical pairings: quarters/months left and budget right; manager follow-up left and status summary right; budget by priority/type left and project count by priority/type right. Put the full-width follow-up table below these panels. Expand priority charts to their populated rows rather than putting them inside small scrolling panes.
16. **Terminology.** Use **الأجندة المعتمدة**, **المواضيع المستجدة**, and **الموازنة المعتمدة**. Do not add **(المعدلة)** to the displayed budget title. The legislation timing labels identify SLC directly; omit the repeated SLC comparison paragraph. Remove the generic legislation-review subtitle beneath its title.
17. **Responsive behavior.** Reflow cards and controls on narrow screens while preserving readable type. Adapt tables to a readable mobile presentation; do not squeeze them into tiny text. Keep the overall page within the viewport; use deliberate table scrolling only when required for a wide data table. Priority charts expand with their visible categories.
18. **Controls and accessibility.** Use one clear primary action per task, predictable button/field states, visible selected tabs and focus, keyboard-accessible menus, explicit labels for icon buttons, text alongside status colors, and reduced-motion support. Keep drilldowns and full-report actions available without adding visual clutter or exposing internal implementation details in product flows.
19. **Print and exports.** Use the separate print scale below, preserve Arabic direction and badge identity, and keep all source content. The default continuous monthly PDF grows its custom page height and uses one header/footer; its unusually long-report fallback uses A4 portrait pages. A4 paper modes add pages and repeat table column headings instead of shrinking the report; keep individual rows together when possible. The first printed header contains the official logo and report title with its source cutoff in the same title; for the monthly report use **التقرير الشهري للأداء والتنفيذ - لتاريخ 30/09/2026**, replacing the example date with the actual cutoff. Place the sector and organisational-unit scope line below this title, at 10.5pt Dubai Regular Ink. Use the active source-backed selections or the existing unrestricted labels. No entity field/value, notes, separate date line or generic explanatory subtitle surround it. Later printed pages have no repeated report title, logo, date or scope masthead; relevant section headings and table column headings remain. Footers contain the exact copyright/legal line and generated page numbering only. Hide navigation, menus, filters, operational controls and the entity filter's selected-value field while preserving all selections' effect on the exported dataset. Actual entity names and source notes in table content remain. Keep template/report data rules unchanged.
20. **Title labels and subtitles.** Remove explanatory labels and subtitles beneath every page, portfolio, section, card and table title across monthly, projects, search, upload, other pages and print. Remove the repeated agenda subtitle **الأجندة المعتمدة والمواضيع المستجدة**, follow-up subtitle **البنود التي تستدعي المتابعة ضمن نطاق التقرير**, and redundant full-table label **جميع بنود المتابعة**. Keep the agenda breakdown labels **الأجندة المعتمدة** and **المواضيع المستجدة** with their values. Preserve required screen date metadata, the explicitly restored first-page exported sector/unit scope metadata, actual notes in the **الملاحظات** column, field labels, status/value labels, counts, currency/percentage units, meaningful definitions and source caveats. Remove the strategy **مؤشرات الأداء** tag while retaining any valid nonzero total-count difference as a neutral unlabeled header change. Retained explanations belong beside the relevant content or in a definitions disclosure, not as title subtitles. Do not leave empty subtitle elements or their reserved spacing.
21. **Navigation and filters.** Apply the approved shared setup above: quiet text navigation, current-page underline, one app menu, grouped task actions and separate core filters. On screen, keep scope with filters rather than in the title block. In exports, restore only the approved first-page sector/unit scope line beneath the actual-date title; entity selection remains omitted from this header while still filtering the dataset. Preserve keyboard behavior, live selections and existing search/upload functions.
22. **Footer.** The screen footer contains the exact copyright/legal line only. Each output footer contains that legal line and generated **صفحة X من Y** only: once on the ordinary one-page continuous monthly PDF, and once per page in A4 output. Remove source filename, calculation date, report title, scope and extra notes from footers. Required definitions and source caveats stay in the report body, subject to the specific removal of financial numeric-availability notes.
23. **Verification and rollout.** Establish this standard on the monthly page first. Review its header, cards, controls, table and interactions at **100% browser zoom**, then inspect the actual PDF at readable size. Verify source totals, previous/current comparison keys, missing values, fonts, colors, wrapping, mobile behavior and exports before reusing the standard on projects, search, uploads and other pages. Visual polish must not change calculations or source meaning.

## Approved print header, pagination and footer

| Element | Approved printed treatment |
| --- | --- |
| First-page masthead | Official logo approximately 38mm wide, a single 24pt DIN Next Arabic Regular report title including the actual cutoff date, and the restored sector/unit scope line below |
| Monthly title format | التقرير الشهري للأداء والتنفيذ - لتاريخ 30/09/2026; substitute the actual source-backed report date |
| Sector / organisational-unit scope | Below the first-page actual-date title; 10.5pt Dubai Regular Ink #4F4E4E. Active selections or existing unrestricted labels; no entity field/value |
| Notes around the title | No generic explanatory subtitle, separate date line or source note. The required sector/unit scope metadata is retained |
| Later-page masthead | None in paginated A4 output; the ordinary continuous monthly PDF has only one page/header |
| Continued content | In A4 output, relevant section titles and repeated 13.5pt Dubai Bold table column headings remain; continuous content stays on its measured page |
| Footer | Exact organisation/copyright legal line and renderer-generated صفحة X من Y only; Dubai Regular 10.5pt Ink. One footer for ordinary continuous monthly output; one per page for A4 output |
| Footer reserve | Continuous monthly: 8mm top/side page margins, 16mm bottom including an additional 8mm footer reserve. A4 retains 10mm margins. Content and table rows never overlap the footer |
| Continuous footer alignment | Direct PDF: fixed baseline with 11mm bottom inset inside the 16mm reserve. Optional native print: top-aligned margin boxes with 1mm top padding. Copyright glyph bounds remain at least 8mm above the physical bottom edge |
| Entity filter | Control, label and selected value hidden; selected scope still filters the exported records and figures |
| Report membership | Preserve all selected filters, source records and row order. Sector/unit text follows the exported scope; omitting the entity field/value does not reset its selection |
| Explanations | Preserve actual table notes, SLC source-date fields and source/history caveats in the report body; omit generic title subtitles |
| Pagination | Continuous monthly: one measured-height page within the 5080mm limit; otherwise A4 portrait with a toast. A4: content-driven page count, fitting rows/cards kept together and readable continuation for unusually tall content |

Page numbers and totals come from the export renderer, not fixed specimen counts.
Direct PDF download writes only the approved header/footer and actual page
counters, independently of browser print settings. For optional native browser
printing, exclude its URL/date/title headers and footers so the report footer
contains only the required copyright and pages.

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
| Monthly dashboard / monthly report — default digital output | Continuous custom PDF | 297mm × measured total height; 281mm content width; 8mm top/side page margins and 16mm bottom |
| Monthly dashboard / monthly report — selected paper mode or height-limit fallback | A4 portrait | 210 × 297mm |
| Annual agenda — dedicated view and agenda report | A4 landscape | 297 × 210mm |
| Council decisions — dedicated view and council report | A4 landscape | 297 × 210mm |
| HH / leadership report | A4 landscape | 297 × 210mm |
| Projects portfolio and project report | A4 portrait | 210 × 297mm |
| Entity report | A4 portrait | 210 × 297mm |
| Monthly comparison | A4 portrait | 210 × 297mm |
| Search results | A4 portrait | 210 × 297mm |
| All remaining printable pages / exports | A4 portrait | 210 × 297mm |

**Continuous monthly geometry:** 297mm custom page width and 281mm content width. Keep an 8mm reading inset plus the additional bottom footer reserve; actual page margins are 8mm top/left/right and 16mm bottom. With both portfolios present, use two 136.5mm columns with an 8mm gap; a single remaining portfolio takes the full content width. Projects remain physically left and executive portfolios right. The followup table spans the full width below both. Height is measured from the complete export content after fonts and images are ready, adding 27mm for the 8mm top margin, 16mm bottom margin and 3mm rounding/clearance. Do not derive it from the browser viewport or a fixed specimen.

**Full-page surface:** Linen #EFEBE7 fills the entire continuous page, including the print page's insets and the matching body/content surfaces. Remove the white outer frame while keeping the 8mm reading inset and the additional bottom footer reserve. Cards and the followup table remain Paper #FCFBFB with the approved Sand boundaries; all text, status, figure and font roles are unchanged. The bundled PDF renderer must preserve this full-page background without requiring browser printer settings. This full-page surface is a continuous monthly rule; selectable A4 paper modes keep their existing presentation and 10mm margins.

| Continuous monthly area | Approved digital spacing |
| --- | --- |
| Page margins / reading inset | 8mm top/left/right; 16mm bottom including an additional 8mm footer reserve |
| Footer placement | Direct PDF baseline: 11mm bottom inset within the 16mm reserve. Optional native-print margin boxes: top-aligned with 1mm top padding. Glyph clearance at least 8mm from the physical bottom |
| Added page-height allowance | 27mm: 8mm top + 16mm bottom + 3mm rounding/clearance |
| Portfolio column gap | 8mm |
| Portfolio heading padding | 6mm inline, aligned with card content; 3mm bottom |
| Card and followup-card padding | 6mm |
| Stacked card gap | 6mm |
| Space below card heading | 4mm |
| Space above metric rows and bars | 3mm |
| Metric horizontal padding | 2.5mm; omit the outer padding at the row's first/last edges |
| Agenda category strip | 2mm vertical / 3mm horizontal padding; 2mm vertical margin |
| Report-summary-to-followup section gap | 8mm |
| Space below followup heading | 3mm |
| Followup status-summary row | 3mm above / 4mm below |
| Table cell padding | 3.5mm vertical / 3.5mm horizontal |

**Digital height fallback:** a measured page above 5080mm switches automatically to A4 portrait for the current export and shows an explanatory toast. Retain the selected scope, every source row/note and all values; the saved continuous/A4 preference does not change. This limit does not authorize clipping, truncation or text shrink. Below the limit, the monthly output remains one continuous page with one masthead and footer.

**Physical paper:** A4 only; A3 settings/options remain removed. Use 10mm margins on every side. Landscape provides a nominal 277 × 190mm content area; portrait provides 190 × 277mm, subject to footer clearance. These paper dimensions also apply when a continuous monthly report needs the unusually long-report fallback.

**Monthly A4 composition:** preserve two portfolio columns, projects physically left and executive portfolios physically right, with full-width followups below both. Keep its approved 4mm column gap; a single remaining portfolio occupies the full width. Financial allocation labels may wrap above their amounts within the two project columns to preserve complete numbers. The wider continuous format retains those source associations and its own 8mm gap.

Other portrait document types retain their separate single-column flow by default; reflow summary metrics into a compact grid that fits the paper width. In A4 modes, keep each fitting card/box and row together where possible, repeat table column headings and wrap Arabic naturally. If content is taller than a usable page, allow readable continuation. Add pages as needed; do not shrink the whole report, clip content or force a fixed A4 page count. In continuous monthly mode, extend page height instead. Preserve all source values, notes, table fields, units and selected filters in both formats.

The format follows the document and the monthly format selector. A project report retains A4 portrait; only agenda, council and HH have the landscape paper exception. These rules govern direct PDF downloads and optional native browser printing; they do not redefine PowerPoint slides or workbook sheet templates.

The entity report retains A4 portrait. The separate proposed entity-dashboard redesign remains a concept and is not imported into this release; its earlier concept package has no implemented PDF export.

## Approved print scale

Print uses its own approved sizes. The latest subgroup, short-label and strategy-label screen-size amendments do not automatically resize print. Keep the sizes below; use the updated text-color roles and solid financial bars in print as well. Verify the actual rendered PDF after implementation. Continuous monthly height follows the content; A4 page count follows the content.

| Element | Font | Print size |
| --- | --- | --- |
| First printed report title, including cutoff date | DIN Next Arabic Regular | 24pt |
| First-page sector / organisational-unit scope | Dubai Regular, Ink #4F4E4E | 10.5pt |
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

Use the selected output profile above: continuous monthly PDF with an 8mm Linen-filled reading inset, 16mm bottom page margin and measured height, or the document-specific A4 orientation with 10mm margins. A3 remains unavailable. Keep these font sizes in both profiles; do not use a fixed whole-page shrink factor. A4 pages accommodate the content with readable continuation for unusually tall rows. Continuous monthly output extends its page height, with the above A4 fallback only when the safe height limit is exceeded.

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

In the strategic-budget card, retain the approved budget total first. Show **المنفق حسب الفواتير**, its amount and valid change, and the solid Teal spending bar next. Place the **المخصص / غير المخصص** row and solid Taupe allocation bar below that spending block. Remove the visible dynamic **الإنفاق … من الموازنة المعتمدة** percentage caption and its spacing; preserve its calculation, approved-budget denominator and the spending bar's accessible label. This arrangement applies to screen, continuous PDF and A4 PDF.

Use the same solid financial fill for complete and partial numeric coverage, on screen and in print. Remove diagonal hatching, completeness marker bars and repeated financial numeric-availability notes such as **قيم متاحة: 59 من 61** or the previously proposed **بيانات جزئية · 59/61**. Do not replace them with another marker, tooltip or note. Remove the unused note spacing as well.

These are presentation changes. Bar lengths, displayed subtotals, financial ratios, eligible records and all calculations retain their existing source-defined scope. Missing or invalid source values remain excluded where the existing calculation excludes them; do not convert them to zero, estimate values or imply complete source coverage. Retain actual recorded notes, status caveats, currency/percentage units and meaningful denominator/metric definitions, subject to the specific visible spending-caption removal above. Numeric-availability annotations beside financial bars remain removed.

Project count/money bars retain the table's shared zero-to-largest-row scale. Progress bars retain valid source progress percentages. A measurement-coverage bar is not a financial completeness marker and remains with its source-backed values and definition.

## Approval and historical previews

Revision 15 is the current approved standard for **Performance App v140**. Its conditional 2027 annotation, spending-above-allocation order, visible spending-caption removal and completed-after-deadline SLC change colors apply to screen, continuous PDF and A4 PDF. It retains Revision 14's removal of the strategy **مؤشرات الأداء** tag and restored sector/unit scope beneath the first-page actual-date exported title; a valid nonzero strategy total-count difference remains neutral and unlabeled in the card header. Entity selection remains omitted from the header and continues to filter data. Revision 13's **تنزيل PDF** and **إعدادات PDF** actions, bundled offline engine, native text, vector charts, fonts, colors and source scope remain approved. It retains Revision 12's 297mm continuous page, 8mm Linen-filled reading inset, bottom footer reserve and roomier spacing. Revision 11's measured-height output, continuous/A4 choice and height-limit fallback remain approved, as do Revision 10's paired composition, 16px dashboard labels, strategy-caption removal, isolated SLC captions and A4 paper orientations. Search, navigation, status palettes, source text/color roles, solid financial bars and earlier compliance corrections remain approved. Current-release outcomes and limits belong in **VERIFICATION-v140.md**; earlier checks retain their historical scope.

Final v139 direct-download checks pass; results and practical limits are recorded in **VERIFICATION-v139.md**. Historical **Revision 13 / Performance App v138** offline-download and corrected optional native-print evidence remains in **VERIFICATION-v138.md**. **Revision 12 / Performance App v137** screen/mobile, settled continuous PDF, selected A4, height-limit fallback and source-regression checks remain in **VERIFICATION-v137.md**; those settled-output checks missed the native first-preview timing defect. No historical pass establishes a v139 result. **Revision 11 / Performance App v136** and **VERIFICATION-v136.md** retain the previous continuous-format approval and evidence; **Revision 10 / Performance App v135** and **VERIFICATION-v135.md** remain historical references for paired A4 output. Earlier standards and verification files retain their own scope.

- [Typography colors and exact TEC palette — historical](https://github.com/ormbh/Performance-App-2/tree/4e235d208f0d7fe155de061ffeeda94ff578909b/Color-Previews)
- [Actual bundled font samples](https://github.com/ormbh/Performance-App-2/tree/4e235d208f0d7fe155de061ffeeda94ff578909b/Font-Previews)
- [Historical status badge preview](https://github.com/ormbh/Performance-App-2/tree/4e235d208f0d7fe155de061ffeeda94ff578909b/Status-Previews)
- [Approved header/navigation/print concept — historical comparison pack](https://github.com/ormbh/Performance-App-2/tree/4e235d208f0d7fe155de061ffeeda94ff578909b/Header-Print-Concept-Revision-4)
- [Compact typography, Ink table text and solid financial-bar comparisons — prior preview](https://github.com/ormbh/Performance-App-2/tree/f8da6bd/Compact-Typography-Concept)

Earlier images may show 18px screen badges, title subtitles, oversized side-by-side labels, 28px subgroup names or hatched financial bars. They do not override this document. The subgroup names in the last compact preview are superseded by the latest **18px** approval. The rejected oversized-label concept is not the approved card arrangement.

This is an app-specific approved standard, not an official TEC brand manual or accessibility certification. Source records, values, calculation definitions and filter behavior remain unchanged. Historical Revision 15 verification covers the v140 runtime bundles using the frozen illustrative workbook, the conditional valid-2027 annotation and retained quarter reference-year label, budget block order, removed visible spending caption with retained calculation/accessibility label, and SLC completion-change colors on screen and in actual continuous/A4 PDF downloads. Retained exported scope/title treatment, strategy tag removal and count changes, and the optional native-print path keep their approved rules. Revision 15 results are in **VERIFICATION-v140.md**; current compact-filter results belong in **VERIFICATION-v141.md**. Native Windows file opening, physical printer output and native Office editing remain outside these browser/PDF checks. Prior extracted-package checks used local HTTP because managed Chromium blocks direct file navigation.

The exported organizational scope line is limited to views with sector/unit filtering. Entity and data-check views retain their own scope models and do not inherit dashboard selections. Search drill scope and search facets both remain in effect.
