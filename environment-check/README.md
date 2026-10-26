# Environment Check

## What it does
Prints a confirmation message to the terminal to prove that Python is installed, the file path is correct, and the environment is ready for coding.

## How to run it
Open Termux, navigate to this folder, and run:
python environment_check.py

## What I learned
1. How to use the `cd` command to navigate directly to a specific folder in Termux.
2. How to use the `touch` command to create a file when the Acode file browser gets confusing.

## What broke
Acode's "Save As" file picker kept defaulting to the old `C language` folder and wouldn't let me save in the new directory. I fixed it by using `touch environment_check.py` in Termux to create the file exactly where it needed to be.

## Status
Complete.
