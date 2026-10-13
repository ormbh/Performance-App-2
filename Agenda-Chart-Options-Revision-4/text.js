/* Illustration only: exact quarterly counts with labels and no bar encoding. */
(function () {
  'use strict';
  window.buildAgendaText = function (spec) {
    // Reuse the checked transpose so every source status, quarter and zero has
    // precisely the same position and meaning as the cleaned matrix option.
    var root = window.buildAgendaOptionA(spec);
    root.classList.add('v4-text');
    root.setAttribute('aria-label', 'ملخص الأجندة السنوية — أعداد المواضيع حسب الحالة والربع');
    root.querySelectorAll('.a-cell-track,.a-scale').forEach(function (element) {
      element.remove();
    });
    root.querySelectorAll('.a-chart-cell').forEach(function (cell) {
      if (Number(cell.dataset.count) === 0) cell.classList.add('v4-text-zero');
    });
    return root;
  };
})();
