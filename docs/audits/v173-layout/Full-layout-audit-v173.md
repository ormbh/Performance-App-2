# Full layout audit — v173

**Verdict: layout consistency fails. No application, workbook, principles or ZIP was changed by this audit.** The owner’s current visual authorities are **التقرير الشهري** for dashboard pages and **تقرير الأجندة السنوية** for formal reports. Projects and entities require a composition review as well as component corrections.

This is a design, implementation and export audit. It does not treat an unchanged old PDF or passing calculations as proof of good layout. Findings below distinguish confirmed differences, proposed composition changes and unresolved principle decisions.

## Evidence and scope

- Exact delivered v173 runtime, ZIP SHA-256 `8136ed90f8d18dab92fba2823aa124b037a5005c8939cdc32ca335906c00d46a`; principles Revision 37 plus the owner’s later baseline instruction.
- 29 captured states × 1280 / 1440 / 1920 desktop widths. Includes landing/upload, monthly, portfolio dashboard/list/single record/formatted report, entity summary/records/history, three formal reports, data checks, comparison setup/overview/detail, search idle/active, drawer, empty scopes, PDF dialogs and menus. Additional real long-name, hover, keyboard-focus, disabled/busy and controlled comparison checks.
- Native print-role inspection for monthly, portfolio, entities, agenda, council, special projects, checks, search and comparison; reused the actual v173 PDFs, including all 115 formal-report pages rendered and native-inventoried. All 115 were also visually scanned in numbered contact sheets; selected dense/suspect pages received readable-size review, with the exact coverage recorded separately. Added full search and populated/exact comparison exports and a real loading-state export. The full search export correctly continues at the engine’s full-width height limit; its long pages are not A4 defects.
- Used the unchanged supplied dummy workbook (30 September 2026). Historical comparison cases are controlled layout fixtures, not genuine prior-month findings. No workbook file, record-level dataset or source-record screenshot is published with this report. Findings include only the measurements needed to explain defects; illustrations use independent synthetic values.

## What is already consistent and should be preserved

The shared sticky text navigation, three-report dropdown order, search-only captionless four-square shortcut, stable 192px workspace logo, official assets, four/five main filter inventories, formal-report-only contents, common recorded-status palette, 14px copyright text, main formal-table column orders and PDF export profiles remain the foundation. All 27 sampled execution-status badge instances pass the shared appearance mapping; generic severity labels are not execution statuses. The tested monthly PDF action preserves width/label and restores focus after loading. Other sampled export controls were checked in normal/hover/focus states, with the search-results exception recorded below. No viewport-wide overflow or browser runtime errors were observed in the captured states.

The monthly table and formal-report main tables retain their primary text roles. Monthly summary footer navigation remains absent from PDF. Genuine internal PDF contents/record links remain useful. The council table’s different six-column sequence is intentional; only special projects has detailed update cards. The broader entity council register and monthly/portfolio financial scopes are intentional data distinctions.



## Findings register

P1 = fix before layout sign-off; P2 = material consistency/usability work; P3 = minor polish. Design/engineering proposals and contract clarifications are separate from confirmed defects.

## Confirmed

### C01 · P1 · Record detail drawer

Observed: The sticky navigation sits over the drawer. The top close button is intercepted by the upload navigation link; actual pointer hit-testing confirms it.

Required/reference: Modal controls must sit above navigation and the background must be inert.

Correction: Use one modal/top-layer system, restore focus to the initiating record and verify close/Escape/background interaction.


### C02 · P1 · Monthly and entity filters — long selections

Observed: At 1280px, a real long unit name makes monthly fields 72 / 92 / 72px and entity fields 72 / 112 / 72 / 72 / 72px.

Required/reference: A coherent field row and properly centered task actions in every selection state.

Correction: Choose one compact-value/wrapping policy; align peers through the row, preserve full names in the picker/accessibility label and recalculate toolbar alignment.


### C03 · P2 · Shared page shell

Observed: At 1440px the first monthly filter starts at y=212.6px; projects, entities and the formal reports start at y=236.6px with equivalent title/logo geometry.

Required/reference: One title-to-controls spacing contract, using the monthly desktop baseline.

Correction: Use the same masthead/context/control slots instead of compensating for different parent padding.


### C04 · P2 · Data checks page

Observed: Main content has 36px side padding while its header and the approved pages use 48px.

Required/reference: 48px desktop gutters.

Correction: Align checks content and tables to the shared page grid.


### C05 · P2 · Comparison and data checks canvas

Observed: Body canvas is #F7F6F3; monthly/projects/entities/reports use the approved Linen #EFEBE7.

Required/reference: Use the approved canvas and Paper surfaces.

Correction: Remove the legacy page-specific canvas override; keep intentional search-home/results exceptions explicit.


### C06 · P2 · Search results PDF action

Observed: The active تنزيل PDF button is Paper/Teal, with a Mist hover, while the same action elsewhere is Teal/Paper with Charcoal hover.

