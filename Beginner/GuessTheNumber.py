import os
import GuessArt
import random

def game():
    
    print(GuessArt.logo)

    guess_number = random.randint(1, 100)

    ask_continue = ("Play again? Type 'y' or 'n':")

    def change_lives(User_difficulty):
        if User_difficulty == "hard":
            return Lives + 5
        if User_difficulty == "easy":
            return Lives + 10

    def check_guess(guess):
        if guess == guess_number:
            return 1
        if guess > guess_number:
            return 2
        if guess < guess_number:
            return 3
            

    # of lives
    Lives = 0

    difficulty = input("Welcome to the Number Guessing Game! \nI am thinking of a number between 1 and 100. \nChoose the difficulty. Type 'Easy' or 'Hard': ").lower()

    Lives = change_lives(difficulty)

    print(f"You chose {difficulty}. Lets begin")

    while Lives > 0:

        user_guess = int(input("Make a guess:"))

        if check_guess(user_guess) == 1:
            print(f"You Win! The number was {guess_number}")
            if input(ask_continue) == "y":
                game()
                os.system("cls")
        elif check_guess(user_guess) == 2:
            print("Guess is too high!")
            Lives -= 1
            print(f"You have {Lives} attempts left")
        else:
            print(f"Guess is too low!")
            Lives -= 1
            print(f"You have {Lives} attempts left")
    
    print("Game Over!")
    if input(ask_continue) == "y":
                game()
                os.system("cls")

game()