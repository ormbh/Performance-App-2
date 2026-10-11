# TEC Apple-Inspired Design — shared workspace standard

**Revision 3 proposal — 11 October 2026.** Prepared for review of filters, menus,
printing, buttons, icons, headers and footers. Revision 2's approved typography,
exact palette, status badges, data meanings and dashboard composition remain the
baseline. The new arrangements and interaction details below are proposals,
not an assertion that the released v129 app has changed.

[Approved Revision 2, retained in full](../Workspace-Standard-Preview/Approved-Standard-Revision-2.md).
[Before/after gallery](../Workspace-Standard-Preview/index.html). All public examples use illustrative data.
The supplied operational PDF is a read-only diagnostic reference, not a source
for public specimen records or an instruction to change calculations.

## 1. Current → proposed setup

| Area | Current v129 / supplied PDF | Proposed common standard |
| --- | --- | --- |
| Report header | Monthly and projects have different navigation/action rows; actual logos at 1440px are 205px and 220px respectively. | One report masthead and navigation grammar: title/date/scope, official logo, three primary destinations and one app menu. Preserve the Google search-home exception. |
| Core filters | Monthly shows three scope fields; projects hides all eight behind its filter disclosure. | Show sector/unit/entity on report pages where applicable. Place only the five project-specific fields under «المزيد من التصفية». |
| Field states | Labels 12px/values 16px already match; a generic button hover makes some fields Mist. | Field hover always stays Paper with a Teal boundary. Keep action-button hover separate from field hover. |
| Popup geometry | Native checkbox filtering and dismissal already work; some close/bulk controls are 34px; surfaces include unapproved white variants. | Paper popups with consistent placement,16px options,44px targets,12px outer corners and one open popup. Retain source-backed live selections. |
| Buttons and icons | Core buttons are mostly 44px, but some menu controls are smaller; action icons vary15–18px, search uses 20px. | Apply the approved minimum 44px target and existing 20px icon family to every action, not only the common button class. |
| Printing controls | Different action names and settings treatments. Monthly dialog title 24px/close 36px; projects 28px/close 44px. | «طباعة التقرير» primary button + named «إعدادات الطباعة» secondary button with an existing chevron. Shared 28px dialog title and 44px close control. |
| Continuation pages | Supplied PDF page2 has no report context; pages3–5 repeat a full 24pt title inside the table header. | Full first-page masthead, then compact report context on every later page before the section/table heading. |
| Print labels | Some supplied PDF labels7.5–8.5pt; quarter figures 18pt despite approved 20pt secondary role. | Enforce the approved effective sizes: support≥9pt, metadata 10.5pt, secondary figures 20pt and table text 13.5pt. |
| Screen footer | File/date metadata visible on projects, hidden on monthly. | Source file + calculation date + legal line consistently visible when a source exists; legal line only before upload. |
| Print footer | Legal text is already 10.5pt; page numbering/document context absent. | Context, cutoff and generated page X of Y, plus the legal line, all 10.5pt. Reserve a footer area; source filename stays screen-only. |
| Definitions | Different small triangle/disclosure treatments. | One labelled 44px disclosure with 20px chevron; exact source definitions and 14px Ink explanation text. |

The supplied PDF has **five A4 landscape pages**. That is not itself an error:
longer source names and notes require more pages. A three-page component specimen
in the gallery is not a proposed complete three-page export of that report.

## 2. Retained fonts and colors

| Role | Screen | Print | Font | Text color |
| --- | --- | --- | --- | --- |
| First-page title |38px|24pt|DIN Next Arabic Regular|Charcoal #333333|
| Portfolio title |30px|18pt|DIN Next Arabic Regular|Charcoal|
| Card/section/dialog title |28px|16pt for report sections|DIN Next Arabic Regular|Charcoal|
| Main figure |34–40px|24–28pt|DIN Next LT Arabic Regular|Charcoal, defined status exceptions|
| Secondary figure |28px|20pt|DIN Next LT Arabic Regular|Charcoal, defined status exceptions|
| Table headings |18px|13.5pt|Dubai Bold|Ink #4F4E4E|
| Table names/notes/body |16px|13.5pt|Dubai Regular|Taupe #756B5F on Paper|
| Control/menu/option text |16px|Hidden|Dubai Regular|Ink or Teal by role|
| Field label |12px|Hidden|Dubai Regular|Taupe on Paper|
| Supporting explanation |14px|9pt|Dubai Regular|Taupe on Paper; Ink for the shared help area|
| Metadata/footer |14px|10.5pt|Dubai Regular|Ink|
| Source change |15px|11pt|Dubai Regular|Ink; existing favorable/adverse exceptions|
| Status badge |18px|13.5pt|Dubai Regular|Existing approved status mapping|
| Compact continuation heading |Not a screen title|16pt|DIN Next Arabic Regular|Charcoal|
| Continuation date/scope/context |Not a screen control|10.5pt|Dubai Regular|Ink|

