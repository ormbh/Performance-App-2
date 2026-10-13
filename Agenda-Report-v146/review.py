from pathlib import Path
import json, hashlib, re, collections, sys
import fitz
from playwright.sync_api import sync_playwright
BASE=Path('/workspace/saytara-work'); OUT=Path(__file__).parent
APP=BASE/'Performance-App-v146'; FIX=BASE/'monthly-apple-preview/ILLUSTRATIVE-monthly-preview.xlsx'
BASELINE=json.loads((BASE/'agenda-report-concept-v2/qa/baseline-contract.json').read_text())
CONTRACT=(BASE/'agenda-report-concept-v2/qa/capture-contract.py').read_text().split("CONTRACT='''",1)[1].split("'''",1)[0]
CASES=[('all',{},[]),('entity',{'entity':['هيئة الطرق والمواصلات']},[]),('sparse',{'entity':['دائرة المالية']},[]),('empty',{'entity':['__QA_no_such_entity__']},[]),('emerging_only',{},['مستجد']),('two_entities',{'entity':['هيئة الطرق والمواصلات','دائرة المالية']},[])]
E={'stage':'Independent production v146 agenda verification. Illustrative workbook; no operational workbook supplied.','fixture':{'name':FIX.name,'sha256':hashlib.sha256(FIX.read_bytes()).hexdigest()},'checks':[],'issues':[],'screen':[],'pdf':[],'errors':[],'externalRequests':[],'limitations':['Native file:// opening is blocked by managed Chromium policy. Browser tests launch through loopback HTTP; all external network requests are denied.','Synthetic edge cases modify an isolated in-memory copy only; source workbook bytes are unchanged.']}
def ck(ok,name,detail=None):
 E['checks'].append({'check':name,'pass':bool(ok)})
 if not ok:E['issues'].append({'check':name,'detail':detail})
 return bool(ok)
def dump():
 E['verdict']='PASS' if not E['issues'] and not E['errors'] else 'FAIL'
 (OUT/'evidence.json').write_text(json.dumps(E,ensure_ascii=False,indent=2))
def scope(p,sc,typ):
 p.evaluate("a=>{let s=Saytara.app.state;s.dash.sector=[];s.dash.unit=[];s.dash.entity=[];Object.assign(s.dash,a.scope);s.report.kind='agenda';s.report.type=a.type;Saytara.app.go('reports')}",{'scope':sc,'type':typ})
 p.evaluate('document.fonts.ready')
def load(p,version):
 p.goto(f'http://127.0.0.1:8916/Performance-App-v{version}/index.html')
 p.locator('input[type=file]').first.set_input_files(FIX)
 p.wait_for_function('!!Saytara.app.state.data');p.evaluate('document.fonts.ready')
def inspect(p):
 return p.evaluate('''()=>{
 const root=document.querySelector('.ag-matrix-overview');if(!root)return null;
 const box=e=>e?e.getBoundingClientRect().toJSON():null,tx=e=>{let r=document.createRange();r.selectNodeContents(e);return r.getBoundingClientRect().right};
 return{total:+root.dataset.sourceTotal,max:+root.dataset.scaleMax,statuses:JSON.parse(root.dataset.statusKeys),quarters:JSON.parse(root.dataset.displayQuarterKeys),
 categories:[...root.querySelectorAll('.a-category-value')].map(e=>e.textContent),hasPercent:root.innerText.includes('%'),corner:[...root.querySelectorAll('.a-final-total')].map(e=>e.innerText),
 legend:[...root.querySelectorAll('.a-legend-entry')].map(e=>({name:e.dataset.status,text:e.innerText,color:getComputedStyle(e.querySelector('.a-legend-swatch')).backgroundColor})),
 panels:[...root.querySelectorAll('.a-chart-panel')].map(p=>({id:p.dataset.cohort,total:+p.dataset.total,
 headings:[...p.querySelectorAll('.a-quarter-heading')].map(e=>e.textContent),statusHeading:p.querySelector('.a-status-heading')?tx(p.querySelector('.a-status-heading')):null,
 labels:[...p.querySelectorAll('tbody .a-status-name')].map(e=>({text:e.textContent,color:getComputedStyle(e).color,right:tx(e)})),
 cells:[...p.querySelectorAll('.a-chart-cell')].map(e=>({status:e.dataset.status,quarter:e.dataset.quarter,count:+e.dataset.count,text:e.querySelector('.a-cell-number').textContent,aria:e.querySelector('.a-cell-number').getAttribute('aria-label'),bar:box(e.querySelector('.a-cell-bar')),track:box(e.querySelector('.a-cell-track')),color:getComputedStyle(e.querySelector('.a-cell-bar')).backgroundColor})),
 rowTotals:[...p.querySelectorAll('tbody .a-status-total')].map(e=>({status:e.dataset.status,count:+e.dataset.count,text:e.querySelector('.a-cell-number').textContent})),
 quarterTotals:[...p.querySelectorAll('.a-quarter-total')].map(e=>({quarter:e.dataset.quarter,count:+e.dataset.count,text:e.querySelector('.a-cell-number').textContent}))})),
 width:innerWidth,scrollWidth:document.documentElement.scrollWidth,overflows:[...root.querySelectorAll('*')].filter(e=>getComputedStyle(e).display!=='none'&&getComputedStyle(e).position!=='absolute'&&getComputedStyle(e).display!=='inline'&&e.clientWidth&&e.scrollWidth>e.clientWidth+2).map(e=>({cls:e.className,text:e.innerText,width:e.clientWidth,scroll:e.scrollWidth})),
 recordKeys:[...document.querySelectorAll('.ag-table tr[data-record]')].map(e=>e.dataset.record),
 sourceNotes:document.querySelectorAll('#agenda-source-notes,[href="#agenda-source-notes"]').length};}''')
