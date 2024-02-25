from docx import Document
from pathlib import Path
from os import makedirs, path
from sys import argv
from re import sub

# Check if user provided the correct number of arguments. 
# If not, print an error message and exit the program.
if len(argv) != 3:
    print("Usage: python compare.py <old_version>.docx <new_version>.docx")
    exit(1)

# Initialize the old and new version names
# without the file extension
old, new = Path(argv[1]).stem, Path(argv[2]).stem 

# Create a directory for the diff files
if not path.exists("diff"):
    makedirs("diff")

# Iterate over the old and new versions 
# and write the paragraphs to a text file.
for ver in [old, new]:   
    paragraphs = [sub(r"\r|\n", "", paragraph.text) for paragraph in Document(f'{ver}.docx').paragraphs]
    with open(f"diff/{ver}.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(paragraphs))

# Write the command to compare the two versions to a text file.
cmd = f"git diff --no-index --word-diff --color diff/{old}.txt diff/{new}.txt"        

# Windows users can use the .bat file
with open(f"diff/compare.bat", "w") as f:
    f.write(f"@echo off\n@{cmd}")

# Linux users can use the .sh file.
with open(f"diff/compare.sh", "w") as f:
    f.write(f"{cmd} | less -c -R")