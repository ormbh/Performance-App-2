/* Illustration only. Vertical count bars; no repeated row/column totals. */
(function () {
  'use strict';
  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }
  function number(value, cls) {
    var n = el('bdi', cls, String(value));
    n.dir = 'ltr';
    return n;
  }
  window.buildAgendaVertical = function (spec) {
    var root = window.agendaV4Shell(spec, 'v4-vertical');
    if (!spec.total) return root;
    var quarters = window.agendaV4Quarters(spec);
    var plots = el('div', 'v4-v-plots');
    spec.cohorts.forEach(function (cohort, ci) {
      if (!cohort.total) return;
      var panel = el('figure', 'v4-v-cohort');
      panel.dataset.cohort = cohort.id;
      panel.dataset.scaleMax = String(spec.scale.max);
      var caption = el('figcaption', 'v4-v-cohort-title', cohort.name);
      caption.id = 'v4-v-cohort-' + ci;
      panel.setAttribute('aria-labelledby', caption.id);
      panel.append(caption);
      var groups = el('div', 'v4-v-quarter-groups');
      groups.style.setProperty('--quarter-count', String(quarters.length));
      quarters.forEach(function (quarter, qi) {
        var source = cohort.quarters.find(function (q) { return q.key === quarter.key; });
        var group = el('section', 'v4-v-quarter');
        group.dataset.quarter = String(quarter.key);
        group.dataset.resolvedZeroQuarter = String(!source);
        var title = el('h4', 'v4-v-quarter-title', quarter.name);
        title.id = 'v4-v-quarter-' + ci + '-' + qi;
        group.setAttribute('aria-labelledby', title.id);
        group.append(title);
        var bars = el('div', 'v4-v-bars');
        bars.style.setProperty('--status-count', String(spec.statuses.length));
        spec.statuses.forEach(function (status, si) {
          var cell = source && source.cells.find(function (c) { return c.name === status.name; });
          var count = cell ? cell.count : 0;
          var item = el('div', 'v4-v-item');
          item.dataset.status = status.name;
          item.dataset.quarter = String(quarter.key);
          item.dataset.count = String(count);
          item.dataset.cohort = cohort.id;
          item.style.setProperty('--value-ratio', String(spec.scale.max ? count / spec.scale.max : 0));
          item.style.setProperty('--status-color', cell ? cell.color : status.color);
          var chart = el('div', 'v4-v-bar-area');
          var value = number(count, 'v4-v-value');
          var label = el('span', 'v4-v-status');
          var words = status.name.split(/\s+/);
          label.append(el('span', '', words.shift()));
          if (words.length) label.append(document.createTextNode(' '), el('span', '', words.join(' ')));
          label.id = 'v4-v-status-' + ci + '-' + qi + '-' + si;
          value.setAttribute('aria-labelledby', label.id + ' ' + title.id);
          var bar = el('span', 'v4-v-bar');
          bar.setAttribute('aria-hidden', 'true');
          chart.append(value, bar);
          item.append(chart, label);
          bars.append(item);
        });
        group.append(bars);
        groups.append(group);
      });
      panel.append(groups);
      plots.append(panel);
    });
    root.append(plots);
    return root;
  };
})();
