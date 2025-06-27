---
layout: default
title: Bandit Writeups
---

This folder contains solutions for the [Bandit](http://overthewire.org/wargames/bandit/) wargame from OverTheWire.

<style>
  body {
    font-family: 'Arial', sans-serif;
    background-color: #eceff1; /* Light gray background for softer look */
    color: #333;
    margin: 0;
  }

  #main {
    max-width: 100% !important;
    width: 100% !important;
    margin: 0 auto;
  }

  .bandit-container {
    display: flex;
    gap: 1.5rem;
    margin-top: 2rem;
    padding: 1rem;
  }

  /* Sidebar */
  .bandit-sidebar {
    min-width: 200px;
    max-height: 90vh;
    overflow-y: auto;
    position: sticky;
    top: 1rem;
    padding: 1.5rem;
    border-radius: 8px;
    background-color: #34495e; /* Slightly darker for more contrast */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    color: #ecf0f1;
    margin-top: 1rem;
  }

  .bandit-sidebar h00 {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
    color: #ecf0f1;
    border-bottom: 2px solid #16a085; /* Greenish accent */
    padding-bottom: 0.5rem;
  }

  .bandit-sidebar ul {
    list-style: none;
    padding-left: 0;
    font-size: 1rem;
    margin: 0;
  }

  .bandit-sidebar li {
    margin-bottom: 0.5rem;
  }

  .bandit-sidebar a {
    display: block;
    padding: 6px 12px;
    border-radius: 6px;
    text-decoration: none;
    color: #ecf0f1;
    transition: background 0.3s ease, color 0.3s ease;
  }

  .bandit-sidebar a:hover {
    background-color: #16a085;
    color: #fff;
  }

  .bandit-content {
    flex: 1;
    max-height: 90vh;
    overflow-y: auto;
    padding-right: 1rem;
    background-color: #ffffff; /* Off-white to reduce contrast */
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    padding: 2rem;
    font-size: 1rem;
    color: #333;
    margin-top: 1rem;
  }

  .bandit-content h00 {
    font-size: 1.4rem;
    font-weight: 600;
    margin-top: 2rem;
    color: #2c3e50;
    scroll-margin-top: 100px;
  }

  hr {
    margin: 2.5rem 0;
    border: none;
    border-top: 1px solid #ddd;
  }

  /* Optional scrollbar styling */
  .bandit-sidebar::-webkit-scrollbar {
    width: 8px;
  }

  .bandit-sidebar::-webkit-scrollbar-thumb {
    background-color: #16a085;
    border-radius: 4px;
  }

  .bandit-sidebar::-webkit-scrollbar-track {
    background-color: #ecf0f1;
  }

  /* Responsive Design */
  @media (max-width: 768px) {
    .bandit-container {
      flex-direction: column;
    }

    .bandit-sidebar {
      max-height: auto;
      width: 100%;
      margin-bottom: 2rem;
    }
  }

  /* Add a banner section after each level */
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

<h00>Bandit Writeups</h00>

<div class="bandit-container">

  <!-- Sidebar -->
  <div class="bandit-sidebar">
    <h00>Levels</h00>
    <ul>
      {% assign bandit_pages = site.pages 
        | where_exp: "p", "p.path contains 'overthewire/bandit'" 
        | reject: "path", "overthewire/bandit/index.md" 
        | reject: "path", "overthewire/bandit/index.html" 
      %}
      {% assign level_pages = bandit_pages | sort_natural: "path" %}
      {% for p in level_pages %}
        {% assign name = p.path | split: '/' | last | split: '.' | first %}
        {% if name != "index" %}
          <li><a href="#{{ name }}">{{ name }}</a></li>
        {% endif %}
      {% endfor %}
    </ul>
  </div>

  <!-- Main content -->
  <div class="bandit-content">
    {% for p in level_pages %}
      {% assign name = p.path | split: '/' | last | split: '.' | first %}
      {% if name != "index" %}
        <h00 id="{{ name }}">{{ name }}</h00>
        {{ p.content | markdownify }}
        
        <!-- Level Banner (added for separation between levels) -->
        <div class="level-banner">Next Level Writeup</div>

        <hr />
      {% endif %}
    {% endfor %}
  </div>

</div>
