# Agenda report — TEC design illustration

**Preview only · 13 October 2026 · app v145 is unchanged.**

This proposal applies the approved [TEC skill](../TEC-Apple-Inspired-Skill-and-Principles/SKILL.md) and [design principles](../TEC-Apple-Inspired-Skill-and-Principles/references/TEC-Apple-Inspired-Design-Principles.md) to the agenda report. The completed monthly dashboard and search pages retain their existing design.

## Before and after

1. [Desktop opening](01-Desktop-Before-After.png)
2. [Complete executive summary](02-Summary-Before-After.png)
3. [Quarter tables](03-Tables-Before-After.png)
4. [Phone opening and record cards](04-Phone-Before-After.png)
5. [Selected entity and source-notes appendix](05-Entity-and-Appendix.png)
6. [A4 landscape PDF](06-PDF-Before-After.png)

| Area | Proposed treatment |
| --- | --- |
| Header and navigation | Existing shared TEC masthead, Search + current report + menu, one Download PDF action. Selected entity appears directly below the title; date remains. |
| Filters | Shared Sector, Organizational unit, Entity and Topic type fields; first-selected +N / الكل summaries. Phone fields open from تصفية. |
| Report editing | Title, period, notes and recommendations grouped under إعداد التقرير. |
| Screen reading order | Executive summary first; simple links to topic tables and emerging topics. |
| Summary | Annual-agenda total and two equal boxes for approved agenda and emerging topics. Existing status pie, quarterly bars, definitions and report narrative retained. |
| Tables | Dubai Regular 16px content and badges; Dubai Bold 18px headings; Ink text, Linen headings and restrained row separators. All columns and record order retained. |
| Phone | One column, 16px outer gutters, readable record cards with all five fields. |
| Source-notes appendix | Remove ملحق ملاحظات المصدر and its links from this report. Keep the separate emerging-topic appendix and entered report notes/recommendations. |
| PDF | A4 landscape, 10mm margins, first title + date + selected entity + sector/unit scope. Copyright and page numbers only in the footer; no continuation masthead. |

The user's two supplied screenshots show the council report. This illustration applies the corresponding controls/appendix treatment to the **agenda report**, retaining agenda terminology and counts. No council-report implementation is included.

## Complete review files

- [All entities — full screen image](Agenda-All-Full.png)
- [Selected entity — full screen image](Agenda-Entity-Full.png)
- [All entities — standalone HTML](Agenda-all-Preview.html)
- [Selected entity — standalone HTML](Agenda-entity-Preview.html)
- [Before PDF](pdf/Agenda-Before.pdf)
- [After PDF](pdf/Agenda-After-Concept.pdf)

HTML files are self-contained **static illustrations**, not app replacements. Fonts and logos are embedded; native disclosure sections can be opened, but filter, navigation and download controls do not operate as an app. Open the PNGs or PDFs for a fixed illustration. The actual v145 app remains the place to use live reports.

## Typography and color

Screen: title 38px DIN Next Arabic; section 30px; card title 28px; total 40px DIN Next LT Arabic; status figure 34px; category figure 28px; category name 18px Dubai; metric label 16px Dubai. Table content/status 16px Dubai Regular, headings 18px Dubai Bold. Supporting text 14px; field labels 12px.

PDF: first title 24pt DIN, entity/scope 10.5pt Dubai, section titles 16pt DIN, table headings 13.5pt Dubai Bold, content 12pt Dubai Regular.

Ink `#4F4E4E` · Taupe `#756B5F` · Teal `#115E67` · Paper `#FCFBFB` · Linen `#EFEBE7` · Sand `#E7E0D3`. Existing chart status colors and meanings are preserved.

## Verification and limits

The existing illustrative workbook dated 30 September 2026 supplies 117 topics: 100 approved-agenda topics and 17 emerging topics. The entity example هيئة الطرق والمواصلات contains 10 topics: 8 approved and 2 emerging. Main status/quarter charts retain their approved-agenda scope. These are illustrative figures, not a new operational report.

The ordinary fixture contains no source-note rows. Board 5 uses a clearly labelled, controlled note added only to the temporary preview DOM to demonstrate removal; the workbook is unchanged. Unclassified topic types, undated groups and populated editorial notes are not represented by these fixture cases.

All ordered records, original table cell text, chart counts, proportions, colors and pie geometry were checked against v145. Desktop, tablet and phone widths were reviewed. Both PDFs contain five A4 landscape pages for this entity fixture; all pages were rendered and inspected. This is not a promise of a fixed page count for other scopes.

All 188 production app files match the released v145 ZIP. The HTML snapshots render with networking disabled and embedded assets. Direct file:// navigation is blocked by managed-browser policy here, so a native file-click launch is not claimed. This visual review is not accessibility certification.

[Independent review](verification/INDEPENDENT-REVIEW.md) · [PDF details](pdf/README.md)

No production app changes are included. Approval of these illustrations precedes implementation.
