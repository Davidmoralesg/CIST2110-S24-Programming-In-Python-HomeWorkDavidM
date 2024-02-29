# HW3.py
# Author:David Morales Gomez

# This Homework assignment is meant to test your ability to make functions within python as well as importing and using modules. This assignment might require you to do some research on your own. If you get stuck, try googling the problem, especially when it comes to importing and using the different modules.

# Hint you will want to enable word wrap in vscode (View -> Toggle Word Wrap) to make it easier to read the instructions.


# Question 1:
# Write a function that takes in a number and returns that number squared
# IE. If the user inputs 3, the function should return 9
number = int(input("Enter a number: "))
def square_number(number: int) -> int:
    """Input number and return the number squared
     Args:
        number (int): [description]
    Returns:
        int: [description]
    """
    return number ** 2

print(square_number(3))

# Question 2:
# Write a function that takes in a string, a letter, and a number and returns the string with the letter replaced at the number index
# IE. If the user inputs "Hello World", "a", and 3, the function should return "Helao World"
# Hint: You will want to use the replace() function
def replace_letter_at_index(input_string: str, letter: str, index: int) -> str:
    if index < 0 or index >= len(input_string):
        return "Index out of range"
    else:
        return input_string[:index] + letter + input_string[index+1:]

result = replace_letter_at_index("Hello World", "a", 3)
print(result)



# Question 3:
# Write a function that takes in a number, a lower_bound, and an upper_bound and returns whether the number is within the bounds
# IE. If the user inputs 5, 1, and 10, the function should return True
function = int(input("Enter a number: "))
lower_bound = int(input("Enter a lower bound: "))
upper_bound = int(input("Enter an upper bound: "))
def number_within_bounds(num: int, lower_bound: int, upper_bound: int) -> bool:
    """takes in a number, a lower_bound, and an upper_bound and returns whether the number is within the bounds
     Args:
        num (int): number
        lower_bound_param (int): lower bound
        upper_bound (int): upper bound
    Returns:
        bool: True or False
    """
    return lower_bound <= num <= upper_bound
print(number_within_bounds(function, lower_bound, upper_bound))



# Question 4:
# write a function with parameters for a name, age, and favorite color. Return the following string using the parameters:
# "Hello, my name is <name>. I am <age> years old. My favorite color is <color>."

# Question 5:
# Write a function that asks the user for their name, age, and favorite color and then calls the function from question 4 using the user's input as the parameters.
# Hint: You will want to save the users input to variables and use them as the parameters for the function from question 4

# Question 6:
# import the random module and use it to generate a random number between 1 and 100
import random

random_number = random.randint(1, 100)
print(random_number)

# Question 7:
# import the math module and use it to find the square root of 16 (hint: use the sqrt() function)
import math
square_number = math.sqrt(16)
print(square_number)

# Question 8:
# import the sys module and use it to print the version of python you are using
# this time import the module using the import "as" keyword
# hint: use the version attribute (sys.version)
import sys as system
print(system.version)



# Question 9:
# import the os module and use it to print the current working directory. This time import the module using the from keyword
# hint: use the getcwd() function
import os
cwd = os.getcwd()  
"""Prints the current working directory""" 
print("Current working directory:", cwd)  

