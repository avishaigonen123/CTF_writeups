import os
from string import Template

TEMPLATE = Template('''---
layout: default
title: ${title} Writeups
---
<a href="/CTF_writeups/overthewire/" style="display:inline-block; margin-bottom: 1rem; text-decoration: none; color: #16a085; font-weight: bold;">
      ← Back to OverTheWire
    </a>
                    
### This folder contains solutions for the [${title}](http://overthewire.org/wargames/${slug}/) wargame from OverTheWire.

<style>
  body {
    font-family: 'Arial', sans-serif;
    background-color: #eceff1;
    color: #333;
    margin: 0;
  }
  #main {
    max-width: 100% !important;
    width: 100% !important;
    margin: 0 auto;
  }
  .${slug}-container {
    display: flex;
    gap: 1.5rem;
    margin-top: 2rem;
    padding: 1rem;
  }
  .${slug}-sidebar {
    min-width: 200px;
    max-height: 90vh;
    overflow-y: auto;
    position: sticky;
    top: 1rem;
    padding: 1.5rem;
    border-radius: 8px;
    background-color: #34495e;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    color: #ecf0f1;
    margin-top: 1rem;
  }
  .${slug}-sidebar h00 {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
    color: #ecf0f1;
    border-bottom: 2px solid #16a085;
    padding-bottom: 0.5rem;
  }
  .${slug}-sidebar ul {
    list-style: none;
    padding-left: 0;
    font-size: 1rem;
    margin: 0;
  }
  .${slug}-sidebar li {
    margin-bottom: 0.5rem;
  }
  .${slug}-sidebar a {
    display: block;
    padding: 6px 12px;
    border-radius: 6px;
    text-decoration: none;
    color: #ecf0f1;
    transition: background 0.3s ease, color 0.3s ease;
  }
  .${slug}-sidebar a:hover {
    background-color: #16a085;
    color: #fff;
  }
  .${slug}-content {
    flex: 1;
    max-height: 90vh;
    overflow-y: auto;
    padding-right: 1rem;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    padding: 2rem;
    font-size: 1rem;
    color: #333;
    margin-top: 1rem;
  }
  .${slug}-content h00 {
    font-size: 1.4rem;
    font-weight: 600;
    margin-top: 2rem;
    color:rgb(143, 151, 159);
    scroll-margin-top: 100px;
  }
  hr {
    margin: 2.5rem 0;
    border: none;
    border-top: 1px solid #ddd;
  }
  .${slug}-sidebar::-webkit-scrollbar {
    width: 8px;
  }
  .${slug}-sidebar::-webkit-scrollbar-thumb {
    background-color: #16a085;
    border-radius: 4px;
  }
  .${slug}-sidebar::-webkit-scrollbar-track {
    background-color: #ecf0f1;
  }
  @media (max-width: 768px) {
    .${slug}-container {
      flex-direction: column;
    }
    .${slug}-sidebar {
      max-height: none;
      width: 100%;
      margin-bottom: 2rem;
    }
  }
  .level-banner {
    background-color: #16a085;
    color: #fff;
    padding: 1rem;
    text-align: center;
    font-weight: bold;
    margin-top: 2rem;
    border-radius: 8px;
  }
</style>

<div class="${slug}-container">

  <!-- Sidebar -->
  <div class="${slug}-sidebar">
    <h00>Levels</h00>
    <ul>
      {% assign ${slug}_pages = site.pages
        | where_exp: "p", "p.path contains 'overthewire/${slug}'"
        | reject: "path", "overthewire/${slug}/index.md"
        | reject: "path", "overthewire/${slug}/index.html"
      %}
      {% assign level_pages = ${slug}_pages | sort_natural: "path" %}
      {% for p in level_pages %}
        {% assign name = p.path | split: '/' | last | split: '.' | first %}
        {% if name != "index" %}
          <li><a href="#{{ name }}">{{ name }}</a></li>
        {% endif %}
      {% endfor %}
    </ul>
  </div>

  <!-- Main content -->
  <div class="${slug}-content">
    {% for p in level_pages %}
      {% assign name = p.path | split: '/' | last | split: '.' | first %}
      {% if name != "index" %}
        <h00 id="{{ name }}">{{ name }}</h00>
        {{ p.content | markdownify }}
        <div class="level-banner">Next Level Writeup</div>
        <hr />
      {% endif %}
    {% endfor %}
  </div>

</div>
''')

def generate_index_file(folder_path, slug):
    index_path = os.path.join(folder_path, "index.md")
    content = TEMPLATE.substitute(title=slug.capitalize(), slug=slug)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated: {index_path}")

def should_generate_index(folder):
    md_files = [f for f in os.listdir(folder) if f.endswith(".md")]
    return len(md_files) > 1  # Now always overwrite

def main(root="overthewire"):
    print(f"🔍 Scanning '{root}' for folders with markdown files...")
    count = 0
    for subdir, dirs, files in os.walk(root):
        if should_generate_index(subdir):
            slug = os.path.basename(subdir)
            generate_index_file(subdir, slug)
            count += 1
    print(f"\n📁 Total index.md files generated: {count}")

if __name__ == "__main__":
    main()
