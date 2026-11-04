Employee Payroll Management System

Description

The Employee Payroll Management System is a Python-based application designed to simplify employee payment calculations.

It supports two categories of employees: full-time employees, who receive a fixed monthly salary, and contract employees, whose payments are calculated based on their daily rate and number of working days.

The system automates payment calculations, validates employee payment information, and calculates the total payroll for all registered employees.

Features

- Calculates monthly payments for full-time employees.
- Calculates contract employee payments using daily rates and working days.
- Displays employee payment information.
- Calculates the total payroll for all registered employees.
- Validates payment information to prevent invalid salary, daily rate, and working-day values.

Object-Oriented Programming Concepts

1. Encapsulation

I used encapsulation to protect employee attributes such as names and categories by making them private. This helps control access to employee information and prevents accidental modification.

2. Inheritance

I used inheritance to allow "FulltimeEmployee" and "ContractEmployee" to inherit common attributes and methods from the parent "Employee" class, reducing code duplication.

3. Polymorphism

I implemented polymorphism by storing different employee objects in a shared list and calling the same "calculate_pay()" method on each object. Each employee class provides its own payment calculation.

4. Abstraction

I used abstraction by creating an abstract "Employee" class with an abstract "calculate_pay()" method. This ensures that every concrete employee class provides its own implementation of the payment calculation.

How to Run

1. Clone or download the project.
2. Open the project folder in your terminal.
3. Run the following command:

python main.py

Technologies Used

- Python 3
- Python Standard Library ("abc" module)
