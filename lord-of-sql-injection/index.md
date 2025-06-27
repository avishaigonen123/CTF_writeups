---
layout: default
title: Lord-of-sql-injection Writeups
---
<a href="/CTF_writeups/lord-of-sql-injection/" style="display:inline-block; margin-bottom: 1rem; text-decoration: none; color: #16a085; font-weight: bold;">
      ← Back to lord-of-sql-injection
</a>

### This folder contains solutions for the [Lord-of-sql-injection](http://los.rubiya.kr/) wargame from lord-of-sql-injection.

<style>
  body {
    font-family: 'Arial', sans-serif;
    background-color: #eceff1;
    color: #333;
    margin: 0;
  }
  #main {
    max-width: 100% !important;
    width: 100% !important;
    margin: 0 auto;
  }
  .lord-of-sql-injection-container {
    display: flex;
    gap: 1.5rem;
    margin-top: 2rem;
    padding: 1rem;
  }
  .lord-of-sql-injection-sidebar {
    min-width: 200px;
    max-height: 90vh;
    overflow-y: auto;
    position: sticky;
    top: 1rem;
    padding: 1.5rem;
    border-radius: 8px;
    background-color: #34495e;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    color: #ecf0f1;
    margin-top: 1rem;
  }
  .lord-of-sql-injection-sidebar h00 {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
    color: #ecf0f1;
    border-bottom: 2px solid #16a085;
    padding-bottom: 0.5rem;
  }
  .lord-of-sql-injection-sidebar ul {
    list-style: none;
    padding-left: 0;
    font-size: 1rem;
    margin: 0;
  }
  .lord-of-sql-injection-sidebar li {
    margin-bottom: 0.5rem;
  }
  .lord-of-sql-injection-sidebar a {
    display: block;
    padding: 6px 12px;
    border-radius: 6px;
    text-decoration: none;
    color: #ecf0f1;
    transition: background 0.3s ease, color 0.3s ease;
  }
  .lord-of-sql-injection-sidebar a:hover {
    background-color: #16a085;
    color: #fff;
  }
  .lord-of-sql-injection-content {
    flex: 1;
    max-height: 90vh;
    overflow-y: auto;
    padding-right: 1rem;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    padding: 2rem;
    font-size: 1rem;
    color: #333;
    margin-top: 1rem;
  }
  .lord-of-sql-injection-content h00 {
    font-size: 1.4rem;
    font-weight: 600;
    margin-top: 2rem;
    color:rgb(143, 151, 159);
    scroll-margin-top: 100px;
  }
  hr {
    margin: 2.5rem 0;
    border: none;
    border-top: 1px solid #ddd;
  }
  .lord-of-sql-injection-sidebar::-webkit-scrollbar {
    width: 8px;
  }
  .lord-of-sql-injection-sidebar::-webkit-scrollbar-thumb {
    background-color: #16a085;
    border-radius: 4px;
  }
  .lord-of-sql-injection-sidebar::-webkit-scrollbar-track {
    background-color: #ecf0f1;
  }
  @media (max-width: 768px) {
    .lord-of-sql-injection-container {
      flex-direction: column;
    }
    .lord-of-sql-injection-sidebar {
      max-height: none;
      width: 100%;
      margin-bottom: 2rem;
    }
  }
  .level-banner {
    background-color: #16a085;
    color: #fff;
    padding: 1rem;
    text-align: center;
    font-weight: bold;
    margin-top: 2rem;
    border-radius: 8px;
  }
</style>

<div class="lord-of-sql-injection-container">

  <!-- Sidebar -->
  <div class="lord-of-sql-injection-sidebar">
    <h00>Levels</h00>
    <ul>
      {% assign lord-of-sql-injection_pages = site.pages
        | where_exp: "p", "p.path contains 'lord-of-sql-injection/'"
        | reject: "path", "lord-of-sql-injection/index.md"
        | reject: "path", "lord-of-sql-injection/index.html"
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
  <div class="lord-of-sql-injection-content">
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
