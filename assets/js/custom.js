// Back link dynamic URL
const backLink = document.getElementById('back-link');
if (backLink) {
  const parts = window.location.pathname.split('/').filter(Boolean);
  parts.pop();
  const parent = parts.length > 0 ? '/' + parts.join('/') + '/' : '/';
  backLink.href = parent;
}

// Simple Jekyll Search
const searchInput = document.getElementById('search-input');
const resultsContainer = document.getElementById('results-container');

if (searchInput && resultsContainer) {
  let allResults = [];
  let displayedCount = 10;

  function renderResults(count) {
    resultsContainer.innerHTML = '';
    const toDisplay = allResults.slice(0, count);
    toDisplay.forEach(post => {
      const li = document.createElement('li');
      li.innerHTML = `<a href="${post.url}">${post.title}</a>`;
      resultsContainer.appendChild(li);
    });

    if (allResults.length > count) {
      const moreBtn = document.createElement('button');
      moreBtn.textContent = 'Search More';
      moreBtn.addEventListener('click', () => {
        displayedCount += 10;
        renderResults(displayedCount);
      });
      resultsContainer.appendChild(moreBtn);
    }
  }

  SimpleJekyllSearch({
    searchInput: searchInput,
    resultsContainer: resultsContainer,
    json: '{{ site.baseurl }}/search.json',
    searchResultTemplate: '',
    fuzzy: false,
    templateMiddleware: (prop, value) => value,
    filter: (post, query) => {
      const terms = query.toLowerCase().trim().split(/\s+/);
      const haystack = `${post.title} ${post.content}`.toLowerCase();
      return terms.every(term => haystack.includes(term));
    },
    searchCallback: (results) => {
      allResults = results;
      displayedCount = 10;
      renderResults(displayedCount);
    }
  });

  searchInput.addEventListener('input', () => {
    if (!searchInput.value.trim()) {
      resultsContainer.innerHTML = '';
      allResults = [];
    }
  });
}
