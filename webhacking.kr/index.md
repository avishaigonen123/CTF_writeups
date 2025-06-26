---
layout: default
title: Writeups
---

# 🧠 Writeups in `{{ page.path | split: "/" | slice: 0 }}`

<div style="max-height: 500px; overflow-y: auto; padding: 1rem; border: 1px solid #ccc; border-radius: 10px;">

<ul>
{% assign current_dir = page.path | split: "/" | first %}
{% for p in site.pages %}
  {% if p.path contains current_dir and p.url != page.url and p.url contains ".html" %}
    <li><a href="{{ p.url }}">{{ p.title | default: p.path }}</a></li>
  {% endif %}
{% endfor %}
</ul>

</div>
