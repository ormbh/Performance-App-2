from pathlib import Path
from bs4 import BeautifulSoup
import base64,json,hashlib,re
O=Path(__file__).parent
APP=Path('/workspace/saytara-work/Performance-App-v154')
model=json.loads((O/'source-model.json').read_text())
fonts=''
for family,name,fmt in [('TEC Dubai','Dubai-Regular.otf','opentype'),('TEC DIN','DIN-Next-Arabic-Regular.otf','opentype'),('TEC DIN LT','DIN-Next-LT-Arabic-Regular.ttf','truetype')]:
 encoded=base64.b64encode((APP/'assets/fonts'/name).read_bytes()).decode()
 fonts+=f"@font-face{{font-family:'{family}';src:url(data:font/{'otf' if fmt=='opentype' else 'ttf'};base64,{encoded}) format('{fmt}');font-weight:400;font-style:normal;}}\n"
soup=BeautifulSoup((O/'overview.html').read_text(),'html.parser')
# The latest review instruction gives ready labels and plain values Teal.
for e in soup.select('[data-status="جاهز للعرض"]'):
 if e.name!='rect':
  e['style']=(e.get('style','')+';color:#115E67;--agenda-count-ink:#115E67')
for e in soup.select('[data-status-totals], [data-status-counts]'):
 for attr in ['data-status-totals','data-status-counts']:
  if e.has_attr(attr):
   values=json.loads(e[attr])
   for s in values:
    if s['name']=='جاهز للعرض':s['textColor']='#115E67'
   e[attr]=json.dumps(values,ensure_ascii=False)
for e in soup.select('.a-axis-label'):
 if e.text=='0':e.string='–'
# In-bar text uses unchanged source rects. Browser layout below decides which labels fit.
for rect in soup.select('rect.a-quarter-segment'):
 text=soup.new_tag('text',attrs={'class':'a-inbar-count','x':str(float(rect['x'])+float(rect['width'])/2),'y':str(float(rect['y'])+float(rect['height'])/2),'text-anchor':'middle','dominant-baseline':'central','direction':'ltr','data-status':rect['data-status'],'data-count':rect['data-count'],'aria-hidden':'true'})
 text.string=rect['data-count']
 text['style']='fill:'+('#FCFBFB' if rect['fill'] in ['#01831E','#C00000','#651D32','#4F4E4E','#115E67'] else '#115E67')
 rect.insert_after(text)

