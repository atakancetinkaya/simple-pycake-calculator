# ==============================================================================================
# Project: PyCake Calculator
# Pass-ID: X9448776
# Author: Atakan Çetinkaya
# Created: 29.05.2023
# Description: This ".py" (hello-calculator.py) simple Python-Script - calculating and greeting
# File Name: hello-calculator.py
# Version: v0.1
# Last Date Version edit: 29.05.2023
# ==============================================================================================

def greet(name):
    print("Hello, " + name + "!")


def add_numbers(a, b):
    return a + b


# Test the greet() function
name = input("Enter your name: ")
greet(name)

# Test the add_numbers() function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = add_numbers(num1, num2)
print("The sum is:", result)