def rgb(hex):return 'rgb('+', '.join(str(int(hex[i:i+2],16))for i in[1,3,5])+')'
def expectations(contract):
 groups={};status=[]
 for family in ['planned','emerging','other']:
  co=contract[family]
  for x in co['stats']:
   if x['name']not in status:status.append(x['name'])
  for g in co['groups']:groups[g['key']]=g['name']
 return groups,status

def verify_screen(p,name,contract,synthetic=False):
 spec=p.evaluate('Saytara.agendaMatrix.spec(Saytara.app.state)')
 ck(spec['total']==contract['total'],name+' model to matrix headline')
 ck(spec['sourceRecordKeys']==[x['key']for x in contract['records']],name+' model to matrix exact record keys')
 expected_status=p.evaluate("(()=>{const S=Saytara,s=S.app.state,m=S.agendaReport.model(s.data,s.dash,s.report.type,S.views.agendaPage.options(s));return S.agendaReport.stats(m.items,s.data).map(x=>x.name)})()")
 ck([s['name']for s in spec['statuses']]==expected_status,name+' source status order and active union')
 expected_quarters=p.evaluate("(()=>{const S=Saytara,s=S.app.state,m=S.agendaReport.model(s.data,s.dash,s.report.type,S.views.agendaPage.options(s));return S.agendaReport.groups(s.data,m.items).map(x=>x.key)})()")
 ck([q['key']for q in spec['displayQuarters']]==expected_quarters,name+' effective quarter order and active union')
 for width in [1440,1024,768,390,320]:
  p.set_viewport_size({'width':width,'height':1000});p.wait_for_timeout(40);v=inspect(p);tag=f'{name} {width}';start=len(E['issues'])
  ck(v is not None,tag+' matrix rendered')
  if v is None:continue
  ck(v['scrollWidth']<=width+1,tag+' no page horizontal overflow',v['scrollWidth']);ck(not v['overflows'],tag+' no matrix element overflow',v['overflows'])
  ck(v['sourceNotes']==0,tag+' source appendix and link absent')
  ck(collections.Counter(v['recordKeys'])==collections.Counter(x['key']for x in contract['records']),tag+' all detail records exactly once',{'expected':len(contract['records']),'actual':len(v['recordKeys'])})
  ck(not v['hasPercent']and all(not x.strip()for x in v['corner']),tag+' percent and final total removed')
  ck(v['statuses']==expected_status and v['quarters']==expected_quarters,tag+' dynamic status quarter visibility')
  ck([x['name']for x in v['legend']]==expected_status if spec['total'] else not v['legend'],tag+' legend follows present statuses')
  ck(v['categories']==[str(c['total'])if c['total']else'–'for c in spec['cohorts']],tag+' headline values and zero dashes')
  ck([p['id']for p in v['panels']]==[c['id']for c in spec['cohorts']]if spec['total']else not v['panels'],tag+' shared cohort panels')
  widths=[]
  for panel in v['panels']:
   co=next(c for c in spec['cohorts']if c['id']==panel['id']);look={(g['key'],x['name']):x['count']for g in co['quarters']for x in g['cells']}
   ck([(c['status'],c['quarter'])for c in panel['cells']]==[(s['name'],q['key'])for s in spec['statuses']for q in spec['displayQuarters']],tag+' matrix intersection order')
   if width>=768:ck(all(abs(x['right']-panel['statusHeading'])<.3 for x in panel['labels']),tag+' status heading aligns to labels')
   for label in panel['labels']:
    color=rgb('#C00000'if label['text']=='متأخر'else '#01831E'if label['text']=='منجز'else '#4F4E4E')
    ck(label['color']==color,tag+' late/done only label color',label)
   for c in panel['cells']:
    count=look.get((c['quarter'],c['status']),0);ck(c['count']==count,tag+' source intersection count')
    ck(c['text']==(str(count)if count else'–'),tag+' zero shown as dash')
    if not count:ck(c['aria']=='صفر'and c['bar']['width']==0,tag+' zero retained for assistive text and no bar')
    expected=c['track']['width']*count/spec['scale']['max']if spec['scale']['max']else 0
    ck(abs(c['bar']['width']-expected)<.15,tag+' proportional shared count scale');widths.append(c['track']['width'])
   for count in panel['rowTotals']+panel['quarterTotals']:ck(count['text']==(str(count['count'])if count['count']else'–'),tag+' subtotal zeros use dash')
  if widths:ck(max(widths)-min(widths)<.3,tag+' equal physical scale across cohorts',max(widths)-min(widths))
  if name in ['all','entity','synthetic']and width in[1440,390]:
   p.locator('#toast').wait_for(state='hidden',timeout=6000);p.locator('.ag-matrix-overview').screenshot(path=OUT/f'{name}-{width}.png')
  E['screen'].append({'scope':name,'width':width,'pass':len(E['issues'])==start,'total':v['total'],'statuses':v['statuses'],'quarters':v['quarters']})
 return spec

