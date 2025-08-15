let allResults = []; // store all search results
let resultsToShow = 10; // initial number to show
const resultsContainer = document.getElementById('results-container');
const showMoreBtn = document.getElementById('show-more-btn');

SimpleJekyllSearch({
  searchInput: document.getElementById('search-input'),
  resultsContainer: resultsContainer,
  json: 'assets/json/search.json',
  searchResultTemplate: '<li><a href="{url}" style="color:#0f0;">{title}</a></li>',
  fuzzy: false,
  templateMiddleware: function (prop, value, template) {
    return value;
  },
  filter: function (post, searchQuery) {
    const terms = searchQuery.toLowerCase().trim().split(/\s+/);
    const haystack = `${post.title} ${post.content}`.toLowerCase();
    return terms.every(term => haystack.includes(term));
  },
  noResultsText: '<li>No results found</li>',
  onResults: function(results) {
    allResults = results; // save all results
    resultsContainer.innerHTML = '';
    showResults();
  }
});

// Function to render results
function showResults() {
  resultsContainer.innerHTML = '';
  allResults.slice(0, resultsToShow).forEach(item => {
    resultsContainer.insertAdjacentHTML('beforeend', `<li><a href="${item.url}" style="color:#0f0;">${item.title}</a></li>`);
  });

  // Show button if there are more results
  showMoreBtn.style.display = allResults.length > resultsToShow ? 'block' : 'none';
}

// Show more button click
showMoreBtn.addEventListener('click', () => {
  resultsToShow += 10; // show 10 more
  showResults();
});

// Clear results when input is empty
const input = document.getElementById('search-input');
input.addEventListener('input', () => {
  if (!input.value.trim()) {
    resultsContainer.innerHTML = '';
    allResults = [];
    resultsToShow = 10;
    showMoreBtn.style.display = 'none';
  }
});
