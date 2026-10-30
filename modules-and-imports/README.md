Personal Utility Toolkit

What it does

This is an interactive terminal program that acts as a utility toolkit. It uses built-in Python modules to perform different tasks: generating random numbers, selecting random names from a list, calculating square roots, and displaying today's and tomorrow's dates.

How to run it

In Termux, run:

python main.py

What I learned

- How to import built-in Python modules: "math", "random", and "datetime".
- How to use "random.randint(a, b)" to generate a random number.
- How to use "random.choice()" to select a random item from a list.
- How to use "math.sqrt()" for mathematical calculations.
- How to get the current date using "datetime.date.today()".
- How to add days to a date using "datetime.timedelta()".
- How nested "while" loops and "break" statements control program flow.
- How to handle invalid input using "try/except ValueError".

What broke and how I fixed it

- Inconsistent imports: I initially imported "randint" directly but still called it using "random.randint()". I learned to use one consistent import style.
- Variable naming: I named a variable "list", which shadows Python's built-in "list" type. I renamed it to "names".
- Infinite loop: My square-root option kept asking for numbers even after calculating a result. I fixed this using "break".
- Invalid input: My program could crash when users entered non-numeric input. I added a "try/except ValueError" block.
- Zero as a valid input: I initially rejected zero as a square-root input. I corrected the condition to accept zero and reject negative numbers.

These mistakes helped me understand imports, variable naming, nested loops, exception handling, and input validation.

Status

Complete
