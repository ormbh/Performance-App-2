---
name: tec-apple-inspired-design
description: Standardize TEC and Saytara dashboards and related interfaces using the approved TEC fonts, colors, compact metric hierarchy, Arabic RTL composition, spacing, navigation, tables, bars and output profiles. Use for dashboard design, app-wide consistency reviews, mockups and report presentation. Preserve each page's data meaning and approved behavior. Illustrate a new visual direction before implementing it; reuse existing approval. Combine with the relevant Saytara QA, accessibility, visualization and export skills.
---

# TEC Apple-Inspired Design

Use a consistent, restrained design approach across the TEC app: clear hierarchy, readable information, deliberate spacing and predictable interactions. Preserve TEC identity and the meaning of the data.

**Edition:** 14 October 2026. Revision 24: consolidates approved decisions for v157, applying the monthly legislation card with combined completion, its nested late subset and a full-scope completion bar. Retains removal of Harvey balls and circular progress indicators, numeric progress, and approved HH, agenda and shared display rules. This is design guidance; publishing or installing it does not change the app.

Read [TEC Apple-Inspired Design Principles](references/TEC-Apple-Inspired-Design-Principles.md) before using this skill. It contains the current tokens, component rules, monthly exceptions and PDF profiles. Both files form one self-contained skill package.

## 1. Establish scope and authority

1. Identify the page, audience, device, data source and requested stage: study, illustration, implementation, audit or export. Use the current conversation to resolve these before asking questions.
2. Apply the latest explicit user instruction first, then the approved rules in the principles document, then the current implementation where no rule exists. Historical screenshots, proposals and CSS declarations are evidence, not automatic approval.
3. Record existing metric definitions, denominators, status meanings, filter behavior, section order and required physical positions. Styling does not authorize changing these.
4. Reuse the shared visual roles across monthly, projects, entity, comparison, search, agenda, council and HH pages. Keep page-specific information architecture, source-report legends and output requirements intact.
5. Treat a request to update these documents as a documentation task. Do not modify, rebuild or release the application unless that work is also requested.

## 2. Preserve TEC identity

- Reuse the supplied logo and actual approved Dubai and DIN font files. Preserve the logo's proportions and clear space. Do not redraw it or substitute SF Pro, SF Arabic, Helvetica or generic system fonts for delivery.
- Plain **جاهز للعرض** labels and counts use Teal; completed uses Green and late uses Red. Text inside filled badges or chart marks uses the approved contrasting ink, including Paper on Teal.
- Apply the exact color roles in the principles document. Use one status appearance mapping across badges, chart marks, legends and exports. Match status fill, readable ink and border; do not maintain a separate legacy chart-status palette. Keep unrelated financial, quantity and coverage colors in their own roles.
- Use Apple-inspired hierarchy, restraint and usable interaction. This is the project's adaptation, not an official Apple or TEC brand manual or a claim of platform certification.
- Use approved solid surfaces, modest radii and restrained depth. Keep analytics crisp; avoid decorative blur, glass, gradients, heavy shadows and status-colored sidebars.
- Retain official Arabic terminology and the existing icon family. Do not silently translate or normalize source organization names.

## 3. Compose with shared components

- Build the page in a clear order: identity and date, navigation/actions, applicable filters, section headings, cards, then supporting records or tables.
- Reuse semantic typography and spacing roles rather than selecting a new size for each card. Use the independent PDF scale for output.
- Keep the compact metric arrangement: short status label above its value, change beneath that value. The card total's label remains beneath its total. Align label, figure and change rows across peers, allowing Arabic to wrap naturally.
- Keep text essential. Remove repeated explanations beneath titles and their empty spacing. Preserve field labels, real record notes, units, definitions and retained source diagnostics. Specific approved removals in the principles document take precedence.
- Use the existing navigation pattern and one clear primary action for each task. Add controls only when requested or already approved.
- Keep card height content-driven. Standardize padding and alignment without forcing all cards to equal height or filling empty space with decorative content.

## 4. Preserve the meaning of visualizations

