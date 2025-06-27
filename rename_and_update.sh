#!/bin/bash

# Settings
DIRECTORY="$1"   # Folder with files
EXT=".md"                          # Extension to match
PAD=2                              # Padding width

echo "Renaming files..."

for file in "$DIRECTORY"/*"$EXT"; do
  filename=$(basename "$file")
  
  if [[ $filename =~ ^([a-zA-Z_]+)([0-9]+)\.md$ ]]; then
    base="${BASH_REMATCH[1]}"
    num="${BASH_REMATCH[2]}"
    new_num=$(printf "%0${PAD}d" "$num")
    new_file="$DIRECTORY/${base}${new_num}${EXT}"
    
    if [[ "$file" != "$new_file" ]]; then
      mv "$file" "$new_file"
      echo "Renamed $filename → $(basename "$new_file")"
    fi
  fi
done

echo "✅ Done."
