import random

play = "yes"

while play in ["yes","Yes","YES"]:
    player = input("\nRock, Paper Or Scissors?:")
    opponent = ["I chose Rock","I chose Paper","I chose Scissors"]
    opponentsaid = random.choice(opponent)
    if player in ["Rock", "rock"]:
        print(opponentsaid)
        if opponentsaid in ["I chose Rock"]:
            print("Draw!")
        elif opponentsaid in ["I chose Scissors"]:
            print("You Won")
        else:
            print("You Lost")
    if player in ["Paper", "paper"]:
        print(opponentsaid)
        if opponentsaid in ["I chose Paper"]:
            print("Draw!")
        elif opponentsaid in ["I chose Rock"]:
            print("You Won!")
        else:
            print("You Lost")
    if player in ["Scissors", "scissors"]:
        print(opponentsaid)
        if opponentsaid in ["I chose Scissors"]:
            print("Draw!")
        elif opponentsaid in ["I chose Paper"]:
            print("You Won!")
        else:
            print("You Lost")
    play = input("Do you wanna play again?:")
