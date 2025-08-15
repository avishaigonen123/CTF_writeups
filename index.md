---
layout: default
title: "CTF Writeups Home"
---

# 🛡️ Welcome to My CTF Writeups

> A collection of writeups for Capture The Flag (CTF) challenges and wargames — solved, documented, and shared for learning.

<div id="writeup-counter" style="font-size: 2rem; font-weight: bold; color: #16a085; text-align:center; margin: 20px 0;">
  Solved CTFs: <span id="counter" data-count="{{ site.pages | where_exp:'p','p.path contains '.md' and p.path != 'index.md' ' | size }}">0</span>
</div>

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




<!-- Counter div -->
<div id="writeup-counter" style="font-size: 2rem; font-weight: bold; color: #16a085; text-align:center; margin: 20px 0;">
  Solved CTFs: <span id="counter" data-count="{{ site.pages | where_exp:'p','p.path contains '.md' and p.path != 'index.md' ' | size }}">0</span>
</div>

<!-- JS for animation -->
<script>
  document.addEventListener("DOMContentLoaded", function() {
    const counter = document.getElementById('counter');
    const target = +counter.getAttribute('data-count');
    let count = 0;
    const speed = 100; // smaller = faster

    const updateCount = () => {
      const increment = Math.ceil(target / speed);
      if (count < target) {
        count += increment;
        if(count > target) count = target;
        counter.innerText = count;
        requestAnimationFrame(updateCount);
      }
    };

    updateCount();
  });
</script>