Use supplied Regular 400 faces. Only table column headings use supplied Dubai
Bold 700. Names stay neutral and regular. Preserve all Revision 2 status colors,
including Green #01831E for completed legislation after its deadline and
Red #C00000 for unfinished late work. Scope chips and navigation are not statuses.

| Surface/control token | Exact color | Usage |
| --- | --- | --- |
| Linen | #EFEBE7|Report page, footer, disabled fill|
| Paper | #FCFBFB|Fields, cards, popups, search surface, light button text|
| Sand | #E7E0D3|Quiet grouping, structural boundaries, secondary pressed|
| Mist | #D9E1E2|Action/menu hover where defined; never filter-field hover fill|
| Taupe | #756B5F|Active field boundary; neutral body text on Paper|
| Teal | #115E67|Action/focus/selection; no recoloring of neutral item names|
| Ink | #4F4E4E|Control values, metadata, help and footer text|
| Silver | #C8C7C7|Disabled boundary, nonessential dividers|
| Charcoal | #333333|Titles and primary-action hover|
| Burgundy | #651D32|Genuine destructive controls and validation; existing status use retained|

No new tints, gradients, blur, icon colors or decorative status sidebars.

## 3. Shared header and navigation

| Setting | Proposed rule |
| --- | --- |
| First row, reports | Title block physically left, TEC logo physically right. Title 38px; source-backed cutoff/scope 14px Ink; official logo 192px wide on desktop, proportions intact. |
| Logo clear space |24px from surrounding desktop elements;16px mobile. This is a layout proposal, not an official brand clearance declaration. |
| Navigation row | Three primary destinations: «البحث», «اللوحة الشهرية», «محفظة المشاريع». Keep navigation separate from report actions. |
| Current destination | Paper/Teal with 2px Teal marker; expose current page. Inactive tab retains approved Sand/Ink treatment. |
| App menu | One named44×44 grid control. Retain entity reports, monthly comparison, reports, upload/change file and data notes in clear groups. Preserve existing destinations and eligible actions. |
| Source context | «البيانات الحالية» and a quiet context marker; this is not a success/status badge. Metadata and detailed filename remain in the footer. |
| Screen gutters |48px desktop≥1024;32px tablet600–1023;16px mobile<600. Header, content and footer share the same edges. |
| Spacing | Approved4/8/12/16/24/32/48 scale;24px between rows,8px between icons/text, no unnecessary blank header bands. |
| Mobile | Logo 144px, title 38px wrapping naturally; navigation reflows or scrolls inside its own labelled region. Preserve 44px controls and 16px labels. |
| Search home exception | Keep centered TEC logo 230px desktop/200px mobile, title 38px, approved680×64px pill and two actions. Shared top navigation and footer adapt without adding a second masthead/logo. |
| Search results | Compact official logo and query field remain; shared app-menu behavior and footer apply. Preserve category tabs and all search functions. |
| Page-specific source scope | Preserve existing state. Consistent controls do not automatically synchronize unrelated page filters or replace selections on navigation. |

## 4. Filters and scope toolbar

