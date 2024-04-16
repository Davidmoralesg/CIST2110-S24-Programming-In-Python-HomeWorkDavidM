# HW5.py
# Author:David Morales Gomez

# This homework assignment tests on list in python

# Question 1: Create a list with 5 of your favorite foods. Print the list
foods = ["Torda", "Burrito", "Burger", "Tamales", "Tacos"]
print(foods)
# Question 2: Using the list from question 1, print the first and last element of the list
print(foods[0:-1])
#the negative is the opposite like in reverse 

# Question 3: Using the list from question 1, print the 3rd element of the list
print(foods[2])

# Question 4: Using the list from question 1, print the 1st through 3rd elements of the list using list slicing
print(foods[0:3])

# Question 5: Using the list from question 1, print the last 2 elements of the list using list slicing
print(foods[-2:])
#In Python, list[-2:] is a slicing operation that extracts a sublist starting from the second-to-last element of the list up to the end of the list
# Question 6: Using the list from question 1, create a for each loop that prints each element of the list
for food in foods:
    print(food)

# Question 7: Using the list from question 1, create a for loop that prints each element of the list in reverse order
for i in range(len(foods)-1, -1, -1):
    print(foods[i])

# Question 8: Using the list from question 1, create a for loop that prints each element of the list and its index (hint use the enumerate() function)
for index, use in enumerate(foods):
    print(index, use)
# Question 9: Using this list of lists, print the first element of the second list (hint: use indexing)
foods = ["Torda", "Burrito", "Burger", "Tamales", "Tacos"]
print(foods[1][0])


# Question 10: Create a function that will take in a list and return the list in reverse order
# Hint: You can take in a list as a parameter and return a list
# You can not use the reverse() function
def reverse_list(foods):
    reversed_foods = []
    for i in range(len(foods)-1, -1, -1):
        reversed_foods.append(foods[i])
    return reversed_foods
foods = ["Torda", "Burrito", "Burger", "Tamales", "Tacos"]
reversed_foods = reverse_list(foods)
print(reversed_foods)


