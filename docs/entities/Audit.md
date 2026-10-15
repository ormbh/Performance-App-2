# تقرير الجهات — focused audit

15 October 2026 (Dubai) · baseline v167 / commit 9710a31 · audit and illustration only

No production implementation, app ZIP update or change to the approved Revision 31 principles is included. This audit reuses the verified v167 runtime and existing source snapshots; fresh tests are limited to entity scope, affected rendering and one actual entity PDF download.

## Source and calculation contract

| Item | Verified basis |
| --- | --- |
| Available attachment | Saytara_2026_Mold_v2.xlsx; source cutoff 30 September 2026 |
| Raw entity-domain rows | 117 agenda + 164 council + 62 special projects = 343 |
| Attachment named rows eligible for entity report | **0** across all three domains; titles are blank |
| Populated illustration | Anonymized fixture, separately loaded and fingerprinted; 343 named rows |
| Entity-report grain | One eligible source row, counted once in the selected scope; not a unique real-world project across portfolios |
| Included domains | Approved agenda, emerging agenda, other agenda classifications when present, all recorded council decisions, special projects |
| Excluded domains | Strategic-budget portfolio, legislation and strategy KPIs; do not add them without validated entity relationships and metric contracts |
| Entity relationships | Primary entity and recognized contributor names remain distinct. A row matching both is counted once. Unresolved contributor text remains visible for review and does not become an inferred match |
| Filters | Union within entity/domain/relationship selections; intersection across different fields; stale or unmatched selections stay empty |
| Status and progress | Preserve recorded source status and recorded progress separately; 100% progress does not force completed status |
| Follow-up lateness | Recorded late status OR an exceeded applicable date for a nonclosed row, deduplicated; not a replacement source status |
| Dates | Ready agenda uses a recorded presentation date where available, otherwise the planned month-end; special projects use the recorded end-month. Meeting dates are not council follow-up deadlines |
| History | No previous workbook in this example; no historical arrows or invented changes |

The attachment cannot establish current operational performance totals. Its zero eligible rows reflect missing titles, not proof that the entities have no work. Source workbooks were read without modification or refresh.

## Confirmed issues and recommended corrections

| Priority | Observed in v167 | Recommendation |
| --- | --- | --- |
| High | Screen and PDF have different compositions. Actual native PDF prints summary and grouped records, omitting the screen's status charts, timeline and relationship context | Derive screen and PDF from one scoped content specification, preserving the same sections and reading order |
| High | The actual PDF hides the entity/scope heading and scope block. The tested selected entity is identifiable only through rows; role and domain selection are not clearly stated | Print the selected entity, relationship, domains and source cutoff once in a readable scope block |
| High | Narrow PDF status cells split **قيد المراجعة** into three lines, including an isolated final letter | Allocate status width and retain a natural badge line; adjust columns before reducing body text |
| High | Source-status counts and derived follow-up bands are both repeated in each domain. A ready topic can appear as date-late in the derived band while staying ready in the source chart | Keep one recorded-status chart per domain and show overdue/due-soon readings separately |
| Medium | Follow-up wording infers late booking from a missing presentation date | Use neutral wording: **تجاوز الموعد المخطط · موعد العرض غير مسجل**. A missing date does not prove a booking failure |
| Medium | PDF columns place status before entity, add an entirely blank contribution column in the sample, repeat administrative sheet/row references and restart numbering in every group | Use the shared leading sequence, meaningful field context, continuous main-list numbering and source references in record details |
| Medium | Emerging topics are still called **مستجدات الأجندة** | Use the approved display label **المواضيع المستجدة**, retaining source classification values |
| Medium | There is no compact contents row or contextual bridge to the corresponding scoped records/reports | Add contents matching the page sequence; preserve selected entity, relationship and exact row scope in destination links |
| Medium | All-entity organization rows can show primary plus contributor membership, while a primary-only entity filter shows primary rows only | Label the relationship basis beside totals and preserve it on drilldown; entity totals overlap and must not be summed or presented as a performance ranking |
| Cross-report defect | On the incomplete attachment, the special-project detail model accepts fallback **بدون عنوان** titles and includes 62 rows, while the entity model correctly includes zero named rows | After approval, align the special-project eligibility guard with the shared named-record rule and verify affected HH counts/filters/exports. This is an existing defect, not an implemented change |

The print HTML contains a source-filename field, but the final native PDF suppresses that scope block. **The tested final PDF does not print the workbook filename.** Administrative sheet/row references do remain. The issue is scope loss and unnecessary row metadata, not a confirmed filename leak in this download.

