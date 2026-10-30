"""
Script: student_file_manager.py
What it does: A menu-driven program that allows the user to save a student's name to a text file, read the saved name back, and handles file and input errors without crashing.
How to run: python student_file_manager.py
Author: David Udoh
Date: 2026-10-30
"""

while True: 
  print("")
  print("===== STUDENT FILE MANAGER =====")
  print("")
  print("1. Save student name")
  print("2. Read saved student name ")
  print("3. Exit")
  print("")

  try:
    choose = int(input("Choose option: "))
    
    if choose == 1:
      with open("student.txt", "w") as file:
        user = input("Enter your name: ")
        file.write(user)
    
    elif choose == 2:
      try:
        with open("student.txt", "r") as file:
          content = file.read()
        print(content)
      
      except FileNotFoundError:
        print("No file exists yet")
    
    elif choose == 3:
      print("Goodbye!")
      break

    else:
      print("Invalid Number")
  
  except ValueError:
    print("Invalid Valuetype")