| Element | Font/colors | Geometry | Required behavior |
| --- | --- | --- | --- |
| Three core fields | Label 12px Taupe; value 16px Ink; Paper/Taupe boundary | Two-line minimum 72px;8px vertical/12px horizontal padding;4px label/value gap;8px corners; natural expansion | Physical RTL order: sector → unit → entity, where applicable. |
| Unrestricted value |16px Ink|Same field|«جميع القطاعات», «جميع الوحدات», «جميع الجهات» consistently. Empty selection means unrestricted, not no results. |
| Selected value |16px Ink|Natural wrapping|Single selection shows its name; multiple selections show alias-aware group count. Full names remain available. |
| Scope summary |14px Ink|One concise line, wraps as needed|«نطاق التقرير الكامل» or selected scope. Stay visible when extras close. |
| Additional project filters |16px control text|Three columns desktop/two tablet/one mobile,16px gaps|Only type, priority, completion quarter, status and manager. «المزيد من التصفية» identifies how many additional groups are active. |
| Selection chips |16px Ink, Paper/Taupe|8px corners; every removal 44px target|Only active constraints; descriptive remove names. For many selections use a named full-list disclosure. No tiny removable x. |
| Reset |16px Teal text action|44px minimum|«مسح التصفية» clears filter fields only; retains workbook, cutoff, notes, comparison and print/display preferences. This is a proposed dedicated reset behavior: the current project defaults reset is broader. |
| Option search |16px Ink,12px label if shown|44px minimum|Filters visible options only; never discards hidden selected values. |
| Option row |16px Ink,Paper|44px minimum with native labelled checkbox|Live update; OR within a field, AND across fields. Keep focus and list scroll stable. |
| Bulk controls |16px Teal|44px minimum each|«تحديد الكل» / «مسح التحديد» retain existing documented option scope; do not silently redefine them as search-visible-only. |
| Field hover |Ink/Paper/Teal boundary|Same geometry|Paper stays Paper; never inherits a generic button's Mist hover. |
| No options/no matches |14px Ink|Natural content height|Distinguish no available source values from no option-search matches. Provide a clear close/reset route. |

Selections are live: do not add an unnecessary Apply step. Closing or collapsing
retains selections. Mobile «تم» dismisses the sheet; it does not commit or roll
back a separate draft. Preserve existing dependent-sector/unit validation and
announce invalidated unit selections. Never merge aliases, invent options or
change source records through presentation.

## 5. Menus, popups and disclosures

| Type | Proposed appearance | Interaction and semantics |
| --- | --- | --- |
| App navigation |Paper/Sand border,12px corners,8px inside padding;320px preferred width|Real links/current destination. If menu roles are used, provide full menu keyboard behavior. Keep new-tab/modified-click support. |
| Command menu |Same shell;16px Ink options;20px icons;44px rows|Enter/Space open; Up/Down and Home/End move; Escape closes and returns focus. Inputs do not belong in a command menu. |
| Checkbox filter popup |Paper/Taupe border,12px corners;320–400px preferred width; viewport clamp|A labelled group of native checkboxes, search and selection commands. Do not label checkboxes as menu items. |
| Popup list |One scrollable options area; header/search/bulk/close remain visible|Limit to available viewport height; opening must not clip controls at the bottom. |
| Additional filter section |Paper/Sand,18px panel corners when a panel is needed|Real disclosure with expanded state; closing never clears filters. |
| Definitions |16px named disclosure,20px directional chevron,44px target; body 14px Ink|Enter/Space toggle; exact source definitions and caveats preserved. |
| Mobile filter sheet |Paper,18px upper corners,16px padding, readable control sizes|Semantic modal; focus contained, background inert, close/«تم»/Escape return to trigger. No tiny desktop popup squeezed to phone width. |
| Print settings dialog |Paper/Sand,18px corners;28px DIN heading;16px fields;12px field labels|Shared layout and semantic dialog.44px close x; Escape and focus restoration. Preserve source cutoff versus printed-date meanings. |

Only one nonmodal popup is open at a time. Outside pointer dismissal must allow
the newly clicked control to receive focus; do not force focus back after every
outside click. Keyboard dismissal returns focus to the trigger. Opening a modal
closes popups. Dialogs and anchored menus have different focus rules.

Existing outside/Escape dismissal already passes in v129; standardization must
preserve that working behavior. New proposal demos are not certification of the
released app or a completed screen-reader review.

## 6. Buttons, states and icons

| Component | Text/fill/border | Size and role |
| --- | --- | --- |
| Primary |Paper/Teal/Teal|Dubai 16px; minimum 44px;16px horizontal padding;8px corners/gap. One main action per task. Report action: «طباعة التقرير». |
| Secondary |Teal/Paper/Teal|Same geometry. Report settings: «إعدادات الطباعة» + existing chevron. Other examples: «عرض جميع النتائج», «المزيد من التصفية». |
| Text action |Teal/transparent/no box|Dubai 16px;44px target; underline on hover/focus. Reset is not destructive. |
| Icon-only |Ink/Paper/Taupe|44×44 minimum hit area;20px existing SVG;8px corners; accessible name required. |
| Genuine destructive |Paper/Burgundy/Burgundy|Only existing genuine destructive actions. Never use for reset, closing or menu dismissal. |
| Disabled |Ink/Linen/Silver|Actually disabled; no opacity fade or active hover; preserve readable labels. |
| Loading |Retains the action recipe|Stable width/label, progress indicator and duplicate prevention. |

