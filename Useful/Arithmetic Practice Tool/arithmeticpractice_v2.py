#v3 will have continuation with line breaks
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

def indices():
    #had to alter it because nobody is doing powers of hundreds in their head lolol
    difficulty = int(input("How many seconds of calculation would you like to allow yourself before the answer is displayed?\nInput:"))
    base_choice = int(input("What is the maximum amount of digits you want the base to be?\nInput:"))
    exponent_choice = int(input("What is the maximum amount of digits you want the exponent to be?\nInput:"))

    #calculating the amount of digits
    base_range_end = (10 ** base_choice) - 1
    exponent_range_end = (10 ** exponent_choice) - 1

    #randomly choosing a value from the range
    base = randint(1, base_range_end)
    exponent = randint(1, exponent_range_end)

    #user side calculation
    print(base, "^", exponent)
    ans = base**exponent
    time.sleep(difficulty)
    print(ans)

def roots():
    difficulty = int(input("How many seconds of calculation would you like to allow yourself before the answer is displayed?\nInput:"))
    base_choice = int(input("What is the maximum amount of digits you want the base to be?\nInput:"))
    root_choice = int(input("What is the maximum amount of digits you want the exponent to be?\nInput:"))

    # calculating the amount of digits
    base_range_end = (10 ** base_choice) - 1
    root_range_end = (10 ** root_choice) - 1

    # randomly choosing a value from the range
    base = randint(1, base_range_end)
    exponent = randint(1, root_range_end)

    # user side calculation
    print(exponent, "√", base)
    ans = base ** (1/exponent)
    time.sleep(difficulty)
    print(ans)


#using multiple factors (capital and lowercase letters)
#for the function to run made them run chronologically
#so I replaced the initials with numbers to avoid confusion
operation_choice = input("Would you like to practice\naddition [1]\nsubraction [2]\nmultiplication [3]\ndivision [4]?\nindices[5]\nroots[6]\nInput:")
if operation_choice == "1":
    addition()
if operation_choice == "2":
    subtraction()
if operation_choice == "3":
    multiplication()
if operation_choice == "4":
    division()
if operation_choice == "5":
    indices()
if operation_choice == "6":
    roots()
