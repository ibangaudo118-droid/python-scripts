# Admission Eligibility Checker

## What it does
This program collects an applicant's details (name, age, UTME score, O-Level credits, and core subject credits) and evaluates them against the university's admission rules. It checks each requirement in order and informs the applicant if they are eligible or exactly why they are not.

## How to run it
In Termux, run:
python admission_checker.py

## What I learned
- I learned how to use `if`, `elif`, and `else` statements to evaluate a sequence of conditions.
- I learned how to use `.lower()` on a user's input so that answers like "No", "NO", or "no" are all treated the same.
- I learned how to make error messages helpful by explaining exactly which rule the applicant failed, rather than just saying "Not eligible."

## What broke and how I fixed it
Nothing broke during the final run. The program correctly evaluates each rule in order and stops at the first failed requirement.

## Status
Complete
