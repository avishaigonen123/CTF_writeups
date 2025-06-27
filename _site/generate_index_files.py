import os
import argparse

TEMPLATE = '''---
layout: default
title: {title} Writeups
---

This folder contains solutions for the [{title}](http://overthewire.org/wargames/{slug}/) wargame from OverTheWire.

<style>
/* Styles same as your Behemoth example – omitted here for brevity */
</style>

<div class="behemoth-container">

  <!-- Sidebar -->
  <div class="behemoth-sidebar">
    <h00>Levels</h00>
    <ul>
      {{% assign {slug}_pages = site.pages 
        | where_exp: "p", "p.path contains 'overthewire/{slug}'" 
        | reject: "path", "overthewire/{slug}/index.md" 
        | reject: "path", "overthewire/{slug}/index.html" 
      %}}
      {{% assign level_pages = {slug}_pages | sort_natural: "path" %}}
      {{% for p in level_pages %}}
        {{% assign name = p.path | split: '/' | last | split: '.' | first %}}
        {{% if name != "index" %}}
          <li><a href="#{{{{ name }}}}">{{{{ name }}}}</a></li>
        {{% endif %}}
      {{% endfor %}}
    </ul>
  </div>

  <!-- Main content -->
  <div class="behemoth-content">
    {{% for p in level_pages %}}
      {{% assign name = p.path | split: '/' | last | split: '.' | first %}}
      {{% if name != "index" %}}
        <h00 id="{{{{ name }}}}">{{{{ name }}}}</h00>
        {{{{ p.content | markdownify }}}}
        <div class="level-banner">Next Level Writeup</div>
        <hr />
      {{% endif %}}
    {{% endfor %}}
  </div>

</div>
'''

def capitalize_folder_name(name):
    return name.replace('-', ' ').replace('_', ' ').title()

def generate_index_file(folder_path, folder_name, dry_run=False):
    title = capitalize_folder_name(folder_name)
    content = TEMPLATE.format(title=title, slug=folder_name)
    index_path = os.path.join(folder_path, "index.md")

    if dry_run:
        print(f"[DRY-RUN] Would create index.md in {folder_path}")
    else:
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[+] Created index.md in {folder_path}")

def process_folders(root_folder, dry_run=False):
    for dirpath, _, filenames in os.walk(root_folder):
        md_files = [f for f in filenames if f.endswith(".md")]
        folder_name = os.path.basename(dirpath)

        if "index.md" in md_files:
            continue  # Skip if index.md already exists

        if "README.md" in md_files:
            readme_path = os.path.join(dirpath, "README.md")
            if dry_run:
                print(f"[DRY-RUN] Would remove README.md in {dirpath}")
            else:
                os.remove(readme_path)
                print(f"[-] Removed README.md in {dirpath}")

        if md_files:  # has .md files
            generate_index_file(dirpath, folder_name, dry_run=dry_run)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto-generate index.md for OverTheWire writeup folders.")
    parser.add_argument("folder", nargs="?", default="overthewire", help="Root folder to process (default: 'overthewire')")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing files")
    args = parser.parse_args()

    process_folders(args.folder, dry_run=args.dry_run)
