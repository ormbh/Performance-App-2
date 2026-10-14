/* Illustration-only shared shell. Reuses the reviewed source order and header. */
(function(){
  'use strict';
  window.agendaV4Shell=function(spec,variant){
    var root=window.buildAgendaOptionA(spec);
    root.classList.add(variant);
    var plots=root.querySelector('.a-chart-panels');if(plots)plots.remove();
    return root;
  };
  window.agendaV4Quarters=function(spec){
    var root=window.buildAgendaOptionA(spec);
    var keys=JSON.parse(root.dataset.displayQuarterKeys||'[]');
    return keys.map(function(key){
      for(var i=0;i<spec.cohorts.length;i++){
        var q=spec.cohorts[i].quarters.find(function(q){return q.key===key;});
        if(q)return {key:key,name:q.name};
      }
      return {key:key,name:String(key)};
    });
  };
})();
