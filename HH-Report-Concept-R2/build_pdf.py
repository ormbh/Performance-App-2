"""Build the illustrative review PDF from the actual revised HTML DOM.

The chart, legend, detail card and display samples come directly from index.html.
Only page furniture and print layout are composed here. Native browser text and
vector output is retained; no screenshot is used as PDF page content.
"""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import hashlib
import html
import json
import threading

import fitz
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
PDF_PATH = ROOT / 'TEC_HH_Report_Review_R2.pdf'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def esc(value):
    return html.escape(str(value))


def marker():
    return '<div class="review-marker">تصور للمراجعة · بيانات توضيحية · صياغة تعريفات الحالات مقترحة</div>'


def footer(number, total):
    return ('<footer class="print-footer"><span>الأمانة العامة للمجلس التنفيذي لإمارة دبي · '
            'حقوق النشر © 2026 · جميع الحقوق محفوظة</span>'
            f'<span>صفحة {number} من {total}</span></footer>')


def heading(title, subtitle):
    return f'<header class="print-head"><h1>{esc(title)}</h1><p>{esc(subtitle)}</p></header>'


PRINT_CSS = r'''
@page{size:A4 landscape;margin:0}
html,body{margin:0;padding:0;direction:rtl;background:#FCFBFB;-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-size:16px;line-height:1.35}
.sheet{width:297mm;height:210mm;padding:8mm 10mm 18mm;position:relative;background:#FCFBFB;overflow:hidden;break-after:page}
.sheet:last-child{break-after:auto}
.print-head{height:13mm;display:flex;align-items:flex-start;justify-content:space-between;gap:10mm;border-bottom:1px solid #E7E0D3;padding-bottom:3mm;margin-bottom:4mm}
.print-head h1{font-size:24px;line-height:1.4}
.print-head p{font-size:16px;white-space:nowrap;padding-top:2mm;color:#756B5F}
.review-marker{position:absolute;left:10mm;bottom:11.8mm;font-size:10px;color:#756B5F}
.print-footer{position:absolute;bottom:4mm;right:10mm;left:10mm;display:flex;justify-content:space-between;border-top:1px solid #E7E0D3;padding-top:2mm;font-size:11px;color:#756B5F}
.cover{padding:0;background-image:url('assets/img/agenda-cover.jpg');background-position:center;background-size:cover}
.cover:before{content:'';position:absolute;inset:0;background:rgba(252,251,251,.9)}
.cover .logos{position:absolute;width:277mm;height:auto;top:13mm;right:10mm}
.cover .cover-copy{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6mm;text-align:center}
.cover h1{font-size:40px;max-width:230mm}
.cover .organization{font-size:21.333px}
.cover .period{font-size:18.667px}
.cover .review-marker{bottom:6mm;font-size:11.333px}
.card{padding:4mm;border-radius:4mm}
.card h2{font-size:21px}
.chart-card{padding:4mm}
.chart-header{gap:3mm;margin-bottom:3mm}
.chart-header span{font-size:11px}
.chart-axis{margin-bottom:1mm;font-size:10px}
.sector-row{padding:2.6mm 0;column-gap:3mm;grid-template-columns:36mm minmax(0,1fr)}
.sector-name{font-size:12px;line-height:1.45}
.sector-track,.sector-segment{height:22px}
.sector-values{font-size:10px;gap:1mm 2mm;margin-top:1.5mm;line-height:1.2}
.sector-segment .num{font-size:14px}
.status-totals{gap:2mm;padding-top:2mm;margin-top:2mm}
.status-total{gap:1mm;font-size:11px;width:auto}
.status-total .num{font-size:18px;margin:0}
.swatch{width:9px;height:9px}
.detail-card{padding:5mm}
.detail-header{padding-bottom:4mm;gap:6mm}
.detail-title h3{font-size:25px;line-height:1.4}
.detail-title p{font-size:13px;margin-top:1.5mm}
.detail-status,.recorded-progress{gap:3mm;flex-direction:row}
.progress-ring{width:64px;height:64px;padding:5px}
.progress-ring .num{font-size:21px}
.progress-caption{font-size:11px;max-width:65px}
.badge{font-size:12px;min-height:26px;border-radius:6px;padding:2px 8px}
.project-meta{gap:5mm;margin:4mm 0}
.data-field dt{font-size:12px;margin-bottom:1mm}
.data-field dd{font-size:14px;line-height:1.45}
.detail-extra{padding-top:4mm;gap:4mm 5mm}
.print-sample-note{font-size:11px;color:#756B5F;margin-bottom:3mm}
.rules-wrap{margin-top:5mm}
.rules-wrap h2{font-size:22px}
.rules-wrap .section-heading{margin-bottom:2mm}
.rules-wrap .section-heading>span{font-size:11px}
.rules-wrap p{font-size:16px}
.paired-charts{margin-top:0}
.paired-charts>.section-heading{display:none}
.cohort-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:4mm}
.cohort-panel{padding:3mm}
.cohort-title{min-height:0;margin-bottom:2mm;gap:3mm;align-items:center}
.cohort-title h3{font-size:23px}
.cohort-title .total-block{min-width:36px}
.cohort-title .total-block .num{font-size:29px}
.cohort-title .total-block span{font-size:16px;margin-top:0}
.cohort-axis,.cohort-row{grid-template-columns:172px minmax(0,1fr) 40px;gap:7px}
.cohort-axis{font-size:16px;margin-bottom:1mm}
.cohort-ticks .num{font-size:16px}
.cohort-row{min-height:45px;padding:2px 0}
.cohort-sector{font-size:16px;line-height:1.15}
.cohort-bar,.cohort-segment{height:23px;min-height:23px}
.cohort-segment .num{font-size:18px}
.cohort-total{font-size:22px}
.segment-keys{font-size:16px;line-height:1.1;gap:3px;margin-top:2px;min-height:18px}
.cohort-status-totals{min-height:0;gap:2px 13px;padding-top:2mm}
.cohort-status{gap:6px}
.cohort-status>span{font-size:16px}
.cohort-status .num{font-size:22px}
.detailed-legend{padding:2mm;margin-top:2mm}
.detailed-legend h3{font-size:21px}
.detailed-legend dl{grid-template-columns:repeat(3,minmax(0,1fr));gap:2mm 6mm;margin-top:2mm;margin-bottom:0}
.detailed-legend dt{font-size:16px;line-height:1.25;gap:2mm;margin-bottom:1mm}
.detailed-legend dd{font-size:16px;line-height:1.2}
.detail-title p,.progress-caption,.badge,.data-field dt,.data-field dd{font-size:16px}
.rules-wrap .section-heading>span{font-size:16px}
.rules-grid{gap:4mm}
.rules-grid h3{font-size:22px}
.rule-sample{min-height:75px}
.ready-example{margin:8px 0}
.ready-bar-example{margin-bottom:8px}

'''


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass


