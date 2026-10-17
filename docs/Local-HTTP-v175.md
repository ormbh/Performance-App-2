# Performance App v175 — optional local HTTP package

[Download the app with the local HTTP launcher](https://github.com/ormbh/Performance-App-2/raw/refs/heads/main/Performance-App-v175-Local-HTTP.zip)

This is the unchanged v175 application with an optional local server for desktop use. All 23 existing runtime files are byte-identical to the verified v175 release. The ZIP adds only two launcher files and a guide: **26 files**, 7,047,605 bytes. It contains no workbooks, audit folders or tests. The design, calculations, filter scope, PDF types and Design Principles Revision 39 are unchanged.

SHA-256: `6bb0383075eb86b02e834bdd914f46c8067803de0e3a38599b0974341e8a09ee`.

## On your Mac

1. Extract the complete ZIP.
2. Double-click **Start Local HTTP.command**. Python **3.8 or newer** must already be available; no additional Python packages are required and the launcher does not install software.
3. Chrome opens at `http://127.0.0.1:8765/index.html`. If it does not, paste that address into Chrome.
4. Leave the launcher window open and select the workbook in the app. To stop the server, press **Control+C** in that window.

The first HTTP use requires selecting the workbook because browser storage for `file://` and HTTP is separate. Keep using the same address and port; changing from `127.0.0.1` to `localhost`, or changing the port, creates separate browser storage. The existing 24-hour retained-workbook rule remains active.

You can still open **index.html** directly. That mode needs no server or Python. Its existing direct-file verification limitations remain; see [v175 verification](Verification-v175.md).

## Server behavior

- Local IPv4 loopback only (`127.0.0.1`), default port 8765. No remote hosting or public network listener is created.
- Read-only GET/HEAD serving of the 23 known app assets. Arbitrary neighboring files, source workbooks, path traversal, directory listings and symbolic-link substitutions are not served. There is no workbook-upload endpoint; selected files are read by the unchanged browser application.
- Same-folder duplicate launch reuses its existing server; a different app/folder occupying the port produces an explicit error instead of silently moving to another browser origin.
- Correct MIME types, no stale HTTP caching, and graceful Control+C shutdown. The helper has no dependency beyond the Python standard library.
- Manual start, if needed: `python3 Start-Local-HTTP.py --open`. An explicit alternative port is available with `--port 8766`, with the separate-storage implications above.

## Focused verification

The independent reviewer tested the actual packaged Python helper, not a substitute development server:

- **38 protocol/lifecycle checks**: real loopback requests, GET/HEAD, asset MIME/query behavior, forbidden files and internal/external/cyclic symlinks, duplicate launch, occupied port, incomplete extraction, Unicode/spaced folder paths and shutdown.
- **34 browser/PDF checks**: actual workbook import, all monthly metric totals/source-row sets and finance against the existing verified baseline, HTTP reload, actual report new-tab transfer/reload, source integrity and zero external runtime requests/browser errors.
- Actual monthly and agenda PDFs downloaded through normal app controls: full-height monthly and 14-page A4-landscape agenda, native text bounds, font roles, record scope and labeled contents counts with valid internal destinations. Other unchanged v175 outputs reuse their exact runtime-hash evidence.
- Launcher shell syntax, mocked macOS browser-opening/quoted-path dispatch, executable ZIP permissions and complete unchanged-runtime inventory receive focused checks. These do not establish actual macOS Finder behavior.

**Not run here:** native Mac Finder double-click, automatic installed-Chrome activation on macOS, or a new Mac direct-file acceptance run. HTTP tests use Linux desktop Chromium. No browser security setting or automation restriction was bypassed. If macOS refuses the launcher or Python is unavailable, preserve the exact message for review.

[HTTP package inventory](local-http-v175-release.json) · [Original v175 verification](Verification-v175.md)
