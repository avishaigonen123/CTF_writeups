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
  {% if wargames contains first_part and p.path != "index.md" %}
    {% assign filtered_pages = filtered_pages | append: p.path | append: "," %}
  {% endif %}
{% endfor %}
{% assign filtered_pages = filtered_pages | split: "," %}


<div class="circle-counter" data-count="{{ filtered_pages | size }}">
   <svg>
    <defs>
      <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#3b82f6"/>
        <stop offset="100%" stop-color="#06b6d4"/>
      </linearGradient>
    </defs>
    <circle class="bg" cx="75" cy="75" r="70"></circle>
    <circle class="progress" cx="75" cy="75" r="70"></circle>
  </svg>
  <div class="text-wrapper">
    <div class="count">0</div>
    <div class="label">Writeups</div>
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


<!-- Scoreboard iframe -->
<div class="scoreboard-wrapper">
  <iframe src="https://your-ctf-platform.com/scoreboard" title="CTF Scoreboard"></iframe>
</div>

<link rel="stylesheet" href="{{ '/assets/css/scoreboard.css' | relative_url }}">
<script src="{{ '/assets/js/scoreboard.js' | relative_url }}"></script>






<title>EliCopter770 CTF Dashboard</title>
<style>
  body {
    font-family: 'Segoe UI', sans-serif;
    background: #0f172a;
    color: #e0e0e0;
    margin: 0;
    padding: 20px;
  }

  h1 {
    text-align: center;
    color: #3b82f6;
    text-shadow: 0 0 10px #3b82f6;
  }

  /* Circle Counter */
  .circle-counter {
    position: relative;
    width: 200px;
    height: 200px;
    margin: 40px auto;
  }

  .circle-counter svg {
    position: absolute;
    top: 0;
    left: 0;
    width: 200px;
    height: 200px;
    transform: rotate(-90deg);
  }

  .circle-counter .bg {
    fill: none;
    stroke: #334155;
    stroke-width: 16;
  }

  .circle-counter .progress {
    fill: none;
    stroke: url(#gradient);
    stroke-width: 16;
    stroke-linecap: round;
    stroke-dasharray: 439.82;
    stroke-dashoffset: 439.82;
    transition: stroke-dashoffset 1s ease;
    filter: drop-shadow(0 0 10px rgba(59, 130, 246, 0.8));
  }

  .circle-counter .text-wrapper {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
  }

  .circle-counter .count {
    font-size: 2.5rem;
    font-weight: 700;
    background: linear-gradient(90deg, #3b82f6, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 10px rgba(59, 130, 246, 0.6);
  }

  .circle-counter .label {
    font-size: 1.2rem;
    color: #3b82f6;
    font-weight: 500;
    text-shadow: 0 0 5px rgba(59, 130, 246, 0.4);
  }

  /* CTF Rank Cards */
  .ctf-ranks {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
    margin-top: 40px;
  }

  .ctf-card {
    background: #1e293b;
    border: 2px solid #3b82f6;
    border-radius: 16px;
    padding: 20px;
    width: 280px;
    text-align: center;
    box-shadow: 0 0 20px rgba(59, 130, 246, 0.3);
  }

  .ctf-card h2 {
    margin: 0 0 10px;
    color: #06b6d4;
  }

  .ctf-card p {
    margin: 5px 0;
    font-size: 1.1rem;
  }

  .ctf-card a {
    color: #3b82f6;
    text-decoration: none;
    font-weight: bold;
  }

  .ctf-card a:hover {
    text-decoration: underline;
  }

</style>
</head>
<body>

<h1>EliCopter770 CTF Dashboard</h1>

<!-- Circle Counter -->
<div class="circle-counter" data-count="380">
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

<!-- CTF Ranks -->
<div class="ctf-ranks">
  <div class="ctf-card">
    <h2>Root-Me</h2>
    <p>Username: <strong>EliCopter770</strong></p>
    <p>Rank: <strong>#123</strong></p>
    <p><a href="https://www.root-me.org/elicopter770?lang=en#fd3288f941c568ba4d7b3d56ed57d3db" target="_blank">View Profile</a></p>
  </div>

  <div class="ctf-card">
    <h2>WebHacking.kr</h2>
    <p>Username: <strong>EliCopter770</strong></p>
    <p>Rank: <strong>#45</strong></p>
    <p><a href="https://webhacking.kr/rank.php?page=2" target="_blank">View Profile</a></p>
  </div>

  <div class="ctf-card">
    <h2>WebSec.fr</h2>
    <p>Username: <strong>EliCopter770</strong></p>
    <p>Rank: <strong>#67</strong></p>
    <p><a href="https://websec.fr/scoreboard/5" target="_blank">View Profile</a></p>
  </div>

  <div class="ctf-card">
    <h2>WeChall</h2>
    <p>Username: <strong>EliCopter770</strong></p>
    <p>Rank: <strong>#89</strong></p>
    <p><a href="https://www.wechall.net/profile/EliCopter" target="_blank">View Profile</a></p>
  </div>
</div>

<script>
document.addEventListener("DOMContentLoaded", () => {
  const counters = document.querySelectorAll(".circle-counter");

  counters.forEach(counter => {
    const countEl = counter.querySelector(".count");
    const progressEl = counter.querySelector(".progress");

    const target = parseInt(counter.getAttribute("data-count")) || 0;
    let current = 0;

    const radius = progressEl.r.baseVal.value;
    const circumference = 2 * Math.PI * radius;

    progressEl.style.strokeDasharray = circumference;
    progressEl.style.strokeDashoffset = circumference;

    const duration = 1500;
    const frameRate = 60;
    const totalFrames = Math.round((duration / 1000) * frameRate);
    let frame = 0;

    const animate = () => {
      frame++;
      const progress = frame / totalFrames;
      const eased = easeOutCubic(progress);

      current = Math.round(target * eased);
      countEl.textContent = current;

      const offset = circumference * (1 - eased);
      progressEl.style.strokeDashoffset = offset;

      if (frame < totalFrames) {
        requestAnimationFrame(animate);
      } else {
        countEl.textContent = target;
        progressEl.style.strokeDashoffset = 0;
      }
    };

    requestAnimationFrame(animate);

    function easeOutCubic(t) {
      return 1 - Math.pow(1 - t, 3);
    }
  });
});
</script>

</body>