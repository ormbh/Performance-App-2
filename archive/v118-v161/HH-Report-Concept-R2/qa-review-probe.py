from pathlib import Path
from playwright.sync_api import sync_playwright
import json,hashlib
ROOT=Path(__file__).resolve().parent
AUDIT=json.loads((ROOT/'source-review.json').read_text())
checks=[]
def check(name,actual,expected=True):
    checks.append({'check':name,'pass':actual==expected,'actual':actual,'expected':expected})
def shot(p,selector,name): p.locator(selector).screenshot(path=str(ROOT/name))
with sync_playwright() as pw:
    browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
    p=browser.new_page(viewport={'width':1440,'height':1000},device_scale_factor=1)
    errors=[]
    p.on('pageerror',lambda e:errors.append(str(e)))
    p.goto('http://127.0.0.1:8917/hh-report-concept-r2/index.html',wait_until='networkidle')
    p.evaluate('document.fonts.ready')
    d=p.evaluate('HH_DATA')
    check('raw fixture payload unchanged from previous concept',(ROOT/'data.js').read_bytes()==(ROOT.parent/'hh-report-concept/data.js').read_bytes())
    state=p.evaluate('HH_PREVIEW_STATE')
    check('summary total/done/work/other',[state['metrics'][x] for x in ['total','done','work','other']],[62,23,38,1])
    cohorts=p.evaluate('HH_COHORTS')
    check('shared chart maximum',cohorts['scaleMax'],15)
    check('cohort coverage and no overlap',len(set(cohorts['leadership'])|set(cohorts['tec']))==62 and not(set(cohorts['leadership'])&set(cohorts['tec'])))
    for cohort in ['leadership','tec']:
        check(cohort+' exact source keys',sorted(cohorts[cohort]),sorted(AUDIT['cohorts'][cohort]['keys']))
        rows=p.locator('[data-cohort="'+cohort+'"] .cohort-row').evaluate_all('''els=>els.map(el=>({sector:el.dataset.sector,total:el.querySelector('.cohort-total').textContent.trim(),segments:[...el.querySelectorAll('.cohort-segment')].map(x=>({status:x.dataset.status,count:+x.dataset.count,label:x.textContent.trim()}))}))''')
        check(cohort+' six aligned sector rows',[x['sector'] for x in rows],AUDIT['sector_order'])
        for actual,expected in zip(rows,AUDIT['cohorts'][cohort]['sectors']):
            check(cohort+'/'+actual['sector']+' total',actual['total'],str(expected['total']) if expected['total'] else '–')
            exp=[{'status':s,'count':v,'label':str(v)} for s,v in zip(AUDIT['status_order'],expected['values']) if v]
            check(cohort+'/'+actual['sector']+' statuses and bar labels',actual['segments'],exp)
        actual=p.locator('[data-cohort="'+cohort+'"] .cohort-status').evaluate_all('els=>Object.fromEntries(els.map(x=>[x.dataset.status,+x.querySelector(".num").textContent]))')
        check(cohort+' status totals',actual,{k:v for k,v in AUDIT['cohorts'][cohort]['status_counts'].items() if v})
    check('detailed legend physically below both charts',p.evaluate('document.querySelector(".detailed-legend").getBoundingClientRect().top>=Math.max(...[...document.querySelectorAll(".cohort-panel")].map(x=>x.getBoundingClientRect().bottom))'))
    check('legend source order',p.locator('.detailed-legend dt').all_text_contents(),AUDIT['status_order'])
    check('ready absent from real HH counts',not any(x['statusLabel']=='جاهز للعرض' for x in d['items']))
    ready=p.locator('.ready-example').evaluate('(el)=>[getComputedStyle(el.querySelector("span")).color,getComputedStyle(el.querySelector("bdi")).color,el.textContent.trim()]')
    check('ready sample label and count teal',ready[:2],['rgb(17, 94, 103)']*2)
    check('ready sample explicitly outside report data','خارج بيانات التقرير' in p.locator('#display-rules').inner_text())
    check('formatter zero and missing boundaries',p.evaluate('[0,"0%","غير مسجل","غير مسجلة","غير متوفر","غير متوفرة",null].map(HH_PREVIEW.display)'),['–','–','','','','',''])
    detail_fail=[]
    source_names=set(str(x['t'].get('sourceName','')) for x in d['items'])-{''}
    for it in d['items']:
        p.evaluate('(key)=>HH_PREVIEW.selectProject(key)',it['key'])
        txt=p.locator('#detail').inner_text()
        if any(s in txt for s in ['Source.Name','ملف المصدر','غير مسجل','غير مسجلة','غير متوفر','غير متوفرة',*source_names]): detail_fail.append(it['key'])
        if it['progress']==0:
            check('zero progress detail '+it['key'],p.locator('#detail .progress-ring .num').inner_text(),'–')
            check('zero progress aria kept numeric '+it['key'],p.locator('#detail .progress-ring').get_attribute('aria-valuenow'),'0')
    check('source filename and missing placeholders absent from all 62 actual detail cards',detail_fail,[])
    p.evaluate("HH_PREVIEW.selectProject('special-26')")
    shot(p,'#detail','qa-detail-desktop.png')
    shot(p,'#chart','qa-charts-desktop.png')
    shot(p,'#display-rules','qa-display-rules.png')
    geom={}
    for width in [1440,1280,1200,390,320]:
        p.set_viewport_size({'width':width,'height':950})
        p.evaluate('HH_PREVIEW.setScope({})')
        vals=p.locator('.cohort-segment').evaluate_all('''els=>els.map(e=>{const r=e.getBoundingClientRect(),n=e.querySelector('.num').getBoundingClientRect();return {count:+e.dataset.count,segmentWidth:r.width,numberWidth:n.width,inside:n.left>=r.left-0.2&&n.right<=r.right+0.2&&n.top>=r.top-0.2&&n.bottom<=r.bottom+0.2}})''')
        geom[str(width)]=vals
        check('numbers fully inside bars at '+str(width),[v for v in vals if not v['inside']],[])
        check('page fits viewport '+str(width),p.evaluate('document.documentElement.scrollWidth<=innerWidth'))
        if width in [390,320]:
            shot(p,'#chart','qa-charts-mobile-'+str(width)+'.png')
            p.evaluate('(sectors)=>HH_PREVIEW.setScope({sector:sectors})',[AUDIT['sector_order'][-1],AUDIT['sector_order'][0]])
            label=p.locator('[data-filter="sector"] .filter-value>b')
            check('first selected plus N label '+str(width),' '.join(label.inner_text().split()),AUDIT['sector_order'][-1]+' +1')
            check('plus N visible and within control '+str(width),label.locator('bdi').evaluate('(e)=>{let r=e.getBoundingClientRect(),p=e.closest("summary").getBoundingClientRect();return r.width>0&&r.left>=p.left&&r.right<=p.right}'))
            shot(p,'#filters','qa-filter-mobile-'+str(width)+'.png')
    p.set_viewport_size({'width':1440,'height':1000})
    for lead,expected in [('نعم','leadership'),('لا','tec')]:
        p.evaluate('(lead)=>HH_PREVIEW.setScope({lead:[lead]})',lead)
        check(expected+' scope hides entire empty cohort',p.locator('.cohort-panel').evaluate_all('els=>els.map(x=>x.dataset.cohort)'),[expected])
        check(expected+' scope exact record set',sorted(p.evaluate('HH_PREVIEW_STATE.keys')),sorted(AUDIT['cohorts'][expected]['keys']))
    p.evaluate('HH_PREVIEW.setScope({sector:["__qa_absent__"]})')
    check('empty total rendered dash',p.locator('[data-metric="total"] .num').inner_text(),'–')
    check('empty completed percentage rendered dash',p.locator('.completion-head .num').inner_text(),'–')
    check('empty scope removes chart panels',p.locator('.cohort-panel').count(),0)
    check('empty scope names no result', 'لا توجد مشاريع ضمن النطاق المحدد' in p.locator('#chart').inner_text())
    p.locator('#clear-filters').click()
    check('reset restores all 62 records',p.evaluate('HH_PREVIEW_STATE.keys.length'),62)
    check('no JavaScript page errors',errors,[])
    browser.close()
result={'date':'2026-10-14','url':'http://127.0.0.1:8917/hh-report-concept-r2/index.html','checks':checks,'total':len(checks),'passed':sum(x['pass'] for x in checks),'failed':[x for x in checks if not x['pass']],'bar_geometry':geom,'source_sha256':hashlib.sha256((ROOT/'data.js').read_bytes()).hexdigest()}
(ROOT/'qa-review-evidence.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in result.items() if k in ['total','passed','failed']},ensure_ascii=False,indent=2))
