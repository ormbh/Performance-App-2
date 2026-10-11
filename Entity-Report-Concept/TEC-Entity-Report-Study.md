# Entity report — revised terminology concept

This specification proposes the entity-page arrangement against the current v133 baseline. It reuses the approved Revision 7 typography and colors; the new arrangement has not yet been approved or applied to the app. Both comparison sides use identical illustrative source records, entity scope and reference date. Entity and relationship selections are read-only fixture scope in this prototype.

The terminology revision changes generated interface labels only. Raw source titles, statuses, notes, fields, record keys, dates, scope and calculations remain unchanged. See `Terminology-Review.md` for the full before / after table.

## Component setup

| Component | Proposed content and behavior | Screen specification |
|---|---|---|
| Header | TEC logo, «محفظة الجهة», reference date only; no repeated explanatory subtitle | Title 38px DIN Next Arabic Regular, Charcoal; date 14px Dubai Regular, Taupe |
| Navigation | Search, current page «تقرير الجهات» and menu; other destinations inside the menu | 16px Dubai Regular; 44px minimum targets; current-page Teal underline |
| Filters | Entity and relationship show the fixed fixture scope; the report-area dropdown filters the prototype | Values 16px Dubai; labels 12px Dubai; Paper surface, Taupe border, Teal focus |
| Summary | Four metrics: scoped total, completed / total, late, due within 30 days | Figures 40px DIN Next LT Arabic Regular; labels 14px Dubai Regular |
| Section headings | «توزيع البنود», «أولويات المتابعة» and «الاستحقاقات خلال 30 يوماً» | 30px DIN Next Arabic Regular, Charcoal |
| Portfolio cards | «الأجندة المعتمدة», «المواضيع المستجدة», «قرارات المجالس» and «المشاريع الخاصة», kept separate | Headings 28px DIN Next Arabic Regular; labels 14px Dubai Regular; status figures 34px DIN LT for agenda/council, 28px for special projects |
| Priorities side card | Source record title, portfolio, status and the actual late / soon / missing-report reasons | Section heading 30px DIN; record text 16px Dubai, Ink; reason text 14px Dubai; existing 16px status badges |
| Due-soon table | All matching open records with a valid deadline in the next 30 days, excluding late records | Body and names 16px Dubai Regular; headings 18px Dubai Bold; badges 16px Dubai Regular; line height 1.6 |
| Working interactions | Report-area dropdown, metric/status drilldowns and record dialogs operate on the illustrative records | Reuse approved 16px buttons, 44px minimum targets, 20px icons |
| Visual-only controls | Header, navigation and other controls illustrate the arrangement without implementing their app actions | Keep the native control appearance; do not imply that navigation or export was tested |
| Footer | Copyright | Dubai Regular; retain the approved footer treatment |

The four portfolio cards describe the four standard groups. If the source contains agenda records with another classification, retain an additional source group instead of silently omitting those records.

## Summary definitions

| Metric | Definition | Display color |
|---|---|---|
| Scoped total | Each matching eligible source row counted once within the selected entity, relationship and area scope | Charcoal #333333 |
| Completed / total | Rows recorded as completed divided by all rows in the same scope; display the count pair directly | Completed figure Green #01831E; denominator Charcoal #333333 |
| Late | Recorded late status, or an exceeded applicable deadline on a record the model treats as open; count each row once | Red #C00000 |
| Due within 30 days | Open, non-late rows with an applicable valid deadline from the reference date through reference date + 30 days | Charcoal #333333 |

These are separate readings of the same scope, not four categories to add together. Display a true zero count as **–**, following approved Revision 7; retain its accessible numeric value. Keep source-backed **0%** completion captions and zero-length bars. A null or unavailable value remains explicitly unavailable; do not turn missing status or date fields into zero.

## Illustrative fixture totals

| Reading | Same value on both comparison sides |
|---|---:|
| All scoped records | 11 |
| Completed / total | 4 / 11 |
| Completed rate | 36.4% |
| Open records | 7 |
| Late records | 1 |
| Due within 30 days | 2 |
| Approved agenda | 3 |
| Emerging agenda | 1 |
| Council decisions | 6 |
| Special projects | 1 |

These counts are illustrative. Portfolio totals sum to 11; open, late and due-soon readings overlap with the total and must not be added to it.

## Due-soon table fields

| Column | Source-safe content |
|---|---|
| «البند» / «الموضوع» / «القرار» / «المشروع» | Full source title and actual portfolio classification, regular Ink text; open the exact record |
| «الموعد ونوعه» | Actual applicable deadline plus its type: recorded presentation date, planned agenda completion, or project end date |
| «الحالة المسجلة» / «الحالة المسجلة / نسبة الإنجاز» | Recorded status with the approved badge treatment, plus recorded progress when the source defines that field and its value is valid; omit progress hints for agenda because its source has no such field. Do not infer progress from status |
| «منسق الأمانة العامة» / «مدير المشروع» | Display the source-provided coordinator or project manager, labelled by that exact role; unavailable values remain unavailable |

For a ready agenda record, use its valid recorded presentation date when available; otherwise retain the model's planned-date reading. A presentation date does not prove that the presentation occurred. Council decisions have no general due-date field in the current model and do not acquire a fabricated due date.

