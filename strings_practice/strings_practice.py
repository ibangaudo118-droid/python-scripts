"""
Script: strings_practice.py
What it does: This script stores string values and demonstrates their conversion using .upper(), .lower(), and .strip(). It also demonstrates how to extract specific characters using indexing and slicing.
How to run: python strings_practice.py
Author: David Udoh
Date: 2026-10-26 
"""

full_name = "Udoh, David Jacob"
sentence = " David is my name and I love coding"

print(f'Full Name: {full_name}')
print(f'Sentence: {sentence}')
print(f'Character length in sentence: {len(sentence)}')

#converting full_name to uppercase
full_name = (full_name).upper()
print(full_name)
#converting full_name to lowercase
full_name = (full_name).lower()
print(full_name)
#removing space at the beginning of the sentence   
sentence = (sentence).strip()
print(sentence)
#demonstrating Indexing
print(full_name[0])
print(full_name[6])
#demonstrating slicing
print(full_name[6:11])
