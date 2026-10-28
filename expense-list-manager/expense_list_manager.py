"""
Script: expense_list_manager.py
What it does: Allows a user to add, remove and view expenses
How to run: python expense_list_manager.py
Author: David Udoh
Date: 2026-10-28
"""

expense = []

while True:
  print("==== MENU ====")
  print("")
  print("1. Add Expense")
  print("2. Remove Expense")
  print("3. View Expense")
  print("4. Exit")

  choice = input("Enter your choice: ")

  if choice == "1":
    amount = input("Enter Expense: ")
    expense.append(amount)
    print("Expense Added Successfully")

  elif choice == "2":

    if len(expense) == 0:
      print("Nothing to remove")
      
    else:
      index = int(input("Enter the index to remove expense: "))
      
      if index >= 0 and index < len(expense):
        expense.pop(index)
        print("Expense Removed Successfully")
        
      else:
        print("Invalid Index")

  elif choice == "3":
    if len(expense) == 0:
      print("List is empty")
      
    else:
      print(f'Expense: {expense}')

  elif choice == "4":
    print("Goodbye!")
    break

  else:
    print("Invalid Choice")