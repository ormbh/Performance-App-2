# v175 — focused Mac Chrome retest

Use the exact v175 ZIP and the same dummy workbook used for v174. Test **the extracted `index.html` using `file://`** in installed Chrome. Keep localhost observations separate. No browser security change or automation-policy bypass is required or authorized by this checklist. If automation rejects the file scheme, perform these user interactions manually and label them manual evidence.

1. Extract the whole ZIP into a fresh folder. Record Chrome/macOS versions and the tested release ZIP hash, when available. Open `index.html` directly and retain evidence that the address is a local file.
2. Select the dummy workbook. Check source cutoff 30/09/2026, monthly populations and finance against the existing independently reconciled v174 Mac controls. An old undated fallback may require selecting files again once.
3. Refresh the same tab. Check the loaded workbook, date and filters remain correct. Open an actual scoped report link in a new tab, then refresh it; confirm data/scope are retained and no unexpected upload request appears. Record any fallback warning exactly.
4. Download the monthly and current-only comparison PDFs through app controls. Check year/currency metadata, follow-up unit and comparison period/scope labels against the corrected samples. Preserve the actual PDF files.
5. Download agenda, council and special-project PDFs. Check contents show **labeled record counts and separate page numbers**; activate each contents link in the native viewer and check its actual landing. Check a filtered scope, an empty scope and a populated notes section: counts follow scope, empty contents are hidden and notes gain no invented record count.
6. Check Arabic alignment, the unchanged monthly thin bars, readable metadata, page numbering and the table/section transitions affected by contents changes. Record exact page/label for a failure.
7. Test the app's explicit end-session action, then reload: removed files must not be silently restored. Do not change or falsify the Mac system clock for retention testing. The controlled clock/quota cases are already recorded separately in cloud regression evidence.

Return PASS/FAIL/NOT RUN for each step, screenshots at readable size, actual PDFs and any captured console errors. State whether each case used direct file or localhost; do not infer one from the other. Only test Edge if it is installed and included in the user's scope.
