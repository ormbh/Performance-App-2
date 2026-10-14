from pathlib import Path
from collections import Counter
from playwright.sync_api import sync_playwright
import openpyxl,json,hashlib,subprocess
O=Path(__file__).parent;F=Path('/workspace/saytara-work/monthly-apple-preview/ILLUSTRATIVE-monthly-preview.xlsx');model=json.loads((O/'source-model.json').read_text())
E={'checks':[],'issues':[],'errors':[],'source':{'fixture':str(F),'sha256':hashlib.sha256(F.read_bytes()).hexdigest(),'cutoff':model['sourceDate'],'period':model['sourcePeriod'],'application':'Performance-App-v154','scope':'All sectors, units and entities; all agenda types; illustrative fixture'}}
def ck(v,n,details=None):
 E['checks'].append({'name':n,'pass':bool(v),'details':details})
 if not v:E['issues'].append(n)
w=openpyxl.load_workbook(F,read_only=True,data_only=True);rows=list(w['الأجندة_السنوية'].values);header=rows.pop(0);records=[dict(zip(header,row))for row in rows]
raw=Counter((r['تصنيف الموضوع'],r['مستوى الإنجاز'])for r in records)
ck(len(records)==model['total']==117,'Raw workbook and fresh v154 model reconcile at 117 rows')
for c in model['cohorts']:
 cat='الأجندة السنوية' if c['id']=='approved' else 'مستجد'
 ck(all(raw[(cat,s['name'])]==s['count']for s in c['totals']),c['id']+' raw source status counts equal model totals',c['totals'])
 ck(sum(s['count']for s in c['totals'])==sum(q['total']for q in c['quarters'])==c['total'],c['id']+' status and quarter totals reconcile')
 ck(all(sum(s['count']for s in q['cells'])==q['total']for q in c['quarters']),c['id']+' every quarter stack reconciles')
