const searchInput = document.getElementById('search-input');
const resultsContainer = document.getElementById('results-container');
const showMoreBtn = document.getElementById('show-more-btn');

let allResults = [];
let displayedCount = 10;

function renderResults(count) {
  resultsContainer.innerHTML = '';
  const toDisplay = allResults.slice(0, count);

  toDisplay.forEach(post => {
    const li = document.createElement('li');
    li.innerHTML = `<a href="${post.url}" style="color:#0f0;">${post.title}</a>`;
    resultsContainer.appendChild(li);
  });

  if (allResults.length > count) {
    showMoreBtn.style.display = 'block';
  } else {
    showMoreBtn.style.display = 'none';
  }
}

showMoreBtn.addEventListener('click', () => {
  displayedCount += 10;
  renderResults(displayedCount);
});

SimpleJekyllSearch({
  searchInput: searchInput,
  resultsContainer: resultsContainer,
  json: 'assets/json/search.json',
  fuzzy: false,
  searchResultTemplate: '<li><a href="{url}" style="color:#0f0;">{title}</a></li>',
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

// Clear results when input is empty
searchInput.addEventListener('input', () => {
  if (!searchInput.value.trim()) {
    resultsContainer.innerHTML = '';
    allResults = [];
    displayedCount = 10;
    showMoreBtn.style.display = 'none';
  }
});
