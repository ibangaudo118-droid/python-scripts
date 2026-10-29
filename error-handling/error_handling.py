"""
Script: error_handling.py
What it does: Asks the user for their age and uses a try/except block inside a while loop to handle invalid input without crashing. 
How to run: python error_handling.py
Author: David Udoh
Date: 2026-10-29
"""

while True:
  try:
    age = int(input("Enter your age: "))
    break

  except ValueError:
    print("Invalid input")
    
print(age)

