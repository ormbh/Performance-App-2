# Search, navigation, print and bar guide — 11 October 2026

Search/navigation/printed-text changes are implemented in v131. Bar wording below is a proposed clarification; existing chart calculations and colors remain.

## Before and after

| Element | Before v130 | After v131 |
| --- | --- | --- |
| Search-home title | 38px DIN Next Arabic Regular, closer to field | 36px DIN Next Arabic Regular, centered in the existing logo-to-field gap |
| Logo/search field/action positions | Existing positions | Identical on desktop and mobile |
| Search-home top links | Monthly report + projects + menu | Menu only; monthly/projects remain inside it |
| Monthly primary links | Search + monthly + projects | Search + current monthly page + menu |
| Projects primary links | Search + monthly + projects | Search + current projects page + menu |
| Other loaded pages | Same three general links | Search + current page + menu |
| Search results | Monthly + projects shortcuts | One active Search link + menu, avoiding a duplicate Search link |
| Printed table body, names and notes | Dubai Regular 13.5pt / 18 CSS px | Dubai Regular 12pt / 16 CSS px |
| Printed status text inside tables | 13.5pt / 18 CSS px | 12pt / 16 CSS px |
| Printed column headings | Dubai Bold 13.5pt / 18 CSS px | Same |
| Screen table content/statuses | Dubai Regular 16px | Same |
| Screen column headings | Dubai Bold 18px | Same |
| Print title / footer | 24pt / 10.5pt | Same |
| Line spacing, row padding, colors and records | Existing | Same |

Two CSS pixels smaller means 18px→16px, equivalent to 13.5pt→12pt. This is a 1.5pt reduction. It is not a 2pt reduction. Print status text outside tables retains 13.5pt.

Desktop search: the old gaps above/below the title line were 32px/12px; they are now approximately 23.4px/23.4px. Mobile: 24px/12px→19.4px/19.4px. Geometry tests confirm logo, field and action bounds are identical within 0.05px. This is a search-home exception; other page titles remain38px.

## Data points in the supplied card screenshot

| Element | Screenshot example | Screen size | Approved font |
| --- | --- | --- | --- |
| Portfolio heading | محفظة المشاريع / محافظ المتابعة التنفيذية | 30px | DIN Next Arabic Regular |
| Card title | الأجندة السنوية / المشاريع الخاصة | 28px | DIN Next Arabic Regular |
| Total figure | 117 / 62 | 40px | DIN Next LT Arabic Regular |
| Agenda status figures | 43 / 16 / 58 | 34px | DIN Next LT Arabic Regular |
| Special-project subgroup total | 24 / 36 | 28px | DIN Next LT Arabic Regular |
| Special-project status figures | 12 / 10 / 26 | 28px | DIN Next LT Arabic Regular |
| Approved/new agenda totals | 100 / 17 | 28px | DIN Next LT Arabic Regular |
| Subgroup names | للقيادة / للأمانة العامة | 16px | Dubai Regular |
| Value/status labels | منجز / قيد العمل / الإجمالي | 12px | Dubai Regular |
| Change arrows and differences | ↑ +3 / ↓ −1 | 15px | Dubai Regular |
| Bar captions and percentages | نسبة المنجز / 27.8% | 12px | Dubai Regular |
| Meaningful information notes | جهة الطلب غير مسجلة… | 14px | Dubai Regular |
| Page title, outside this crop | التقرير الشهري للأداء والتنفيذ | 38px | DIN Next Arabic Regular |

## What the bars mean

| Bar | Data meaning | Colors |
| --- | --- | --- |
| Special-project single green strip | Completed project count divided by that subgroup total:12/24=50%,10/36=27.8% | Green#01831E; unused track Linen#EFEBE7 |
| Agenda/council/legislation multicolor strip | Each disjoint status count divided by that card’s eligible total. It fills the whole width to show the distribution. | Completed Green#01831E; active/pending Taupe#756B5F; ready Stone#ABA394; late Red#C00000; unclassified Silver#C8C7C7 |
| Monthly allocation strip | Allocated amount divided by approved budget | Taupe#756B5F; track Linen#EFEBE7 |
| Monthly invoices-spending strip | Invoices spent divided by approved budget | Teal#115E67; track Linen#EFEBE7 |
| KPI measurement strip | Measured indicator count divided by registered indicator count | Teal#115E67; track Linen#EFEBE7 |
| Project average-progress strip | Unweighted mean of valid source progress percentages | Teal#115E67; track Linen#EFEBE7 |
| Project status count/budget row bars | Relative count or money subtotal on the table’s shared0-to-largest-row scale | Completed-count Green#01831E; other count Teal#115E67; budget Taupe#756B5F |
| Hatched financial bar | Partial financial subtotal because usable values are missing for some projects | Stone#ABA394 + Sand#E7E0D3 diagonal pattern |

The bar does not always express a completion percentage. Its label and denominator determine whether it is a status distribution, completion rate, measurement coverage or financial ratio. Monthly simple financial sums and project matched-cohort financial ratios keep their source-defined denominators.

The cropped «44» belongs to a financial aggregate in this view. The crop omits the column heading, so its precise unit cannot be established from the image. **Hatch length shows the financial subtotal; 59/61 shows coverage of its source values.** Two projects have no usable numeric value for that metric; they are excluded, not counted as zero. The availability count is metric-specific.

## Partial-data note concept

| Current | Proposed | Reason |
| --- | --- | --- |
| قيم متاحة:59 من61 | بيانات جزئية · 59/61 ⓘ | Shorter while signalling incomplete data |
| Hover-only detail | Focus/tap/keyboard disclosure | Usable on desktop and touch devices |
| Values present in every row | Hide repetitive full-coverage note | No missing-value qualification to explain |
| Missing-value qualification in print | Keep a short visible note:59 من 61؛ قيمتان غير متاحتين | Export cannot depend on a tooltip |

The disclosure explains: «تُجمع 59 قيمة مالية من 61 مشروعاً؛ قيمتان غير متاحتين ولا تُحتسبان صفراً.» Keep the hatch and explain it once in a chart legend. Notes describing missing statuses, eligibility scope, unmatched cohorts or overspending still carry necessary meaning. Notes that only repeat a title can be removed.

## Bar colors

| Role | Code |
| --- | --- |
| Completed | #01831E |
| Late | #C00000 |
| Invoices, measurement, progress | #115E67 |
| Active/pending and allocation | #756B5F |
| Ready / partial hatch foreground | #ABA394 |
| Unclassified | #C8C7C7 |
| Unused track | #EFEBE7 |
| Partial hatch background | #E7E0D3 |
| Divider between on-time/after-time completion | #FCFBFB |

Both completed legislation cohorts remain green. Chart-series colors describe chart metrics; they are separate from the approved filled/outlined status badge surfaces. Existing project calendar series are documented in BAR-AUDIT-v130.md; this change does not silently recolor them.

## Native verification

Actual assembled before/after apps at device scale 1 and100% browser zoom. Search geometry unchanged at1920 / 390px. Search+current-page links checked on seven desktop/mobile routes; menus retain other pages, keyboard dismissal and focus. Search still returns the same four illustrative records. Monthly native A4 exports keep the same eight records and four pages; search exports keep four records and two pages. Body/status text changes18→16CSSpx, headings remain18px; padding, title and footer sizes match. Exact page counters verified. Screenshots/PDF report content is illustrative; the user’s operational workbook was not supplied.
