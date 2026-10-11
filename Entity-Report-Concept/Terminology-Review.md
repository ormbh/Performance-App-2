# Entity report — terminology before / after

Concept revision only. The app and approved canonical TEC standard are unchanged. Source names, statuses, notes, dates and metric definitions remain intact.

| Part | Previous concept | Revised terminology | Screen font and size |
| --- | --- | --- | --- |
| Page title | محفظة الجهة | محفظة الجهة — retained | DIN Next Arabic Regular · 38px |
| Current navigation | تقرير الجهات | تقرير الجهات — retained | Dubai Regular · 16px |
| Menu button accessible name | القائمة | صفحات التطبيق | Icon 20px · target at least 44px |
| Relationship filter | نطاق العلاقة | العلاقة بالجهة | Dubai Regular · 12px label / 16px value |
| Area filter | مجالات التقرير | مجال التقرير | Dubai Regular · 12px label / 16px value |
| Reset action | إعادة ضبط المجال | عرض جميع المجالات | Dubai Regular · 16px |
| Repeated section heading | محفظة الجهة | توزيع البنود | DIN Next Arabic Regular · 30px |
| Priorities section | أولوية المتابعة | أولويات المتابعة | DIN Next Arabic Regular · 30px |
| Due-soon section | الاستحقاقات خلال 30 يوماً | الاستحقاقات خلال 30 يوماً — retained | DIN Next Arabic Regular · 30px |
| Emerging-agenda category | مستجدات الأجندة | المواضيع المستجدة | DIN Next Arabic Regular · 28px card title / Dubai Regular · 16px filter value |
| Total summary label | إجمالي بنود الجهة | إجمالي البنود | Dubai Regular · 14px |
| Open count | غير المغلق 7 بنداً | البنود غير المغلقة: 7 | Dubai Regular · 14px |
| Completion share | المنجز من إجمالي البنود | المنجز / الإجمالي | Dubai Regular · 14px |
| Completion bar caption | المنجز من إجمالي البنود | نسبة المنجز | Dubai Regular · 14px |
| Inclusive late metric | متأخر أو تجاوز الموعد | متأخر حسب الحالة أو الموعد | Dubai Regular · 14px |
| Mixed-scope record column | الموضوع / المشروع | البند | Dubai Bold · 18px |
| Status / progress column | الحالة المسجلة / الإنجاز | الحالة المسجلة / نسبة الإنجاز | Dubai Bold · 18px |
| Agenda status column | الحالة المسجلة / الإنجاز | الحالة المسجلة | Dubai Bold · 18px |
| Personnel column | المنسق / مدير المشروع | منسق الأمانة العامة / مدير المشروع | Dubai Bold · 18px |
| Recorded progress | الإنجاز المسجل | نسبة الإنجاز المسجلة | Dubai Regular · 14px |
| Missing recorded progress | الإنجاز غير مسجل | نسبة الإنجاز غير مسجلة — only if the source defines the field | Dubai Regular · 14px |
| Remaining-day count | متبقي N يوماً | الأيام المتبقية: N | Dubai Regular · 14px |
| Date and status alert column | تنبيه الموعد | تنبيه المتابعة | Dubai Bold · 18px |
| Follow-up list action | عرض جميع حالات المتابعة | عرض جميع بنود المتابعة | Dubai Regular · 16px |
| Close record list | إغلاق التفاصيل | إغلاق قائمة البنود | Dubai Regular · 16px |
| Definitions disclosure | تعريف المقاييس والعلاقة المسجلة | تعريف المقاييس | Dubai Regular · 16px |
| Special-project achievement field | المنجز خلال الفترة | المنجز للآن | Dubai Regular · 14px label / 16px source value |
| Note and recommendation fields | الملاحظات / التوصيات / ملاحظات المقرر | Exact portfolio source labels and attribution | Dubai Regular · 14px label / 16px source value |
| Source filename label | Source.Name | اسم ملف المصدر — filename retained verbatim | Dubai Regular · 14px label / 16px source value |
| Record-detail classification | المحفظة | مجال التقرير | Dubai Regular · 14px label / 16px value |
| Organizational source fields | القطاع / الوحدة | القطاع and الإدارة as separate source-labelled fields | Dubai Regular · 14px label / 16px source value |

## Date alerts are separate from recorded status

| Actual condition | Revised alert / explanation |
| --- | --- |
| Planned date exceeded; recorded ready status; presentation date blank | تجاوز الموعد المخطط · موعد العرض غير مسجل |
| Deadline equals report cutoff | مستحق في تاريخ التقرير |
| Planned date within the window | الموعد المخطط خلال 30 يوماً |
| Recorded presentation date exceeded | تجاوز موعد العرض المسجل |
| Project end date exceeded | تجاوز موعد انتهاء المشروع |
| Source records late status only | متأخر حسب الحالة المسجلة |
| Source records late status and the date is overdue | متأخر حسب الحالة ومتجاوز للموعد |
| Source explicitly records no council update report | لا يتوفر تقرير بالمستجدات |
| Source has no presentation-date fields | حقول موعد العرض غير متاحة في المصدر |

The source status badge remains verbatim, including «جاهز للعرض», «قيد التطوير», «قيد المراجعة» and «منجز». An exceeded date does not rewrite that status. A missing date does not prove booking failure or create a required action.

## Scope nouns and preserved values

| Selected scope | Record noun / count noun |
| --- | --- |
| Approved or emerging agenda | الموضوع / المواضيع |
| Council decisions | القرار / القرارات |
| Special projects | المشروع / المشاريع |
| Mixed scope | البند / البنود |

The same rules apply to drilldowns, table headings, count captions, empty states and completion-bar text alternatives. Source identifiers and raw classification strings remain unchanged. Agenda has no progress-percentage field, so the concept omits progress hints rather than labelling that field missing.

Illustrative counts remain **11 total, 4 completed, 7 open, 1 late, 2 due within 30 days; 36.4% completed**. The source-row split remains **3 approved agenda + 1 emerging agenda + 6 council decisions + 1 special project**.

## Reused visual standard

DIN headings and figures; Dubai body and controls. Headings Charcoal **#333333**; essential labels and table body Ink **#4F4E4E**; secondary metadata Taupe **#756B5F**. Table body and badges **16px**, headings **18px Dubai Bold**, line height **1.6**. Control focus **2px Teal #115E67 with 2px gap**; primary hover **Paper #FCFBFB on Charcoal #333333**. No subtitle is added beneath a title.

This is a terminology revision of the concept, reviewed using the TEC Apple-Inspired Design, Saytara QA and Saytara Dashboard Accessibility skill methods. It is not an app implementation or full accessibility certification.
