"""
Script: operators_practice
What it does: Demonstrate Arithemetic, Logical, Comparison and Assignment operators using two variables.
How to run: python operators_practice.py
Author: David Udoh
Date: 2026-10-26
"""

number1 = 5
number2 = 7

#For Arithmetic operators
#1. Addition (+)

addition = number1 + number2

#2. Subtraction (-)

subtraction = number1 - number2

#3. Multiplication (*)

multiplication = number1 * number2

#4. Division(/)

division = number1 / number2

#5. Floor Division (//)

floor_division = number1 // number2

#6. Modulus (%)

modulus = number1 % number2

#7. Exponentiation (**)

exponentiation = number1 ** number2

print(f'Sum: {addition}')
print(f'Subtraction: {subtraction}')
print(f'Multiplication: {multiplication}')
print(f'Division: {division}')
print(f'Floor Division: {floor_division}')
print(f'Modulus: {modulus}')
print(f'Exponentiation: {exponentiation}')

#For Comparison operators
#1. Equal to symbol (==)

if number1 == number2:
  print("Both numbers are equal")
else:
  print("Both numbers aren't equal")

#2. Not equal to symbol (!=)

if number1 != number2:
  print("Both numbers aren't equal")
else:
  print("Both numbers are equal")

#3. Greater than symbol (>)

if number1 > number2:
  print(f'{number1} is greater than {number2}')

else:
  print(f'{number1} is not greater than {number2}')

  #4. Less than symbol (<)

if number1 < number2:
  print(f'{number1} is less than {number2}')

else:
  print(f'{number1} is not lesser than {number2}')

#5. Greater than or equal to symbol (>=)

if number1 >= number2:
  print(f'{number1} is greater than or equal to {number2}')

else:
  print(f'{number1} is not greater than or equal to {number2}')

#6. Less than or equal to symbol (<=)

if number1 <= number2:
  print(f'{number1} is less than or equal to {number2}')

else: 
  print(f'{number1} is not less than or equal to {number2}')

#For Logical operators
#1. and 
# using the comparison expressions to evaluate whether a logical expression is True or False

if number1 > number2 and number1 == number2:
  print(f'Is {number1} greater than {number2} and is {number1} equal to {number2}? True')

else:
  print(f'Is {number1} greater than {number2} and is {number1} equal to {number2}? False')

#2. or

if number1 < number2 or number1 == number2:
  print(f'Is {number1} less than {number2} or is {number1} equal to {number2}? True')

else:
  print(f'Is {number1} less than {number2} or is {number1} equal to {number2}? False')


#3. not

if not (number1 == number2):
  print(f'{number1} is not equal to {number2}')

else:
  print(f'{number1} is equal to {number2}')

#For Assignment operators
#+=

number1 += 20

print(f'Number1: {number1}')

#-=

number2 -= 1

print(f'Number2: {number2}')

#*=

number1 *= 3

print(f'Number1: {number1}')
  


  