The recorded primary entity appears in the record dialog, regardless of whether the selected fixture relationship is primary or contributor. It is not an additional column in this four-column table.

## Priorities and source limits

| Area | Rule for the concept |
|---|---|
| Priority reasons | Describe the actual recorded-late, exceeded-deadline, due-soon and explicit missing-report flags. Keep reasons attached to the same source row. Do not infer a booking failure or prescribe an action from an unrecorded presentation date |
| Priority ordering | Late first, then soon, then missing report; retain stable source ordering within each group |
| Missing council report | Show only when the source field explicitly records «لا»; blank or unavailable fields do not establish that a report is missing |
| Entity relationships | Keep primary entity and recognized contributors distinct. A contributing entity is not automatically the lead entity or owner |
| Strategic projects | The current entity workspace scopes agenda, council and special-project records. A validated strategic-project entity mapping is needed before extending this scope; the concept must not imply strategic-project coverage |
| General owner | No source-backed owner field is shared across all these portfolios. Do not invent a person, assign the primary entity as a personal owner, or relabel another field as ownership |
| Next commitment / required action | There is no universal source-backed commitment/action field. Portfolio-specific fields, such as the special-project upcoming phase or council follow-up requirement, may appear verbatim in source details; do not generate new instructions from a date or status |
| Sector / unit controls | Do not add them to this concept without validating their wiring into the existing entity scope. The proposed controls remain entity, relationship and report area |
| Partial coverage | Do not silently treat unavailable portfolios, missing status fields or undated eligible records as fully covered data |

## Colors, spacing and output

| Role | Approved color / treatment |
|---|---|
| Headings and figures | Charcoal #333333 |
| Essential labels, source names, actual notes and table body | Ink #4F4E4E |
| Reference date and secondary metadata | Taupe #756B5F |
| Controls, focus and progress | Teal #115E67 |
| Completed / late | Green #01831E / Red #C00000 |
| Page / card surfaces | Linen #EFEBE7 / Paper #FCFBFB |
| Card borders and separators | Sand #E7E0D3; Silver #C8C7C7 where a stronger divider is needed |
| Controls | 44px minimum height; 8px radius; 2px Teal focus outline with 2px offset; primary hover uses Paper on Charcoal |
| Layout spacing | 24px between major sections; 16px inside grouped controls; 8px between icon and label |
| Mobile | Reflow summary metrics and portfolio cards; retain readable sizes and full source text. The table owns horizontal scrolling within its container; no stacked mobile-table implementation is included |
| Print scale reference | The study records the approved separate scale: 12pt table body/statuses and 13.5pt bold table headings. The approved first-page title includes the date; no continuation header; footer contains copyright and page numbers only; controls and the entity filter are hidden |
| Print implementation | No print capture or export implementation is included in this entity-page study |

Use natural Arabic wrapping and aligned metric rows. Status colors belong to the status figures or badges; record names remain neutral and regular weight. Financial bars remain solid without a hatching marker or availability note, as approved for the concept. No record counts, classifications or metric formulas change as part of this presentation proposal.

Source basis: the current v133 app's entity model and view, the approved Revision 7 TEC rules, and the illustrative prototype's scoped records. This is a component specification, not an app implementation or a claim of expanded data coverage.

## Terminology and source attribution

- Generated count labels follow the existing app terminology: agenda uses «المواضيع», councils «القرارات», special projects «المشاريع», and mixed scope «البنود». Use “عدد …: N” to avoid awkward number agreement.
- Completion share is «المنجز / الإجمالي» and the bar caption is «نسبة المنجز». Recorded percentage progress remains «نسبة الإنجاز المسجلة»; 100% progress does not change a recorded review status to completed.
- The inclusive summary is «متأخر حسب الحالة أو الموعد». Individual alerts distinguish «متأخر حسب الحالة المسجلة» from «تجاوز الموعد المخطط», «تجاوز موعد العرض المسجل» or «تجاوز موعد انتهاء المشروع», using the actual applicable date.
- Blank presentation-date fields say «موعد العرض غير مسجل»; unavailable source columns say «حقول موعد العرض غير متاحة في المصدر». Neither wording establishes a failed booking or that an appointment does not exist.
- Record details retain exact source-field attribution: «ملاحظات فريق الأمانة العامة», «ملاحظات مدير المشروع», «توصيات إدارة الأداء والتنفيذ», «ملاحظات مقرر المجالس» and «المنجز للآن». Sector and administration appear as separate source-labelled fields. The generated source-file caption is «اسم ملف المصدر»; the raw Source.Name field and filename remain unchanged.
- Keep the page title «محفظة الجهة» and current navigation «تقرير الجهات». The menu button is named «صفحات التطبيق» for assistive technology. No explanatory subtitles are added beneath headings.

Applied skill methods: TEC Apple-Inspired Design, Saytara QA and Saytara Dashboard Accessibility. The approved Revision 7 file provides exact project tokens and terminology. Supplementary TEC/accessibility reference resources were unavailable through the skill reader; the main skill instructions and local approved standard were used.
