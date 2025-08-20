const searchInput = document.getElementById('search-input');
const resultsContainer = document.getElementById('results-container');

let allResults = [];  // Store all matches
let displayedCount = 0;
const batchSize = 10; // Number of results to show initially and per "Load More"

// Render results function
function renderResults(start = 0, count = batchSize) {
    const fragment = document.createDocumentFragment();
    const slice = allResults.slice(start, start + count);

    slice.forEach(post => {
        const li = document.createElement('li');
        li.innerHTML = `<a href="${post.url}" style="color:#0f0;">${post.title}</a>`;
        fragment.appendChild(li);
    });

    resultsContainer.appendChild(fragment);
    displayedCount += slice.length;

    // Show or hide "Load More" button
    if (displayedCount < allResults.length) {
        if (!document.getElementById('load-more-btn')) {
            const btn = document.createElement('button');
            btn.id = 'load-more-btn';
            btn.textContent = 'Load More';
            btn.addEventListener('click', () => renderResults(displayedCount, batchSize));
            resultsContainer.parentElement.appendChild(btn);
        }
    } else {
        const btn = document.getElementById('load-more-btn');
        if (btn) btn.remove();
    }
}

// Search logic
function doSearch(query) {
    allResults = [];
    displayedCount = 0;
    resultsContainer.innerHTML = '';

    fetch('{{ site.baseurl }}/search.json')
        .then(res => res.json())
        .then(posts => {
            const terms = query.toLowerCase().trim().split(/\s+/);
            allResults = posts.filter(post => {
                const haystack = `${post.title} ${post.content}`.toLowerCase();
                return terms.every(term => haystack.includes(term));
            });

            renderResults();
        });
}

// Input event
searchInput.addEventListener('input', () => {
    const query = searchInput.value;
    if (!query.trim()) {
        resultsContainer.innerHTML = '';
        allResults = [];
        displayedCount = 0;
        const btn = document.getElementById('load-more-btn');
        if (btn) btn.remove();
        return;
    }
    doSearch(query);
});
