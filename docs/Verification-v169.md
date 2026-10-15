# Verification — v169

Date: 15 October 2026. Baseline: v168 (`627338f6cc5f1e729f8e7748a09f4a0fe3e0781d`). Principles revision 33. Approved matching contract remains `approved-connections-2026-10-09`; no guessed identities or source-workbook edits.

## Delivered behavior

- Monthly +/− opens the exact metric in the same tab, focuses the explanation and highlights relevant fields. Both incoming and outgoing contributors remain visible, including zero-net movements. Other source edits are separate. The tested query, full-record route, return context and file setup retain their intent.
- Domain/metric overview tables replace mixed grand totals and paired total bars. Money and measurement use separate units. Agenda, emerging topics, special-project cohorts, council follow-up eligibility and completed-legislation definitions retain their established populations. Late within legislation work remains a subset. Missing required fields remain unavailable, not zero.
- Source-field comparison is shared with entity history and includes notes/narratives, managers and other relevant source fields. Possible mutable-key changes are unresolved diagnostics, never replacement identities. Duplicate/missing keys remain quarantined. Source absence is not proof of cancellation or completion.
- Count and monetary contributions reconcile. Department transfers plus status changes do not subtract from a status the old unit never held. Organizational levels are not added into a disjoint total. Rates/averages show eligible coverage and the matching measured cohort, without fabricated additive record contributions.
- Supported browser storage retains the validated binary workbook pair locally, through small versioned references. Large pairs survive refresh. Explicit tabs share a session identity and retain a known version; older tabs announce newer files and update deliberately. Ending a session removes its stored versions and clears the tested open tabs. Sessions expire after 24 hours; expired data is cleaned on the next successful app start.
- Blocked storage has a verified small-file fallback and an honest unsaved warning for oversized/quota cases. Live files remain available. A retained older pair is not silently claimed as a saved replacement. No workbook is transmitted to a service.
- Native PDFs retain both snapshot dates, selected scope/metric/query and ordered source rows. Arabic headings fit columns; long rows continue with repeated headers and numbered footers. Drawn legend swatches avoid unsupported font glyphs.

## Verification performed

**159 top-level focused checks passed** on the clean 26-file runtime. No browser runtime exceptions were recorded. The final loaded JS hash agrees with the clean runtime manifest.

| Suite | Checks | Scope |
|---|---:|---|
| Comparison, browser, native PDF | 80 | Contributions, exact landing, duplicates/missing keys, possible key changes, notes, filters, keyboard/dialog focus, desktop/phone tables, explicit tabs, version refresh, reload and overview/focused/other/empty PDFs |
| Shared calculations and exports | 35 | v168 raw/monthly/agenda/HH/council/portfolio calculation fingerprints, financial/average and 85-line note PDFs, shared portfolio export regression |
| Retention | 14 | Large workbook pair, tiny references, upload intent, refresh, optional tab refresh, cross-tab session ending, blocked store and quota fallbacks |
| Final focused regressions | 30 | Compound attribution, shared note detection, real date-only recalculation, full-record route, transfer/unresolved-query PDFs, colors, blocked popup, entity export, file clearing, original source integrity |

The reused underlying portfolio PDF assertions also pass. The overview is two A4 portrait pages. Selected +1, other edits, financial, average, empty and unresolved-search outputs are one page each; transfer output is content-driven. The controlled 85-line source note continues across nine pages without truncation. Portfolio retains its six-page export and selected entity output its four-page plan.

Actual native PDFs were rendered and inspected. Selected row sequences agree, all native source text lines are placed, headings fit their columns, text is selectable, and no replacement glyph or out-of-page text was found. Comparison outputs are A4 portrait. Captures and example PDFs are illustrative test outputs, not operational figures. This verifies the app's native export, separately from the earlier Chromium proposal mockup.

## Source and limits

Tests use the existing anonymized `ILLUSTRATIVE-monthly-preview.xlsx`, SHA-256 `4b10d057090cf522d73c28667d29b1875b0d7b37e75892f5eb676c82b7fbcf08`, plus explicitly controlled copies/in-memory changes. Originals remain unchanged. The supplied operational attachment has incomplete named records; no filled operational current/previous pair was supplied. These checks validate behavior and calculation contracts, not the user's live department deltas.

Managed Chromium rejects `file://` navigation with `ERR_BLOCKED_BY_ADMINISTRATOR`. Direct-file reload/new-tab behavior remains **not run**, with no policy bypass attempted. Hosted/local-HTTP Chromium was tested. Other browsers, mobile native browsers and screen readers were not certified. This is not WCAG certification, an Excel/Power Query refresh, or an Office editability claim. Storage remains subject to browser policy/quota; its fallback warnings are intentional.

[Results and exact runtime hashes](checks/comparison.json). The clean ZIP contains no workbook, source modules, QA scripts or screenshots. Readable development source is archived separately.
