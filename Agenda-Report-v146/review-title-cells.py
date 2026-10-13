from pathlib import Path
import fitz,json,re,collections,hashlib
O=Path(__file__).parent;E=json.loads((O/'evidence.json').read_text());results=[];issues=[]
for run in E['pdf']:
 name=run['scope'];d=fitz.open(O/(name+'.pdf'));P=json.loads((O/(name+'-geometry.json')).read_text());n=0
 for row in P['rows']:
  t=row['title'];matches=[]
  for pi,plan in enumerate(P['plan']):
   for r in plan['regions']:
    s=r['source']
    if s['y']-.1<=t['y']and s['y']+s['h']+.1>=t['y']+t['h']:
     x=(t['x']-s['x']+r['x'])*.75+28.346;y=(t['y']-s['y']+r['y'])*.75+28.346
     clip=fitz.Rect(x-.2,y-.2,x+t['w']*.75+.2,y+t['h']*.75+.2)
     text=' '.join(''.join(c['c']for c in sp['chars']if clip.contains(fitz.Point((c['bbox'][0]+c['bbox'][2])/2,(c['bbox'][1]+c['bbox'][3])/2)))for b in d[pi].get_text('rawdict')['blocks']for l in b.get('lines',[])for sp in l['spans'])
     matches.append(text)
  tokens=lambda s:collections.Counter(re.findall(r'\w+',s))
  ok=len(matches)==1 and tokens(matches[0])==tokens(t['text']);n+=1
  if not ok:issues.append({'check':name+' actual PDF source title cell preserved','detail':{'key':row['key'],'expected':t['text'],'actual':matches}})
 results.append({'scope':name,'titleCells':n,'failures':sum(x['check'].startswith(name+' ')for x in issues),'pdfSHA256':hashlib.sha256((O/(name+'.pdf')).read_bytes()).hexdigest()})
for check in E['checks']:
 if 'actual PDF source title cell preserved'in check['check']:check['pass']=not any(i['check']==check['check']for i in issues)
E['issues']=[i for i in E['issues']if 'actual PDF source title cell preserved'not in i['check']]+issues
for run in E['pdf']:run['pass']=not any(i['check'].startswith(run['scope']+' ')for i in E['issues'])
E['titleCellMethod']='Select glyphs from full-page raw text by actual cell rectangle; compare source word/number multiset to allow RTL/LTR extraction order. Direct PyMuPDF clipped extraction was avoided because it introduced a phantom zero-width lam absent in whole-page raw glyph data.'
E['titleCellReview']=results;E['verdict']='PASS'if not E['issues']and not E['errors']else'FAIL'
(O/'evidence.json').write_text(json.dumps(E,ensure_ascii=False,indent=2));(O/'title-cell-evidence.json').write_text(json.dumps({'method':E['titleCellMethod'],'cases':results,'issues':issues},ensure_ascii=False,indent=2));print(E['verdict'],len(E['checks']),'checks',len(E['issues']),'issues',sum(r['titleCells']for r in results),'exact title cells')
for issue in issues:print(issue)
