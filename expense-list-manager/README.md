# Expense List Manager

## What it does
A terminal-based menu program that allows the user to manage a list of expenses. The user can add new expenses, remove an expense by its index, and view the current list of expenses.

## How to run it
In Termux, run:
python expense_list_manager.py

## What I learned
- I learned how to use a `while True` loop to keep a menu running continuously without repeating my code.
- I learned how to use `.append()` to add items to a list, and `.pop()` to remove items by their index.
- I learned about defensive programming: handling potential errors (like trying to remove an item from an empty list, or typing an invalid index) *before* Python runs the code, to prevent the program from crashing.
- I learned why menu choices are stored as strings (so we compare them with `"1"`, `"2"`), but amounts are converted to integers with `int()`.

## What broke and how I fixed it
In my first draft, I had copy-pasted the menu and the `input()` prompt inside every single `if` statement, which made the code messy and hard to read. I also had a bug where the remove feature would crash if the list was empty. 

I fixed this by restructuring the code with a `while True:` loop at the top to handle the menu, and using a `break` statement to exit. I also added an `if len(expense) == 0:` check before attempting to remove items, and an index range check to ensure the user can't remove an item that doesn't exist.

## Status
Complete
