# Monthly comparison: audit and full workflow proposal

Review date: 15 October 2026 (Asia/Dubai). Baseline: v168, repository commit `627338f6cc5f1e729f8e7748a09f4a0fe3e0781d`.

**Stage: audit and illustration only. No application implementation, source-data amendment, matching-contract change, principles revision or release ZIP change.**

## Scope and evidence

This review covers the comparison overview, monthly metric links, department/sector/entity movements, status and numerical changes, matching confidence, previous/current uploads, new tabs, empty/unavailable states, and the intended screen/PDF presentation. It reuses the v168 baseline and existing QA harness; it does not repeat the whole-application audit.

Application checks use the existing anonymized illustrative workbook (`ILLUSTRATIVE-monthly-preview.xlsx`, SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`) and clearly controlled previous copies or in-memory changes. Large-file checks add harmless unreferenced ZIP content to valid workbook copies. Originals remain unchanged.

The previously supplied operational attachment has incomplete named records and is not a populated current/previous operational pair. These results establish reproducible app behavior, not the user's live department totals. The four illustrations use explicitly fictional values; their examples must not be imported into operational data. `P01`–`P07` are illustrative stable IDs, not newly approved application keys.

## Findings

| Priority | Finding | Evidence and implication |
|---|---|---|
| High | Monthly +/− does not land on the explanation | A real +1 click preserved `specialGsDone` and scope, but opened at scroll 0; detail began at y=1328 with viewport height 1100 and no focused target. |
| High | Broad edits are mixed with contributions to the clicked number | Special-project total remained 62→62 while the default Changes list showed two edited records. Those edits were real but did not explain a count difference. |
| High | Uploading a previous workbook loses the requested metric | In a comparison tab, `agendaTotal` became an empty view after upload, while the URL still named `agendaTotal`. Setup can erase the user's intended destination. |
| High | Tabs retain independent file pairs | Previous workbook uploaded in the child was available there but absent in the parent. Returning to the parent can prompt another upload. This is a workflow limitation, not proof of arbitrary same-tab data loss. |
| High | Browser storage failure loses reload retention | Two valid files, each below the app's 3.5 MiB individual saving limit, exceeded combined session storage. In-memory comparison remained available; storage was absent and reload returned to upload with neither file. |
| High | Mutable key fields can split a real record | Changing sector in controlled budget-project and legislation records produced one absent and one added entry. Their approved keys contain sector. Titles and Source.Name are mutable components in other keys too. |
| Medium | Source-field comparison is incomplete | A notes-only special-project edit was classified unchanged. Comparison/context fields omit some notes, descriptions, managers and other source fields; it should not imply every source field was checked. |
| Medium | Legislation wording lags the current metric | Comparison labels/methodology still describe “في الموعد”, while the model uses current `legDone`, which combines the defined completed cohorts. Wording must reflect the monthly report's actual definition. |
| Medium | Overview obscures the question | Mixed record totals, paired bars, change-type counters, repeated context tables and many change tabs precede or compete with the selected explanation. A mixed total is not a meaningful performance measure across these domains. |

Primary inspected modules: `assets/js/app.js` (tab handoff, session saving/restoration, file load, monthly routing); `assets/js/views/comparison.js` (overview, records and methodology); `assets/js/model/comparison.js` (matching, membership and movements); `assets/js/model/schema.js` (approved keys); `assets/js/model/rules.js` and `assets/js/views/dashboard.js` (metric definitions and changes).

## What already works and must be preserved

- Matching indexes the full datasets before applying organizational scope. The earlier recommendation to compare globally is already satisfied in this part of the code. The improvement is attribution, identity reliability, navigation and explanation—not a claim that the current join is department-only.
- With an unchanged unique key, a transfer yields −1 in the old unit, +1 in the new unit, and no change overall. A simultaneous status change affects the appropriate status metric separately.
- Duplicate keys are quarantined on both sides; missing keys are not silently paired. The controlled duplicate test produced three unresolved source rows, with no arbitrary match.
- Ordinary same-tab navigation retained both loaded files in the tested sequence. A small file pair also survived reload. The large-pair retention failure is distinct from these passing cases.
- Preserve date confirmation, same-file rejection, missing-table safeguards, raw typed key values, source exclusions and existing unavailable-history reasons.

## Proposed comparison flow

### From the menu: overview

Show period, scope and file-pair version, followed by a domain/metric table in the monthly report's order. Keep approved agenda and emerging topics separate. Show previous, current, net and the relevant completed/measured figure with an entry to details. Do not combine projects, decisions, indicators and money into one primary grand total.

A zero net remains visible as a dash and does not imply no changes. Show incoming/outgoing movement when present. The prototype illustrates unit B retaining two records while one enters and another leaves.

Use tables here instead of paired total bars: the decision is about explaining a difference, not comparing unrelated category sizes. Retain the established status colors, typography, restrained panels and compact legend. Monetary and rate measures remain separate and labelled.

### From monthly +/−: focused explanation

Retain the originating metric, portfolio/cohort, sector, unit, concerned entity, period and source-pair version. Open the explanation immediately in the same tab, with focus on its heading and the relevant rows/fields highlighted. Back restores the monthly scope and position. “Open in new tab” remains an explicit option.

For counts, reconcile:

`current = previous + incoming − outgoing + unresolved residual`

Do not force the residual to zero when identity is uncertain. Do not interpret record edits as contributions merely because they appear in the same metric population. Show both directions even for a positive change.

Use the RTL detail sequence:

**م ← الموضوع / المشروع ← سبب التغير ← السابق ← الحالي ← الأثر على المقياس**

The source and destination unit, status and other relevant fields appear together for a compound change. Field labels and signed values explain meaning without relying only on color. Full source information and provenance remain available on demand; technical source filenames do not become primary card labels.

Keep three distinct views: effects on the selected number, other source-field edits within its population, and unchanged records. Put identity review in its own visible section. Do not sum overlapping categories such as transfers plus status changes as if they were distinct records.

### Attribution and identity

For every exact matched record, derive its before/after membership at every affected organizational level and metric. Preserve separate reasons for organizational transfer, status change, eligibility/date recalculation, field-value edit, and presence in only one source.

Keep the approved matching contract until a replacement is explicitly approved. Preferred long-term design: an immutable source identifier, validated unique in both snapshots. A source-owner-approved mapping can resolve existing identity changes. Do not silently drop sector/title/Source.Name from a key or finalize fuzzy matches. One-sided keys establish presence under the current key, not proof that the underlying work is new, deleted or completed. Diagnostic candidates remain unresolved until confirmed.

Account for blank/unassigned departments, invalid sector–department combinations, multi-entity membership rules and scope transitions. Transfer conservation applies to the same eligible overall population. Never sum overlapping entity memberships into a supposedly disjoint total. A transfer is not itself a data-quality error; an invalid organizational relationship is a separate observation.

### Money, percentages and calculated dates

- Financial reconciliation uses project-level amounts in the same currency and population. A pure departmental transfer redistributes amounts without creating money. Missing/invalid values remain distinguishable from valid zero; retain the strict decimal-reader contract and its diagnostics.
- Averages and rates show eligible numerator/denominator or sum/count, and percentage-point differences. Do not invent an additive per-record attribution for an average. The illustration explicitly shows a higher average caused by expanded measurement coverage while the shared cohort remains unchanged.
- Keep monthly all-row financial sums distinct from named-project portfolio sums where the established rules intentionally differ.
- Preserve the actual completed-legislation definition and late-within-work subset; do not count overlapping populations twice.
- A different calculation date may change lateness without a source-cell edit. Explain it as recalculation, with both dates visible.
- Aggregate history alone cannot supply a record list. Show its valid totals, disclose the limitation beside them, and request the previous source only for the unavailable detail. Do not manufacture history or turn unavailable values into zero.

### File retention and new tabs

Use one versioned working session holding both validated workbooks and confirmed dates. Save files as binary data in a supported browser store rather than repeatedly encoding both into limited sessionStorage. Validate write/read and handle quota or browser-policy failure explicitly. Treat IndexedDB as a candidate to verify in hosted and direct-file use, not a capability already certified for every browser.

Stage and validate replacements before committing a new pair/version. Never silently mix a new current file with an unrelated previous file. Retain the originating drill intent through setup and resume it when the required data is ready. Do not erase a valid saved version merely because saving its replacement fails; identify any difference between active and retained versions explicitly.

Explicit new tabs reference the same session and a known file-pair version. Loading/replacing a file is a session action; older views identify that newer data exists and refresh deliberately. They must not silently show recalculated values against a different snapshot. Provide clear session-ending/cache-removal controls and a documented retention/expiry policy. Do not promise automatic deletion merely because a tab closes. File handoff remains available as a tested fallback where browser storage is unavailable; normal same-tab navigation must still work.

## Illustrations

1. `overview.png`: full monthly comparison overview.
2. `focused.png`: a department-total +1 explained by two incoming records and one outgoing record, including a transfer plus status change.
3. `session.png`: file pair, dates, versioning, explicit new-tab behavior, aggregate-only history and retention failure.
4. `measures.png`: money, average/coverage changes, unresolved identity and unavailable/empty states.

`comparison-proposal.pdf` is a four-page A4 portrait design review pack. Page 3 explains file management; it is not a proposal to include upload settings in an operational report. These are prototype PDFs made with Chromium, not a verified change to the app's native PDF pipeline.

The synthetic seven-project example reconciles 6→7 overall, unit A 4→5 (incoming 2, outgoing 1), unit B 2→2 (incoming 1, outgoing 1), completed 2→4, ready 1→0, and in-work 3→3. Other overview domain figures are design-only placeholders, not audited operational totals.

## Verification performed and release gates

Current study evidence is recorded in the adjoining JSON files:

- Six passing focused model checks: old-unit movement, new-unit movement, global conservation, simultaneous status change, duplicate quarantine and missing-key handling.
- Three additional model checks reproduce limitations: two sector-key splits and an undetected notes-only edit.
- Browser evidence reproduces the offscreen +1 landing, lost drill intent after upload, independent tab file state and large-pair reload loss. Small-pair reload and the tested ordinary navigation sequence pass.
- All four prototype views load Dubai font, have no desktop or 390px-wide page overflow, and preserve real horizontally scrollable tables on narrow screens.
- Four A4 portrait prototype pages, one page per illustration; selectable text and no extracted words outside page bounds. Actual PDF raster pages were inspected for Arabic, table alignment, clipping, legend and pagination. This is prototype layout verification, not accessibility certification or native-production PDF verification.

After design approval, implementation should proceed in three focused groups: matching/attribution and field coverage; session/routing; screen/PDF rendering. Required release checks include exact contribution reconciliation for each affected unit/metric, equal incoming/outgoing zero-net cases, organizational moves plus status/amount changes, data-quality anomalies, duplicates/blanks/missing tables, financial contracts and rate denominators, dates, filter unions/intersections, upload-intent return, refresh/new-tab/replacement/quota/blocked-storage handling, Arabic layouts and long notes, selected PDF scope, repeated headers, empty states and pagination. Regress shared monthly, entity, portfolio and report links against the verified baseline. Use the app's native export for production validation.

Direct-file/browser-specific storage and popup behavior remains unverified for the user's actual browser. No filled operational current/previous pair was supplied for this audit. No production changes or new clean ZIP are delivered at this stage.
