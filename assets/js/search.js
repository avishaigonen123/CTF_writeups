// =========================
// 🚀 Advanced Search with Fuse.js
// =========================

document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search-input');
    const resultsContainer = document.getElementById('results-container');

    let fuse;
    let allResults = [];
    let displayedCount = 0;
    const batchSize = 10;

    // 🔸 Better snippet generation
    function getSnippet(post, query) {
        const content = post.content;
        const lowerContent = content.toLowerCase();
        const lowerQuery = query.toLowerCase();
        const matchIndex = lowerContent.indexOf(lowerQuery);

        if (matchIndex === -1) {
            return content.slice(0, 150) + (content.length > 150 ? '...' : '');
        }

        const start = Math.max(0, matchIndex - 40);
        const end = Math.min(content.length, matchIndex + 110);
        let snippet = content.slice(start, end);
        if (start > 0) snippet = '...' + snippet;
        if (end < content.length) snippet += '...';
        return snippet;
    }

    // ✨ Highlight matched text
    function highlightMatch(text, query) {
        if (!query) return text;
        const regex = new RegExp(`(${query})`, 'gi');
        return text.replace(regex, '<mark>$1</mark>');
    }

    // 📜 Render results with pagination
    function renderResults(start = 0, count = batchSize) {
        const fragment = document.createDocumentFragment();
        const slice = allResults.slice(start, start + count);

        slice.forEach(result => {
            const post = result.item;
            const li = document.createElement('li');

            let snippet = getSnippet(post, searchInput.value);
            snippet = highlightMatch(snippet, searchInput.value);

            li.innerHTML = `
                <a href="${post.url}" style="color:#0f0; font-weight:600;">
                    ${highlightMatch(post.title, searchInput.value)}
                </a>
                <div style="font-size:0.9em; color:#aaa; margin-top:4px;">
                    ${snippet}
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

    // 🕵️ Perform search
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

        const results = fuse.search(query); // no limit now
        allResults = results;
        renderResults();
    }

    // 🌍 Load search index (absolute path)
    const baseUrl = window.location.origin + '/CTF_writeups';
    searchInput.disabled = true;

    fetch(`${baseUrl}/search.json`)
        .then(res => res.json())
        .then(posts => {
            fuse = new Fuse(posts, {
                includeMatches: true,
                shouldSort: true,
                threshold: 0.5, // a bit looser for better matching
                keys: [
                    { name: 'title', weight: 0.6 },
                    { name: 'content', weight: 0.4 }
                ]
            });
            searchInput.disabled = false;
        })
        .catch(err => console.error('Error loading search.json', err));

    // ⌨️ Live search as user types
    searchInput.addEventListener('input', () => {
        doSearch(searchInput.value);
    });

    // ⌨️ "/" focuses the search bar
    document.addEventListener('keydown', (e) => {
        if (e.key === '/' && document.activeElement !== searchInput) {
            e.preventDefault();
            searchInput.focus();
        }
    });
});