defs=BeautifulSoup((O/'definitions.html').read_text(),'html.parser')
for e in defs.select('[data-agenda-status="جاهز للعرض"] dt'):e['style']='color:#115E67'
css=fonts+(APP/'assets/css/tec-agenda-matrix.css').read_text()+'''
:root{--font:'TEC Dubai';--heading-font:'TEC DIN';--figure-font:'TEC DIN LT';--tec-paper:#FCFBFB;--tec-linen:#EFEBE7;--tec-sand:#E7E0D3;--tec-teal:#115E67;--tec-charcoal:#333333;--tec-ink:#4F4E4E;--tec-taupe:#756B5F}
*{box-sizing:border-box}body{margin:0;background:#EFEBE7;color:#4F4E4E;font:400 16px/1.6 var(--font)}main{padding:24px 48px 32px;margin:auto;max-width:1920px}.review-meta{display:flex;align-items:center;justify-content:space-between;gap:24px;margin:0 0 16px;font-size:14px;color:#756B5F}.review-meta p{margin:0}.ag-definitions{margin-top:24px;padding:24px;background:#FCFBFB;border:1px solid #E7E0D3;border-radius:18px}.ag-definitions h2{font:400 28px/1.4 var(--heading-font);color:#333333;margin:0 0 24px}.ag-definitions dl{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;margin:0}.ag-definitions dt{display:flex;align-items:baseline;gap:8px;font:400 18px/1.6 var(--font)}.ag-definitions dd{font:400 14px/1.6 var(--font);margin:8px 0 0}.ag-definition-swatch{display:inline-block;width:10px;height:10px;flex:none;border-radius:2px}.ag-matrix-overview .a-quarter-chart{max-height:none}.ag-matrix-overview .a-quarter-chart .a-inbar-count{font:400 18px var(--figure-font);pointer-events:none}.a-label-backing{pointer-events:none}.review-note{color:#756B5F;font-size:14px;margin:16px 0 0}.review-reference{margin-top:24px;background:#FCFBFB;padding:24px;border:1px solid #E7E0D3;border-radius:18px}.review-reference h2{font:400 28px/1.4 var(--heading-font);color:#333333;margin:0 0 16px}.review-reference .a-count-disclosure{display:none}.review-reference .count-reference-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}.review-reference .count-reference-grid>section{min-width:0}.review-reference h3{font:400 24px/1.5 var(--heading-font);color:#333333;margin:0 0 12px}.review-reference .ag-matrix-overview{padding:0;border:0;border-radius:0}.review-reference .a-matrix{min-width:0}.review-reference .a-count-table-scroll{overflow:auto}.review-reference .a-matrix .a-status-col{width:23%}.review-reference .a-matrix .a-sum-col{width:12%}
@media screen and (max-width:700px){main{padding:16px}.review-meta{flex-direction:column;align-items:flex-start;gap:4px}.ag-definitions{padding:16px}.ag-definitions dl{grid-template-columns:1fr}.review-reference{padding:16px}.review-reference .count-reference-grid{grid-template-columns:1fr}.review-reference .a-matrix{min-width:560px}}
@page{size:A4 landscape;margin:10mm}
@media print{
 body{background:#FCFBFB}.review-meta{font-size:8pt;margin-bottom:2mm}main{padding:0;max-width:none}.ag-matrix-overview{padding:3mm;border-radius:3mm}.ag-matrix-overview .a-overview-lead{margin-bottom:0}.ag-matrix-overview .a-chart-head{margin:0 0 1mm}.ag-matrix-overview .a-chart-panels{gap:4mm}.ag-matrix-overview .a-chart-panel{padding:2mm}.ag-matrix-overview .a-axis-title{font-size:9pt;margin:1mm 0 0}.ag-matrix-overview .a-quarter-chart{margin-top:0;max-height:none}.ag-matrix-overview .a-quarter-detail{min-height:0;padding-top:2mm}.ag-matrix-overview .a-status-context{font-size:9pt;margin:0 0 1mm}.ag-matrix-overview .a-status-values{font-size:10.5pt;gap:1mm 3mm}.ag-matrix-overview .a-detail-number{font-size:12pt}.ag-matrix-overview .a-count-disclosure{display:none!important}.ag-matrix-overview .a-quarter-total{font-size:29px!important}.ag-matrix-overview .a-axis-label{font-size:18px}.ag-matrix-overview .a-quarter-label{font-size:18px}.ag-matrix-overview .a-quarter-chart .a-inbar-count{font-size:22px}.ag-definitions{margin-top:2mm;padding:3mm;border-radius:3mm;break-inside:avoid}.ag-definitions h2{font-size:14pt;margin-bottom:2mm}.ag-definitions dl{gap:2mm 5mm}.ag-definitions dt{font-size:10.5pt;gap:2mm}.ag-definitions dd{font-size:9pt;margin-top:1mm;line-height:1.45}.ag-definition-swatch{width:2mm;height:2mm;border-radius:.4mm}.review-note{font-size:8pt;margin-top:2mm}.review-reference{break-before:page;page-break-before:always;margin:0;padding:3mm}.review-reference h2{font-size:16pt}.review-reference h3{font-size:14pt}.review-reference .count-reference-grid{gap:4mm}.review-reference .a-matrix{font-size:10.5pt}.review-reference .a-matrix :is(th,td){padding:2mm 1mm}.review-reference .a-matrix :is(.a-status-name,.a-status-heading){font-size:10.5pt}.review-reference .a-matrix thead th{font-size:10pt}.review-reference .a-cell-number{font-size:16pt}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}
}
'''
# Reuse the original v154 event behavior in this isolated DOM snapshot.
source=(APP/'assets/js/views/agenda-matrix.js').read_text()
start=source.index('  function node(');stop=source.index('  function appearance(')
helpers=source[start:stop]+source[source.index('  function detailContent('):source.index('  function chart(')]
behavior=source[source.index('  function resetPanel('):source.index('  S.agendaMatrix =')]
script='''const S={};\n'''+helpers+behavior+'''
function setPlotHeight(height,topPad=36,bottomPad=56){
 document.querySelectorAll('.a-quarter-chart').forEach(svg=>{
  if(!svg.dataset.original)svg.dataset.original=svg.innerHTML;
  svg.innerHTML=svg.dataset.original;
  const ratio=height/236, bottom=topPad+height;
  svg.setAttribute('viewBox','0 0 650 '+(bottom+bottomPad));
  svg.querySelectorAll('.a-chart-grid').forEach(line=>{const y=topPad+(+line.getAttribute('y1')-90)*ratio;line.setAttribute('y1',y);line.setAttribute('y2',y)});
  svg.querySelectorAll('.a-axis-label').forEach(t=>t.setAttribute('y',topPad+(+t.getAttribute('y')-4-90)*ratio+4));
  svg.querySelectorAll('.a-quarter-bar').forEach(g=>{
   const total=g.querySelector('.a-quarter-total'),top=topPad+(+total.getAttribute('y')+12-90)*ratio;
   total.setAttribute('y',top-12);
   const focus=g.querySelector('.a-bar-focus');focus.setAttribute('y',Math.max(30,top-36));focus.setAttribute('height',bottom-Math.max(30,top-36)+80);
   g.querySelectorAll('.a-quarter-label').forEach(t=>t.setAttribute('y',bottom+31));
   g.querySelectorAll('.a-quarter-segment').forEach(rect=>{
    const y=topPad+(+rect.getAttribute('y')-90)*ratio,h=+rect.getAttribute('height')*ratio;
    rect.setAttribute('y',y);rect.setAttribute('height',h);
    const label=rect.nextElementSibling;label.setAttribute('y',y+h/2);
   });
  });
 });
}
function fitCounts(){
 document.querySelectorAll('.a-quarter-chart').forEach(svg=>{
  const scale=svg.getBoundingClientRect().width/svg.viewBox.baseVal.width;
  svg.querySelectorAll('.a-quarter-segment').forEach(rect=>{
   const next=rect.nextElementSibling;
   const backing=next&&next.classList.contains('a-label-backing')?next:null;
   const label=backing?backing.nextElementSibling:next;
   if(!label||!label.classList.contains('a-inbar-count'))return;
   label.style.display='';if(backing)backing.style.display='';
   const box=label.getBBox();const room=+rect.getAttribute('height');
   const canvas=document.createElement('canvas').getContext('2d');const fontSize=parseFloat(getComputedStyle(label).fontSize);canvas.font=fontSize+'px "TEC DIN LT"';
   const ink=canvas.measureText(label.textContent);const inkHeight=ink.actualBoundingBoxAscent+ink.actualBoundingBoxDescent;
   label.setAttribute('dominant-baseline','auto');
   label.setAttribute('y',+rect.getAttribute('y')+room/2+(ink.actualBoundingBoxAscent-ink.actualBoundingBoxDescent)/2);
   // 16 CSS px minimum on screen; use the full font box plus 2 SVG-unit breathing room.
   const print=matchMedia('print').matches;
   const readable=print||fontSize*scale>=16;
   const fits=room>=inkHeight+4&&+rect.getAttribute('width')>=box.width+8&&readable;
   label.style.display=fits?'':'none';if(backing)backing.style.display=fits?'':'none';
   label.dataset.fits=String(fits);
  });
 });
}
window.addEventListener('resize',fitCounts);
window.addEventListener('beforeprint',()=>{resetDetails();setPlotHeight(236,20,56);fitCounts()});
window.addEventListener('afterprint',()=>{setPlotHeight(480);fitCounts()});
document.fonts.ready.then(()=>{setPlotHeight(480);fitCounts()});
'''
reference='<section class="review-reference"><h2>الأعداد الدقيقة حسب الربع</h2><div class="count-reference-grid">'
for panel in soup.select('.a-chart-panel'):
 table=BeautifulSoup(str(panel.select_one('.a-count-table-scroll')),'html.parser')
 for e in table.select('[id]'):e['id']='reference-'+e['id']
 for e in table.select('[headers]'):e['headers']=' '.join('reference-'+v for v in e['headers'])
 reference+='<section><h3>'+panel.select_one('h4').text+'</h3><div class="ag-matrix-overview">'+str(table)+'</div></section>'
reference+='</div></section>'
meta='<div class="review-meta"><p>تصور للمراجعة · أرقام داخل الأعمدة</p><p>بيانات توضيحية · يناير – سبتمبر 2026 · تاريخ المصدر <bdi>30/09/2026</bdi></p></div>'
note='<p class="review-note">تظهر الأرقام داخل المقاطع التي تتسع لها. المقاطع الصغيرة تحتفظ بحجمها النسبي؛ أعدادها الدقيقة متاحة عند المرور على العمود وفي جدول الأعداد.</p>'
html='<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>الأجندة — تصور الأرقام داخل الأعمدة</title><style>'+css+'</style></head><body><main>'+meta+'<div id="paired-charts-and-definitions">'+str(soup)+str(defs)+note+'</div>'+reference+'</main><script>'+script+'</script></body></html>'
(O/'Agenda-In-Bar-Illustration.html').write_text(html)
print('Built self-contained HTML:',len(html),'characters')
