// =========================================
// 🚀 Advanced Search using Web Worker
// =========================================

document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search-input');
    const resultsContainer = document.getElementById('results-container');
    const baseUrl = window.location.origin + '/CTF_writeups';

    let allPosts = [];
    let worker;
    let debounceTimeout;

    // ==============================
    // 🧠 Initialize Web Worker
    // ==============================
    try {
        worker = new Worker(baseUrl + '/assets/js/searchWorker.js');
    } catch (err) {
        console.error('Failed to start search worker:', err);
        return;
    }

    // ==============================
    // 🔍 Handle Worker Responses
    // ==============================
    worker.onmessage = function (e) {
        const results = e.data;
        renderResults(results);
    };

    worker.onerror = function (err) {
        console.error('Worker error:', err);
    };

    // ==============================
    // 📦 Load search.json data
    // ==============================
    searchInput.disabled = true;
    fetch(`${baseUrl}/search.json`)
        .then(res => res.json())
        .then(posts => {
            allPosts = posts;
            searchInput.disabled = false;
            console.log(`✅ Loaded ${posts.length} posts for search`);
        })
        .catch(err => console.error('Error loading search index:', err));

    // ==============================
    // ⌨️ Debounced Search Input
    // ==============================
    searchInput.addEventListener('input', (e) => {
        clearTimeout(debounceTimeout);
        const query = e.target.value;

        debounceTimeout = setTimeout(() => {
            if (query.trim()) {
                worker.postMessage({ query, posts: allPosts });
            } else {
                resultsContainer.innerHTML = '';
            }
        }, 250); // Wait 250ms after user stops typing
    });

    // ==============================
    // 🧩 Render Search Results
    // ==============================
    function renderResults(results) {
        resultsContainer.innerHTML = '';

        if (results.length === 0) {
            resultsContainer.innerHTML = `<p style="color:#999;">No results found.</p>`;
            return;
        }

        const fragment = document.createDocumentFragment();
        results.slice(0, 50).forEach(post => { // limit to first 50
            const li = document.createElement('li');
            li.style.marginBottom = '10px';

            li.innerHTML = `
                <a href="${post.url}" style="color:#0f0; font-weight:600;">
                    ${highlight(post.title, searchInput.value)}
                </a>
                <div style="font-size:0.9em; color:#aaa; margin-top:4px;">
                    ${makeSnippet(post.content, searchInput.value)}
                </div>
            `;
            fragment.appendChild(li);
        });

        resultsContainer.appendChild(fragment);
    }

    // ==============================
    // ✨ Helpers
    // ==============================

    function highlight(text, query) {
        if (!query) return text;
        const words = query.toLowerCase().split(/\s+/);
        const regex = new RegExp(`(${words.join('|')})`, 'gi');
        return text.replace(regex, '<mark>$1</mark>');
    }

    function makeSnippet(content, query) {
        const text = content || '';
        const lower = text.toLowerCase();
        const q = query.toLowerCase();
        const idx = lower.indexOf(q);

        if (idx === -1) return text.slice(0, 150) + (text.length > 150 ? '...' : '');

        const start = Math.max(0, idx - 40);
        const end = Math.min(text.length, idx + 110);
        let snippet = text.slice(start, end);

        if (start > 0) snippet = '...' + snippet;
        if (end < text.length) snippet += '...';
        return highlight(snippet, query);
    }

    // Shortcut: focus on search bar when pressing "/"
    document.addEventListener('keydown', (e) => {
        if (e.key === '/' && document.activeElement !== searchInput) {
            e.preventDefault();
            searchInput.focus();
        }
    });
});
