---
layout: default
title: Appsec Il 2025 Writeups
---

This folder contains solutions for the [Appsec Il 2025](http://overthewire.org/wargames/appSec-IL-2025/) wargame from OverTheWire.

<style>
/* Styles same as your Behemoth example – omitted here for brevity */
</style>

<div class="behemoth-container">

  <!-- Sidebar -->
  <div class="behemoth-sidebar">
    <h00>Levels</h00>
    <ul>
      {% assign appSec-IL-2025_pages = site.pages 
        | where_exp: "p", "p.path contains 'overthewire/appSec-IL-2025'" 
        | reject: "path", "overthewire/appSec-IL-2025/index.md" 
        | reject: "path", "overthewire/appSec-IL-2025/index.html" 
      %}
      {% assign level_pages = appSec-IL-2025_pages | sort_natural: "path" %}
      {% for p in level_pages %}
        {% assign name = p.path | split: '/' | last | split: '.' | first %}
        {% if name != "index" %}
          <li><a href="#{{ name }}">{{ name }}</a></li>
        {% endif %}
      {% endfor %}
    </ul>
  </div>

  <!-- Main content -->
  <div class="behemoth-content">
    {% for p in level_pages %}
      {% assign name = p.path | split: '/' | last | split: '.' | first %}
      {% if name != "index" %}
        <h00 id="{{ name }}">{{ name }}</h00>
        {{ p.content | markdownify }}
        <div class="level-banner">Next Level Writeup</div>
        <hr />
      {% endif %}
    {% endfor %}
  </div>

</div>
