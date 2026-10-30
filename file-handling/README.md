# Student File Manager

## What it does
This is a terminal-based menu program that demonstrates file handling. It allows the user to save a name to a text file (`student.txt`), read the name back from the file, or exit the program. It includes robust error handling to prevent crashes from invalid menu choices or missing files.

## How to run it
In Termux, run:
python student_file_manager.py

## What I learned
- I learned how to open and write to a file using `open("filename.txt", "w")` and `.write()`.
- I learned how to read from a file using `open("filename.txt", "r")` and `.read()`.
- I learned how to use the `with` statement, which ensures the file is automatically closed after the block of code runs.
- I learned how to catch a `FileNotFoundError` if the program tries to read a file that hasn't been created yet.
- I learned how to catch a `ValueError` if the user types a string instead of a number in the menu.

## What broke and how I fixed it
When I first wrote the code, I faced a lot of challenges. The program would crash with a `FileNotFoundError` if I chose option 2 before saving any data, and it would crash with a `ValueError` if I typed letters in the menu. I fixed this by wrapping the file-reading logic in a `try/except FileNotFoundError` block, and wrapping the menu input in a `try/except ValueError` block.

## Status
Complete
