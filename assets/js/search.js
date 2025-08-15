  SimpleJekyllSearch({
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('results-container'),
    json: '{{ site.baseurl }}/search.json',
    searchResultTemplate: '<li><a href="{url}" style="color:#0f0;">{title}</a></li>',
    fuzzy: false,
    templateMiddleware: function (prop, value, template) {
      return value;
    },
    filter: function (post, searchQuery) {
      const terms = searchQuery.toLowerCase().trim().split(/\s+/);
      const haystack = `${post.title} ${post.content}`.toLowerCase();
      return terms.every(term => haystack.includes(term));
    }
  });

  // Clear results when input is empty
  const input = document.getElementById('search-input');
  const results = document.getElementById('results-container');

  input.addEventListener('input', () => {
    if (!input.value.trim()) {
      results.innerHTML = '';
    }
  });