---
layout: default
title: HackTheBox Writeups
---

Welcome to the HackTheBox Wargames writeups hub. Choose a wargame below to view detailed solutions.

<style>
  .wargame-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-top: 2rem;
  }

  .wargame-card {
    background-color: #34495e;
    color: #ecf0f1;
    border-radius: 10px;
    padding: 1rem;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    transition: transform 0.2s ease;
    text-decoration: none;
  }

  .wargame-card:hover {
    transform: scale(1.05);
    background-color: #16a085;
    color: #fff;
  }

  .wargame-card img {
    width: 100%;
    height: 140px;
    object-fit: cover;
    border-radius: 8px 8px 0 0;
    display: block;
    margin-bottom: 12px;
  }

  .wargame-card h2 {
    font-size: 1.1rem;
    margin: 0.5rem 0;
  }

  .wargame-card p {
    font-size: 0.9rem;
    color: #bdc3c7;
  }
</style>



<div class="wargame-container">
{% assign seen = "" | split: "" %}
{% for folder in site.pages %}
  {% if folder.path contains 'hackthebox/' and folder.path != 'hackthebox/index.md' %}
    {% assign path_parts = folder.path | split: '/' %}
    {% assign folder_name = path_parts[1] %}
    
    {% comment %}
      Only include folders with a valid wargame image or writeup.
    {% endcomment %}
    {% unless seen contains folder_name %}
      
      {% capture folder_path %}hackthebox/{{ folder_name }}{% endcapture %}
      
      {% assign img_rel_path = 'hackthebox/' | append: folder_name | append: '/wargame.png' %}
      {% assign has_image = false %}
      
      {% for f in site.static_files %}
        {% assign file_path = f.path | remove: site.source %}
        {% if file_path == img_rel_path %}
          {% assign has_image = true %}
          {% break %}
        {% endif %}
      {% endfor %}

      <a class="wargame-card" href="{{ site.baseurl }}/{{ folder_path }}/">
        
        {% if has_image %}
          <img src="{{ site.baseurl }}/{{ img_rel_path }}" alt="{{ folder_name | capitalize }} wargame image"
               style="width:100%; height:160px; object-fit:cover; border-radius:8px 8px 0 0; display:block; margin-bottom:12px;">
        {% else %}
          <img src="{{ site.baseurl }}/assets/hackthebox.png" alt="default image"
               style="width:100%; height:160px; object-fit:cover; border-radius:8px 8px 0 0; display:block; margin-bottom:12px;">
        {% endif %}
        
        <h2>{{ folder_name | capitalize }}</h2>
        <p>Writeups for {{ folder_name | capitalize }} wargame</p>
      </a>

      {% assign seen = seen | push: folder_name %}
    {% endunless %}
  {% endif %}
{% endfor %}


</div>
