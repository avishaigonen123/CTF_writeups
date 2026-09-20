---
layout: default
title: "CTF Writeups Home"
---

# 🛡️ Welcome to My CTF Writeups

> A collection of writeups for Capture The Flag (CTF) challenges and wargames — solved, documented, and shared for learning.

{%- comment -%}
  Writeup counter.

  Replaces a rule that undercounted by 108. Three separate faults:
    - only 12 of the 15 platforms were listed; websec.il was absent entirely
    - hackthebox and tryhackme were counted through a second, separate branch
    - the `file_name != "index.md"` test skipped every writeup stored as
      <name>/index.md, which is how android_hacking, websec.il and several
      sub-wargames (overthewire/vortex, ringzer0/*, root-me/*) are organised

  The rule now: every page under a known platform, excluding that platform's own
  hub index, and excluding anything marked `status: incomplete`. That is 687
  pages total, 661 of them finished - the number shown.

  The platform list stays hardcoded deliberately. Deriving it from site.pages is
  what caused the undercount. RENAMING A TOP-LEVEL DIRECTORY REQUIRES EDITING
  THIS LIST, or the count silently drops.
{%- endcomment -%}
{%- assign platforms_string = "AppSec-IL-2025,android_hacking,flare-on,hacker101,hackthebox,lord-of-sql-injection,overthewire,pwnable.kr,ringzer0,root-me,tryhackme,websec.fr,websec.il,trythis0ne,webhacking.kr" -%}
{%- assign platforms = platforms_string | split: "," -%}

{%- assign writeups = 0 -%}
{%- assign htb_count = 0 -%}
{%- assign thm_count = 0 -%}

{%- for p in site.pages -%}
  {%- assign parts = p.path | split: '/' -%}
  {%- assign file_name = parts | last -%}
  {%- assign plat = parts[0] -%}
  {%- assign is_hub = false -%}
  {%- if parts.size == 2 and file_name == "index.md" -%}{%- assign is_hub = true -%}{%- endif -%}
  {%- if platforms contains plat and is_hub == false and p.status != "incomplete" -%}
    {%- assign writeups = writeups | plus: 1 -%}
    {%- if plat == "hackthebox" -%}{%- assign htb_count = htb_count | plus: 1 -%}{%- endif -%}
    {%- if plat == "tryhackme" -%}{%- assign thm_count = thm_count | plus: 1 -%}{%- endif -%}
  {%- endif -%}
{%- endfor -%}



<!-- MAIN CIRCLE -->
<div class="circle-counter" data-count="{{ writeups }}">
  <svg>
    <defs>
      <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#3b82f6"/>
        <stop offset="100%" stop-color="#06b6d4"/>
      </linearGradient>
    </defs>
    <circle class="bg" cx="130" cy="130" r="110"></circle>
    <circle class="progress" cx="130" cy="130" r="110"></circle>
  </svg>

  <div class="text-wrapper">
    <div class="count">0</div>
    <div class="label">Writeups so far</div>
  </div>
</div>


<!-- SMALL CIRCLES WRAPPER -->
<div class="circles-wrapper">

  <!-- HTB -->
  <div class="circle-counter small" data-count="{{ htb_count }}" onclick="window.location='/CTF_writeups/hackthebox'">
    <svg>
      <defs>
        <linearGradient id="gradient-htb" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#2d3748"/>
          <stop offset="100%" stop-color="#4a5568"/>
        </linearGradient>
      </defs>
      <circle class="bg" cx="80" cy="80" r="65"></circle>
      <circle class="progress" cx="80" cy="80" r="65" stroke="url(#gradient-htb)"></circle>
    </svg>
    <div class="text-wrapper">
      <img src="/CTF_writeups/assets/hackthebox.svg" class="logo" alt="HTB">
      <div class="count">{{ htb_count }}</div>
      <div class="label">HTB</div>
    </div>
  </div>


  <!-- THM -->
  <div class="circle-counter small" data-count="{{ thm_count }}" onclick="window.location='/CTF_writeups/tryhackme'">
    <svg>
      <defs>
        <linearGradient id="gradient-thm" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#fbbf24"/>
          <stop offset="100%" stop-color="#fcdb61"/>
        </linearGradient>
      </defs>
      <circle class="bg" cx="80" cy="80" r="65"></circle>
      <circle class="progress" cx="80" cy="80" r="65" stroke="url(#gradient-thm)"></circle>
    </svg>
    <div class="text-wrapper">
      <img src="/CTF_writeups/assets/tryhackme.svg" class="logo" alt="THM">
      <div class="count">{{ thm_count }}</div>
      <div class="label">THM</div>
    </div>
  </div>

</div>


<!-- JS Link -->
<script src="{{ '/assets/js/counter.js' | relative_url }}"></script>

<!-- CSS Link -->
<link rel="stylesheet" href="{{ '/assets/css/counter.css' | relative_url }}">

<!-- JS Link -->


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
    <img src="./assets/websec_il.png" alt="icon" width="25" height="25" style="display:block;">
      <a href="./websec.il/" style="text-decoration: none; color: #16a085;"> Websec.co.il</a>
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
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s; display:flex; align-items:center; gap:8px;">
      <img src="./assets/android_hacking.webp" alt="icon" width="25" height="25" style="display:block;">
      <a href="./android_hacking/" style="text-decoration: none; color: #16a085; font-weight:500;">Android Hacking</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s; display:flex; align-items:center; gap:8px;">
      <img src="./assets/hacker101.png" alt="icon" width="25" height="25" style="display:block;">
      <a href="./hacker101/" style="text-decoration: none; color: #16a085; font-weight:500;">Hacker 101</a>
    </li>
    <li style="margin-bottom: 12px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; transition: background-color 0.3s; display:flex; align-items:center; gap:8px;">
      <img src="./assets/flare-on.jpeg" alt="icon" width="25" height="25" style="display:block;">
      <a href="./flare-on/" style="text-decoration: none; color: #16a085; font-weight:500;">Flare-On</a>
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
