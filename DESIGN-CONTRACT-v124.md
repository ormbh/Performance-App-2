# TEC Apple-Inspired Design — v124 implementation contract

The approved monthly illustration and the user's latest decisions govern this
release. This is an implementation correction to the approved direction.

## Identity and hierarchy

- Reuse the supplied TEC logo, exact existing TEC colour tokens and licensed
  local font assets. Arabic headings use bundled DIN Next Arabic; body text and
  numeric values use bundled Dubai. Locally licensed Ample is optional for Latin
  headlines, with Dubai fallback. No additional font files are bundled.
- Use clear title → value/chart → supporting detail hierarchy, one shared spacing
  scale, restrained paper surfaces, modest radii, and content-based card heights.
  Shallow charcoal shadows and tints are derived treatments, not brand colours.
- Preserve section order and physical placement. Monthly strategy stays in the
  executive right column below legislation. Projects keep finance right / schedule
  left, status right / managers left, counts right / priority budgets left.

## Content and meaning

- Labels: «الأجندة المعتمدة», «المواضيع المستجدة», «الموازنة المعتمدة».
  Legislation's top note describes reviews and progress. Its SLC explanation
  appears once below the chart.
- Hide empty status and H/M/L categories; preserve their records in totals and
  source review. Keep zero distinct from missing. Retain meaningful quarter/year
  and missing-date context. Avoid repeated legends where labels identify segments.
- Late is always #C00000; completed is #01831E, including legislation completed
  after its deadline. Text labels accompany status colours.
- Both follow-up tables show late → frozen → cancelled → transferred, stable
  within each group. Names are neutral and regular weight. A comment alone does
  not add a project to follow-up. Preserve meaningful source notes.
- Financial percentages show their actual eligible cohort and budget basis beside
  the chart. Keep the portfolio total separate. Preserve exclusions, flags and
  unavailable-chart explanations; detailed diagnostics can collapse on screen and
  remain visible in print. Do not change native finance calculations.
- Completion percentages/bars and ↑/↓ changes remain source-derived. Compact
  change indicators appear only for valid comparable historical snapshots.

## Interaction and verification

- Preserve filter union within a field / intersection across fields, reset,
  drilldowns, suggestions, sorting, pagination, local upload and error recovery.
- Check keyboard focus, controls, RTL and mixed-direction numbers, text alternatives,
  mobile reflow, and desktop/print reading order on actual rendered views.
- Check source totals and comparison guards independently of styling. Inspect
  populated, partial-financial, missing-value and historical-comparison states.
- Inspect delivered A4/A3 outputs and reconcile their filtered numbers with screen.
- The attached mold is authoritative for its source/template rules but has blank
  project titles and financial values. Populated QA fixtures are illustrative and
  excluded from the deliverable. The operational workbook shown in screenshots
  was not uploaded; its numerical reconciliation cannot be claimed.

The main TEC Apple-Inspired Design, Saytara QA and dashboard accessibility skills
were read. The TEC skill's linked reference pages were unavailable from the skill
provider; existing approved assets and explicit conversation decisions establish
the identity and layout rules above. Verification records actual tested states
and limits, rather than claiming formal accessibility or Apple certification.
