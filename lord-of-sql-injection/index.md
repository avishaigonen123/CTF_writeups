---
layout: default
title: Lord Of Sql Injection Writeups
---

This folder contains solutions for the [Lord Of Sql Injection](http://overthewire.org/wargames/lord-of-sql-injection/) wargame from OverTheWire.

<style>
/* Styles same as your Behemoth example – omitted here for brevity */
</style>

<div class="behemoth-container">

  <!-- Sidebar -->
  <div class="behemoth-sidebar">
    <h00>Levels</h00>
    <ul>
      {% assign lord-of-sql-injection_pages = site.pages 
        | where_exp: "p", "p.path contains 'overthewire/lord-of-sql-injection'" 
        | reject: "path", "overthewire/lord-of-sql-injection/index.md" 
        | reject: "path", "overthewire/lord-of-sql-injection/index.html" 
      %}
      {% assign level_pages = lord-of-sql-injection_pages | sort_natural: "path" %}
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
