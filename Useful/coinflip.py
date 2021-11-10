import random

def coin_flip():

    random_choice = random.randint(1,2)

    user_input = ""

    if random_choice == 1:

        random_choice = "Heads"

    else:

        random_choice = "Tails"

    while user_input != "Heads" or user_input != "Tails":

        user_input = input("Heads or Tails?")

    if user_input == random_choice:

        print("Congratulations!", "The result was", random_choice, " and you guess correctly!")

    else:

        print("Bad luck!", "The result was", random_choice, " and you guessed incorrectly.")