Required/reference: One primary PDF action treatment.

Correction: Use the shared export button for results, including normal, hover, disabled, busy and focus states.


### C07 · P2 · PDF settings dialogs

Observed: Monthly settings title is 24px and #2E4445; portfolio settings title is 28px and Charcoal.

Required/reference: Equivalent modal title roles should match the approved hierarchy and palette.

Correction: Render both settings dialogs through the same title/body/action frame; preserve their different settings.


### C08 · P2 · Monthly settings close control

Observed: Close target is 36×36px with legacy #466764 ink and #F2F2EB fill; portfolio close is 44×44px with approved Ink/Paper.

Required/reference: 44×44px icon target and approved state colors.

Correction: Use the shared icon button and modal tokens.


### C09 · P2 · Filter picker actions

Observed: تحديد الكل and مسح التحديد are approximately 36px high and use 6px corners.

Required/reference: At least 44px action targets, 8px action corners.

Correction: Standardize picker commands without enlarging or moving the option data.


### C10 · P2 · Project main list and single-record table

Observed: The project record-list and single-record tables use 16px Bold column headings; agenda and monthly use 18px Bold. The default projects follow-up table already uses 18px Bold headings and 16px body text.

Required/reference: Use the agenda table-heading baseline.

Correction: Share the table heading role across portfolio main/follow-up/drill views.


### C11 · P2 · Project list table density

Observed: Project record-list/detail cells use 14px vertical / 12px horizontal padding, versus 16px in the agenda/monthly baseline; ordinal/date cells have separate narrower rules. This does not describe every projects table.

Required/reference: A documented density tier for equivalent record tables.

Correction: Use the common comfortable record-table density, retaining deliberate ordinal/date column widths and natural source-text wrapping.


### C12 · P2 · Entity comparison/history view

Observed: The entity comparison/history view reuses entity-print-table on screen: headings are 17px Regular and body text is 17px, versus the 18px Bold / 16px record-table baseline.

Required/reference: Desktop table headings 18px Dubai Bold, body 16px.

Correction: Use a screen table component; reserve print-role overrides for print output.


### C13 · P2 · Entity detail/domain controls

Observed: Domain controls use 17px text, 7px corners and #FFFFFF active ink, versus the standard 16px / 8px / Paper roles.

Required/reference: One desktop control system.

Correction: Reuse the shared tab/filter/action roles, with explicit selected and focus states.


### C14 · P2 · Entity scope metadata

Observed: The same five-field scope is rendered below filters and again in the body; the source cutoff repeats after the masthead.

Required/reference: One clear on-screen scope/context presentation.

Correction: Keep scope/reset below filters; use the same scope model once in PDF metadata without repeating it on screen.


### C15 · P2 · Portfolio legend heading

Observed: The heading uses 20px Dubai; the agenda baseline uses the heading-font role at 20px.

Required/reference: Equivalent legend-heading typography.

Correction: Use the agenda legend type role while retaining portfolio-specific definitions.


### C16 · P3 · Portfolio legend density

Observed: Legend container uses 16px / 24px padding and 12px / 24px definition gaps rather than the compact 16px legend contract.

Required/reference: One compact legend layout, with enough chart area.

Correction: Apply one related-chart legend component; keep source-specific wording and status identities.


### C17 · P3 · Portfolio PDF legend labels

Observed: Labels use 11pt while the formal-report legend contract is 10.5pt.

Required/reference: Revision 37 section 11 points detailed chart/legend annotations to the explicit section 7 chart roles; use that annotation role in full PDF too, retaining named chart-specific exceptions.

Correction: Standardize the role; do not apply a blanket font change to whole tables or charts.


### C18 · P2 · Entity PDF primary total

Observed: The primary overall total is 20pt; monthly primary totals are 28pt and the principles specify 24–28pt main figures.

Required/reference: Preserve the primary/secondary hierarchy in full PDF.

Correction: Use the shared primary-total print role and verify the downloaded file.


### C19 · P2 · Entity PDF secondary figures

Observed: Summary figures are 18pt; the current PDF secondary-figure role is 20pt.

Required/reference: A single secondary-figure print role.

Correction: Correct the role mapping, preserving counts, labels and semantic nesting.


### C20 · P2 · Special-project PDF progress caption

Observed: نسبة الإنجاز المسجلة is 8.25pt on ordinary detail pages (for example physical page 10), below the 9pt caption role.

Required/reference: Readable, consistent print captions.

Correction: Use the approved caption size, remeasure the identity row and verify page breaks without shrinking source notes.


### C21 · P2 · Interactive portfolio and monthly figures

Observed: Some monthly count targets are 21–39px high. Portfolio record links are 26px high; some proportional segment buttons are only a few pixels wide.

Required/reference: 44px action targets, with proportional chart geometry preserved.

