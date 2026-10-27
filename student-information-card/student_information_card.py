"""
Script: student_information_card.py
What it does: Collects a student's details using input() and displays them in a formatted information card.
How to run: python student_information_card.py 
Author: David Udoh
Date: 2026-10-27
"""

full_name = input("Enter your full name: ")
age = input("Enter your age: ")
university = input("Enter your university: ")
course_of_study = input("Enter your course of Study: ")
fav_programming_lang = input("Enter your favourite programming language: ")

print("")
print("============== STUDENT INFORMATION CARD")
print("==============")
print(f'Name: {full_name}')
print(f'Age: {age}')
print(f'University: {university}')
print(f'Course: {course_of_study}')
print(f'Favourite Programming Language: {fav_programming_lang}')
print("=========================================================")
print("===========")
