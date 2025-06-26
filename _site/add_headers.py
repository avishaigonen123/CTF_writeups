import os
import re

ext_map = {
    ".sh": "bash",
    ".php": "php",
    ".c": "c",
    ".cpp": "cpp",
    ".py": "python",
    ".js": "javascript",
    ".pl": "perl",
    ".asm": "nasm",
}

def guess_lang(filepath):
    _, ext = os.path.splitext(filepath)
    return ext_map.get(ext.lower(), "")  # fallback to plaintext

def process_markdown_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.splitext(os.path.basename(path))[0]

    # Add YAML front matter only if missing
    if not content.lstrip().startswith('---'):
        front_matter = f"""---
layout: default
title: {filename}
---

"""
        content = front_matter + content

    # Replace (./scripts/...) pattern
    def repl_parens(match):
        script_path = match.group(1).replace('./', '', 1)
        lang = guess_lang(script_path)
        return f"\n```{lang}\n% {script_path}\n```\n"

    content = re.sub(r"\(\s*(\./scripts/[^\)]+)\s*\)", repl_parens, content)

    # Replace [label](./scripts/...) links too
    def repl_links(match):
        script_path = match.group(2).replace('./', '', 1)
        lang = guess_lang(script_path)
        return f"\n```{lang}\n% {script_path}\n```\n"

    content = re.sub(r"\[([^\]]+)\]\((\./scripts/[^)]+)\)", repl_links, content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated: {filename}")

# Process all .md files
for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".md"):
            full_path = os.path.join(root, file)
            process_markdown_file(full_path)