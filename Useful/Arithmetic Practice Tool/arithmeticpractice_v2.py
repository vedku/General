#v3 will have indices, roots and continuation with line breaks
import time
from random import randint
def addition():
    difficulty = int(input("How many seconds of calculation would you like to allow yourself before the answer is displayed?\nInput:"))
    digit_choice = int(input("What is the maximum amount of digits you want to work with?\nInput:"))
    range_end = (10 ** digit_choice) - 1
    a1 = randint(1, range_end)
    a2 = randint(1, range_end)
    print(a1, "+", a2)
    ans = a1 + a2
    time.sleep(difficulty)
    print(ans)

def subtraction():
    difficulty = int(input("How many seconds of calculation would you like to allow yourself before the answer is displayed?\nInput:"))
    digit_choice = int(input("What is the maximum amount of digits you want to work with?\nInput:"))
    range_end = (10 ** digit_choice) - 1
    a1 = randint(1, range_end)
    a2 = randint(1, range_end)
    print(a1, "-", a2)
    ans = a1 - a2
    time.sleep(difficulty)
    print(ans)

def multiplication():
    difficulty = int(input("How many seconds of calculation would you like to allow yourself before the answer is displayed?\nInput:"))
    digit_choice = int(input("What is the maximum amount of digits you want to work with?\nInput:"))
    range_end = (10 ** digit_choice) - 1
    a1 = randint(1, range_end)
    a2 = randint(1, range_end)
    print(a1, "x", a2)
    ans = a1*a2
    time.sleep(difficulty)
    print(ans)

def division():
    difficulty = int(input("How many seconds of calculation would you like to allow yourself before the answer is displayed?\nInput:"))
    digit_choice = int(input("What is the maximum amount of digits you want to work with?\nInput:"))
    range_end = (10 ** digit_choice) - 1
    a1 = randint(1, range_end)
    a2 = randint(1, range_end)
    print(a1, "/", a2)
    ans = a1 / a2
    time.sleep(difficulty)
    print(ans)

#using multiple factors (capital and lowercase letters)
#for the function to run made them run chronologically
#so I replaced the initials with numbers to avoid confusion
operation_choice = input("Would you like to practice\naddition [1]\nsubraction [2]\nmultiplication [3]\ndivision [4]?\nInput:")
if operation_choice == "1":
    addition()
if operation_choice == "2":
    subtraction()
if operation_choice == "3":
    multiplication()
if operation_choice == "4":
    division()
