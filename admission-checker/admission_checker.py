"""
Script: admission_checker.py
What it does: Evaluates a student's details against university admission requirements and displays if they are eligible or not.
How to run: python admission_checker.py
Author: David Udoh
Date: 2026-10-27
"""

full_name = input("Enter your full name: ") 
age = int(input("Enter your age: "))
score = int(input("Enter your UTME score: "))
credit = int(input("Enter number of O-level credit: "))
check = input("Do you have a credit in both English and Mathematics?(yes or no): ").lower()

#Admission rules:
#The applicant must be at least 16 years old.
#The UTME score must be at least 180.
#The applicant must have at least 5 O-Level credits.
#The applicant must have credits in both English and Mathematics.
#Important: A candidate who fails one requirement must not be told that they qualify.

if age < 16:
  print("NOT ELIGIBLE FOR ADMISSION. (You must be at least 16 years old)")

elif score < 180:
  print("NOT ELIGIBLE FOR ADMISSION. (You must score at least 180)")

elif credit < 5:
  print("NOT ELIGIBLE FOR ADMISSION. (You must have at least 5 O-Level credits)")

elif check == "no":
  print("NOT ELIGIBLE FOR ADMISSION. (You must have both credits in English and Mathematics)")

else:
  print("ELIGIBLE FOR ADMISSION")
  