| State | Consistent treatment |
| --- | --- |
| Primary/destructive hover |Paper on Charcoal #333333, matching border|
| Primary/destructive pressed |Paper on Ink #4F4E4E, matching border|
| Secondary/icon hover |Mist #D9E1E2, role foreground/border retained|
| Secondary pressed |Sand #E7E0D3, Teal text/border|
| Icon pressed |Sand, Ink icon/Taupe boundary|
| Field hover |Paper surface, Teal boundary|
| Keyboard focus |One 2px Teal ring with 2px gap; normal component colors retained|
| Validation |Burgundy boundary and concise Burgundy text on Paper; input retained|
| Informational status |Existing approved badge appearance, no action hover or loading|

| Icon purpose | Existing glyph | Shared size/label |
| --- | --- | --- |
| Application destinations |Grid|20px; «صفحات التطبيق»|
| Report print |Printer|20px with «طباعة التقرير»|
| Print settings |Existing chevron|20px beside visible «إعدادات الطباعة»; no invented settings icon|
| Open/close filter or disclosure |Chevron down/up|20px, expanded state exposed|
| Close dialog/popup |X|20px in 44px target, explicit name|
| Search |Search|20px workspace; separately approved search-pill glyph retained|
| Upload/change file |Upload/document|20px with visible action text|
| Data observations |Warning|20px with label and source count; no status-red decoration|
| Export/download |Download|20px, file format in action label|

Use the existing outline SVG family and preserve its stroke character. No emoji,
new icon-font family or mixed filled/outline set. Mirror only genuinely directional
navigation; never mirror printer/grid/document/upload icons or numeric/time axes.

## 7. Printing setup and header/footer

| Setting | Proposed shared setup |
| --- | --- |
| Action |«طباعة التقرير» directly opens native printing using current validated scope; no new mandatory confirmation screen. |
| Settings |Named adjacent secondary action; existing paper/date/content settings in a shared readable dialog. Settings are optional, not an extra prerequisite. |
| Default/output options |A4 landscape,10mm outside margins; A3 landscape where supported. Density changes spacing, never approved fonts or source values. |
| First-page header |Official logo≈38mm,24pt DIN title,10.5pt date and sector/unit scope. |
| Every continuation |Compact report context above the section/table:16pt DIN label,10.5pt cutoff/sector/unit, official logo≈30mm. No full 24pt masthead nested inside a repeated table header. |
| Repeated table headers |13.5pt Dubai Bold column headings on each continued table page; keep section heading with first row. |
| Print footer |Context/cutoff + generated «صفحة X من Y», plus organisation/copyright;10.5pt Dubai Regular. Context is distinct from source filename. |
| Source metadata |Filename and local-workflow metadata remain screen-only. Never print local filesystem paths. |
| Header/footer reserve |Reserve these inside usable content space while keeping 10mm outer margins. Body/table rows never overlap them. |
| Entity scope |Entity control, label and selected value absent from printed header; selection still filters the data. Actual source-table entity names remain. |
| Other scope |Date/sector/unit and relevant search-query context preserved. Print uses the same scoped dataset as the screen. |
| Search print |All matches, not the visible50-row page. Do not turn search into the follow-up table. |
| Pagination |Content-driven pages, readable table 13.5pt and support≥9pt. No fixed whole-page scale or promised page count. |
| Long rows |Keep whole where they fit; allow readable continuation when taller than a page. Preserve every source note and caveat. |
| Screen chrome |Hide navigation, menus, filters, operational buttons, focus rings and disclosure arrows. |
| Definitions |Keep source-required caveats and the SLC definition. An optional explanation setting must not silently hide interpretive warnings. |

Footer page totals must come from the export renderer, not hardcoded values.
The component PDF is a layout specimen using frozen illustrative data, not an
implemented replacement for the current production export.

