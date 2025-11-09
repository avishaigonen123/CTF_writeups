---
layout: default
title: "CTF Writeups Home"
---

# 🛡️ Welcome to My CTF Writeups

> A collection of writeups for Capture The Flag (CTF) challenges and wargames — solved, documented, and shared for learning.

{% assign wargames_string = "AppSec-IL-2025,overthewire,ringzer0,root-me,trythis0ne,webhacking.kr,websec.fr,pwnable.kr,lord-of-sql-injection,hackthebox,tryhackme" %}
{% assign wargames = wargames_string | split: "," %}
{% assign md_pages = site.pages | where_exp: "p", "p.path contains '.md'" %}
{% assign filtered_pages = "" %}
{% for p in md_pages %}
  {% assign first_part = p.path | split: '/' | first %}
  {% assign file_name = p.path | split: '/' | last %}
  {% if wargames contains first_part and file_name != "index.md" %}
    {% assign filtered_pages = filtered_pages | append: p.path | append: "," %}
  {% endif %}
{% endfor %}
{% assign filtered_pages = filtered_pages | split: "," | reject: "" %}


<div class="circle-counter" data-count="{{ filtered_pages | size }}">
    <svg>
    <defs>
      <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#3b82f6"/>
        <stop offset="100%" stop-color="#06b6d4"/>
      </linearGradient>
    </defs>
    <circle class="bg" cx="100" cy="100" r="90"></circle>
    <circle class="progress" cx="100" cy="100" r="90"></circle>
  </svg>
  <div class="text-wrapper">
    <div class="count">0</div>
    <div class="label">Writeups so far</div>
  </div>
</div>

<link rel="stylesheet" href="{{ '/assets/css/counter.css' | relative_url }}">
<script src="{{ '/assets/js/counter.js' | relative_url }}"></script>


---

## 📁 Contents

<div style="font-size: 1.4rem; line-height: 2.5; padding: 10px;">
  <ul style="list-style-type: none; padding: 0;">
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s; display:flex; align-items:center; gap:8px;">
    <img src="./assets/overthewire.jpeg" alt="icon" width="25" height="25" style="display:block;">
      <a href="./overthewire/" style="text-decoration: none; color: #16a085;"> OverTheWire</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s; display:flex; align-items:center; gap:8px;">
    <img src="./assets/rootme.png" alt="icon" width="25" height="25" style="display:block;">
      <a href="./root-me/" style="text-decoration: none; color: #16a085;"> Root-me</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s; display:flex; align-items:center; gap:8px;">
    <img src="./assets/trythis0ne.png" alt="icon" width="25" height="25" style="display:block;">
      <a href="./trythis0ne/" style="text-decoration: none; color: #16a085;"> trythis0ne</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s; display:flex; align-items:center; gap:8px;">
    <img src="./assets/webhacking.ico" alt="icon" width="25" height="25" style="display:block;">
      <a href="./webhacking.kr/" style="text-decoration: none; color: #16a085;"> Webhacking.kr</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s; display:flex; align-items:center; gap:8px;">
    <img src="./assets/websec.png" alt="icon" width="25" height="25" style="display:block;">
      <a href="./websec.fr/" style="text-decoration: none; color: #16a085;"> Websec.fr</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s; display:flex; align-items:center; gap:8px;">
    <img src="./assets/pwnable.ico" alt="icon" width="25" height="25" style="display:block;">
      <a href="./pwnable.kr/" style="text-decoration: none; color: #16a085;"> Pwnable.kr</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s; display:flex; align-items:center; gap:8px;">
    <img src="./assets/los.png" alt="icon" width="25" height="25" style="display:block;">
      <a href="./lord-of-sql-injection/" style="text-decoration: none; color: #16a085;"> Lord of SQL Injection</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s; display:flex; align-items:center; gap:8px;">
    <img src="./assets/ringzer0.png" alt="icon" width="25" height="25" style="display:block;">
       <a href="./ringzer0" style="text-decoration: none; color: #16a085;"> RingZer0</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s; display:flex; align-items:center; gap:8px;">
    <img src="./assets/appsecil2025.ico" alt="icon" width="25" height="25" style="display:block;">
      <a href="./AppSec-IL-2025/" style="text-decoration: none; color: #16a085;"> AppSec-IL-2025</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s; display:flex; align-items:center; gap:8px;">
    <img src="./assets/hackthebox.svg" alt="icon" width="25" height="25" style="display:block;">
     <a href="./hackthebox/" style="text-decoration: none; color: #16a085; font-weight:500;">HackTheBox</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s; display:flex; align-items:center; gap:8px;">
      <img src="./assets/tryhackme.svg" alt="icon" width="25" height="25" style="display:block;">
      <a href="./tryhackme/" style="text-decoration: none; color: #16a085; font-weight:500;">TryHackMe</a>
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



<link rel="stylesheet" href="{{ '/assets/css/scoreboard.css' | relative_url }}">


<!-- CTF Ranks -->
<div class="iframe-container">

  <div class="iframe-wrapper">
     <div class="iframe-title">WeChall</div>
    <iframe src="https://www.wechall.net/profile/EliCopter" title="WebHacking.kr Profile"></iframe>
  </div>

  <div class="iframe-wrapper">
     <div class="iframe-title">WebHacking.kr</div>
    <iframe src="https://webhacking.kr/rank.php?page=2" title="WebHacking.kr Profile"></iframe>
  </div>

  <div class="iframe-wrapper">
    <div class="iframe-title">Root-Me</div>
    <img class="no-style" src="assets/screenshots/root-me.png" alt="Root-Me Scoreboard">
    <!-- <iframe src="https://www.root-me.org/elicopter770?lang=en#fd3288f941c568ba4d7b3d56ed57d3db" title="Root-Me Profile"></iframe> -->
  </div>

  <div class="iframe-wrapper">
     <div class="iframe-title">WebSec.fr</div>
     <img class="no-style" src="assets/screenshots/websec-fr.png" alt="WebSec.fr Scoreboard">
    <!-- <iframe src="https://websec.fr/scoreboard/5" title="WebSec.fr Profile"></iframe> -->
  </div>
</div>



<!-- change to see if num of CTF's changing -->
