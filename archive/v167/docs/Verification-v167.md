# Performance App v167 — project portfolio

15 October 2026 (Dubai) · TEC design principles Revision 31

## Applied

The approved full-page portfolio proposal is implemented in the workspace and formatted report. The overall total and compact summary lead the page; budget sits physically right and the deadline chart left on desktop. Deadline bars use one project-count scale across all years and quarters, with endpoint totals and readable in-bar counts. Recorded progress, completed-project share, allocation, spending and work value keep their separate definitions and denominators.

The status breakdown retains unknown categories, uses the approved badge colors and a compact detailed legend, and presents full financial values. Frozen displays as **مجمّد** while preserving source codes and existing filter tokens. Zero displays as a dash; missing numeric values stay blank. Empty follow-up sections disappear. Manager ranking retains its existing 50/50 unfinished-count and budget weighting.

All eight filters, dependent choices, union/intersection behavior and exact-record drilldowns remain available. The main and follow-up tables share the leading RTL sequence **م ← المشروع ← الجهة المعنية ← الحالة ← نسبة الإنجاز ← موعد الإنجاز**; follow-up appends **ملاحظات**. Entity, sector and unit stay distinct. Populated project context and full source notes are retained. Phone tables scroll within their own region with readable text and keyboard access. Optional editorial notes appear at the end, and their contents link updates immediately.

The PDF retains A4 portrait, the same source content and section order, current title/period, active scope, page numbers and copyright. Its compact first page holds the overview and budget section. Deadline headings fit on one line, table headings repeat on continuation pages, and long notes continue without truncation. Portfolio adds no cover or separate contents page.

Financial eligibility now uses one strict decimal reader across the portfolio, report, monthly financial measures and comparisons. Valid decimal text and true zero remain eligible; hexadecimal text, booleans, errors, nonfinite values and nonnumeric text do not become money. Existing independently defined source populations remain distinct: monthly source sums can include untitled rows while the portfolio requires a project name. Legacy cached financial changes are unavailable unless their source explicitly declares the compatible parsing contract; uploaded previous workbooks are recalculated consistently. Nonfinancial history remains available.

## Verification

The release was checked against the approved proposal, Revision 31 principles, unchanged source files, v166 model fingerprints, exact filtered record sets and the actual native PDF output. Machine-readable results identify the tested runtime hashes and distinguish comprehensive regression runs from final-build checks.

- Source-level financial contract checks and independent cross-report regression pass. Tests cover numeric types, real zero versus missing, source membership, status definitions, historical comparisons and actual financial drill interactions.
- Fresh-browser checks cover the eight filters, combined/empty scopes, formatted report and main-list navigation, record return links, chart drills, keyboard behavior and editorial contents. The final page was inspected at desktop, tablet and phone widths, including 320px, with no page-level horizontal overflow.
- Nine actual native PDF downloads cover the workspace, formatted report, compact display, completed filter, empty filter, full main list, custom title/period, long notes and the incomplete attachment. Screen/PDF record order, complete notes, count labels, internal destinations, Arabic font glyphs, cell bounds, repeated headings, page bounds, copyright and page numbering pass.
- The illustrative full portfolio exports to **6 A4 pages**; its 84-record main list to **14 pages**. The controlled long-note case uses **20 pages**. Empty scopes and the incomplete attachment each produce **one page**, without a blank continuation page. Filtered completed projects use **5 pages**.
- Build freshness, JavaScript syntax, runtime file hashes and ZIP integrity pass. Original Arabic fonts and the native PDF engine are unchanged. Source workbooks remain byte-for-byte unchanged.

See [screen and interaction evidence](checks/screen.json), [independent data regression](checks/regression.json), [financial contract checks](checks/financial-contract.json), [native PDF evidence](checks/pdf.json), [PDF inspection](portfolio/PDF-verification.md) and [release hashes](release.json) for exact counts, scope and limitations.

## Source scope and limits

The available attachment has **84 raw project rows but zero eligible named projects**: its project names, manager names and financial values are blank. The app and PDF correctly show the empty eligible population and explain the excluded rows. The populated public screenshots and PDF use an explicitly illustrative, anonymized workbook; their 84 projects and financial figures are not claims about the attachment. No missing operational values were filled from the example.

Testing used the clean runtime over local HTTP in Chromium. Cold file opening was not verified in this release; the managed browser blocked file navigation in the prior environment check. No Excel recalculation, Power Query refresh, Office rendering or full accessibility certification was performed. Current operational totals require a complete operational workbook. Source workbook dates remain independent of the release date.

## Delivery

The clean app ZIP contains exactly **26 runtime files**, with no workbook, source modules, previews or QA folders. The development source and previous release are archived separately.

- [Actual illustrative screen and PDF](portfolio/README.md)
- [Design principles — Revision 31](TEC-Design-Principles.md)
- [Approved proposal and audit](../archive/v166/docs/portfolio/README.md)