Correction: Reserve coherent hit areas for text/count actions. Use whole chart rows and separate readable drill controls for tiny marks; never inflate data bars or overlap adjacent hit areas.


### C22 · P2 · Entity chart-to-list links

Observed: Some chart list links are only 22px high.

Required/reference: Quiet links must still be usable controls with the agreed target size.

Correction: Use one shared report/list-link component with a reserved target and visible keyboard focus.


### C24 · P2 · Special-project screen/PDF zero presentation

Observed: The live screen and physical PDF page 30 print a standalone 0 for الموازنة المخصصة إن وجدت. The source-detail rendering allows the raw numeric value through instead of the agreed display formatter.

Required/reference: App-wide displayed zero values use a dash; source values remain unchanged.

Correction: Apply the shared missing/zero display formatter to this numeric detail field on screen and in PDF, then verify nonzero amounts and real source text remain intact.


### C25 · P1 · Special-project PDF orphan section heading

Observed: Physical page 47 (logical content page 46) contains the completed-project detail section heading/count and footer, but its first project card starts on physical page 48. This is an orphan heading rather than harmless final-page whitespace.

Required/reference: A section heading must stay with the start of its first real record.

Correction: Add a keep-with-next pagination rule for section lead plus first-card identity; remeasure the actual native PDF and ensure no empty/orphan heading page or missing content is introduced.


### C26 · P1 · Entity full-PDF ordinal column

Observed: Three-digit row numbers wrap onto two lines in the actual PDF: physical page 2 middle and page 3 top/end. For example 120 renders as 12 / 0 and 179 as 17 / 9.

Required/reference: Ordinal values stay on one line and retain clear RTL/LTR isolation.

Correction: Reserve enough ordinal-column width, isolate numerals and prevent wrapping. Verify three- and four-digit ordinals on screen and full PDF without reducing body type or truncating record text.


### C27 · P1 · Comparison overview PDF contains screen-only commands

Observed: The actual populated comparison PDF prints عرض التغيرات, تفسير الفرق, عرض كل التعديلات and عرض البنود. The downloaded PDF has zero link annotations, so these are dead application commands rather than genuine PDF destinations.

Required/reference: Keep app-only navigation/actions on screen; retain a PDF link only if it has a real, verified destination within the exported document.

Correction: Use a print-specific overview table without drill-command columns/buttons, or include the corresponding detail content with real internal destinations if explicitly approved. Preserve the actual comparison measures and explanations.


## Design proposal

### D01 · P1 · Projects page composition

Observed: A largely untitled full-width summary, multiple technical tables presented as charts, manager analysis and priority/budget panels compete before the main record list.

Required/reference: A monthly-style hierarchy: clear primary measures, generous comparable plots, then the record table.

Correction: Recompose the page as illustrated; preserve financial scope, mean-progress meaning, manager ranking and every existing analysis/detail route.


### D02 · P1 · Entities page composition

Observed: The supplied scope creates approximately 67,000px of page height. Separate status cards, priority rows, relationship rows and grouped full registers produce heavy repetition.

Required/reference: A readable monthly-style summary, a shared domain distribution and a clear main register.

Correction: Use progressive desktop record browsing with exact totals and full matching-record PDF export. Retain approved/emerging agenda separation and full council-register scope.


### D03 · P2 · Projects/entities summary leads

Observed: Removing generic overview headings left prominent totals with no visible card identity and unused header space.

Required/reference: An intentional title/total lead following the agenda baseline.

Correction: Recompose the summary lead; do not restore the rejected generic نظرة عامة label.


### D04 · P2 · Entity follow-up presentation

Observed: Priority rows repeat later in the full register, with overlapping date-alert and status measures that require explanatory prose.

Required/reference: Clear separation of recorded status and date-based follow-up; one obvious path to exact records.

Correction: Keep date alerts nested/contextual and let their counts filter the main list. Preserve full alert reasons and source notes.


### D05 · P2 · Comparison composition

Observed: Period box, file setup, extra actions, nested filter card and the detail card have different visual rhythms from the baseline. Setup can push the main controls below the first viewport.

Required/reference: One predictable header/control row and a compact task-specific setup state.

Correction: Use a compact date/file setup panel and the shared page grid; retain exact metric drill, incoming/outgoing contributions and unresolved records.


### D06 · P2 · Full-PDF table density

Observed: Monthly, entity, portfolio, comparison, results and checks use different padding systems. Their type sizes often pass while their page density still looks unrelated.

Required/reference: Define comfortable/compact full-PDF density against the monthly PDF and formal-report density against agenda.

Correction: Specify shared density tiers and deliberate exceptions; remeasure actual native outputs instead of shrinking text to obtain a page count.


## Engineering proposal

### D07 · P2 · Screen/print composition architecture

Observed: Monthly and entity have different screen and print markup paths. A correct native text advance does not prove that the print role is the right one.

Required/reference: One scoped content model and a shared semantic role map for each view/output.