def main():
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(ROOT)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f'http://127.0.0.1:{server.server_port}'
    errors = []
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(executable_path='/usr/bin/chromium', headless=True,
                                        args=['--no-sandbox', '--disable-dev-shm-usage'])
            page = browser.new_page(viewport={'width':1440,'height':1000}, device_scale_factor=1)
            page.on('pageerror', lambda exc: errors.append(str(exc)))
            page.goto(base + '/index.html', wait_until='networkidle')
            page.evaluate('document.fonts.ready')
            page.wait_for_function('window.HH_PREVIEW && window.HH_DATA')
            page.evaluate("HH_PREVIEW.setScope({});HH_PREVIEW.selectProject('special-26')")
            chart_html = page.locator('#chart').inner_html()
            detail_html = page.locator('#detail').inner_html()
            rule_selector = '#display-rules'
            rules_html = page.locator(rule_selector).inner_html() if page.locator(rule_selector).count() else ''
            snapshot = page.evaluate('''() => ({
                total: HH_DATA.items.length,
                leadership: HH_DATA.items.filter(x=>x.t.lead==='نعم').length,
                tec: HH_DATA.items.filter(x=>x.t.lead!=='نعم').length,
                blankLeadership: HH_DATA.items.filter(x=>!String(x.t.lead??'').trim()).length,
                state: window.HH_PREVIEW_STATE,
                cohorts: window.HH_COHORTS,
                detailKey: document.querySelector('#detail [data-record]')?.dataset.record
            })''')
            assert (snapshot['total'], snapshot['leadership'], snapshot['tec']) == (62,24,38), snapshot
            cohorts = snapshot['cohorts']
            assert cohorts['scaleMax'] == 15
            assert len(cohorts['leadership']) == 24 and len(cohorts['tec']) == 38
            assert not (set(cohorts['leadership']) & set(cohorts['tec']))
            assert len(set(cohorts['leadership']) | set(cohorts['tec'])) == 62
            assert 'ملف المصدر' not in detail_html
            assert 'source-field' not in detail_html
            assert not errors, errors
            cover = ('<section class="sheet cover"><img class="logos" src="assets/img/agenda-logos.png" '
                     'alt="حكومة دبي والمجلس التنفيذي"><div class="cover-copy"><h1>تقرير المشاريع الخاصة</h1>'
                     '<p class="organization">الأمانة العامة للمجلس التنفيذي</p>'
                     '<p class="period">حتى تاريخ <bdi dir="ltr">30/09/2026</bdi></p></div>' + marker() + '</section>')
            summary = ('<section class="sheet chart-sheet">'
                       + heading('توزيع المشاريع حسب القطاع', 'حتى تاريخ 30/09/2026 · النطاق: الكل · الإجمالي: 62')
                       + '<div id="print-chart">' + chart_html + '</div>' + marker() + footer(1,2) + '</section>')
            detail = ('<section class="sheet detail-sheet">'
                      + heading('تفاصيل المشروع', 'عينة للمراجعة من بيانات توضيحية')
                      + '<div id="print-detail">' + detail_html + '</div>'
                      + ('<div class="rules-wrap" id="print-rules">' + rules_html + '</div>' if rules_html else '')
                      + marker() + footer(2,2) + '</section>')
            doc = ('<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">'
                   '<meta name="viewport" content="width=device-width,initial-scale=1">'
                   '<title>تصور تقرير المشاريع الخاصة · مراجعة ثانية</title>'
                   '<link rel="stylesheet" href="style.css"><style>' + PRINT_CSS + '</style></head><body>'
                   + cover + summary + detail + '</body></html>')
            (ROOT/'report-print.html').write_text(doc)
            page.set_viewport_size({'width':1123,'height':794})
            page.goto(base + '/report-print.html', wait_until='networkidle')
            page.evaluate('document.fonts.ready')
            page.wait_for_function('Array.from(document.images).every(i=>i.complete && i.naturalWidth>0)')
            assert page.locator('#print-chart').inner_html() == chart_html
            assert page.locator('#print-detail').inner_html() == detail_html
            assert page.locator('#print-rules').inner_html() == rules_html
            chart_geometry = page.evaluate('''() => [...document.querySelectorAll('.cohort-panel')].map(p=>({
                cohort:p.dataset.cohort,
                total:Number(p.querySelector('.total-block .num').textContent),
                segments:[...p.querySelectorAll('.cohort-segment')].map(s=>{
                    const r=s.getBoundingClientRect(),n=s.querySelector('.num').getBoundingClientRect();
                    return {count:Number(s.dataset.count),status:s.dataset.status,
                        displayed:Number(s.textContent),sector:s.closest('.cohort-row').dataset.sector,
                        numberInside:n.left>=r.left-.1&&n.right<=r.right+.1&&n.top>=r.top-.1&&n.bottom<=r.bottom+.1,
                        proportional:Math.abs(r.width/s.parentElement.getBoundingClientRect().width-Number(s.dataset.count)/15)<.001};
                }),
                statusTotals:[...p.querySelectorAll('.cohort-status')].map(s=>({status:s.dataset.status,count:Number(s.querySelector('.num').textContent)}))
            }))''')
            assert [c['total'] for c in chart_geometry] == [24,38]
            assert all(s['numberInside'] and s['proportional'] and s['count']==s['displayed'] for c in chart_geometry for s in c['segments'])
            assert all(sum(s['count'] for s in c['segments'])==c['total'] for c in chart_geometry)
            assert all(sum(s['count'] for s in c['statusTotals'])==c['total'] for c in chart_geometry)
            body_sizes = page.evaluate('''() => [...document.querySelectorAll('.cohort-sector,.cohort-axis,.segment-keys,.cohort-status>span,.detailed-legend dt,.detailed-legend dd,.data-field dt,.data-field dd,.rules-grid p')].map(e=>parseFloat(getComputedStyle(e).fontSize))''')
            assert min(body_sizes)>=16
            bounds = page.evaluate('''() => [...document.querySelectorAll('.sheet')].map(s=>({
                height:s.clientHeight,scrollHeight:s.scrollHeight,
                children:[...s.children].map(e=>({class:e.className,id:e.id,
                    top:e.getBoundingClientRect().top-s.getBoundingClientRect().top,
                    bottom:e.getBoundingClientRect().bottom-s.getBoundingClientRect().top}))
            }))''')
            assert all(s['scrollHeight']==s['height'] for s in bounds), bounds
            for s in bounds[1:]:
                marker_top = next(c['top'] for c in s['children'] if c['class']=='review-marker')
                assert all(c['bottom'] <= marker_top-10 for c in s['children'] if c['id'].startswith('print-')),s
            page.pdf(path=str(PDF_PATH),print_background=True,prefer_css_page_size=True)
            browser.close()
    finally:
        server.shutdown()
    pdf = fitz.open(PDF_PATH)
    assert len(pdf)==3, len(pdf)
    for n, page in enumerate(pdf,1):
        page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(ROOT/f'print-{n}.png')
    outside = [{'page':n+1,'bbox':list(sp['bbox']),'text':sp['text']}
               for n,pg in enumerate(pdf) for block in pg.get_text('dict')['blocks'] if 'lines' in block
               for line in block['lines'] for sp in line['spans']
               if sp['bbox'][0]<0 or sp['bbox'][1]<0 or sp['bbox'][2]>pg.rect.width+.1 or sp['bbox'][3]>pg.rect.height+.1]
    fonts = [{'page':n+1,'fonts':[{
        'name':f[3] or f[4],'type':f[2],
        'selfContained':bool(pdf.extract_font(f[0])[3]) or (f[2]=='Type3' and '/CharProcs' in pdf.xref_object(f[0])),
        'toUnicode':'/ToUnicode' in pdf.xref_object(f[0])} for f in pg.get_fonts()]} for n,pg in enumerate(pdf)]
    evidence = {
        'pages':len(pdf),'pdfFile':PDF_PATH.name,'pdfSha256':sha(PDF_PATH),
        'geometry':[list(p.rect) for p in pdf],
        'inputs':{f:sha(ROOT/f) for f in ('index.html','app.js','style.css','data.js')},
        'scope':'All 62 illustrative HH records; leadership is t.lead=نعم (24); TEC is every other record including blanks (38). Detail page is one sample record.',
        'snapshot':snapshot,'bounds':bounds,'browserErrors':errors,
        'chartGeometry':chart_geometry,
        'minimumBodyFontPoints':min(body_sizes)*72/96,
        'checks':{'cohortsDisjointComplete':True,'segmentNumbersInsideBars':True,'commonCountScale15':True,'segmentAndStatusTotalsReconciled':True,'noPageOverflow':True,'footerClearance':True,'sourceFilenameAbsentFromCard':True},
        'nativeDomClones':{'chart':True,'detail':True,'displayRules':bool(rules_html)},
        'domFragmentSha256':{'chart':hashlib.sha256(chart_html.encode()).hexdigest(),'detail':hashlib.sha256(detail_html.encode()).hexdigest(),'rules':hashlib.sha256(rules_html.encode()).hexdigest()},
        'bodyTextExtracted':[len(p.get_text()) for p in pdf],
        'imageCounts':[len(p.get_images()) for p in pdf],
        'fonts':fonts,
        'fontNote':'Chromium embeds the supplied OTF faces as Type3 vector glyph subsets with ToUnicode maps; DIN LT uses an embedded TrueType subset. Appearance and selectable text are checked, not PDF accessibility certification.',
        'textOutsidePage':outside,
    }
    (ROOT/'print-evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2))
    print(json.dumps({'pages':len(pdf),'textOutsidePage':outside,'bounds':bounds},ensure_ascii=False))


if __name__ == '__main__':
    main()
