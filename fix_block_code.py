import os
import re

# Define the directory where your markdown files are located
directory = '.'  # Your target directory

# Recursive processing of markdown files
def replace_in_files(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as file:
                        content = file.read()
                except UnicodeDecodeError:
                    print(f"Skipping binary file: {filepath}")
                    continue

                # Regex to match:
                # ```language
                # % path/to/file
                # ```
                pattern = r'```([^\n]+)\n% ([^\n]+)\n```'

                # Replace with:
                # ```path/to/file
                # {% relative_include path/to/file %}
                # ```
                def replacer(match):
                    filename = match.group(2).strip()
                    return f'```{filename}\n{{% relative_include {filename} %}}\n```'

                updated_content = re.sub(pattern, replacer, content)

                if updated_content != content:
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(updated_content)
                    print(f"Updated: {filepath}")

replace_in_files(directory)
print("Recursive replacement done!")
