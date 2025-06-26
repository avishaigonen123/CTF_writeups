import os
import re

def clean_up_links(md_dir=".", script_dir="scripts"):
    extensions = ["sh", "php", "c", "asm", "js", "pl", "py", "cpp"]
    for root, _, files in os.walk(md_dir):
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)
                with open(md_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Remove standalone [filename.ext] lines
                for ext in extensions:
                    # Match lines with [filename.ext] followed by block with % scripts/...
                    pattern = rf"^.*\[(.+\.{ext})\].*\n```.*\n% {script_dir}/.*/\1\n```"
                    content = re.sub(pattern, lambda m: f"```{ext}\n% {script_dir}/{m.group(1)}\n```", content, flags=re.MULTILINE)

                    # OR: match a line that only contains the [filename.ext]
                    content = re.sub(rf"^.*\[(.+\.{ext})\].*\n(?=```{ext}\n% {script_dir}/.*/\1\n```)", "", content, flags=re.MULTILINE)

                with open(md_path, "w", encoding="utf-8") as f:
                    f.write(content)

    print("Cleanup complete.")

clean_up_links()