Correction: Share structure and component roles where possible; retain the approved paper typography, covers, date title and margins.


### D08 · P2 · CSS ownership

Observed: The source builds 86 ordered CSS modules. Equivalent controls receive several page-specific and later override rules.

Required/reference: A clear owner for shared shell, controls, tables, figures, legends and print roles.

Correction: Consolidate source rules behind component tokens in the correction pass. Keep the already-clean 23-file runtime ZIP.


## Contract clarification

### R07 · Decision · Comparison file setup headings

Observed: Previous/current file-card titles use 23px; equivalent card headings in the monthly baseline use 28px.

Required/reference: Define the file-setup card heading role explicitly; it is not automatically equivalent to a dashboard metric-card heading.

Correction: Decide whether 23px is a named setup-role exception or use the standard card heading. Do not infer a material usability defect from the size difference alone.


### R01 · Decision · Baseline precedence

Observed: The owner now names the monthly page and agenda page as the visual authorities.

Required/reference: Record those references above older contradictory implementations.

Correction: Update the principles with baseline screenshots/role tables and an explicit exception register.


### R02 · Decision · Baseline typography exceptions

Observed: The monthly requester-label implementation uses 16px, while the written subgroup-name rule says 18px.

Required/reference: One unambiguous role value or a named baseline exception.

Correction: Preserve the selected baseline while resolving this in the role map; do not silently resize the baseline.


### R03 · Decision · Spacing exceptions

Observed: The spacing scale excludes values such as 20px and 28px that remain in the chosen baseline and older components.

Required/reference: Document approved component exceptions or normalize them after visual review.

Correction: Replace competing generic rules with a small explicit spacing/role table.


### R04 · Decision · Chart hit areas

Observed: The 44px button rule and tiny proportional segment buttons need a compatible interaction contract.

Required/reference: Exact marks plus accessible separate interactions.

Correction: Specify row/quarter activation, readable exact-value controls and keyboard behavior without enlarging data marks.


### R05 · Decision · Legend scope

Observed: Formal reports need full workflow definitions; monthly has a compact key. Entity/portfolio need an explicit page-specific choice.

Required/reference: No blanket legend additions.

Correction: Illustrations use one related-chart key. Retain formal-report definitions and record the chosen entity/portfolio detail treatment.


### R06 · Decision · HH PDF repeated context

Observed: Ordinary detail pages repeat the group title/count; desktop groups it once. The trail rejected repeated administrative strips.

Required/reference: Define ordinary page context separately from unavoidable long-card continuation identity.

Correction: Review the repeated group header against the owner’s intended treatment before changing it.


### R08 · Decision · Nonzero chart rows with blank source category

Observed: A special-project chart row has real contributing projects but an empty source sector label. The existing blank-value policy leaves the label empty.

Required/reference: Keep every contributing record and preserve the blank source value while making chart interpretation explicit.

Correction: Decide a chart-only missing-category treatment or nearby explanatory note. Do not silently omit the projects or invent a recorded sector value.


## Page-by-page coverage and outcome

This covers the full application rather than only the projects/entities redesign. A named baseline defines comparable visual roles; a shared defect reproduced on the baseline page remains a defect to correct. Desktop measurements cover 87 state/width combinations, not 87 independent workflows.

