(function () {
  const root = document.documentElement;
  const toggle = document.querySelector('[data-theme-toggle]');
  const themeColor = document.querySelector('meta[name="theme-color"]');
  const colors = { light: '#F7F6F3', dark: '#141A21' };

  function apply(theme, persist) {
    root.dataset.theme = theme;
    if (themeColor) themeColor.content = colors[theme];
    if (toggle) {
      const label = theme === 'light' ? toggle.dataset.labelDark : toggle.dataset.labelLight;
      toggle.setAttribute('aria-label', label);
      toggle.setAttribute('title', label);
      toggle.setAttribute('aria-pressed', String(theme === 'dark'));
    }
    if (persist) {
      try { localStorage.setItem('appmonto-theme', theme); } catch (_) {}
    }
  }

  apply(root.dataset.theme === 'dark' ? 'dark' : 'light', false);
  if (toggle) toggle.addEventListener('click', function () {
    apply(root.dataset.theme === 'dark' ? 'light' : 'dark', true);
  });

  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
