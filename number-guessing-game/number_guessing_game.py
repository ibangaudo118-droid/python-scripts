"""
Script: number-guessing-game
What it does: A simple guessing game where the user tries to guess a secret number between 1 and 10, with hints if they guess too high or too low.
How to run: python number_guessing_game.py
Author: David Udoh
Date: 2026-10-27
"""

secret_number = 7

guess = int(input("Guess the secret number(1-10): "))

while guess != secret_number:
  if guess > secret_number:
    print("Too High!. Try again")
  else:
    print("Too Low!. Try again")

  guess = int(input("Guess the secret number(1-10): "))
print("You guessed correctly! Congratulations")