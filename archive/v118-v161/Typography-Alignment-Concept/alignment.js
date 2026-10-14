/* Preview only: align visible glyph tops after the real fonts have loaded. */
document.fonts.ready.then(()=>{
 const canvas=document.createElement('canvas'),ctx=canvas.getContext('2d');
 function inkTop(el,text){
  const c=getComputedStyle(el);ctx.font=`${c.fontWeight} ${c.fontSize} ${c.fontFamily}`;ctx.direction=c.direction;
  const m=ctx.measureText(text || el.innerText.trim());
  const line=parseFloat(c.lineHeight),asc=m.fontBoundingBoxAscent,desc=m.fontBoundingBoxDescent;
  return (line-asc-desc)/2+asc-m.actualBoundingBoxAscent;
 }
 const metrics=[];
 document.querySelectorAll('.requested .wb-subgroup h4>button:first-child,.compact .wb-subgroup h4>button:first-child').forEach(pair=>{
  const text=Array.from(pair.childNodes).find(n=>n.nodeType===Node.TEXT_NODE && n.textContent.trim());
  if(text){const label=document.createElement('span');label.className='subgroup-label';label.textContent=text.textContent;pair.replaceChild(label,text);}
 });
 document.querySelectorAll('.requested .wb-stat-main,.compact .wb-stat-main,.requested .wb-total-main,.compact .wb-total-main,.strategy-literal .wb-stat-main,.requested .wb-subgroup h4>button:first-child,.compact .wb-subgroup h4>button:first-child').forEach(pair=>{
  const label=pair.querySelector(':scope>.wb-stat-label,:scope>.subgroup-label,:scope>span'),number=pair.querySelector(':scope>strong,:scope>.wb-subtotal-value');
  if(!label||!number)return;
  // The first visible line governs wrapped-label optical alignment.
  const words=label.innerText.trim().split(/\s+/);let first='';const cs=getComputedStyle(label);
  ctx.font=`${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`;
  for(const word of words){const next=(first?first+' ':'')+word;if(first && ctx.measureText(next).width>label.clientWidth)break;first=next;}
  const lt=inkTop(label,first),nt=inkTop(number);const top=Math.max(lt,nt);
  label.classList.add('optical-label');number.classList.add('optical-number');
  label.style.setProperty('--optical-shift',`${top-lt}px`);number.style.setProperty('--optical-shift',`${top-nt}px`);
  const lr=label.getBoundingClientRect(),nr=number.getBoundingClientRect();
  metrics.push({kind:pair.closest('.specimen').dataset.kind,phase:pair.closest('.specimen').dataset.phase,label:label.innerText,firstLine:first,labelShift:top-lt,numberShift:top-nt,labelInkY:lr.top+lt,numberInkY:nr.top+nt});
 });
 window.conceptAlignment=metrics;window.conceptReady=true;
});
