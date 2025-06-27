---
layout: default
title: Trythis0Ne Writeups
---

This folder contains solutions for the [Trythis0Ne](http://overthewire.org/wargames/trythis0ne/) wargame from OverTheWire.

<style>
/* Styles same as your Behemoth example – omitted here for brevity */
</style>

<div class="behemoth-container">

  <!-- Sidebar -->
  <div class="behemoth-sidebar">
    <h00>Levels</h00>
    <ul>
      {% assign trythis0ne_pages = site.pages 
        | where_exp: "p", "p.path contains 'overthewire/trythis0ne'" 
        | reject: "path", "overthewire/trythis0ne/index.md" 
        | reject: "path", "overthewire/trythis0ne/index.html" 
      %}
      {% assign level_pages = trythis0ne_pages | sort_natural: "path" %}
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