| Page or shared area | Screen review | PDF/content review | Outcome and correction scope |
|---|---|---|---|
| Search home and upload | Centering, original four-square shortcut, logo, upload/file-state hierarchy, shared navigation | No invented PDF/export for landing/upload | Retain original search shortcut and approved assets. Comparison file setup heading role needs clarification. |
| Monthly report | Card/bar hierarchy, requester labels, filters, link/action states, settings dialog | Actual monthly PDF, matching six groups and follow-up record sequence; screen-only summary links omitted | Preserve approved cards and bars. Correct long selections, settings title/close, and small drill targets. |
| Projects dashboard | Four filters; summary, finance, month/year timing, manager and priority analyses, follow-up table | Actual full-PDF layout, source populations and existing export profile | Full composition proposal; preserve recorded-progress meaning, budget order, analytical views and every drill route. |
| Projects list / single record / formatted report | Table typography/density, exact record destination, report route, four-filter context | Reuse verified scope/record evidence; formatted full-PDF structure | C10–C11 apply to record-list/detail tables. Default follow-up table already has the baseline 18px bold headings and 16px body. |
| Entities summary and registers | Five filters; duplicate metadata; domain charts; priority/relationship rows; main registers; history/comparison | Full matching-record PDF, filtered scope and empty export | Full composition proposal; preserve domain separation, broader council scope, contributing-entity context and all records in PDF. Correct print figure hierarchy and history-table type. |
| Annual agenda | Formal baseline shell, contents, quarter stacks, detailed definitions, tables, empty scope | 14-page actual A4 landscape report; sequence, headers, internal contents destinations; empty export | Preserve its approved chart type and table order. Shared shell/control corrections apply. |
| Council decisions | Issuer charts and full-width unspecified-issuer panel, year grouping and quarter order, six-column records, empty scope | 31-page actual A4 landscape report; decision metadata/full text, sequence and destinations; empty export | Preserve agreed issuer layout, year grouping and metadata inside decision cell. No special-project detail cards. |
| Special projects | Cohort/sector charts, compact definitions, main table, detailed updates, leadership classification and empty scope | 70-page actual A4 landscape report; detail cards, continuation, sequence and destinations; empty export | Correct undersized progress caption. Resolve repeated ordinary-page group context separately from necessary long-card continuation. Additional visual findings are recorded below. |
| Comparison setup / overview / exact impact detail | Previous/current setup, filter/context rhythm, controlled matched record and entity-change view | Actual populated and exact-impact full PDFs; existing exact-change/transfer tests reused | Correct canvas; propose compact setup composition. Fixtures are controlled clones, not real historical changes. |
| Search results / drawer | Idle/active results, table, PDF normal/hover/focus, drawer layering and close target | Actual seven-page full export at engine height limit | Correct PDF action treatment and blocked drawer close. Long export pages are permitted full-PDF continuation. |
| Data checks | Page grid, tables, severity display, source membership context | Actual full PDF; native bounds and screen-only commands | Correct gutter and canvas; retain severity distinctions and full source notes. |
| Shared components and states | Sticky nav/report dropdown, logo/footer, open filter menu, actual click targets, focus/hover/disabled/busy, long/empty selections | Font roles, cover/contents separation, full versus A4 profiles, export-only omissions | Monthly export loading/focus test passes; do not generalize that single busy-state test to every export button. 27 sampled execution-status badge instances pass the shared mapping. |

## Reused verification and evidence boundaries

The exact delivered v173 application remains unchanged. Its existing release evidence contains 249 passing checks covering source rowsets, metric preservation, filter inventory/state, actual record/report destinations, selected navigation/new-tab workflows, PDF record sequence, internal link destinations, export geometry and empty exports. Those checks are reused as functional evidence, not relabeled as new visual tests or proof that layout is consistent. This audit adds desktop measurements, targeted interaction/state checks, native print-role inspection, new search/comparison PDFs and specialist visual reviews.

Private evidence files are retained in the audit workspace: `desktop.json`, `interactions.json`, `states.json`, `badges.json`, `print.json`, `pdf-inventory.json`, `clip-probe.json`, and the visual-review logs. Published illustrations contain independent synthetic data. They are proposals, not replacements silently applied to the app.


## Proposed page sequence

**Projects:** shared monthly shell → four filters/scope/actions → monthly-style status and financial summaries → larger timing/management views with chart-related keys → exact main record table → the existing priority/type/financial detail analyses in a clearly labeled secondary area. Keep existing source dimensions, ranking weights and record routes. The illustration retains count-scaled month bars, quarter/year totals and independent recorded-progress meaning; other-year and undated source records must remain accessible.

**Entities:** shared monthly shell → five filters and one scope row → total/recorded-status summary with separate date-alert context → one comparable domain distribution retaining each source status and approved/emerging agenda separation → exact main register and record details. The proposed unified register is a design recommendation, not permission to replace source-specific date or column meanings; those must remain explicit per domain. Preserve contributing-entity context and unresolved source relationships. Proposed progressive screen browsing must not limit full-PDF matching records.

**Formal reports:** use agenda as the layout reference for shell, controls, contents, title/total lead, surfaces, typography, legend density and record tables. Preserve each report’s approved chart type and source definition: vertical quarter stacks for agenda, sector/cohort stacks for special projects and issuing-body counts for council. Preserve the council unassigned full-width box and special-only detailed updates.

## Correction and acceptance approach

1. Freeze the two baseline pages and an exception register. Approve the projects/entities full-page compositions and resolve R01–R08 before visual implementation.
2. Correct the shared shell, modal layering, controls and long-selection behavior together. Fix shared tables/type/legend/print roles, then compose the two priority pages. Do not append another broad override layer to disguise conflicting source styles.
3. Use one scoped record model. Reuse prior calculation/identity tests; rerun affected filters, exact drills and source membership. No visual task may change follow-up eligibility, financial populations, date meanings or missing-value semantics.
4. Verify default/long/multiple/stale/empty selections, open/closed menus, drawer and both settings dialogs, hover/focus/disabled/loading, actual link activation, back/forward and explicit new tabs. Compare equivalent rendered roles, not just DOM existence.
5. Verify actual native PDFs against screen content/order and the agreed role matrix. Check type sizes, alignment, badges, full text, covers, repeated headings, empty sections, internal destinations and pagination. Judge whitespace with content context; do not force a page count.
6. Test the exact final ZIP, preserve the 23-file runtime inventory and publish a single correction release with a resolved finding register. A claim of “perfect” is not a substitute for these acceptance gates.

