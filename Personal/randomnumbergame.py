import random
number = random.randint(1,10)
guess = [11]
guesses = 0
#print(number)
# number = 3
while guess != number:
    try:
        guess = int(input("\n\nGuess what number I'm thinking of. It's between 1 and 10. You have 3 guesses so use them wisely \n input here:"))
    except:
        print("That is not an acceptable number")
        continue
    if guess == number:
        print("\n\nHooray! You got it correct")
    elif guesses >= 2:
        print("\n\nSorry you are out of guesses. The number was", number,)
        break
    elif guess not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print("\n\nThat isn't within the range of 1-10. Try again")

    elif guess > number:
        print("\n\nNope, your guess is too high")
        guesses = guesses+1
    elif guess < number:
        print("\n\nSorry, your guess is too low")
        guesses = guesses+1
