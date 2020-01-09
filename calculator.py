"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here



def get_user_input():
    """Gets calculator input from user."""

    user_input = input("> ")
    
    return user_input


def tokenize_user_input():
    """Convert user input string into list"""

    user_input_2 = get_user_input()
    user_input_2 = user_input_2.split()
    
    return user_input_2


def update_type_of_user_input():
    """Changes second and third indexes from strings to floats."""

    user_input_3 = tokenize_user_input()
    if len(user_input_3) > 1:
        user_input_3[1] = float(user_input_3[1])
        if len(user_input_3) == 3:
            user_input_3[2] = float(user_input_3[2])
   
    return user_input_3


def interpret_user_input():
    """Interprets user input and calls appropriate arithmetic function.

    Function will loop and continue to ask for user input until user inputs "q"
    """

    while True:
        user_input_3 = update_type_of_user_input()
        first_argument = user_input_3[0]
        
        if len(user_input_3) > 1:
            second_argument = user_input_3[1]
            if len(user_input_3) == 3:
                third_argument = user_input_3[2]
        
        if first_argument == "q":
            print("Quitting calculator.")
            break
        
        elif first_argument == "+":
            print(add(second_argument, third_argument))
        
        elif first_argument == "-":
            print(subtract(second_argument, third_argument))
        
        elif first_argument == "*":
            print(multiply(second_argument, third_argument))
        
        elif first_argument == "/":
            print(divide(second_argument, third_argument))
        
        elif first_argument == "square":
            print(square(second_argument))
        
        elif first_argument == "cube":
            print(cube(second_argument))
        
        elif first_argument == "pow":
            print(power(second_argument, third_argument))
        
        elif first_argument == "mod":
            print(mod(second_argument, third_argument))
        
        else:
            print("That's not a valid operator.")



interpret_user_input() # call function to start calculator program