## Limits and open checks

Direct `file://` execution in the managed browser is blocked before app load by `ERR_BLOCKED_BY_ADMINISTRATOR`. Actual extracted-file Chrome/Edge behavior and native-viewer opening zoom still need target-environment verification. No security-setting change or bypass is recommended. Copied/extracted Arabic reading order and PDF accessibility are not certified by visual/vector checks. No real previous-month workbook was supplied. Mobile/tablet and PowerPoint are excluded.

The earlier below-0.04pt native text-advance result establishes exporter fidelity to the prepared print layout. It does not settle whether every print component matches the agreed screen hierarchy. C18–C20 and D06–D07 identify concrete print-role work; the owner’s broad reported shift must still be reproduced in the target workflow before being called fixed.


## Specialist review record

# Formal-report PDF visual review — exact v173

Verdict: **FAIL: two additional confirmed presentation/pagination defects.** This is an audit only. No application, workbook, principle or release files were changed.

## Artifact and method

Reviewed `/workspace/saytara-work/v173-qa/agenda.pdf` (14 physical pages), `council.pdf` (31), and `hh.pdf` (70). Reused the existing native-font/geometry inventory and the existing 1.1× rendered pages. Source is the unchanged dummy Performance_2026_Mold_v4.xlsx, cutoff 30 September 2026. No real historical workbook was introduced.

All **115 pages** were visually scanned in numbered six-page contact sheets, with each page displayed approximately 600 × 424 pixels. This establishes full sequence/layout coverage: covers, contents, chart pages, register continuation, section transitions, detail-card sequence and footers. It is **not** word-by-word readability certification for all source text at thumbnail size.

Readable-size follow-up used the existing **927 × 655** individual-page renders for 42 pages:

- Agenda physical pages **3, 4, 6, 9, 13, 14** (6).
- Council physical pages **3, 4, 9, 12, 13, 14, 16, 20, 21, 24, 25, 26, 28, 31** (14).
- Special projects physical pages **3, 4, 7, 9, 10, 11, 12, 20, 26, 29, 30, 35, 40, 42, 43, 45, 47, 48, 51, 53, 63, 68** (22).

These include dense notes, multiple-year transitions, long entity/contributor fields, blank optional fields, progress captions, first/last and sparse pages, badges, and suspected page-break cases. Narrow browser/source checks reproduced the two failures and wrote `formal-visual-probe.json`. The specialist did not rerun broad native inventories, calculations, export engines or existing tests.

## FV01 — P1 — Orphan completed-project section heading in special-project PDF

**Observed:** physical page **47**, logical footer **46 of 69**, contains only `المستجدات التفصيلية للمشاريع المنجزة`, the project count, rules and footer. The first completed project's actual identity/card begins on physical page **48**. This is a nonempty group of 23 projects. It is an orphan section-heading page, not harmless whitespace on the final page of a complete group.

**Evidence:** `pdf-hh-47.png`, `pdf-hh-48.png`, and `formal-visual-probe.json`. The current native page plan explicitly produces:

- Completed-section heading: source layout y **26725.046875–26771.828125px**.
- First card starts at **26784.828125px**, height **665.203125px**.
- Logical page 46: start **26725.046875**, end **26784.828125** (heading only).
- Logical page 47: start **26784.828125**, end **27451.03125** (first card).

The desktop places the section heading and first project in the same `#hh-completed` sequence; the export separates their context. The first ongoing-detail group on physical page 10 successfully carries its heading and first card together.

**Expected:** a section heading must remain with at least the first project identity and meaningful content. A larger source card may continue with the approved identity continuation; no source text may be discarded or shrunk merely to achieve a page count.

**Correction approach:** add an explicit section-heading/first-identity keep constraint to the prepared print plan. Accommodate the heading in the first card's available height or split its body at a meaningful field boundary. Preserve the once-per-group heading and complete text. Recheck both detail groups, all affected subsequent page numbers and contents destinations.

## FV02 — P2 — Numeric zero bypasses display policy in HH additional fields, on screen and PDF

**Observed:** special-project PDF physical page **30**, `الميزانية المخصصة إن وجدت`, prints a literal **0**. The same detail field on the desktop is also **0**. The agreed app-wide presentation is **0 → -** while retaining the underlying numeric value.

**Evidence:** `pdf-hh-30.png`, native standalone-zero text bbox **(279.350830, 418.661957, 285.830841, 438.917969)pt**, and `formal-visual-probe.json`.

The typed source cell is numeric zero, while its preformatted display value is the string "0"; the live screen and prepared print both retain that string. Schema-aware formatting is needed without rewriting narrative text, IDs or dates.

A targeted scan of the existing HH PDF found no other exact standalone `0` words. This is not a claim that every possible zero format in the application has been checked.

**Expected:** source-grounded numeric optional fields use the same zero display policy as other numeric roles. Keep zero distinct from missing, and do not remove its populated field merely because its number is zero.

