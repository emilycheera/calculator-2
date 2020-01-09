"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

def greeting_and_instructions():
    """Greets users and provides instructions on how to use calculator"""
    print("Welcome to calculator!")
    print("To use the calculator, follow these instructions:")
    print("""
        To add two numbers, enter: + num1 num2
        To subtract num2 from num1, enter: - num1 num2
        To multiply two numbers, enter: * num1 num2
        To divide num1 by num2, enter: / num1 num2
        To find the square of a num, enter: square num
        To find the cube of a num, enter: cube num
        To raise num1 to the power of num2, enter: pow num1 num2
        To find the remainder of num1 divided by num2, enter: mod num1 num2
        To quit the program, enter: q
        """)

def get_user_input():
    """Gets calculator input from user."""

    user_input = input("> ")
    
    return user_input


def tokenize_user_input():
    """Convert user input string into list"""

    user_input_2 = get_user_input()
    user_input_2 = user_input_2.split()
    
    takes_1_argument = ["square", "cube"]
    takes_2_arguments = ["+", "-", "*", "/", "pow", "mod"]

    if user_input_2[0] == "q":
        return user_input_2
    elif user_input_2[0] in takes_1_argument:
        if len(user_input_2) != 2:
            print("Please check your syntax.")
            interpret_user_input()
        else:
            return user_input_2
            print(user_input_2)
    elif user_input_2[0] in takes_2_arguments:
        if len(user_input_2) != 3:
            print("Please check your syntax.")
            interpret_user_input()
        else:
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
        user_input_4 = update_type_of_user_input()
        first_argument = user_input_4[0]
        
        if len(user_input_4) > 1:
            second_argument = user_input_4[1]
            if len(user_input_4) == 3:
                third_argument = user_input_4[2]
        
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


greeting_and_instructions() # call function to print greeting/instructions
interpret_user_input() # call function to start calculator program
