# Rock, paper, scissors game

import random

def rock_paper_scissors():
    """
    A game of rock-paper-scissors against the computer.

    Prompts the user for input of "rock," "paper," or "scissors,"
    generates a random choice for the computer, and then compares
    the two and prints out the result.

    Returns:
        None
    """
    choices = ["rock", "paper", "scissors"]
    user_choices = input("Enter rock, paper, or scissors: ").lower()
    computer_choices = random.choice(choices)

    print(f"You chose {user_choices}, computer chose {computer_choices}.")

    if user_choices == computer_choices:
        print("It's a tie!")
    elif user_choices == "rock" and computer_choices == "scissors":
        print("You win!")
    elif user_choices == "paper" and computer_choices == "rock":
        print("You win!")
    elif user_choices == "scissors" and computer_choices == "paper":
        print("You win!")
    else:
        print("You lose.")

rock_paper_scissors()