**Correction approach:** format numeric fields according to their schema and original typed cell rather than `typeof` on the preformatted string. Do not replace zeros inside narrative text, IDs or dates. Recheck the live detail, its PDF field, shared numeric optional fields, decimal amounts, empty values and narrative strings.

## Existing observations confirmed / preserve

- The three covers use the same official assets, centered title/date construction and title-name pattern. The visible contents and footer pagination exclude the cover consistently.
- The council unspecified-issuer summary is a full-width box below the two issuer charts, as requested. It is not an unwanted third peer column.
- Main record column sequences are deliberate: agenda and HH share ordinal/subject/entity/status then their relevant deadline/progress fields; council retains its six-column subject/last-decision contract. The council number/issuer/meeting metadata stays inside the decision cell and absent source metadata does not produce empty labels in inspected cases.
- Table headers repeat on continuation pages. Full-size checks resolved thumbnail suspicions on council pages 13, 14, 25 and 26: their headers are present and legible.
- No apparent table/footer collision, cropped rightmost ordinal, broken status chip, visible missing-glyph placeholder, empty optional narrative panel, Harvey ball, or printed app-return controls appeared in the scanned sequence. Readable-size samples have sound Arabic alignment and preserve multiline notes/contributor lists. These are scoped visual observations, not text equality or accessibility certification.
- Agenda physical page 14 and HH physical page 68 have substantial whitespace because their remaining source content is short and intact. Unlike HH47, those pages contain actual complete records; sparsity alone is not a defect.
- The HH recorded-progress caption is visibly much smaller than body text in readable samples; the existing native 8.25pt finding C20 remains valid. No duplicate finding was added.
- The dummy data includes source contradictions such as a completed badge alongside 40% recorded progress. Preserve the recorded values; that is a source-data observation, not a reason to restyle or recalculate completion.
- One nonzero HH chart row has an empty source sector label. It contributes a real count. Do not silently drop it or invent source text under the existing blank-label policy; any clearer missing-category treatment is a separate contract decision.

## Limits and acceptance boundary

The full 115-page sequence received structural visual review; only the 42 listed pages received individual readable-size follow-up. No word-by-word reading/equality certification is claimed for the remaining text. Internal PDF destinations and screen/PDF membership checks are covered by the parent audit's existing tests, not re-certified by this specialist. Native Chrome/Edge PDF opening/copy behavior and direct extracted `file://` app execution were not tested here. No mobile, tablet or PPT work was performed. Do not call the release visually verified until FV01/FV02 and the parent audit's existing material defects are resolved and affected outputs are rechecked.


## Specialist review record

# v173 non-formal PDF visual review — independent specialist

Reviewed 16 physical full-PDF pages through 50 readable sampled tiles, plus existing contact sheets. This is sampled visual inspection of long pages, not every pixel or every source row. Formal A4 PDFs were delegated separately and are excluded here. Existing native bounds, content-order, destination and calculation checks were reused rather than rerun. No application, source workbook, principles or public review artifact was changed.

## Coverage

| PDF | Physical pages | Visually inspected samples | Evidence |
|---|---:|---|---|
| monthly.pdf | 1 | Top, middle, footer, legislation/strategy transition, finance/follow-up transition: 5 tiles | nonformal-tiles/monthly-p1-{top,middle,end,legislation,finance}.png |
| portfolio.pdf | 1 | Top, middle, footer, timing/status, legend/manager, completed-manager/priority, finance/register transitions: 7 tiles | nonformal-tiles/portfolio-p1-{top,middle,end,status,manager,priority,register}.png |
| entity.pdf | 4 | Top, middle and footer of each physical page: 12 tiles | nonformal-tiles/entity-p{1,2,3,4}-{top,middle,end}.png |
| checks.pdf | 1 | Top readiness table, middle source observations, final observations/footer: 3 tiles | nonformal-tiles/checks-p1-{top,middle,end}.png |
| search-full.pdf | 7 | Top, middle and footer of all seven physical pages: 21 tiles | nonformal-tiles/search-full-p{1,2,4,7}-{top,middle,end}.png; reused audit-root/search-full-p{3,5,6}-{top,middle,end}.png |
| comparison-populated.pdf | 1 | Complete overview page: 1 tile | nonformal-tiles/comparison-populated-p1-full.png |
| comparison-exact-detail.pdf | 1 | Complete exact-impact page: 1 tile | nonformal-tiles/comparison-exact-detail-p1-full.png |

The 41 newly generated tiles use 1.3× native scale. Their PDF point ranges are recorded in nonformal-tiles/index.json. Nine existing readable search tiles were reused. Native PDFs are /workspace/saytara-work/v173-qa/{monthly,portfolio,entity,checks}.pdf and the current audit directory's search/comparison PDFs. All remain private; rendered dummy-source records must not be copied into published review assets.

## Confirmed findings

