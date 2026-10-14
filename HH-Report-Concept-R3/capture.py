from playwright.sync_api import sync_playwright
from pathlib import Path
import json
P=Path(__file__).parent
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
import threading
server=ThreadingHTTPServer(('127.0.0.1',0),partial(SimpleHTTPRequestHandler,directory=str(P)))
threading.Thread(target=server.serve_forever,daemon=True).start()
URL=f'http://127.0.0.1:{server.server_port}/index.html'
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1600,'height':1100},device_scale_factor=1)
 errors=[];page.on('pageerror',lambda e: errors.append(str(e)))
 page.goto(URL);page.evaluate('document.fonts.ready')
 page.evaluate('scrollTo(0,0)');box=page.locator('#overview').bounding_box();height=int(box['y']+box['height']+32)
 page.set_viewport_size({'width':1600,'height':height});page.screenshot(path=str(P/'overview-desktop.png'))
 page.locator('#chart').screenshot(path=str(P/'charts-desktop.png'))
 page.locator('#project-list').screenshot(path=str(P/'project-list.png'))
 page.locator('#project-detail').screenshot(path=str(P/'project-detail.png'))
 page.locator('#display-rules').screenshot(path=str(P/'display-rules.png'))
 page.evaluate("HH_PREVIEW.setScope({unit:['مكتب خطة دبي']})")
 page.evaluate('scrollTo(0,0)');box=page.locator('#overview').bounding_box();height=int(box['y']+box['height']+32)
 page.set_viewport_size({'width':1600,'height':height});page.screenshot(path=str(P/'overview-filtered.png'))
 page.set_viewport_size({'width':390,'height':844});page.goto(URL);page.evaluate('document.fonts.ready')
 box=page.locator('#overview').bounding_box();height=int(box['y']+box['height']+16)
 page.set_viewport_size({'width':390,'height':height});page.screenshot(path=str(P/'overview-phone.png'))
 page.locator('#project-detail').screenshot(path=str(P/'detail-phone.png'))
 (P/'capture-evidence.json').write_text(json.dumps({'browser_errors':errors,'mobile_width':page.evaluate('({content:document.documentElement.scrollWidth,viewport:innerWidth})')},ensure_ascii=False,indent=2))
 print('Captured, errors:',errors);b.close()

server.shutdown()
