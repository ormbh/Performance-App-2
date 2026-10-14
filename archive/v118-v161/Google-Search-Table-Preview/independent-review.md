# Independent table-findings preview review

Reviewed on 11 October 2026. **No blocking issue found.** This is an isolated design preview review, not live-app integration or accessibility certification.

The desktop and mobile renders retain the approved Google-like search composition and replace list findings with a readable six-column RTL table. The six columns preserve the original source meanings: item/title, status/progress, timing, follow-up contact, entity/organizational unit and updates/next step.

Independent Chromium checks confirmed:

- Six semantic column headers use supplied **Dubai Bold**, 18px, weight 700, Ink `#4F4E4E` on Linen `#EFEBE7`. The actual embedded Bold font face is loaded; no synthetic bold is used.
- Names use **Dubai Regular**, 16px, weight 400, neutral Taupe `#756B5F`. Notes/context use the agreed readable body treatment.
- Four illustrative query result keys remain in their original order: `secretariat-7`, `council-51`, `agenda-7`, `council-7`. Sorting preserves the matched records.
- Each row has a semantic row header and five data cells. The table has a named caption.
- Meaningful 0% project progress is retained; absent timing reads `غير متاح` rather than zero.
- Project details retain source reference 57, frozen status and 0% progress. Escape closes details and returns focus to the item trigger.
- Completed legislation and the source completed-after-deadline note `تجاوز الموعد` remain Green `#01831E`; unfinished `متأخر` remains Red `#C00000`.
- KPI contact labels remain `ملاك الهدف`; portfolio-specific timing and context fields use the original source helpers.
- At mobile 390px, the whole page fits the viewport. The named, focusable table region is 356px wide with a 1120px table; keyboard Arrow Left scrolls the table without expanding the page.
- Desktop and mobile approved-home PNG hashes exactly match the preceding approved Google-like home previews.
- The working app's index, CSS bundle and JS bundle checksums remain unchanged.

The fixture is illustrative. Screen-reader certification, print output and deployment were outside this preview review.
