---
layout: default
title: Bandit Writeups
---

<h1>Bandit Levels</h1>

<div style="display: flex; gap: 2rem;">

<!-- Sidebar -->
<div style="min-width: 200px;">
  <h3>Levels</h3>
  <ul style="list-style: none; padding-left: 0;">
    {% assign bandit_pages = site.pages | where_exp: "p", "p.path contains 'overthewire/bandit' and p.path != 'overthewire/bandit/index.md'" | sort: 'path' %}
    {% for p in bandit_pages %}
      <li><a href="#{{ p.path | split: "/" | last | split: "." | first }}">{{ p.title | default: p.path }}</a></li>
    {% endfor %}
  </ul>
</div>

<!-- Content -->
<div style="max-height: 80vh; overflow-y: auto; flex: 1; padding-right: 1rem;">
  {% for p in bandit_pages %}
    <h2 id="{{ p.path | split: "/" | last | split: "." | first }}">{{ p.title | default: p.path }}</h2>
    {% capture content %}{% include_relative {{ p.path | split: "/" | last }} %}{% endcapture %}
    {{ content | markdownify }}
    <hr />
  {% endfor %}
</div>

</div>
