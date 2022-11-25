#v2 will have division, multiplication, roots, powers and will be more practical with while loops
import time
from random import randint
def addition():
    difficulty = int(input("How many seconds of calculation would you like to allow yourself before the answer is displayed?\nInput:"))
    a_digit_choice = int(input("What is the maximum amount of digits you want to work with?\nInput:"))
    range_end = (10 ** a_digit_choice) - 1
    a1 = randint(1, range_end)
    a2 = randint(1, range_end)
    print(a1, "+", a2)
    ans = a1 + a2
    time.sleep(difficulty)
    print(ans)

def subtraction():
    difficulty = int(input("How many seconds of calculation would you like to allow yourself before the answer is displayed?\nInput:"))
    a_digit_choice = int(input("What is the maximum amount of digits you want to work with?\nInput:"))
    range_end = (10 ** a_digit_choice) - 1
    a1 = randint(1, range_end)
    a2 = randint(1, range_end)
    print(a1, "-", a2)
    ans = a1 - a2
    time.sleep(difficulty)
    print(ans)

operation_choice = input("Would you like to practice addition [1] or subraction [0]?\nInput:")
if operation_choice == "1":
    addition()
elif operation_choice == "0":
    subtraction()