## 8. Screen footer and help area

| Element | Proposed rule |
| --- | --- |
| File identity |14px Dubai Regular Ink; source filename only, natural wrapping; visible consistently when a workbook is loaded. |
| Calculation date |14px Dubai Regular Ink, clearly named «تاريخ الاحتساب»; preserve distinction from source/report/history dates. |
| Legal text |14px Dubai Regular Ink; exact existing organisation/copyright wording, no branding rename. |
| Surface/boundary |Linen surface, Sand top divider; same48/32/16px gutters as page/header. |
| Placement |At bottom of short pages, after all content on long pages; never a fixed overlay over controls/tables. |
| Mobile |Readable stacked rows,16px gaps as needed; no single-line tiny filename. |
| Before file load |Legal line only; no fabricated filename/date. |
| Help disclosure |Separate «تعريف المؤشرات» above footer;44px trigger/20px chevron; expanded 14px Ink source text with 16px paragraph gaps. |

## 9. Rules to save and apply after review

1. Use the approved fonts, sizes, exact colors, status labels and source definitions.
2. Share component roles and their states, not just colors: actions, fields,
   navigation, informational badges, popups, disclosures and dialogs are distinct.
3. Keep report identity, navigation, task actions and filter scope in predictable
   places. Retain the Google search-home composition as the deliberate exception.
4. Show the same three core scope fields on report pages where applicable. Extras
   are progressive disclosure; collapsing them never clears selected values.
5. Preserve live filtering, OR-within/AND-across, source keys/aliases and dependency
   validation. Do not silently transfer scope across unrelated pages.
6. Reset only filters in the proposed new implementation; retain unrelated dates,
   data, notes and preferences. Make this explicit when replacing broader defaults.
7. Every action/option/close/remove control has at least 44px target and a correct
   name/state. Use existing 20px icons consistently.
8. Keep field hover Paper; do not reuse button hover fills for inputs or selectors.
9. Use one popup at a time with outside/Escape dismissal. Keyboard returns focus;
   outside click allows natural focus. Modal sheets/dialogs contain focus.
10. Use one report print label and one shared settings surface; optional settings
    do not create an extra approval or data-commit step.
11. Preserve the independent print scale, source scope, row membership/order,
    zero/missing meanings and valid history arrows. Add pages instead of shrinking.
12. Every print page has report/date context and page numbering; repeated column
    headings remain readable and do not contain a duplicate full masthead.
13. Entity filter details stay screen-only while the selected scope continues to
    determine printed figures and rows.
14. Header/footer margins align, metadata stays readable and file names wrap.
    No fixed footer may cover content. Preserve exact legal wording.
15. Inspect the monthly workspace first at 100% browser zoom, then reuse the shared
    components in projects/search/upload/reports. Test desktop/mobile, keyboard,
    long option lists, disabled/busy/errors and every actual PDF page. A prototype
    review does not prove live data parity or accessibility certification.

## Review status

Retained Revision 2 rules remain approved. New composition,72px field recipe,
12px popup shell, shared navigation/print/footer context and dedicated filter-reset
behavior are proposed here for review. The app, uploaded PDF and source workbooks
were not changed by creation of these tables and illustrations.


---

# Retained approved specification — Revision 2

The following original approved specification is retained in full. The proposed shared-workspace rules above are the additions for this review.

# TEC Apple-Inspired Design standard

Approved typography, action controls, status badges, layout and report rules, including the final six typography amendments. **Revision 2 — 11 October 2026.** This is a design specification; it does not change the app or source data. The monthly page is the first implementation and review target at 100% browser zoom.

All choices below are approved for this app. The six latest changes apply to screen typography: page title 38px, portfolio heading 30px, card title 28px, supporting explanation 14px, table content/names/notes 16px, and Dubai Bold table headings. The independently approved print sizes remain unchanged; table headings use Dubai Bold in print as well. Earlier preview images illustrate the previous revision and are retained as historical comparisons.

Use the supplied **Regular (400)** faces for headings, figures, body text and controls. **Table column headings use the supplied Dubai Bold (700)** face. DIN Next Arabic and DIN Next LT Arabic are distinct supplied font families.

## Master component table

For text-only rows, “Inherited” means the text follows the surrounding surface; it does not create a separate box. Taupe text must remain on Paper for readable contrast. A dash means no separate border or fill.

