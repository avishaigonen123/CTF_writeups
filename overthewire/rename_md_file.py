import os
import re

# Base path to your directory
base_path = r"C:\USERS\AVISH\GIT\CTF_WRITEUPS\OVERTHEWIRE"

def rename_md_files(base_path):
    for root, dirs, files in os.walk(base_path):
        for file_name in files:
            # Process only .md files starting with "level"
            if file_name.endswith(".md") and file_name.startswith("level"):
                # Extract the parent folder name
                parent_folder = os.path.basename(root)
                # Extract the level number
                match = re.match(r"level(\d+)\.md", file_name)
                if match:
                    level_number = match.group(1)
                    new_name = f"{parent_folder}{level_number}.md"
                    old_path = os.path.join(root, file_name)
                    new_path = os.path.join(root, new_name)
                    
                    # Rename the file
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")

rename_md_files(base_path)
