---
layout: default
title: HackTheBox Writeups
---

Welcome to the HackTheBox Wargames writeups hub. Choose a wargame below to view detailed solutions.

<style>
  .wargame-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
  }

  .wargame-card {
    position: relative;         /* needed for badge positioning */
    background-color: #34495e;
    color: #ecf0f1;
    border-radius: 10px;
    padding: 1rem;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    transition: transform 0.2s ease;
    text-decoration: none;
    overflow: hidden;           /* ensures content stays inside */
  }

  .wargame-card:hover {
    transform: scale(1.05);
    background-color: #16a085;
    color: #fff;
  }

  .wargame-card img {
    width: 100%;
    height: 200px;             /* fixed height */
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

  /* INCOMPLETE badge */
  .card-status.unfinished {
    position: absolute;
    top: 16px;                 /* slightly below top */
    left: 50%;                 /* center horizontally */
    transform: translateX(-50%);
    background: rgba(238, 31, 8, 0.9);
    color: #fff;
    font-size: 1.1rem;
    font-weight: 700;
    padding: 6px 12px;
    border-radius: 8px;
    letter-spacing: 0.05em;
    z-index: 2;                /* above image */
    text-align: center;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
  }
</style>

<div class="wargame-container">
  {%- comment -%}
    Precomputed ONCE for the page, not once per machine.

    The original nested a full scan of site.static_files inside the per-machine
    loop, purely to test whether wargame.png exists - on the order of 100,000
    string comparisons - and the loop body emitted a blank line for every
    non-matching iteration. That whitespace is where this page's size came from
    (847 KB for hackthebox, 7.7 MB for tryhackme). Joining the static paths once
    turns the inner test into a single substring check, and the whitespace
    control on the tags removes the per-iteration blank lines.

    Nothing visible changes: same cards, same order, same images, same badges.
  {%- endcomment -%}
  {%- assign static_blob = site.static_files | map: "path" | join: "|" -%}

  {%- comment -%}
    Names of machines holding at least one page marked incomplete, also resolved
    once rather than re-scanning site.pages for every card.
  {%- endcomment -%}
  {%- assign incomplete_blob = "|" -%}
  {%- for p in site.pages -%}
    {%- if p.path contains 'hackthebox/' and p.status == "incomplete" -%}
      {%- assign pp = p.path | split: "/" -%}
      {%- assign incomplete_blob = incomplete_blob | append: pp[1] | append: "|" -%}
    {%- endif -%}
  {%- endfor -%}

  {%- assign seen = "" | split: "" -%}
  {%- for folder in site.pages -%}
    {%- if folder.path contains 'hackthebox/' and folder.path != 'hackthebox/index.md' -%}
      {%- assign path_parts = folder.path | split: '/' -%}
      {%- assign folder_name = path_parts[1] -%}
      {%- unless seen contains folder_name -%}
        {%- capture folder_path -%}hackthebox/{{ folder_name }}{%- endcapture -%}
        {%- assign img_rel_path = folder_name | append: '/wargame.png' -%}
        {%- assign has_image = false -%}
        {%- if static_blob contains img_rel_path -%}{%- assign has_image = true -%}{%- endif -%}
        {%- assign marker = "|" | append: folder_name | append: "|" -%}
        {%- assign incomplete = false -%}
        {%- if incomplete_blob contains marker -%}{%- assign incomplete = true -%}{%- endif -%}
        <a class="wargame-card" href="{{ site.baseurl }}/{{ folder_path }}/">{%- if has_image -%}<img src="{{ site.baseurl }}/{{ folder_path }}/wargame.png" alt="{{ folder_name | capitalize }} wargame image">{%- else -%}<img src="{{ site.baseurl }}/assets/hackthebox.svg" alt="default image">{%- endif -%}{%- if incomplete -%}<div class="card-status unfinished">INCOMPLETE</div>{%- endif -%}<h2>{{ folder_name | capitalize }}</h2><p>Writeups for {{ folder_name | capitalize }} wargame</p></a>
        {%- assign seen = seen | push: folder_name -%}
      {%- endunless -%}
    {%- endif -%}
  {%- endfor -%}
</div>