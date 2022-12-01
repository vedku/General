from random import randint
from time import sleep
while True:
    operation_choice = input("Would you like to practice\naddition [+]\nsubraction [-]\nmultiplication [*]\ndivision [/]\nindices[**]\nInput:")
    digit_choice = int(input("What is the maximum amount of digits you want to work with?\nInput:"))
    difficulty = int(input("How many seconds of calculation would you like to allow yourself before the answer is displayed?\nInput:"))
    range_end = (10 ** digit_choice) - 1
    num1 = str(randint(1, range_end))
    num2 = str(randint(1, range_end))
    question=(num1+operation_choice+num2)
    print(question)
    sleep(difficulty)
    print(eval(question))
    proceed = input("Would you like to continue?:")
    if proceed == "no" or proceed == "No" or proceed == "n" or proceed == "N":
        break
    else:
        print("====================================================")
