// =========================
// Enhanced Search with Fuse.js (Fixed)
// =========================

document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search-input');
    const resultsContainer = document.getElementById('results-container');

    let fuse;
    let allResults = [];
    let displayedCount = 0;
    const batchSize = 10;

    function highlightMatch(text, query) {
        if (!query) return text;
        const regex = new RegExp(`(${query})`, 'gi');
        return text.replace(regex, '<mark>$1</mark>');
    }

    function renderResults(start = 0, count = batchSize) {
        const fragment = document.createDocumentFragment();
        const slice = allResults.slice(start, start + count);

        slice.forEach(result => {
            const post = result.item;
            const li = document.createElement('li');

            let snippet = post.content.slice(0, 150) + '...';
            const match = result.matches?.find(m => m.key === 'content');
            if (match && match.indices.length > 0) {
                const idx = match.indices[0][0];
                const startIdx = Math.max(0, idx - 30);
                snippet = post.content.slice(startIdx, idx + 120) + '...';
            }

            li.innerHTML = `
                <a href="${post.url}" style="color:#0f0; font-weight:600;">
                    ${highlightMatch(post.title, searchInput.value)}
                </a>
                <div style="font-size:0.9em; color:#aaa; margin-top:4px;">
                    ${highlightMatch(snippet, searchInput.value)}
                </div>
            `;
            fragment.appendChild(li);
        });

        resultsContainer.appendChild(fragment);
        displayedCount += slice.length;

        const btn = document.getElementById('load-more-btn');
        if (displayedCount < allResults.length) {
            if (!btn) {
                const loadMoreBtn = document.createElement('button');
                loadMoreBtn.id = 'load-more-btn';
                loadMoreBtn.textContent = 'Load More';
                loadMoreBtn.style.marginTop = '10px';
                loadMoreBtn.addEventListener('click', () => renderResults(displayedCount, batchSize));
                resultsContainer.parentElement.appendChild(loadMoreBtn);
            }
        } else if (btn) {
            btn.remove();
        }
    }

    function doSearch(query) {
        displayedCount = 0;
        resultsContainer.innerHTML = '';

        if (!query.trim()) {
            allResults = [];
            const btn = document.getElementById('load-more-btn');
            if (btn) btn.remove();
            return;
        }

        if (!fuse) {
            console.warn('Search index not ready yet');
            return;
        }

        const results = fuse.search(query, { limit: 50 });
        allResults = results;
        renderResults();
    }

    searchInput.disabled = true;

    fetch('{{ site.baseurl }}/search.json')
        .then(res => res.json())
        .then(posts => {
            fuse = new Fuse(posts, {
                includeMatches: true,
                shouldSort: true,
                threshold: 0.4,
                keys: [
                    { name: 'title', weight: 0.7 },
                    { name: 'content', weight: 0.3 }
                ]
            });
            searchInput.disabled = false;
        });


    searchInput.addEventListener('input', () => {
        doSearch(searchInput.value);
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === '/' && document.activeElement !== searchInput) {
            e.preventDefault();
            searchInput.focus();
        }
    });
});
