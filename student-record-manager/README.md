# Dictionary Practice

## What it does
This script demonstrates how to create and manipulate a Python dictionary. It starts with a student's information and allows the user to update an existing value (age), add a completely new key-value pair, and remove an existing key, with input validation at each step.

## How to run it
In Termux, run:
python student_record_manager.py

## What I learned
- I learned that dictionaries store data in key-value pairs, like `{"name": "David"}`.
- I learned how to update an existing value by targeting its key: `student["age"] = new_age`.
- I learned how to add a new key-value pair dynamically using variables: `student[new_key_name] = new_key_value`.
- I learned how to remove an item using `.pop(key)`.
- I learned how to check if a key exists before trying to remove it, using `if key not in student:`.

## What broke and how I fixed it
When trying to validate the key for removal, I originally wrote a condition comparing the key string directly to the dictionary (`if ask_of_key != student:`). This was a logic error. I fixed it by using the `in` keyword: `if ask_of_remove_key not in student:`. This correctly checks if the key does not exist inside the dictionary before attempting to remove it.

## Status
Complete