ck(len(model['sourceRecordKeys'])==len(set(model['sourceRecordKeys'])),'No duplicate source model keys')
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 p=b.new_page(viewport={'width':1440,'height':1800},device_scale_factor=1);requests=[];p.on('pageerror',lambda e:E['errors'].append(str(e)));p.on('request',lambda r:requests.append(r.url))
 p.goto('http://127.0.0.1:8955/agenda-inbar-concept-r1/Agenda-In-Bar-Illustration.html');p.evaluate('document.fonts.ready');p.wait_for_timeout(100)
 ck(len(requests)==1,'Self-contained HTML makes no external asset requests',requests)
 ck(p.evaluate("document.fonts.check('18px \"TEC Dubai\"')&&document.fonts.check('18px \"TEC DIN\"')&&document.fonts.check('18px \"TEC DIN LT\"')"),'Original Dubai and DIN fonts loaded')
 panels=p.locator('#paired-charts-and-definitions .a-chart-panel')
 ck(panels.nth(0).bounding_box()['x']>panels.nth(1).bounding_box()['x'],'Approved category physically right, emerging left')
 ck(p.locator('.a-quarter-chart').evaluate_all("xs=>xs.every(s=>s.dataset.scaleMax==='50')"),'Both charts retain zero-to-50 common numeric scale')
 ck(p.locator('.a-axis-label').evaluate_all("xs=>xs.filter(x=>x.textContent==='–').length===2&&!xs.some(x=>x.textContent==='0')"),'Axis baseline is zero numerically and dash in display')
 for i,c in enumerate(model['cohorts']):
  panel=panels.nth(i);bars=panel.locator('.a-quarter-bar');first=bars.first
  ck(first.bounding_box()['x']>bars.last.bounding_box()['x'],c['id']+' Q1 physically right')
  ck(panel.locator('.a-quarter-detail').get_attribute('data-detail-mode')=='totals',c['id']+' initial totals')
  first.hover();ck(panel.locator('.a-quarter-detail').get_attribute('data-detail-mode')=='totals',c['id']+' hover keeps totals')
  first.focus();ck(panel.locator('.a-quarter-detail').get_attribute('data-detail-mode')=='totals',c['id']+' focus keeps totals')
  first.press('Enter');ck(panel.locator('.a-quarter-detail').get_attribute('data-detail-mode')=='quarter',c['id']+' explicit activation shows quarter')
  first.press('Escape');ck(panel.locator('.a-quarter-detail').get_attribute('data-detail-mode')=='totals',c['id']+' Escape restores totals')
  first.click();first.evaluate('e=>e.blur()');ck(first.locator('.a-bar-focus').evaluate("e=>getComputedStyle(e).stroke==='rgba(0, 0, 0, 0)'"),c['id']+' no persistent selected outline')
  p.locator('.review-meta').click();ck(panel.locator('.a-quarter-detail').get_attribute('data-detail-mode')=='totals',c['id']+' outside click restores totals')
  for j,q in enumerate(c['quarters']):
   bar=bars.nth(j)
   ck(int(bar.get_attribute('data-count'))==q['total'],c['id']+' '+q['name']+' exact total')
   for segment in bar.locator('.a-quarter-segment').all():
    count=int(segment.get_attribute('data-count'));height=float(segment.get_attribute('height'))
    ck(abs(height-480*count/50)<0.001,c['id']+' '+q['name']+' '+segment.get_attribute('data-status')+' segment proportional')
 E['labels']=p.locator('.a-inbar-count').evaluate_all("xs=>xs.map(x=>({cohort:x.closest('.a-chart-panel').dataset.cohort,quarter:x.closest('.a-quarter-bar').dataset.quarter,status:x.dataset.status,count:+x.dataset.count,visible:x.dataset.fits==='true',fontPx:parseFloat(getComputedStyle(x).fontSize)*x.closest('svg').getBoundingClientRect().width/650,fill:getComputedStyle(x).fill}))")
 ck(all(x['visible']==(x['count']>=2)for x in E['labels']),'Desktop labels show all 2+ segments and omit 1-count segments')
 ck(all(x['fontPx']>=16 for x in E['labels']if x['visible']),'Visible desktop in-bar type is at least 16 CSS px')
 ck(all(x['fill']=='rgb(252, 251, 251)'for x in E['labels']if x['status']=='جاهز للعرض'),'Ready in-bar count uses Paper for contrast on Teal')
 ck(p.locator('.a-status-detail[data-status="جاهز للعرض"]').evaluate_all("xs=>xs.every(x=>getComputedStyle(x).color==='rgb(17, 94, 103)')"),'Ready labels and values below charts are Teal')
 ck(p.locator('td[data-count="0"] bdi').evaluate_all("xs=>xs.every(x=>x.textContent==='–')"),'Zero matrix counts use dash')
 ck(p.locator('.ag-definitions [data-agenda-status]').count()==5,'All five original detailed definitions retained')
 ck(p.evaluate("()=>{const x=[...document.querySelectorAll('[id]')].map(e=>e.id);return new Set(x).size===x.length}"),'No duplicate IDs in expanded count reference')
 p.screenshot(path=O/'Agenda-In-Bar-Desktop.png',full_page=True);p.locator('#paired-charts-and-definitions').screenshot(path=O/'Agenda-In-Bar-Paired.png')
 p.pdf(path=O/'Agenda-In-Bar-A4-Landscape.pdf',prefer_css_page_size=True,print_background=True)
 for width in [390,768]:
  p.set_viewport_size({'width':width,'height':1200});p.wait_for_timeout(100)
  ck(p.evaluate('document.documentElement.scrollWidth<=innerWidth+1'),str(width)+' no document horizontal overflow')
  p.screenshot(path=O/f'responsive-{width}.png',full_page=True)
 b.close()
info=subprocess.check_output(['pdfinfo',str(O/'Agenda-In-Bar-A4-Landscape.pdf')],text=True)
ck('Pages:           2' in info,'PDF has charts with definitions on page 1 and exact matrix on page 2')
ck('841.92 x 594.96 pts (A4)' in info,'PDF is A4 landscape')
fontinfo=subprocess.check_output(['pdffonts',str(O/'Agenda-In-Bar-A4-Landscape.pdf')],text=True)
E['pdfFonts']=fontinfo
ck(all('yes' in line for line in fontinfo.splitlines()[2:]),'PDF fonts embedded')
E['verdict']='PASS' if not E['issues']and not E['errors'] else 'FAIL'
(O/'evidence.json').write_text(json.dumps(E,ensure_ascii=False,indent=2));print(json.dumps({'verdict':E['verdict'],'checks':len(E['checks']),'issues':E['issues'],'errors':E['errors']},ensure_ascii=False))
