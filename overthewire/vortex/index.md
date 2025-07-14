---
layout: default
title: Vortex Writeups
---

<a href="/CTF_writeups/overthewire/" style="display:inline-block; margin-bottom: 1rem; text-decoration: none; color: #16a085; font-weight: bold;">
  ← Back to OverTheWire
</a>

Welcome to the **Vortex** wargame writeups. Click a level below to view its detailed solution.

<style>
  .level-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
  }

  .level-card {
    background-color: #34495e;
    color: #ecf0f1;
    border-radius: 10px;
    padding: 1.5rem;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    transition: transform 0.2s ease;
    text-decoration: none;
    display: block;
  }

  .level-card:hover {
    transform: scale(1.03);
    background-color: #16a085;
    color: #fff;
  }

  .level-card h2 {
    margin: 0;
    font-size: 1.2rem;
  }

  .level-card p {
    margin-top: 0.5rem;
    font-size: 0.9rem;
    color: #bdc3c7;
  }
</style>

<div class="level-grid">
  {% assign vortex_pages = site.pages
    | where_exp: "p", "p.path contains 'overthewire/vortex'"
    | reject: "path", "overthewire/vortex/index.md"
    | reject: "path", "overthewire/vortex/index.html"
  %}
  {% assign level_pages = vortex_pages | sort_natural: "path" %}

  {% for p in level_pages %}
    {% assign name = p.path | split: '/' | last | split: '.' | first %}
    {% unless name == "index" %}
      <a class="level-card" href="{{ site.baseurl }}{{ p.url }}">
        <h2>{{ name | capitalize }}</h2>
        <p>Solution for {{ name }}</p>
      </a>
    {% endunless %}
  {% endfor %}
</div>
