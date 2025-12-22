---
layout: default
title: TryHackMe Writeups
---

Welcome to the TryHackMe Wargames writeups hub. Choose a wargame below to view detailed solutions.

<style>
  .wargame-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
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
    overflow: hidden;  /* Ensures the content stays inside the container */
  }

  .wargame-card:hover {
    transform: scale(1.05);
    background-color: #16a085;
    color: #fff;
  }

  .wargame-card img {
    width: 100%;
    height: 400px;  /* Fixed height */
    object-fit: cover;  /* Ensures the image covers the area without distortion */
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

  .wargame-card {
  position: relative;
  }

  .card-status.unfinished {
    position: absolute;
    top: 12px;
    right: 12px;
    background: rgba(107, 114, 128, 0.9);
    color: #fff;
    font-size: 0.7rem;
    padding: 4px 8px;
    border-radius: 6px;
    letter-spacing: 0.05em;
  }

</style>



<div class="wargame-container">
  {% assign seen = "" | split: "" %}
  {% for folder in site.pages %}
    {% if folder.path contains 'tryhackme/' and folder.path != 'tryhackme/index.md' %}
      {% assign path_parts = folder.path | split: '/' %}
      {% assign folder_name = path_parts[1] %}
      {% unless seen contains folder_name %}
        
        {% capture folder_path %}tryhackme/{{ folder_name }}{% endcapture %}
        
        {% assign img_rel_path = folder_name | append: '/wargame.png' %}
        {% assign has_image = false %}
        
        {% comment %}
          Checking if wargame.png exists for the current folder.
        {% endcomment %}
        {% for f in site.static_files %}
          {% if f.path contains img_rel_path %}
            {% assign has_image = true %}
            {% break %}
          {% endif %}
        {% endfor %}

        <a class="wargame-card" href="{{ site.baseurl }}/{{ folder_path }}/">
          
          {% if has_image %}
            <img src="{{ site.baseurl }}/{{ folder_path }}/wargame.png" alt="{{ folder_name | capitalize }} wargame image"
                 style="width:100%; height:200px; object-fit:cover; border-radius:8px 8px 0 0; display:block; margin-bottom:12px;">
          {% else %}
            <img src="{{ site.baseurl }}/assets/tryhackme.svg" alt="default image"
                 style="width:100%; height:200px; object-fit:cover; border-radius:8px 8px 0 0; display:block; margin-bottom:12px;">
          {% endif %}

          {% assign incomplete = false %}
          {% for f in site.static_files %}
            {% if f.status == "incomplete" and f.path contains folder_name %}
              {% assign incomplete = true %}
            {% endif %}
          {% endfor %}

          {% if incomplete %}
            <div class="card-status unfinished">INCOMPLETE</div>
          {% endif %}


          
          <h2>{{ folder_name | capitalize }}</h2>
          <p>Writeups for {{ folder_name | capitalize }} wargame</p>
        </a>

        {% assign seen = seen | push: folder_name %}
      {% endunless %}
    {% endif %}
  {% endfor %}
</div>
