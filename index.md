---
layout: default
title: "CTF Writeups Home"
---

# 🛡️ Welcome to My CTF Writeups

> A collection of writeups for Capture The Flag (CTF) challenges and wargames — solved, documented, and shared for learning.

{% assign wargames_string = "AppSec-IL-2025,overthewire,ringzer0,root-me,trythis0ne,webhacking.kr,websec.fr,pwnable.kr,lord-of-sql-injection" %}
{% assign wargames = wargames_string | split: "," %}
{% assign md_pages = site.pages | where_exp: "p", "p.path contains '.md'" %}
{% assign filtered_pages = "" %}
{% for p in md_pages %}
  {% assign first_part = p.path | split: '/' | first %}
  {% unless p.path | slice: -8 == "index.md" %}
    {% if wargames contains first_part %}
      {% assign filtered_pages = filtered_pages | append: p.path | append: "," %}
    {% endif %}
  {% endunless %}
{% endfor %}
{% assign filtered_pages = filtered_pages | split: "," | reject: "" %}


<div class="circle-counter" data-count="{{ filtered_pages | size }}">
   <svg>
    <defs>
      <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#3b82f6"/>
        <stop offset="50%" stop-color="#06b6d4"/>
        <stop offset="100%" stop-color="#8b5cf6"/>
      </linearGradient>
      <filter id="glow">
        <feGaussianBlur stdDeviation="4" result="blur"/>
        <feMerge>
          <feMergeNode in="blur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
    </defs>
    <circle class="bg" cx="100" cy="100" r="90"></circle>
    <circle class="progress" cx="100" cy="100" r="90"></circle>
  </svg>
  <div class="text-wrapper">
    <div class="count">0</div>
    <div class="label">Writeups so far :D</div>
  </div>
</div>

<link rel="stylesheet" href="{{ '/assets/css/counter.css' | relative_url }}">
<script src="{{ '/assets/js/counter.js' | relative_url }}"></script>


---

## 📁 Contents

<div style="font-size: 1.4rem; line-height: 2.5; padding: 10px;">
  <ul style="list-style-type: none; padding: 0;">
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s;">
      🔓 <a href="./overthewire/" style="text-decoration: none; color: #16a085;">OverTheWire</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s;">
      🏴‍☠️ <a href="./root-me/" style="text-decoration: none; color: #16a085;">Root-me</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s;">
      🕵️ <a href="./trythis0ne/" style="text-decoration: none; color: #16a085;">trythis0ne</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s;">
      🌐 <a href="./webhacking.kr/" style="text-decoration: none; color: #16a085;">Webhacking.kr</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s;">
      🕸️ <a href="./websec.fr/" style="text-decoration: none; color: #16a085;">Websec.fr</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s;">
      🧨 <a href="./pwnable.kr/" style="text-decoration: none; color: #16a085;">Pwnable.kr</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s;">
      🧮 <a href="./lord-of-sql-injection/" style="text-decoration: none; color: #16a085;">Lord of SQL Injection</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s;">
      🎯 <a href="./ringzer0" style="text-decoration: none; color: #16a085;">RingZer0</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s;">
      🇮🇱 <a href="./AppSec-IL-2025/" style="text-decoration: none; color: #16a085;">AppSec-IL-2025</a>
    </li>
  </ul>
</div>

---

## 🧭 Wargame Guide

Each folder includes:
- ✍️ **Level Writeups**: Short, step-by-step walkthroughs with clear flags.
- 💻 **Scripts/Code**: Relevant exploit or helper code placed alongside the writeups.

---

## 📝 Notes

- Writeups are **concise**, focusing only on the **essential steps** to solve each challenge.
- This project is constantly growing — **new challenges will be added regularly**.
- All content is meant for **educational purposes**.

---

## 🙌 Happy Hacking!

Feel free to [connect with me](https://github.com/avishaigonen123) or contribute.  
Learn, explore, and enjoy the world of CTFs 🧠💥




