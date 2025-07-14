---
layout: default
title: Vortex Writeups
---

<a href="/CTF_writeups/overthewire/" style="display:inline-block; margin-bottom: 1.5rem; text-decoration: none; color: #16a085; font-weight: bold;">
  ← Back to OverTheWire
</a>

Welcome to the **Vortex** wargame writeups! Click a level below to view the detailed solution.

<style>
  .level-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
  }

  .level-card {
    background-color: #34495e;
    color: #ecf0f1;
    border-radius: 10px;
    padding: 1.5rem;
    text-align: center;
    text-decoration: none;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    transition: transform 0.2s ease, background 0.2s ease;
    position: relative;
  }

  .level-card:hover {
    transform: translateY(-5px);
    background-color: #16a085;
    color: #fff;
  }

  .level-card h3 {
    margin: 0;
    font-size: 1.3rem;
  }

  .level-card p {
    margin-top: 0.5rem;
    font-size: 0.95rem;
    color: #bdc3c7;
  }

  .level-icon {
    font-size: 1.8rem;
    margin-bottom: 0.5rem;
    display: block;
  }
</style>

<div class="level-grid">
  {% assign vortex_pages = site.pages
    | where_exp: "p", "p.path contains 'overthewire/vortex'"
    | reject: "path", "overthewire/vortex/index.md"
    | reject: "path", "overthewire/vortex/index.html"
  %}
  {% assign sorted_levels = vortex_pages | sort_natural: "path" %}
  {% for page in sorted_levels %}
    {% assign name = page.path | split: '/' | last | split: '.' | first %}
    <a class="level-card" href="{{ site.baseurl }}/CTF_writeups/overthewire/vortex/{{ name }}.html">
      <span class="level-icon">🧩</span>
      <h3>{{ name }}</h3>
      <p>Solution for {{ name }}</p>
    </a>
  {% endfor %}
</div>
