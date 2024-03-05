# Project1.py
# Author: David Morales Gomez
import sys

# This project is meant to test your ability from everything we have learned so far in class
# You will need to use variables, if statements, loops, and functions

# Quiz Game: 
# Create a simple console-based quiz game where the user answers a series of questions.
# The game should keep track of the user's score and provide feedback based on the answers given.

# Write a function that displays a welcome message to the user and explains the rules of the game

# Implement at least 5 questions, each with 4 answer options (a, b, c, d). Each question should be worth 1 point.
# For each question, display the question and the answer options to the user.
# Use input() to get the user's answer.
# Use if or if-else statements to check if the answer is correct.
# If the answer is correct, display a positive feedback message and add points to the user's score.
# If the answer is incorrect, display a negative feedback message and provide the correct answer.
# Score Tracking:

# Keep track of the user's score throughout the game.
# After all questions have been answered, display the user's total score and a farewell message.
# Function Utilization:

# Create a function to ask a question and check the answer. This function should accept parameters like the question, options, the correct answer, and return whether the user was correct.
# an example would be def ask_question(question:str, option_1:str, option_2:str, option_3,:str option_4:str, correct_answer:str)->bool:
# the return value should be a boolean (True or False) for whether the user was correct

# Create a function to display the final score, which takes the score as a parameter and displays a message.
# Loops:
# Use a for or while loop to iterate through the questions.
# Variable Casting:
# Ensure that user input is cast and checked appropriately to avoid errors during execution.
# Error Handling:
# Implement basic error handling to manage invalid inputs from the user (e.g., an answer other than a, b, c, or d).


input("Welcome to the quiz game! Press enter to start the game")
input_value = input("This quiz game is about simple knowledge, for example: how many sides does a triangle have?")

def ask_question(question:str, option_1:str, option_2:str, option_3:str, option_4:str, correct_answer:str):
    print(question)
    print(option_1)
    print(option_2)
    print(option_3)
    print(option_4)
    user_answer = input("Please enter your answer: ")
    while user_answer.lower() not in ['a', 'b', 'c', 'd']:
        print("Invalid input. Please enter a, b, c, or d.")
        user_answer = input("Please enter your answer: ")
  
    return user_answer.lower() == correct_answer.lower()

score = 0




input_question1 = input("Question 1: How many sides does a square have? \n a) 3 \n b) 4 \n c) 5 \n d) 6 \n")

if input_question1.lower() == "b":
    print("Correct! The answer is 4")
    score += 1
else:
    print("Incorrect! The answer is 4")

if input_question1.lower() not in ['a', 'b', 'c', 'd']:
    print("Invalid input. Please enter a, b, c, or d.")
    input_question1 = input("Please enter your answer: ")

print("Your score is:", score)

#dont rewrite print = input_question1
#print = input_question1




input_question2 = input(str("Question 2: When driving, what gear should the car be in? \n a) Park \n b) Reverse \n c) Neutral \n d) Drive \n"))
if input_question2.lower() == "d":
    print("Correct! The answer is Drive")
    score += 1
else:
    print("Incorrect! The answer is Drive")
if input_question2.lower() not in ['a', 'b', 'c', 'd']:
    print("Invalid input. Please enter a, b, c, or d.")
    input_question2 = input("Please enter your answer: ")    


print("Your score is:", score)
    


input_question3= input(str("Question 3: When reversing, what gear should the car be in? \n a) Park \n b) Reverse \n c) Neutral \n d) Drive \n"))
if input_question3.lower() == "b":
    print("Correct! The answer is Drive")
    score += 1
else:
    print("Incorrect! The answer is Drive")
if input_question3.lower() not in ['a', 'b', 'c', 'd']:
    print("Invalid input. Please enter a, b, c, or d.")
    input_question3 = input("Please enter your answer: ")
    
print("Your score is:", score)
    





intput_question4 = input(str("Question 4: What is the capital of the United States? \n a) New York \n b) Washington D.C. \n c) Los Angeles \n d) Miami \n"))
if intput_question4.lower() == "b":
    print("Correct! The answer is Washington D.C.")
    score += 1
else:
    print("Incorrect! The answer is Washington D.C.")
if intput_question4.lower() not in ['a', 'b', 'c', 'd']:
    print("Invalid input. Please enter a, b, c, or d.")
    intput_question4 = input("Please enter your answer: ")

print("Your score is:", score)
    





input_question5 = input(str("Question 5: What is the capital of Mexico? \n a) New York \n b) Washington D.C. \n c) Los Angeles \n d) Mexico City \n"))
if input_question5.lower() == "d":
    print("Correct! The answer is Mexico City")
    score += 1
else:
    print("Incorrect! The answer is Mexico City")
if input_question5.lower() not in ['a', 'b', 'c', 'd']:
    print("Invalid input. Please enter a, b, c, or d.")
    input_question5 = input("Please enter your answer: ")
    
print("Your score is:", score)

print("Your final score is:", score)
print("Thank you for playing the quiz game! Goodbye!")

sys.exit()

    