| Element | Font / screen size | Text | Background | Border |
| --- | --- | --- | --- | --- |
| Page title | DIN Next Arabic Regular / 38px | Charcoal #333333 | Inherited | — |
| Portfolio heading | DIN Next Arabic Regular / 30px | Charcoal #333333 | Inherited | — |
| Card / table-section title | DIN Next Arabic Regular / 28px | Charcoal #333333 | Paper #FCFBFB | — |
| Main figures | DIN Next LT Arabic Regular / 34–40px | Charcoal #333333, with defined status exceptions | Paper #FCFBFB | — |
| Secondary figures | DIN Next LT Arabic Regular / 28px | Charcoal #333333, with defined status exceptions | Paper #FCFBFB | — |
| Table column headings | Dubai Bold / 18px | Ink #4F4E4E | Linen #EFEBE7 | Sand #E7E0D3 bottom divider |
| Table content, names and notes | Dubai Regular / 16px | Taupe #756B5F | Paper #FCFBFB | Linen #EFEBE7 row dividers |
| Important labels | Dubai Regular / 12px | Taupe #756B5F | Paper #FCFBFB | — |
| Supporting explanations | Dubai Regular / 14px | Taupe #756B5F | Paper #FCFBFB | — |
| Change arrows and differences | Dubai Regular / 15px | Ink #4F4E4E, with meaning-based exceptions | Inherited | — |
| Minor metadata | Dubai Regular / 14px | Ink #4F4E4E | Inherited | — |
| Primary action button | Dubai Regular / 16px | Paper #FCFBFB | Teal #115E67 | Teal #115E67 |
| Secondary action button | Dubai Regular / 16px | Teal #115E67 | Paper #FCFBFB | Teal #115E67 |
| Text action / action link | Dubai Regular / 16px | Teal #115E67 | Transparent | — |
| Destructive action button, when present | Dubai Regular / 16px | Paper #FCFBFB | Burgundy #651D32 | Burgundy #651D32 |
| Icon button | Existing icon family / 20px icon | Ink #4F4E4E | Paper #FCFBFB | Taupe #756B5F |
| Filter / input value | Dubai Regular / 16px | Ink #4F4E4E | Paper #FCFBFB | Taupe #756B5F |
| Filter / input label | Dubai Regular / 12px | Taupe #756B5F | Paper #FCFBFB | — |
| Inactive navigation tab | Dubai Regular / 16px | Ink #4F4E4E | Sand #E7E0D3 | Sand #E7E0D3 |
| Selected navigation tab | Dubai Regular / 16px | Teal #115E67 | Paper #FCFBFB | 2px Teal #115E67 selected marker |
| Disabled action button | Dubai Regular / 16px | Ink #4F4E4E | Linen #EFEBE7 | Silver #C8C7C7 |
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

## Exact color palette

| Color | Hex code | Approved role |
| --- | --- | --- |
| Charcoal | #333333 | Headings, default figures, primary/destructive hover |
| Ink | #4F4E4E | Table headings, metadata, neutral differences, field values |
| Taupe | #756B5F | Table body, names, notes, short labels and supporting explanations on Paper; active field borders |
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
| Inputs, filters and tabs | Minimum 44px height; 12px horizontal padding; expand for the label/value | 8px radius; 1px control border where listed |
| Status badges | 6px vertical / 12px horizontal padding; natural width; 18px text at 1.6 line-height | 8px radius; 1px border; no shadow; no fixed height |
| Cards | 24px padding on desktop / 16px on mobile | Preserve 18px corners; Paper surface; 1px Sand border; restrained existing depth |
| Table cells | 16px vertical / 16px horizontal padding; content-driven row height | Fine Linen dividers; no heavy grid or nested boxes |

Status badges are informational. An actual drilldown action has a separately accessible hit area and interaction behavior; badge appearance alone does not imply a button.

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
| Selected tab / current page | Teal text and a 2px Teal marker on Paper; expose the correct selected/current state to assistive technology |
| Clickable table name | Retain Taupe, Dubai Regular 16px; use underline/focus to reveal the action without changing the agreed name color or weight |
| Informational badge | Preserve its status treatment; no action-style hover or loading state |

Taupe control borders are chosen as a readable boundary on Paper. Stone #ABA394 and Silver #C8C7C7 remain suitable for nonessential separators, chart marks and disabled boundaries rather than as the sole visible boundary of an active input.

