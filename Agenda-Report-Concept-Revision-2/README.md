# Agenda report — revised illustrations

**Revision 2 · 13 October 2026 · illustration only. The app remains v145 and is unchanged.**

This revision follows the [TEC skill and principles](https://github.com/ormbh/Performance-App-2/blob/2cee060b3bd1b2fef90a3f9b51f4b9de926affba/TEC-Apple-Inspired-Skill-and-Principles/SKILL.md), with the user's latest first-page header and chart redesign instructions taking precedence.

## Review the illustrations

- [Previous versus revised A4 chart placement](01-A4-Charts-Together.png)
- [Charts with all, selected-entity and single-topic filters](02-Filtered-Chart-Concept.png)
- [Long topic/entity text — before and after](03-Long-Text-Before-After.png)
- [First-page header versus continuation page](04-First-Page-Header.png)
- [Phone charts and records](05-Phone-Concept.png)

## Proposed changes

**One overview page.** Replace the pie and detached quarter charts with two compact views: approved agenda and emerging topics. Quarters are rows; statuses are columns. Every cell contains an exact count and a solid horizontal bar. Both chart views remain together on the first A4 landscape page, with no separate contents page ahead of them.

**Filtered charts.** Preserve the source status order, colors and effective-quarter rules. Bars share a zero-to-largest-cell count scale within each filtered overview. Each cohort has its own count and percentage denominator. Zero cells remain zero; entirely unused status columns disappear. Empty quarters are omitted under the existing report rule. An empty cohort retains its zero category total but does not occupy a chart panel. A single remaining panel fills the available width; an empty selection shows a clear empty state.

**First-page header only.** The example reads:

> مستجدات الأجندة السنوية  
> هيئة الطرق والمواصلات  
> يناير – سبتمبر 2026

The entity line appears only when an entity is selected. All-scope output omits that line. Title, entity and reporting period are not repeated on continuation pages. The period shown is an illustrative start-of-year-to-report-month label; it does not add a new deadline filter to the source data.

**More room for long text.** Main table order becomes sequence, topic, entity, deadline and status, with widths **4% / 45% / 28% / 9% / 14%**. Quarter section headings are compact. The narrow deadline column stays beside status and preserves every original row value, including cases where the source deadline differs from effective quarter grouping. Content stays 16px Dubai Regular on screen and 12pt in PDF; headings remain 18px/13.5pt Dubai Bold. The long-text board is explicitly a controlled typography specimen, not altered operational data.

**Remove the complete source-notes appendix.** Omit **ملحق ملاحظات المصدر**, every source-note box beneath it and the links leading to it. The actual emerging-topic records remain. Existing definitions, report narrative and any entered editorial notes/recommendations retain their separate meaning.

**Phone.** Quarter/status charts become readable quarter cards. Record tables reflow with every source field retained.

## Complete previews

- [All entities PDF](pdf/Agenda-All-Revision-2.pdf) — 117 illustrative topics, 12 pages.
- [Selected entity PDF](pdf/Agenda-Entity-Revision-2.pdf) — 10 illustrative topics, 3 pages.
- [All entities — full screen image](Agenda-All-Full.png)
- [Selected entity — full screen image](Agenda-Entity-Full.png)
- [All entities — static HTML](Agenda-all-Preview.html)
- [Selected entity — static HTML](Agenda-entity-Preview.html)

Both PDFs are **A4 landscape, 297 × 210mm, with 10mm insets**, and copyright/page numbers only in the footer. All charts fit on their first page. Table pages continue as needed; these fixture page counts do not imply a fixed page count for other data.

The HTML files are self-contained visual snapshots with embedded fonts and images, not functioning app replacements. Filter/navigation/export controls in those snapshots are illustrations. The PDFs use an isolated, measured browser composition for review; production PDF export code has not been changed.

## Verification

The existing illustrative workbook dated 30 September 2026 supplies 117 topics: 100 approved and 17 emerging. The selected entity هيئة الطرق والمواصلات has 8 approved and 2 emerging topics. Source records, ordered table rows, every original cell value, status counts and effective quarter grouping were retained.

Screen checks cover all, entity, multi-entity, single-topic, emerging-only, empty, undated and long-text states. The PDFs use the all-entity and selected-entity examples; all 15 pages were inspected, including first-page containment, continuation headers, table text, margins and footer clearance. PDFs contain self-contained glyph subsets and Unicode text. A populated source-notes specimen verifies whole-section removal; the fixture itself has no source-note rows.

This is a design review using illustrative data, not a new app release or operational-workbook audit. [Independent verification](verification/README.md) records the precise checks and limits.