- Use exact data-driven charts. Preserve totals, eligible records, scales, denominators, zero/missing distinctions and filter scope. Put numbers inside proportional segments only when they fit legibly; keep exact small counts available through details and the exported matrix rather than enlarging segments or squeezing numerals.
- HH leadership includes only explicit **نعم**; TEC includes all other records, including blank. Hide zero sector rows independently and hide empty cohort panels. Use one comparable zero-based scale, totals immediately beyond actual bar endpoints, aggregate status totals and the detailed HH legend. Omit individual status labels beneath HH bars.
- Display true numeric zero as **–**, including zero percentages, without changing numeric data, geometry, sorting or accessible numeric values. Render generated **غير مسجل / غير مسجلة** placeholders as blank. Preserve dates, identifiers, narrative text and missing-state semantics. Hide source filenames in user-facing cards and their exports while retaining raw provenance.
- Show recorded progress as a readable numeric percentage; remove Harvey balls and circular progress indicators from app views and printed/PDF output, including tables, cards and details. A true zero remains **–** and a missing value remains blank. Retain approved linear completion and distribution bars and their source-defined meaning.
- Agenda quarter charts show per-category status totals by default. Only explicit quarter activation shows that quarter’s status breakdown; hover and keyboard focus alone must not change it. Keep keyboard focus visible without a persistent selected-bar outline. PDF always shows the aggregate status totals, independent of the last screen selection.
- The monthly legislation card combines the existing completed SLC cohorts into **منجز**, keeps unfinished late items within **قيد العمل** as **منها متأخر**, and uses one Green/Linen completion bar over the full scoped total. Preserve source cohorts and exact drilldown membership; combine history only when all required comparisons are eligible. Do not hardcode the approved illustration’s figures or add its review footnote. Apply the same composition to continuous and A4 PDFs.
- Identify whether a bar expresses completion, a status distribution, finance or measurement coverage before styling it. Do not interchange those meanings.
- Use solid financial bars for complete and partial numeric coverage. Do not restore hatching, completeness markers or the removed availability notes.
- Keep completion captions beside their percentages beneath the approved bars. Do not automatically add these captions to financial or strategy measurement bars.
- Base change colors on agreed performance meaning, not simply on whether a number increased. Keep neutral changes Taupe and unavailable comparisons unavailable.
- Do not introduce a new breakdown, shortcut, tooltip or explanatory note merely to make an audited discrepancy look resolved. Investigate the source and preserve existing diagnostics within the authorized scope.

## 5. Support Arabic, mobile and accessible use

- Set Arabic structure to RTL. Isolate Latin identifiers, dates, ratios, percentages and signed changes with explicit directional elements. Preserve approved physical placement; do not rely on Unicode reordering alone.
- Align visible text and numeric rows, not just box edges. Inspect actual Dubai and DIN rendering before adding optical corrections; avoid accumulating arbitrary per-label offsets.
- Reflow live pages at narrow widths while preserving approved type sizes, labels, controls and data associations. Use the specific mobile exceptions in the principles document.
- Keep controls keyboard accessible, visibly focused and meaningfully named. Preserve at least 44px action targets, logical focus order, Escape behavior and focus restoration for dialogs and menus.
- Use text in addition to color. Check approved foreground/background pairings and chart text alternatives. If a pairing fails contrast, resolve it with approved treatments or document a specific proposed change; do not silently invent brand colors.
- Respect reduced motion. Do not claim accessibility certification from a visual inspection.

## 6. Illustrate, implement and verify at the requested stage

1. For a new visual direction, show a concrete illustration before changing the working app. Keep before/after scope, scale and data comparable. Identify illustrative records and any temporary font substitutions.
2. Reuse approval already given for the same work. Do not create a repeated confirmation loop. The rejected additional-status disclosure and follow-up shortcut are excluded from this standard.
3. For implementation, reuse shared components and tokens; avoid new page-specific overrides where a shared semantic role exists. Scope selectors so a dashboard label change does not resize table content, legends or PDF text unintentionally.
4. Inspect actual output at desktop, tablet and phone sizes relevant to the change. Include long Arabic labels, mixed scripts, zero values, empty results and partial/all-selected filters where applicable.
5. Verify exported output independently. Check page geometry, background, margins, embedded fonts, Arabic shaping, scope, dates, figures, tables and footer clearance. A browser screenshot alone does not verify a PDF.
6. Reconcile source values and scope with `saytara-qa`. Use `saytara-data-analysis` when calculations or source comparisons need investigation, `saytara-data-visualization` for chart decisions, `saytara-dashboard-accessibility` for interactive behavior, and `saytara-report-exports` for exports. Use the appropriate authoring workflow for each format.
7. Run checks proportionate to the change. For documentation-only work, check consistency, links and package contents; do not claim a new app or PDF validation run.

## 7. Deliver precisely

- Provide the requested documents, illustration or implementation. Distinguish those outcomes clearly and report only relevant limitations.
- If the user requests a paired visual comparison, deliver a fixed full-composition image or PDF that remains viewable at full resolution. Do not make an automatically stacked mobile layout the only comparison.
- Preserve editability where requested. Do not replace exact charts, Arabic report text or tables with generated imagery to conceal layout problems.
- A supplied skill package is not evidence that an installed skill was replaced. Claim installation or deployment only when the corresponding operation was completed and verified.