## Complete formatting and content rules

1. **Fonts and hierarchy.** Use DIN Next Arabic Regular for headings, DIN Next LT Arabic Regular for main/secondary figures, Dubai Bold for table column headings, and Dubai Regular for table content, labels, notes, metadata, controls and status badges. Use the supplied font files; do not simulate bold or substitute Apple system fonts. English table names also use Dubai Regular.
2. **Screen sizes.** Use 38px page titles, 30px portfolio headings, 28px card titles, 34–40px main figures, 28px secondary figures, 18px Dubai Bold table headings, 16px Dubai Regular table content/names/notes, 18px status badges, 12px important labels, 14px supporting explanations, 15px changes, 14px metadata and 16px control values. Do not shrink the agreed table text to fit content. Filter labels retain 12px; their values use 16px.
3. **Text color roles.** Names and notes stay neutral Taupe and regular weight. Table headers use Dubai Bold, Ink on Linen. Taupe labels and supporting explanations use Paper backgrounds. Main figures default to Charcoal; completed figures use Green #01831E and late figures use Red #C00000 where those status meanings apply. The Paper text inside filled badges is a separate treatment from figure color.
4. **Palette.** Use the exact existing TEC colors and the agreed green/red status exceptions. Paper #FCFBFB is the card/table surface; Linen #EFEBE7 is the page/table-header surface; Sand #E7E0D3 is a quiet grouping/border tone; Mist #D9E1E2 is an accent surface. Stone #ABA394, Silver #C8C7C7 and Grey #808080 serve appropriate chart/decorative roles, not small regular body-text roles. Grey may be used for large or decorative elements. No new colors or undocumented tints.
5. **Arabic and mixed text.** Use approximately 1.6 line-height for table text, natural Arabic wrapping, comfortable padding and top/middle alignment appropriate to the content. Preserve source names. Keep English identifiers, dates, values, fractions, percentages and currency units in their correct reading order. Align numeric columns consistently.
6. **Badge identity.** Use the final badge mapping in the master table, including frozen as a solid Burgundy badge and cancelled as Burgundy on Sand. Keep badges visually distinct from ordinary table text. Preserve the actual source-backed status label; styling aliases do not create combined labels or new business categories.
7. **Completion and lateness.** Late unfinished work is always red. Completed legislation is green for both completion within the deadline and completion after the deadline; completion after the deadline does not become unfinished-late work.
8. **Legislation composition.** Place late legislation beside the other statuses and include it in the bar. Split pending items into late and remaining pending so each item appears once. Keep the SLC definition once below the status area: **مقارنة: تاريخ الإنجاز الفعلي بالموعد المعتمد لدى SLC**.
9. **Follow-up tables.** Show only items requiring follow-up. For projects, include unfinished overdue projects with a valid deadline, frozen, cancelled and transferred items, with or without comments. Keep the group order **late → frozen → cancelled → transferred**, and stable source order within each group. Names remain neutral and regular. Preserve the agreed columns and omit the removed delay-reason column.
10. **Zero and missing values.** Show true zero counts and zero table values as **–**. Hide empty status and H/M/L groups. Keep meaningful chart-axis zero baselines and source-backed 0% completion captions where required. Missing or invalid values remain distinct from true zero; use **غير متاح** where a dash would be ambiguous. Do not turn missing financial/progress data into zero.
11. **Progression arrows.** Use source-backed comparisons only. Put 15px arrows/differences directly below their corresponding value, on aligned baselines, reserving a single 24px comparison line where needed. ↑ means a numeric increase and ↓ a decrease. Green/red describes whether the change is favorable/adverse; use Ink for neutral changes such as a total or spend increase without an agreed performance meaning. A decline in late items is favorable; an increase is adverse. Hide unchanged or unavailable comparisons.
12. **Charts and legends.** Use flat bars, clear direct labels, visible values/units and comparable scales. Add a legend only when the series/category labels above or beside the bar do not already identify its colors. Distinguish category counts, average completion and budget shares; do not interchange these measures. Preserve financial source scope, valid denominators and category meaning.
13. **Layout and spacing.** Use a consistent 4 / 8 / 12 / 16 / 24 / 32 / 48px spacing scale. Retain the widened fluid layout: 48px desktop gutters, 32px tablet gutters and 16px mobile gutters, subject to available screen width. Use 24px between main columns and 16px between stacked cards. Keep cards as tall as their content requires; avoid large empty areas and decorative status sidebars.
14. **Monthly composition.** Preserve the approved two-column monthly composition: project portfolio physically left, executive-follow-up portfolio physically right, with strategy below legislation. Remove **سيطرة · لوحة المتابعة الشهرية** from displayed branding. Remove the extra **لم يبدأ 7 / منقول 2** line in the monthly projects card. Keep the official TEC logo and approved proportions/clear space.
15. **Projects composition.** Preserve the agreed physical pairings: quarters/months left and budget right; manager follow-up left and status summary right; budget by priority/type left and project count by priority/type right. Put the full-width follow-up table below these panels. Expand priority charts to their populated rows rather than putting them inside small scrolling panes.
16. **Terminology.** Use **الأجندة المعتمدة**, **المواضيع المستجدة**, and **الموازنة المعتمدة**. Do not add **(المعدلة)** to the displayed budget title. Keep the SLC explanation below and a concise legislation-review description above.
17. **Responsive behavior.** Reflow cards and controls on narrow screens while preserving readable type. Adapt tables to a readable mobile presentation; do not squeeze them into tiny text. Keep the overall page within the viewport; use deliberate table scrolling only when required for a wide data table. Priority charts expand with their visible categories.
18. **Controls and accessibility.** Use one clear primary action per task, predictable button/field states, visible selected tabs and focus, keyboard-accessible menus, explicit labels for icon buttons, text alongside status colors, and reduced-motion support. Keep drilldowns and full-report actions available without adding visual clutter or exposing internal implementation details in product flows.
19. **Print and exports.** Use the separate print scale below, repeat table headers, preserve Arabic direction and badge identity, and keep individual rows together where possible. Add pages to accommodate content instead of shrinking the entire report. Hide navigation, filters, menus and operational buttons. The entity filter is screen-only: omit its control, label and selected-value field from the printed layout, including the print header. Its selection still filters the printed report content. Preserve sector/unit scope, date and the official logo. Keep template/report data rules unchanged.
20. **Verification and rollout.** Establish this standard on the monthly page first. Review its header, cards, controls, table and interactions at **100% browser zoom**, then inspect the actual PDF at readable size. Verify source totals, previous/current comparison keys, missing values, fonts, colors, wrapping, mobile behavior and exports before reusing the standard on projects, search, uploads and other pages. Visual polish must not change calculations or source meaning.

