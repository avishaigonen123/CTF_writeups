// ================================
// 🔧 Web Worker for Searching
// ================================

// Receive message from main thread
self.onmessage = function (e) {
    const { query, posts } = e.data;

    if (!query.trim()) {
        self.postMessage([]); // No query, no results
        return;
    }

    const lowerQuery = query.toLowerCase();
    const queryWords = lowerQuery.split(/\s+/);

    // ⚙️ Simple but fast search — supports multi-word
    const results = posts.filter(post => {
        const title = (post.title || '').toLowerCase();
        const content = (post.content || '').toLowerCase();

        // Return posts that contain *all* query words in title or content
        return queryWords.every(word =>
            title.includes(word) || content.includes(word)
        );
    });

    // Send results back to main thread
    self.postMessage(results);
};
