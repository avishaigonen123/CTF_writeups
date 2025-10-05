---
layout: default
title: HackTheBox Writeups
---

Welcome to the HackTheBox Wargames writeups hub. Choose a wargame below to view detailed solutions.

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



  .wargame-card {
    display: block;              /* ensures the anchor is block-level */
    overflow: hidden;
    padding: 0.75rem;            /* reduced padding since image occupies top */
  }

  .wargame-card h2 { margin-top: 0.5rem; }
  .wargame-card p { margin-bottom: 0; }

</style>


{% assign seen = "" | split: "" %}
{% for folder in site.pages %}
  {% if folder.path contains 'hackthebox/' and folder.path != 'hackthebox/index.md' %}
    {% assign path_parts = folder.path | split: '/' %}
    {% assign folder_name = path_parts[1] %}
    {% unless seen contains folder_name %}
      
      {% capture folder_path %}hackthebox/{{ folder_name }}{% endcapture %}
      
      {% comment %}
        Check if the image exists in the folder
      {% endcomment %}
      {% assign img_rel_path = 'hackthebox/' | append: folder_name | append: '/wargame.png' %}
      {% assign has_image = false %}
      
      {% for f in site.static_files %}
        {% if f.path == img_rel_path %}
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