## Approved print scale

Print uses its own approved sizes. The latest screen-size amendments do not automatically resize print. Verify the actual rendered PDF after implementation; page count follows the content.

| Element | Font | Print size |
| --- | --- | --- |
| Page title | DIN Next Arabic Regular | 24pt |
| Portfolio headings | DIN Next Arabic Regular | 18pt |
| Card / table-section titles | DIN Next Arabic Regular | 16pt |
| Main figures | DIN Next LT Arabic Regular | 24–28pt |
| Secondary figures | DIN Next LT Arabic Regular | 20pt |
| Table column headings | Dubai Bold | 13.5pt |
| Table content, names, notes and status badges | Dubai Regular | 13.5pt |
| Important labels and supporting explanations | Dubai Regular | 9pt |
| Change arrows and differences | Dubai Regular | 11pt |
| Minor metadata | Dubai Regular | 10.5pt |
| Entity filter, label and selected-value field | Screen only | Hidden in print |

Use A4 landscape with 10mm margins. Larger paper remains an export option for wider reports. Avoid forced two-page output or a fixed whole-page shrink factor. If an unusually tall row cannot fit a page, allow a readable continuation instead of clipping it.

Entity selection continues to determine the exported rows and figures; hiding its printed field does not reset the selected filter. This rule does not remove entity names where they are part of the report's actual table content.

## Related previews

- [Typography colors and exact TEC palette](https://github.com/ormbh/Performance-App-2/blob/main/Color-Previews/README.md)
- [Actual bundled font samples](https://github.com/ormbh/Performance-App-2/blob/main/Font-Previews/README.md)
- [Latest status badge preview](https://github.com/ormbh/Performance-App-2/blob/main/Status-Previews/README.md)

This specification consolidates the approved app design. It does not claim that the app already implements this revision, that it is an official TEC brand manual, or that it certifies accessibility.
