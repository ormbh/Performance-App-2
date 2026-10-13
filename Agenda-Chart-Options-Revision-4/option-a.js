/* Illustration only. Same quarter/status specification, without repeated matrix totals. */
(function () {
  'use strict';
  function node(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }
  function num(value, cls) {
    var e = node('bdi', cls, String(value));
    e.dir = 'ltr';
    return e;
  }
  function sharedQuarters(spec) {
    // Presentation order comes from the source grouping order. No source records
    // or calculated cohort values are inserted into the specification.
    var names = {}, first = [], edges = {}, degree = {};
    spec.cohorts.forEach(function (c) {
      c.quarters.forEach(function (q, i) {
        if (!Object.prototype.hasOwnProperty.call(names, q.key)) {
          names[q.key] = q.name; first.push(q.key); edges[q.key] = []; degree[q.key] = 0;
        }
        if (i) {
          var previous = c.quarters[i - 1].key;
          if (edges[previous].indexOf(q.key) < 0) { edges[previous].push(q.key); degree[q.key] += 1; }
        }
      });
    });
    var canonical = ['الربع الأول', 'الربع الثاني', 'الربع الثالث', 'الربع الرابع'];
    var S = window.Saytara, data = S && S.app && S.app.state && S.app.state.data;
    function tie(a, b) {
      if (a === 'undated' || b === 'undated') return a === b ? 0 : a === 'undated' ? 1 : -1;
      if (data && S.order && S.order.compare) {
        var sourceOrder = S.order.compare(data, 'Quarters', names[a], names[b]);
        if (sourceOrder) return sourceOrder;
      }
      var ai = canonical.indexOf(a), bi = canonical.indexOf(b);
      if (ai >= 0 && bi >= 0) return ai - bi;
      return first.indexOf(a) - first.indexOf(b);
    }
    var remaining = first.slice(), ordered = [];
    while (remaining.length) {
      var ready = remaining.filter(function (key) { return degree[key] === 0; }).sort(tie);
      // Source groups share one order; a cycle would indicate an invalid spec.
      if (!ready.length) throw new Error('Conflicting source quarter order');
      var key = ready[0]; ordered.push(key); remaining.splice(remaining.indexOf(key), 1);
      edges[key].forEach(function (next) { degree[next] -= 1; });
    }
    return ordered.map(function (key) { return { key: key, name: names[key] }; });
  }
  window.buildAgendaOptionA = function (spec) {
    var quarterColumns = sharedQuarters(spec);
    var root = node('section', 'ag-v3-overview ag-v3-option-a');
    root.dir = 'rtl';
    root.setAttribute('aria-label', 'ملخص الأجندة السنوية — الحالات حسب الربع');
    root.dataset.sourceTotal = String(spec.total);
    root.dataset.scaleMin = '0';
    root.dataset.scaleMax = String(spec.scale.max);
    root.dataset.displayQuarterKeys = JSON.stringify(quarterColumns.map(function (q) { return q.key; }));
    root.dataset.presentationQuarterPolicy = 'shared-active-union';
    var lead = node('header', 'a-overview-lead');
    var total = node('div', 'a-grand-total');
    total.append(num(spec.total, 'a-total-number'), node('span', '', 'الإجمالي'));
    lead.append(node('h2', '', 'الأجندة السنوية'), total);
    root.append(lead);
    var head = node('div', 'a-chart-head');
    var scale = node('span', 'a-scale');
    scale.append(node('span', '', 'عدد المواضيع '), num('0–' + spec.scale.max));
    head.append(node('h3', '', 'مستويات الإنجاز حسب الربع'), scale);
    if (spec.total) root.append(head);
    var categories = node('div', 'a-category-boxes');
    categories.style.setProperty('--cohorts', String(spec.cohorts.length));
    spec.cohorts.forEach(function (c) {
      var box = node('div', 'a-category');
      box.id = 'a-cohort-' + c.id;
      box.append(node('span', '', c.name), num(c.total, 'a-category-value'));
      categories.append(box);
    });
    root.append(categories);
    if (!spec.total) {
      root.append(node('p', 'a-empty', 'لا توجد مواضيع ضمن النطاق المحدد.'));
      return root;
    }
    var panels = node('div', 'a-chart-panels');
    panels.style.setProperty('--cohorts', String(spec.cohorts.filter(function (c) { return c.total > 0; }).length));
    spec.cohorts.forEach(function (c, ci) {
      if (!c.total) return;
      var displayQuarters = quarterColumns.map(function (q) {
        var sourceQuarter = c.quarters.find(function (x) { return x.key === q.key; });
        return sourceQuarter || { key: q.key, name: q.name, total: 0, recordKeys: [], cells: [], resolvedZero: true };
      });
      var panel = node('figure', 'a-chart-panel');
      panel.dataset.cohort = c.id;
      panel.dataset.total = String(c.total);
      panel.dataset.denominator = String(c.total);
      panel.style.setProperty('--quarters', String(displayQuarters.length));
      panel.dataset.resolvedZeroQuarters = JSON.stringify(displayQuarters.filter(function (q) { return q.resolvedZero; }).map(function (q) { return q.key; }));
      panel.setAttribute('aria-labelledby', 'a-cohort-' + c.id);
      var caption = node('figcaption', 'a-panel-title');
      caption.append(node('h4', '', c.name), num(c.total, 'a-panel-total'));
      panel.append(caption);
      var table = node('table', 'a-matrix');
      table.setAttribute('aria-label', c.name + ': حالات الإنجاز في الصفوف والأرباع في الأعمدة');
      var cols = node('colgroup');
      cols.append(node('col', 'a-status-col'));
      displayQuarters.forEach(function () { cols.append(node('col', 'a-quarter-col')); });
      table.append(cols);
      var thead = node('thead'), hr = node('tr');
      var sh = node('th', 'a-status-heading', 'الحالة');
      sh.scope = 'col';
      hr.append(sh);
      displayQuarters.forEach(function (q, qi) {
        var qh = node('th', 'a-quarter-heading', q.name);
        qh.scope = 'col';
        qh.id = 'a-quarter-' + ci + '-' + qi;
        hr.append(qh);
      });
      thead.append(hr);
      table.append(thead);
      var tbody = node('tbody');
      spec.statuses.forEach(function (status, si) {
        var row = node('tr');
        row.dataset.status = status.name;
        var label = node('th', 'a-status-name', status.name);
        label.scope = 'row';
        label.id = 'a-status-' + ci + '-' + si;
        row.append(label);
        displayQuarters.forEach(function (q, qi) {
          var cell = q.cells.find(function (x) { return x.name === status.name; });
          var count = cell ? cell.count : 0;
          var td = node('td', 'a-chart-cell');
          td.dataset.status = status.name;
          td.dataset.quarter = String(q.key);
          td.dataset.count = String(count);
          td.dataset.resolvedZeroQuarter = String(!!q.resolvedZero);
          td.dataset.sourceRecordCount = String(q.recordKeys.length);
          td.setAttribute('headers', label.id + ' a-quarter-' + ci + '-' + qi);
          td.append(node('span', 'a-mobile-quarter', q.name), num(count, 'a-cell-number'));
          var track = node('span', 'a-cell-track');
          var bar = node('span', 'a-cell-bar');
          track.setAttribute('aria-hidden', 'true');
          bar.style.width = (spec.scale.max ? count / spec.scale.max * 100 : 0) + '%';
          bar.style.backgroundColor = cell ? cell.color : status.color;
          track.append(bar);
          td.append(track);
          row.append(td);
        });
        tbody.append(row);
      });
      table.append(tbody);
      panel.append(table);
      panels.append(panel);
    });
    root.append(panels);
    return root;
  };
})();
