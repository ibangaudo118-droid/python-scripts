# Tuples and Sets Practice

## What it does
This script demonstrates the properties of Python sets (removing duplicates and adding new items) and tuples (retrieving elements by index). It includes input validation to ensure the user answers the yes/no prompt correctly, and checks if a requested tuple index is valid before printing.

## How to run it
In Termux, run:
python tuples_and_sets.py

## What I learned
- I learned that Python sets automatically remove duplicate values. When I put "python" in the set twice, it only printed once.
- I learned how to use `.add()` to insert a new item into a set.
- I learned how to use a `while` loop to validate user input, making sure they can only proceed by typing "yes" or "no".
- I learned how to use an `if` statement to ensure the user doesn't try to access an index that doesn't exist in the tuple, preventing an `IndexError`.

## What broke and how I fixed it
I accidentally used parentheses `()` to define my set instead of curly braces `{}`. This made Python treat it as a Tuple, which caused an error when I tried to use the `.add()` method (because Tuples are immutable). I fixed it by changing the parentheses to curly braces, which correctly defined it as a Set.

## Status
Complete
