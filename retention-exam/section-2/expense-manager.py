expense = []
total = 0

while True:
  print("====== EXPENSE MANAGER ======")
  print("")
  print("1. Add an expense")
  print("2. View all recorded expense")
  print("3. Calculate the total expenses")
  print("4. Remove an expense")
  print("5. Exit the program")

  try:
    choose = int(input("Enter number: "))
    if choose <= 0 or choose > 5:
      print("select number 1-5")

    elif choose == 1:
      try:
        item = float(input("Enter your expense: "))
        if item > 0:
          expense.append(item)
          total = total + item
          print("Expense successfully added")
        else:
          print("Type in a positive expense")
      except ValueError:
        print("Enter expense as floating numbers")

    elif choose == 2:
      if expense == []:
        print("No expenses to view")
      else:
        print(expense)

    elif choose == 3:
      print(total)
 
    elif choose == 4: 
      try:
        if expense != []:
          print(expense)
          item_index = int(input("What index of item do you want to remove: "))
          result = expense.pop(item_index)
          total = total - result
          
          print(expense)
          
        else:
          print("No expense to remove")
      except IndexError:
          print("Index not available")
          

    elif choose == 5:
      print("Goodbye!")
      break
    else:
      print("Select number 1-5")
  except ValueError:
    print("Select number 1-5")
  
  
  