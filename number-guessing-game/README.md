# Number Guessing Game

## What it does
This is an interactive terminal game where the user tries to guess a secret number between 1 and 10. The program provides hints ("Too High!" or "Too Low!") and keeps asking for guesses until the user finds the correct number.

## How to run it
In Termux, run:
python number_guessing_game.py

## What I learned
- I learned how to use a `while` loop to keep the program running until a specific condition is met (`guess != secret_number`).
- I learned how to use `if/else` statements inside a loop to give the user real-time feedback based on their input.
- I learned the importance of updating the variable inside the loop (asking for a new `guess`); otherwise, the program would get stuck in an infinite loop.
- I learned to use variables (like `secret_number`) instead of hardcoding numbers directly into the logic, making the code easier to change later.

## What broke and how I fixed it
Nothing broke during the final run. The program correctly loops and evaluates the user's input until the correct number is guessed.

## Status
Complete	