### Entity full PDF: three-digit ordinal numbers split across lines

Actual raster output wraps the ordinal column's 120 as `12` then `0`, 179 as `17` then `9`, 180 as `18` then `0`, and similarly 280–307. This can make record references ambiguous and makes the table visibly less readable than its screen/formal counterparts.

- Physical page 2 middle: row120/121/122/123.
- Physical page 3 top: row179/180/181/182.
- Physical page 3 end: row280/281/282.
- Physical page 4 top/middle/footer: row283 onward, including305–307.
- Evidence: entity-p2-middle.png, entity-p3-top.png, entity-p3-end.png, entity-p4-top.png, entity-p4-end.png in nonformal-tiles.
- Correction: reserve enough width for the ordinal role, keep each numeral on one line and isolate numeral direction. Verify three-plus-digit ordinals without shrinking type or taking needed source-text space arbitrarily. Check related full-PDF record tables after the shared change.

### Comparison overview full PDF: screen-only commands survive export

The overview PDF visibly retains repeated `عرض التغيرات` and `تفسير الفرق` table actions, and button-shaped `عرض كل التعديلات` / `عرض البنود`. Parent independently confirmed this PDF has zero native links, so these are not working internal PDF destinations. This violates the exclusion of screen-only navigation commands from PDF and directly reproduces the class of defect previously raised for monthly cards.

- Evidence: comparison-populated-p1-full.png.
- Correction: remove the screen-only commands and their action column/empty space from exported overview content, retaining meaningful row data, review counts and unresolved-match explanation. Do not replace dead controls with plain navigation captions. Keep genuine internal PDF destinations when actually present.
- Exact-impact detail PDF has no equivalent leaked command controls in its reviewed complete page.

## Existing findings corroborated visually

- Entity primary total and secondary summary figures are visibly weaker than monthly's hierarchy (C18/C19); exact sizes already recorded elsewhere.
- Portfolio is long and analytically dense, with technical table/chart combinations before follow-up records (D01/D06), whereas monthly has a clearer card hierarchy. This is a composition recommendation, not evidence of wrong data.
- Portfolio detailed legend differs in typography/spacing from formal-report reference (C15–C17). Full PDF still uses its own output profile; only the shared detailed-legend role is being compared.

## Sampled passes and deliberate exceptions

- Monthly's screen-only detailed-report footer navigation is absent from the sampled exported summary cards; the card dividers reserved for that navigation are absent as well.
- Monthly and portfolio preserve source status/financial meanings; completed green, ready teal, work/review pale teal and frozen/cancelled/moved treatments remain legible in the reviewed samples.
- Sampled zero totals/progress values display a dash rather than numeric0 or0%. Identifiers, dates and narrative numbers are preserved. This is not an exhaustive zero-field assertion.
- Monthly's legislation late value stays nested beneath in-progress; it is not visually added as a third peer group.
- The sampled portfolio completion ratios and finance figures are distinguishable; zero-numerator manager summaries use dashes while keeping source values/denominators visible.
- Entity/search continuation pages repeat their table header and preserve right-to-left column placement. Entity ordinal wrapping is the separate failure above.
- Search's recorded progress remains readable numeric text; no Harvey balls appear in the reviewed tiles. Long source titles/organizational names wrap naturally in sampled rows.
- No visibly clipped source narrative or footer collision was found in these tiles. A crop boundary through a row is a sampling boundary, not evidence of a PDF page split.
- Reviewed footers carry copyright/page numbering and remain separate from body content.
- Search/entity very long pages and technical-height continuation are consistent with full PDF mode. They must not be judged as A4 landscape failures; only the three formal reports use A4 landscape.
- Comparison exact-impact page keeps full subject, previous/current state, cause and numeric impact, with legible before/after field highlighting. The previous workbook is a controlled fixture, not a genuine historical result.

## Role-equivalence cautions for the main register

- C15/C16 compare the same detailed-legend role to agenda, not every typography role across unrelated views.
- C17 can cite Revision37 section11's explicit delegation of chart/legend typography to section7. Avoid implying full-PDF body typography must equal A4 formal-report typography.
- C18/C19 follow the general PDF primary24–28pt/secondary20pt roles; preserve explicit chart-specific total sizes in formal reports.
- C23's file-selector headings are not automatically equivalent to a monthly metric-card title. Treat that as R07 hierarchy choice/minor design review, not a proved material defect.
- Main actual export busy/focus behavior was tested for monthly; don't generalize that lifecycle pass to every export action.

## Limits

No every-row/per-pixel visual certification of these huge PDFs is claimed. Existing 249 functional checks are reused source-baseline evidence, not 249 new layout inspections. Current87 state/viewport measurements are dimensions/computed-style samples, not87 complete perceptual page reviews. Direct extracted-index Chrome/Edge execution remains blocked by the managed environment before app load. This review does not settle native-viewer zoom, copied Arabic reading order or PDF accessibility certification.
