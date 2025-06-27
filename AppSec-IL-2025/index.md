---
layout: default
title: AppSec-IL-2025 Writeups
---

Welcome to the AppSec-IL-2025 Wargames writeups hub. Choose a wargame below to view detailed solutions.

<style>
  .wargame-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
  }

  .wargame-card {
    background-color: #34495e;
    color: #ecf0f1;
    border-radius: 10px;
    padding: 1.5rem;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    transition: transform 0.2s ease;
    text-decoration: none;
  }

  .wargame-card:hover {
    transform: scale(1.03);
    background-color: #16a085;
    color: #fff;
  }

  .wargame-card h2 {
    margin: 0;
    font-size: 1.2rem;
  }

  .wargame-card p {
    margin-top: 0.5rem;
    font-size: 0.9rem;
    color: #bdc3c7;
  }
</style>

<div class="wargame-container">
  {% assign seen = "" | split: "" %}
  {% for folder in site.pages %}
    {% if folder.path contains 'appSec-IL-2025/' and folder.path != 'appSec-IL-2025/index.md' %}
      {% assign path_parts = folder.path | split: '/' %}
      {% assign folder_name = path_parts[1] %}
      {% unless seen contains folder_name %}
        {% capture folder_path %}appSec-IL-2025/{{ folder_name }}{% endcapture %}
        <a class="wargame-card" href="{{ site.baseurl }}/{{ folder_path }}/">
          <h2>{{ folder_name | capitalize }}</h2>
          <p>Writeups for {{ folder_name | capitalize }} wargame</p>
        </a>
        {% assign seen = seen | push: folder_name %}
      {% endunless %}
    {% endif %}
  {% endfor %}
</div>
