document.fonts.ready.then(()=>{
 const ctx=document.createElement('canvas').getContext('2d'),result=[];
 function top(el,text){const c=getComputedStyle(el);ctx.font=`${c.fontWeight} ${c.fontSize} ${c.fontFamily}`;ctx.direction=c.direction;const m=ctx.measureText(text),l=parseFloat(c.lineHeight);return(l-m.fontBoundingBoxAscent-m.fontBoundingBoxDescent)/2+m.fontBoundingBoxAscent-m.actualBoundingBoxAscent;}
 document.querySelectorAll('.refined .wb-subgroup h4>button:first-child').forEach(pair=>{
  const text=Array.from(pair.childNodes).find(n=>n.nodeType===Node.TEXT_NODE && n.textContent.trim());
  if(text){const label=document.createElement('span');label.className='concept-subgroup-name';label.textContent=text.textContent;pair.replaceChild(label,text);}
  const label=pair.querySelector('.concept-subgroup-name'),value=pair.querySelector('.wb-subtotal-value');
  if(!label||!value)return;const lt=top(label,label.innerText.trim()),nt=top(value,value.innerText.trim()),target=Math.max(lt,nt);
  label.style.setProperty('--optical-shift',`${target-lt}px`);value.style.setProperty('--optical-shift',`${target-nt}px`);
  const lr=label.getBoundingClientRect(),nr=value.getBoundingClientRect();result.push({label:label.innerText,labelInkY:lr.top+lt,valueInkY:nr.top+nt});
 });
 window.conceptAlignment=result;window.conceptReady=true;
});
