// Back link dynamic URL
const backLink = document.getElementById('back-link');
if (backLink) {
  const parts = window.location.pathname.split('/').filter(Boolean);
  parts.pop();
  const parent = parts.length > 0 ? '/' + parts.join('/') + '/' : '/';
  backLink.href = parent;
}

