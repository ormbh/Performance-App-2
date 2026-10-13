/* Review illustration only: grouped horizontal quarter bars; no repeated totals. */
(function () {
  'use strict';
  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }
  function number(value) {
    var n = el('bdi', 'g-count', String(value));
    n.dir = 'ltr';
    return n;
  }
  window.buildAgendaGrouped = function (spec) {
    var root = window.agendaV4Shell(spec, 'v4-grouped');
    root.setAttribute('aria-label', 'الأجندة السنوية — مقارنة الأرباع بأشرطة أفقية لكل حالة');
    var quarters = window.agendaV4Quarters(spec);
    root.dataset.displayQuarterKeys = JSON.stringify(quarters.map(function (q) { return q.key; }));
    if (!spec.total) return root;
    var panels = el('div', 'g-panels');
    var active = spec.cohorts.filter(function (c) { return c.total > 0; });
    panels.style.setProperty('--cohorts', String(active.length));
    active.forEach(function (cohort, ci) {
      var panel = el('figure', 'g-panel');
      panel.dataset.cohort = cohort.id;
      panel.dataset.scaleMax = String(spec.scale.max);
      panel.setAttribute('aria-label', cohort.name + ': مقارنة عدد المواضيع في الأرباع لكل حالة');
      panel.append(el('figcaption', 'g-mobile-title', cohort.name));
      var columnHead = el('div', 'g-column-head');
      columnHead.append(el('span', 'g-status-column', 'الحالة'), el('span', 'g-bars-column', 'الأرباع'));
      panel.append(columnHead);
      spec.statuses.forEach(function (status, si) {
        var group = el('section', 'g-status-group');
        group.dataset.status = status.name;
        var label = el('h4', 'g-status-name', status.name);
        label.id = 'grouped-status-' + ci + '-' + si;
        group.setAttribute('aria-labelledby', label.id);
        group.append(label);
        var bars = el('div', 'g-bars');
        quarters.forEach(function (quarter) {
          var sourceQuarter = cohort.quarters.find(function (q) { return q.key === quarter.key; });
          var cell = sourceQuarter && sourceQuarter.cells.find(function (c) { return c.name === status.name; });
          var count = cell ? cell.count : 0;
          var row = el('div', 'g-bar-row');
          row.dataset.status = status.name;
          row.dataset.quarter = quarter.key;
          row.dataset.count = String(count);
          row.dataset.resolvedZeroQuarter = String(!sourceQuarter);
          row.setAttribute('aria-label', quarter.name + ': ' + count + ' — ' + status.name);
          var quarterLabel = el('span', 'g-quarter-label', quarter.name);
          quarterLabel.setAttribute('aria-hidden', 'true');
          var track = el('span', 'g-track');
          track.setAttribute('aria-hidden', 'true');
          var bar = el('span', 'g-bar');
          bar.style.width = (spec.scale.max ? count / spec.scale.max * 100 : 0) + '%';
          bar.style.backgroundColor = cell ? cell.color : status.color;
          track.append(bar);
          var countNode = number(count);
          countNode.setAttribute('aria-hidden', 'true');
          row.append(quarterLabel, track, countNode);
          bars.append(row);
        });
        group.append(bars);
        panel.append(group);
      });
      panels.append(panel);
    });
    root.append(panels);
    return root;
  };
})();
