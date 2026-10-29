"""
Script: calculator_functions.py
What it does: A calculator program that performs addition, subtraction, multiplication, and division using four separate functions that return their results.
How to run: python calculator_functions.py
Author: David Udoh
Date: 2026-10-29
"""

def add(a, b):
  return(a + b)

def minus(a, b):
  return(a - b)

def multiply(a, b):
  return(a * b)

def division(a, b):
  return(a / b)


a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))

choose = input("Choose your arithmetic operator(+ - * /): ")

if choose == "+":
  results = add(a, b)

elif choose == "-":
  results = minus(a, b)

elif choose == "*":
  results = multiply(a, b)

elif choose == "/":
  if b == 0:
    print("Use number other than zero for b")
    exit()
  else:
    results = division(a, b)
    results = round(results,2)

else:
  print("Invalid Arithmetic operator")
  exit()

print(f'Result: {results}')