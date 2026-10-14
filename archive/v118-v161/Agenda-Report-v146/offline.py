from pathlib import Path
import json
from playwright.sync_api import sync_playwright
OUT=Path(__file__).parent
with sync_playwright()as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage']);ctx=b.new_context(accept_downloads=True)
 p=ctx.new_page();requests=[];failed=[];p.on('request',lambda r:requests.append(r.url));p.on('requestfailed',lambda r:failed.append({'url':r.url,'failure':r.failure}))
 p.goto('http://127.0.0.1:8916/Performance-App-v146/index.html');p.locator('input[type=file]').first.set_input_files('/workspace/saytara-work/monthly-apple-preview/ILLUSTRATIVE-monthly-preview.xlsx');p.wait_for_function('!!Saytara.app.state.data')
 p.evaluate("Saytara.app.state.dash.entity=['دائرة المالية'];Saytara.app.state.report.kind='agenda';Saytara.app.go('reports')")
 with p.expect_download(timeout=120000)as d:p.locator('[data-act="download-pdf"]').first.click()
 d.value.save_as(OUT/'offline-primed.pdf');p.wait_for_function('!Saytara.app.state.pdfDownloading');first_requests=len(requests)
 ctx.set_offline(True)
 ok=False;error=''
 try:
  with p.expect_download(timeout=45000)as d:p.locator('[data-act="download-pdf"]').first.click()
  d.value.save_as(OUT/'offline-no-network.pdf');ok=True
 except Exception as ex:error=str(ex)[:1000]
 out={'offlineAfterPriming':ok,'internetRequests':[u for u in requests if not u.startswith('http://127.0.0.1:8916/')and not u.startswith('data:')and not u.startswith('blob:')],'offlineRequests':requests[first_requests:],'failed':failed,'error':error,'toast':p.locator('#toast').inner_text()}
 (OUT/'offline-evidence.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print(json.dumps(out,ensure_ascii=False));ctx.close();b.close()
