# Error Handling Practice

## What it does
This script continuously asks the user for their age. It uses a `try/except` block to catch a `ValueError`. If the user types letters instead of numbers (like "hello"), the program prints "Invalid input" and asks again instead of crashing. The loop only breaks when a valid number is entered, at which point the program prints the age.

## How to run it
In Termux, run:
python error_handling.py

## What I learned
- I learned how to use `try` and `except ValueError` to prevent the program from crashing when `int()` receives a non-numeric string.
- I learned how to combine `try/except` with a `while True` loop to force the user to keep trying until they provide valid input.
- I learned that using `break` inside the `try` block is a better way to exit a loop than using `exit()`, because `break` allows the rest of the program to continue running.

## What broke and how I fixed it
My first version used `exit()` to stop the loop, which killed the whole program and made the final `print(age)` line unreachable. I fixed it by replacing `exit()` with `break` so the loop stops cleanly and the program can finish executing.

## Status
Complete
