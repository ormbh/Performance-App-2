# Monthly legislation v157 — focused QA

**PASS: 166 independent checks on the final bundled app.** No runtime errors or external requests.

- Existing illustrative source is unchanged: 191 total = 180 completed + 11 in progress, including 2 late. Completed is the exact unique union of 152 on-time and 28 overrun source records.
- Every pre-existing metric remains unchanged. All five other monthly card texts match v156 in both screen and print. Follow-up record keys/order survive both PDF formats.
- Native completed/in-progress/late drills return their exact unique source records; sector/unit/multiple-unit and empty filters retain scope.
- RTL layout passes 320, 390, 768 and 1440 px; completed is right, in progress left, late below its parent. Completed labels/counts are Green; late labels/counts Red. Caption stays beside its percentage.
- Actual app PDF downloads pass in continuous and A4 modes. Card remains whole on a page, figures/text are native selectable output, no chart raster, all PDF text is bounded. Original other cards, title, date and footer remain.
- Controlled approved scenario reproduces 183 total, 178 completed, 5 in progress with 2 late and 97.3%; eligible total/completed/late deltas are +17/+14/+1. In-progress change is correctly calculated +3 from the controlled prior count2.
- Empty total hides the card. All-done/all-progress scopes collapse empty columns. True zero percentage uses dash. Missing, invalid or overlapping completion suppresses bar/caption. Late outside in-progress remains separately labeled rather than falsely nested.

Visual review: desktop and phone cards, complete A4 page, continuous card, and approved synthetic A4 card. No clipping, overlapping text or mismatched status colors observed.

Limitations: the workbook is illustrative, and the 183/178/5/2 scenario is controlled test input. Actual native mobile devices and cold file startup were not retested. This is a focused change verification, not an unrelated full app regression or accessibility certification.
