---
layout: default
title: Ringzer0 Writeups
---

This folder contains solutions for the [Ringzer0](http://overthewire.org/wargames/ringzer0/) wargame from OverTheWire.

<style>
/* Styles same as your Behemoth example – omitted here for brevity */
</style>

<div class="behemoth-container">

  <!-- Sidebar -->
  <div class="behemoth-sidebar">
    <h00>Levels</h00>
    <ul>
      {% assign ringzer0_pages = site.pages 
        | where_exp: "p", "p.path contains 'overthewire/ringzer0'" 
        | reject: "path", "overthewire/ringzer0/index.md" 
        | reject: "path", "overthewire/ringzer0/index.html" 
      %}
      {% assign level_pages = ringzer0_pages | sort_natural: "path" %}
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
