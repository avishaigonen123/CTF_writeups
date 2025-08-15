const searchInput = document.getElementById('search-input');
const resultsContainer = document.getElementById('results-container');
const showMoreBtn = document.getElementById('show-more-btn');

let allResults = [];
let displayedCount = 10;

// Fetch the JSON once
fetch('{{ "/assets/json/search.json" | relative_url }}')
  .then(response => response.json())
  .then(data => {
    allResults = data;
  })
  .catch(err => console.error('Error loading search.json:', err));

// Render results up to displayedCount
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

// Filter results based on search query
function filterResults(query) {
  if (!query.trim()) return [];
  const terms = query.toLowerCase().trim().split(/\s+/);

  return allResults.filter(post => {
    const haystack = `${post.title} ${post.content}`.toLowerCase();
    return terms.every(term => haystack.includes(term));
  });
}

// Show more button click
showMoreBtn.addEventListener('click', () => {
  displayedCount += 10;
  const filtered = filterResults(searchInput.value);
  renderResults(filtered);
});

// Input event
searchInput.addEventListener('input', () => {
  displayedCount = 10;
  const filtered = filterResults(searchInput.value);
  renderResults(filtered);
});
