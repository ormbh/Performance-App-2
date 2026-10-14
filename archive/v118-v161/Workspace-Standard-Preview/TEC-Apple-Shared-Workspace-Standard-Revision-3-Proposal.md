# TEC Apple-Inspired Design — shared workspace standard

**Revision 3 proposal — 11 October 2026.** Prepared for review of filters, menus,
printing, buttons, icons, headers and footers. Revision 2's approved typography,
exact palette, status badges, data meanings and dashboard composition remain the
baseline. The new arrangements and interaction details below are proposals,
not an assertion that the released v129 app has changed.

[Approved Revision 2, retained in full](Approved-Standard-Revision-2.md).
[Before/after gallery](index.html). All public examples use illustrative data.
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
