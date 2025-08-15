const searchInput = document.getElementById('search-input');
const resultsContainer = document.getElementById('results-container');
const showMoreBtn = document.getElementById('show-more-btn');

let allResults = [];
let displayedCount = 10;

// Render function for our controlled results
function renderResults() {
  resultsContainer.innerHTML = '';
  const toDisplay = allResults.slice(0, displayedCount);

  toDisplay.forEach(post => {
    const li = document.createElement('li');
    li.innerHTML = `<a href="${post.url}" style="color:#0f0;">${post.title}</a>`;
    resultsContainer.appendChild(li);
  });

  showMoreBtn.style.display = allResults.length > displayedCount ? 'block' : 'none';
}

// Show more button click
showMoreBtn.addEventListener('click', () => {
  displayedCount += 10;
  renderResults();
});

// Initialize SimpleJekyllSearch
SimpleJekyllSearch({
  searchInput: searchInput,
  resultsContainer: resultsContainer,
  json: 'assets/json/search.json',
  fuzzy: false,
  templateMiddleware: (prop, value) => value,
  filter: (post, query) => {
    const terms = query.toLowerCase().trim().split(/\s+/);
    const haystack = `${post.title} ${post.content}`.toLowerCase();
    return terms.every(term => haystack.includes(term));
  },
  searchResultTemplate: '', // we'll handle rendering ourselves
  searchCallback: (results) => {
    allResults = results;
    displayedCount = 10;
    renderResults();
  }
});

// Clear results when input is empty
searchInput.addEventListener('input', () => {
  if (!searchInput.value.trim()) {
    allResults = [];
    displayedCount = 10;
    resultsContainer.innerHTML = '';
    showMoreBtn.style.display = 'none';
  }
});
