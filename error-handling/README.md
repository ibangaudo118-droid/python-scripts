# Error Handling Practice

## What it does
This script continuously asks the user for their age. It uses a `try/except` block to catch a `ValueError`. If the user types letters instead of numbers (like "hello"), the program prints "Invalid input" and asks again instead of crashing. The loop only breaks when a valid number is entered.

## How to run it
In Termux, run:
python error_handling.py

## What I learned
- I learned how to use `try` and `except ValueError` to prevent the program from crashing when `int()` receives a non-numeric string.
- I learned how to combine `try/except` with a `while True` loop to force the user to keep trying until they provide valid input.
- I learned that once the `try` block succeeds, I can use `exit()` to break out of the program.

## What broke and how I fixed it
Nothing broke during the final run. The `except` block successfully caught the error when I typed letters.

## Status
Complete
