import random

choices = ["rock", "paper", "scissors"]

print("+==============WELCOME TO STONE, PAPER, SCISSORS GAME===============+ ")

play = input("\nDo you want to play? [yes/no] : ").lower()

while play == 'yes' or play == 'y' :

    computer_choice = random.choice(choices)

    user_choice = (input("\nEnter your choice [rock, paper, scissors] : "))
    user_choice = user_choice.lower()

    while user_choice not in choices :

        print("\nPlease select valid choice [rock, paper, scissors]")

        user_choice = (input("\nEnter your choice [rock, paper, scissors] : "))
        user_choice = user_choice.lower()

    print("\nComputer chose :",computer_choice)

    if computer_choice == user_choice :

        print("\nIt's a Tie...")

    elif (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors") or (computer_choice == "scissors" and user_choice == "rock") :

        print("\nYou WON the round!")

    else :

            print("\nOops! You LOST")

    play = input("\nDo you want to play again? [yes/no] : ").lower()

print("+================THANK YOU=================+")

    




