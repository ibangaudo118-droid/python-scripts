"""
Script: list_comprehensions.py
What it does: Demonstrates how to use a list comprehension to create a new list by doubling each number from an original list.
How to run: python list_comprehensions.py
Author: David Udoh
Date: 2026-10-29
"""
numbers = [2, 4, 6, 8, 10]
doubled = []

doubled = [number * 2 for number in numbers]

print(numbers)
print(doubled)