## Scope differences that must be explained, not forced to match

- The illustrative entity model includes **164 recorded council rows**. The council detail report uses its own eligibility rule: **70 eligible + 94 excluded = 164**. These totals answer different questions. Show the scope and bridge to exact records; do not silently replace 164 with 70.
- The entity model keeps **100 approved agenda + 17 emerging topics = 117** separate. The example has no other-classification agenda rows; a nonempty group must still be retained.
- The illustrative all-entity summary is **343 total, 157 completed, 186 open, 20 date-late and 13 due within 30 days**. Late and due-soon are overlapping readings of the open population, not additional total components.
- The selected illustration has **11 rows = 3 approved agenda + 1 emerging topic + 6 council decisions + 1 special project**. Its 4 completed and 7 open rows reconcile. The 1 overdue row remains **جاهز للعرض**; 2 more rows are due on the cutoff date. The 30-day window includes the cutoff day.
- Across the populated fixture, **39 rows have no recorded status**. Their rows remain in totals. A neutral chart segment and coverage note must retain them while individual missing status values remain blank.
- Recognized contributor membership is exact against the reference dictionary. Ten rows have unresolved contributor text in the illustrative fixture. Retain that text for review; do not infer entity ownership from it.

## Proposed page and table sequence

**Title/date and selected scope → contents → compact overview → domain status charts and legend → follow-up table → timing/relationship context → grouped main list → populated report notes/recommendations.**

Use the same domain order in charts, contents destinations and grouped tables: approved agenda, emerging topics, other agenda when present, council decisions, special projects. Empty groups and empty notes disappear. Keep a single report-level empty state when nothing matches. Distinguish missing source names from a genuine zero population.

Leading entity-table columns: **م ← الموضوع/المشروع ← الجهة المعنية ← الحالة**. Add recorded progress only where the source has that field, followed by the applicable date and populated notes. Keep contributors as labeled entity context. Council number/issuer/meeting date sit with decision context, omitting each empty field; meeting date is not placed in a deadline column. The council-specific detailed report retains its separately approved latest-decision layout.

The illustration uses the actual source-status values, shared colors, in-bar counts and one common count scale across domain panels. It does not add percentage labels or a composite performance score. Optional source notes retain their full text and field attribution. No source-note appendix or detailed-update cards are added to the entity overview.

## Implementation approach after approval

1. Reuse the existing entity relationships and scope model; apply only the audited eligibility correction and neutral follow-up wording where authorized.
2. Create one presentation specification for screen/PDF, with source statuses and date alerts kept separate.
3. Reuse shared filters, badges, tables, scope summaries and exact-record navigation. Do not broaden contributor scope through primary-only report links.
4. Add compact contents, consistent grouping/numbering, complete notes and scoped destinations; keep provenance in record details.
5. Compose the approved native PDF with the same content, readable Arabic and content-driven pagination.
6. Run focused model/filter tests, affected shared-component regressions, screen checks at desktop/phone widths and actual native downloads for full, filtered, empty and long-note scopes. Do not fix unrelated reports without evidence or broaden this stage into another redesign.

## Verification and limits

- Reused separate fresh-browser snapshots of the attachment and illustration, with filename and SHA-256 checks.
- **15 focused checks pass**: entity union, cross-field intersection, primary/contributor deduplication, unmatched scope, all generated selector membership, per-domain/status reconciliation, late/status separation, unavailable history, selected native-PDF membership and A4 geometry.
- **29 proposal checks pass**: all 11 records and chart counts, continuous numbering, four domain filters, empty follow-up hiding, resolved in-page links, approved fonts, fitting in-bar labels and no page overflow at 1560, 390 and 320px.
- Inspected the actual current two-page entity PDF and the new desktop, chart, follow-up/table and phone illustrations. Current PDF preserves the selected 11 record keys, sequential page counts and copyright, while the composition/scope/readability defects above remain open.
- Proposal entity/relationship fields are fixed example context; domain filtering and in-page navigation work. Production navigation and PDF export are not implemented in the prototype.
- No all-application re-audit, new production export pipeline, Office rendering, recalculation/query refresh or accessibility certification is claimed. Long-note PDF and shared-component regression tests are reserved for implementation, because no production component changed here.

See [machine-readable evidence](evidence.json), [full-page illustration](entity-full-1560.png) and [self-contained HTML proposal](review.html).
