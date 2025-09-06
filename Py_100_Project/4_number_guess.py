import random

def number_guessing_game():
    """
    A simple number guessing game where the user tries to guess a randomly
    generated number between 1 and 100. The user receives feedback if their 
    guess is too low or too high, and the game continues until the correct 
    number is guessed. The number of attempts is displayed upon correctly 
    guessing the number.
    """

    number = random.randint(1, 100)
    attempts = 0

    print("Guess a number between 1 and 100:")
    while True:
        guess = int(input("Enter your guess:"))
        attempts += 1
        if guess<number:
            print("Too low")
        elif guess>number:
            print("Too high")
        else:
            print(f"Congratulations!, you found the number in {attempts} attempts")
            break

number_guessing_game()


#Tags:
#module - random
# function - number_guessing_game
# variable - number, attempts, guess
# data type - int, str, bool
# control structure - while loop