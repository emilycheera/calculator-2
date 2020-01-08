"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here


# get user input
def get_user_input():
    user_input = input("> ")
    return user_input

# tokenize user input
def tokenize_user_input():
    user_input_2 = get_user_input()
    user_input_2 = user_input_2.split()
    return user_input_2

# create a quit function
# interpret which arithemtic function to use
# call appropriate function from arithmetic.py using 2nd/3rd arguments