HOOK='''()=>{const S=Saytara,orig=S.printPagination.preparedDocument;S.printPagination.preparedDocument=async function(){let a=await orig.apply(this,arguments);let data=S.offlinePdf.collect(a),g=Object.assign({},a.geometry,{layout:a.layout,direction:a.direction}),origin=a.root.getBoundingClientRect(),rect=e=>{let r=e.getBoundingClientRect();return{x:r.x-origin.x,y:r.y-origin.y,w:r.width,h:r.height}};window.__qaPDF={plan:S.offlinePdf.pagePlan(data,g),geometry:g,lines:data.lines.map(x=>({text:x.text,x:x.x,y:x.y,w:x.w,h:x.h,headerText:x.headerText,size:x.size,color:x.color})),tables:data.tables,chart:a.root.querySelector('.ag-matrix-overview')?rect(a.root.querySelector('.ag-matrix-overview')):null,chartText:a.root.querySelector('.ag-matrix-overview')?.innerText,chartLabels:[...a.root.querySelectorAll('.a-matrix tbody .a-status-name')].map(e=>({text:e.innerText,color:a.window.getComputedStyle(e).color,...rect(e)})),rows:[...a.root.querySelectorAll('.ag-table tr[data-record]')].map(e=>({key:e.dataset.record,text:e.innerText,...rect(e),title:e.children[1]?{text:e.children[1].innerText,...rect(e.children[1])}:null})),title:[...a.root.querySelectorAll('.tec-print-first-header')].map(e=>({text:e.innerText,...rect(e)}))};return a;};}'''
def native_pdf(p,name,contract):
 p.set_viewport_size({'width':1440,'height':1000});p.evaluate('scrollTo(0,0)');p.evaluate('document.fonts.ready')
 with p.expect_download(timeout=120000)as d:p.locator('[data-act="download-pdf"]').first.click()
 dl=d.value;path=OUT/f'{name}.pdf';dl.save_as(path);p.wait_for_function('!Saytara.app.state.pdfDownloading',timeout=120000)
 proof=p.evaluate('window.__qaPDF');(OUT/f'{name}-geometry.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2))
 doc=fitz.open(path);start=len(E['issues']);text='\n'.join(pg.get_text()for pg in doc);first=doc[0].get_text()
 ck(all(abs(pg.rect.width-841.89)<1 and abs(pg.rect.height-595.28)<1 for pg in doc),name+' native PDF A4 landscape')
 ck(proof['chart'] is not None and proof['chart']['y']+proof['chart']['h']<=max((r['source']['y']+r['source']['h'] for r in proof['plan'][0].get('regions',[])),default=proof['plan'][0].get('end',0))+.5,name+' chart entire first PDF page',{'chart':proof['chart'],'firstPlan':proof['plan'][0]})
 ck(len(proof['plan'])==len(doc),name+' native page count matches plan')
 ck(collections.Counter(r['key']for r in proof['rows'])==collections.Counter(x['key']for x in contract['records']),name+' all table row keys included')
 ck('ملحق ملاحظات المصدر' not in text,name+' appendix absent from actual PDF')
 # Arabic text extraction in this native engine is logical. Remove all whitespace for wrapping tolerance.
 norm=lambda s:re.sub(r'\s+','',s).replace('\u200f','').replace('\u200e','')
 ck('مستجداتالأجندةالسنوية' in norm(first),name+' first-page title restored')
 ck(all('مستجداتالأجندةالسنوية' not in norm(pg.get_text())for pg in list(doc)[1:]),name+' no repeated title')
 for row in proof['rows']:
  title=row['title']
  if not title:ck(False,name+' title cell exists',row['key']);continue
  matched=[]
  for pi,plan in enumerate(proof['plan']):
   for region in plan.get('regions',[]):
    src=region['source']
    if src['y']-.1<=title['y'] and src['y']+src['h']+.1>=title['y']+title['h']:
     x=(title['x']-src['x']+region['x'])*.75+28.346;y=(title['y']-src['y']+region['y'])*.75+28.346
     clip=fitz.Rect(x-.2,y-.2,x+title['w']*.75+.2,y+title['h']*.75+.2)
     matched.append(' '.join(''.join(ch['c']for ch in span.get('chars',[])if clip.contains(fitz.Point((ch['bbox'][0]+ch['bbox'][2])/2,(ch['bbox'][1]+ch['bbox'][3])/2)))for block in doc[pi].get_text('rawdict')['blocks']for line in block.get('lines',[])for span in line['spans']))
  tokens=lambda s:collections.Counter(re.findall(r'\w+',s))
  ck(len(matched)==1 and tokens(matched[0])==tokens(title['text']),name+' actual PDF source title cell preserved',{'key':row['key'],'expected':title['text'],'actual':matched})
 for idx,pg in enumerate(doc):
  spans=[s for b in pg.get_text('dict')['blocks']for l in b.get('lines',[])for s in l['spans']if s['text'].strip()]
  ck(all(s['bbox'][0]>=-1 and s['bbox'][1]>=-1 and s['bbox'][2]<=pg.rect.width+1 and s['bbox'][3]<=pg.rect.height+1 for s in spans),name+f' page {idx+1} text within page')
  ck('حقوق النشر' in pg.get_text()and 'صفحة' in pg.get_text(),name+f' page {idx+1} copyright/pages')
  pg.get_pixmap(matrix=fitz.Matrix(1,1),alpha=False).save(OUT/f'{name}-page-{idx+1:02}.png')
 # Compare chart number multiset in actual native page crop to rendered print DOM.
 if proof['chart']:
  r=proof['chart'];clip=fitz.Rect((r['x']*.75)+28.346,(r['y']*.75)+28.346,(r['x']+r['w'])*.75+28.346,(r['y']+r['h'])*.75+28.346)
  tokens=lambda s:collections.Counter(re.findall(r'(?<![A-Za-z])\d+(?:\.\d+)?',s))
  ck(tokens(doc[0].get_text(clip=clip))==tokens(proof['chartText']),name+' actual PDF chart numeric tokens',{'dom':dict(tokens(proof['chartText'])),'pdf':dict(tokens(doc[0].get_text(clip=clip)))})
 for label in proof['chartLabels']:
  expected='#C00000'if label['text']=='متأخر'else '#01831E'if label['text']=='منجز'else '#4F4E4E'
  ck(label['color']==rgb(expected),name+' print DOM late/done label colors',label)
  x=label['x']*.75+28.346;y=label['y']*.75+28.346
  clip=fitz.Rect(x-.2,y-.2,x+label['w']*.75+.2,y+label['h']*.75+.2)
  spans=[s for b in doc[0].get_text('dict',clip=clip)['blocks']for l in b.get('lines',[])for s in l['spans']if s['text'].strip()]
  ck(bool(spans)and all(s['color']==int(expected[1:],16)for s in spans),name+' actual PDF late/done only label colors',{'label':label['text'],'colors':[s['color']for s in spans]})
 E['pdf'].append({'scope':name,'pages':len(doc),'filename':dl.suggested_filename,'pass':len(E['issues'])==start,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'sourceRows':len(proof['rows'])})
 print(name,'PDF',len(doc),'pages',flush=True)

with sync_playwright()as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage']);ctx=b.new_context(viewport={'width':1440,'height':1000},accept_downloads=True)
 def route(req):
  url=req.request.url
  if url.startswith('http://127.0.0.1:8916/')or url.startswith('data:')or url.startswith('blob:'):req.continue_()
  else:E['externalRequests'].append(url);req.abort()
 ctx.route('**/*',route);p=ctx.new_page();p.on('pageerror',lambda x:E['errors'].append(str(x)));load(p,146)
 ck(p.evaluate('!!Saytara.agendaMatrix'),'production bundle contains approved matrix')
 if not p.evaluate('!!Saytara.agendaMatrix'):dump();sys.exit(1)
 original=p.evaluate('JSON.stringify(Saytara.app.state.data.items)');p.evaluate(HOOK)
 for name,sc,typ in CASES:
  scope(p,sc,typ);contract=p.evaluate(CONTRACT);base=BASELINE['cases'][name]
  for field in ['total','planned','emerging','other','records']:
   ck(contract[field]==base[field],name+' unchanged v145 '+field)
  spec=verify_screen(p,name,contract)
  if name in ['all','entity','sparse','empty','emerging_only','two_entities']:native_pdf(p,name,contract)
  ck(original==p.evaluate('JSON.stringify(Saytara.app.state.data.items)'),name+' source data unchanged after screen and export')
  dump();print(name,'screens complete',flush=True)
 # Isolated edge-case copy: present late, absent Q2/Q4, undated group and an empty status/cohort intersection.
 p.evaluate('''()=>{const S=Saytara,s=S.app.state;let records=s.data.byPf.agenda.filter(i=>i.t.type==='الأجندة السنوية').slice(0,3).concat(s.data.byPf.agenda.filter(i=>i.t.type==='مستجد').slice(0,3));let statuses=['متأخر','منجز','قيد التطوير','جاهز للعرض','متأخر','منجز'],quarters=['الربع الأول','الربع الثالث','','الربع الثالث','','الربع الأول'];records.forEach((i,k)=>{i.entity='هيئة دبي لتطوير البنية التحتية والخدمات الحكومية والتنسيق بين الجهات المعنية';i.t.entity=i.k.entity=i.x.entity=i.entity;for(let map of[i.t,i.k,i.x]){map.status=statuses[k];map.quarter=quarters[k];map.month='';map.newMonth='';map.year='2026';}i.statusLabel=statuses[k];i.statusCat=S.rules.catOf(statuses[k]);if(k===0){i.title=Array(4).fill('تطوير منظومة تنسيق الخدمات الحكومية واعتماد الخطة التنفيذية للمبادرات الاستراتيجية المشتركة مع الجهات المعنية وتحديد مسؤوليات المتابعة والتقييم').join(' ');i.t.title=i.k.title=i.x.title=i.title;}});}''')
 scope(p,{'entity':['هيئة دبي لتطوير البنية التحتية والخدمات الحكومية والتنسيق بين الجهات المعنية']},[]);contract=p.evaluate(CONTRACT);spec=verify_screen(p,'synthetic',contract,True)
 ck('متأخر'in[s['name']for s in spec['statuses']],'synthetic recorded late row appears')
 ck('undated'in[q['key']for q in spec['displayQuarters']],'synthetic undated group retained')
 ck(not any('الثاني'in q['name']or 'الرابع'in q['name']for q in spec['displayQuarters']),'synthetic absent quarters hide')
 native_pdf(p,'synthetic',contract)
 ctx.close();b.close()
ck(not E['externalRequests'],'no external network requests',E['externalRequests']);ck(not E['errors'],'no browser runtime errors',E['errors'])
ck(hashlib.sha256(FIX.read_bytes()).hexdigest()==E['fixture']['sha256'],'fixture bytes preserved')
E['appFiles']={str(x.relative_to(APP)):hashlib.sha256(x.read_bytes()).hexdigest()for x in[APP/'assets/js/app-bundle.js',APP/'assets/css/app-bundle.css',APP/'assets/css/print-measure-bundle.css']}
dump();print(E['verdict'],len(E['checks']),'checks;',len(E['issues']),'issues')
for issue in E['issues'][:30]:print(issue)
