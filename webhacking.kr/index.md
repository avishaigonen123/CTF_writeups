---
layout: default
title: Webhacking.Kr Writeups
---

This folder contains solutions for the [Webhacking.Kr](http://overthewire.org/wargames/webhacking.kr/) wargame from OverTheWire.

<style>
/* Styles same as your Behemoth example – omitted here for brevity */
</style>

<div class="behemoth-container">

  <!-- Sidebar -->
  <div class="behemoth-sidebar">
    <h00>Levels</h00>
    <ul>
      {% assign webhacking.kr_pages = site.pages 
        | where_exp: "p", "p.path contains 'overthewire/webhacking.kr'" 
        | reject: "path", "overthewire/webhacking.kr/index.md" 
        | reject: "path", "overthewire/webhacking.kr/index.html" 
      %}
      {% assign level_pages = webhacking.kr_pages | sort_natural: "path" %}
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
