/* Review illustration only. Both chart alternatives consume one source specification. */
(function(){
  'use strict';
  function el(tag,cls,text){var n=document.createElement(tag);if(cls)n.className=cls;if(text!==undefined)n.textContent=text;return n;}
  function number(value,cls){var n=el('bdi',cls,String(value));n.dir='ltr';return n;}
  window.buildAgendaOptionB=function(spec){
    var root=el('section','ag-v3-overview ag-v3-option-b');root.dir='rtl';root.dataset.sourceTotal=spec.total;root.dataset.scaleMin=0;root.dataset.scaleMax=spec.scale.max;
    root.setAttribute('aria-label','ملخص الأجندة السنوية حسب الربع ومستوى الإنجاز');
    var lead=el('header','b-lead'),heading=el('div','b-heading');heading.append(el('h2','','الأجندة السنوية'));
    var total=el('div','b-grand-total');total.append(number(spec.total),el('span','','الإجمالي'));lead.append(heading,total);root.append(lead);
    var scale=el('div','b-chart-heading');scale.append(el('h3','','مستويات الإنجاز حسب الربع'));
    var scaleCaption=el('span','b-scale');scaleCaption.append(el('span','','عدد المواضيع '),number('0–'+spec.scale.max));scale.append(scaleCaption);
    if(spec.total)root.append(scale);
    var summaries=el('div','b-summaries');summaries.style.setProperty('--cohorts',spec.cohorts.length);
    spec.cohorts.forEach(function(c){var summary=el('div','b-summary');summary.dataset.summaryCohort=c.id;summary.append(el('span','',c.name),number(c.total));summaries.append(summary);});root.append(summaries);
    if(!spec.total){root.append(el('p','b-empty','لا توجد مواضيع ضمن النطاق المحدد.'));return root;}
    var cohorts=el('div','b-cohorts');cohorts.style.setProperty('--cohorts',spec.cohorts.filter(function(c){return c.total>0;}).length);
    spec.cohorts.forEach(function(c){
      if(!c.total)return;
      var cohort=el('section','b-cohort');cohort.dataset.cohort=c.id;cohort.dataset.total=c.total;cohort.setAttribute('aria-label',c.name);
      var mobileHeading=el('h4','b-mobile-cohort',c.name);mobileHeading.append(number(c.total));cohort.append(mobileHeading);
      var quarters=el('div','b-quarters');
      c.quarters.forEach(function(q){
        var quarter=el('section','b-quarter');quarter.dataset.quarter=q.key;quarter.dataset.total=q.total;
        var head=el('header','b-quarter-head');head.append(el('h4','',q.name));var count=el('span','b-quarter-total');count.append(number(q.total),el('span','','الإجمالي'));head.append(count);quarter.append(head);
        var rows=el('div','b-bars');
        q.cells.forEach(function(cell){
          if(!cell.count){var zero=el('span','b-sr-only',cell.name+': 0');zero.dataset.zeroStatus=cell.name;zero.dataset.count=0;rows.append(zero);return;}
          var row=el('div','b-bar-row');row.dataset.status=cell.name;row.dataset.count=cell.count;row.setAttribute('aria-label',cell.name+': '+cell.count+' من '+q.total+' موضوعاً في '+q.name);
          var label=el('span','b-status-label',cell.name), track=el('span','b-track'), fill=el('span','b-fill');track.setAttribute('aria-hidden','true');fill.style.width=(spec.scale.max?100*cell.count/spec.scale.max:0)+'%';fill.style.background=cell.color;track.append(fill);row.append(label,track,number(cell.count,'b-value'));rows.append(row);
        });quarter.append(rows);quarters.append(quarter);
      });cohort.append(quarters);cohorts.append(cohort);
    });root.append(cohorts);return root;
  };
})();
