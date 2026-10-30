"""
Script: main.py
What it does: A menu-driven program that uses Python's standard library to generate random numbers, pick random names, calculate square roots, and display dates.
How to run: python main.py
Author: David Udoh
Date: 2026-10-30
"""

import math
import random
import datetime

while True:
  try:
    print("")
    print("Personal Utility Toolkit")
    print("")
    print("1. Generate a random between a and b ")
    print("2. Select a random name from a list ")
    print("3. Calculate the square root of a number ")
    print("4. Display today's date ")
    print("5. Display tommorrow's date ")
    print("6. Exit ")
    print("")

    choose = int(input("choose an option: "))
    print("")
    if choose == 1:
      a = int(input("Enter your first number: "))
      b = int(input("Enter your second number: "))

      result = random.randint(a, b)

      print(f'Random number: {result}')

    elif choose == 2:
      names = ["David", "Jacob", "John", "Nathan", "Daniel"]
      random_name = random.choice(names)
      print(f'Random name: {random_name}')

    elif choose == 3:
      while True:
        number = int(input("Enter a number to find the square root: "))
        if number >= 0:
          sqrt_number = math.sqrt(number)
          print(f'Square root of number: {sqrt_number}')
          break
        else:
          print("Please enter a positive number")
          print("")

    elif choose == 4:
      date = datetime.date.today()
      print(f'Today is {date}')

    elif choose == 5:
      today = datetime.date.today()
      tommorrow = today + datetime.timedelta(days=1)
      print(f'Tommorrow is: {tommorrow}')
    
    elif choose == 6:
      print("Goodbye!")
      break

    else:
      print("Invalid number")
  
  except ValueError:
    print("please choose a valid input")
    