expense = []
total = 0


def expense_add(amount):
    expense.append(amount)
    print(f"{amount} added!")
    print("")


def view_expense():
    print(f"Your expense(s): {expense}")
    print("")


def expense_remove():
    amount = int(input("Enter the amount you want to remove: "))

    if amount in expense:
        expense.remove(amount)
        print(f"{amount} removed (first occurrence).")
        print("")
        return amount
    else:
        print("Expense not found.")
        print("")
        return 0


def total_expense():
    print(f"Your total expense is: {total}")
    print("")


def close():
    print("Tracker Closed")


while True:
    try:
        print("===== EXPENSE TRACKER =====")
        print()
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Remove an expense")
        print("4. View total spending")
        print("5. Exit")
        print()

        choice = int(input("Enter your choice number: "))

        if choice <= 0 or choice > 5:
            print("Invalid number")
            print()

        elif choice == 1:
            amount = int(input("Enter expense: "))

            if amount <= 0:
                print("Enter a positive number")
                print()
            else:
                expense_add(amount)
                total += amount

        elif choice == 2:
            view_expense()

        elif choice == 3:
            if expense == []:
                print("Expense not found")
            else:
                removed_amount = expense_remove()
                total -= removed_amount

        elif choice == 4:
            total_expense()

        elif choice == 5:
            close()
            break

    except ValueError:
        print("Please enter a valid whole number")
        print()