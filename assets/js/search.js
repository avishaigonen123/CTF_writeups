const searchInput = document.getElementById('search-input');
const resultsContainer = document.getElementById('results-container');
const showMoreBtn = document.getElementById('show-more-btn');

let allResults = [];
let displayedCount = 10;

// Render only the first `displayedCount` results
function renderResults(results) {
  resultsContainer.innerHTML = '';
  const slice = results.slice(0, displayedCount);

  slice.forEach(post => {
    const li = document.createElement('li');
    li.innerHTML = `<a href="${post.url}" style="color:#0f0;">${post.title}</a>`;
    resultsContainer.appendChild(li);
  });

  showMoreBtn.style.display = results.length > displayedCount ? 'block' : 'none';
}

// Show more button
showMoreBtn.addEventListener('click', () => {
  displayedCount += 10;
  renderResults(allResults);
});

// Initialize search WITHOUT giving resultsContainer
SimpleJekyllSearch({
  searchInput: searchInput,
  json: 'assets/json/search.json',
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
    renderResults(allResults);
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
