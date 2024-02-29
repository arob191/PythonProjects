import os
import GuessArt
import random

def check_guess(guess, answer, lives):
        if guess == answer:
            print(f"You Win! The number was {answer}")
        if guess > answer:
            print("Guess is too high!")
            return lives - 1
        if guess < answer:
            print(f"Guess is too low!")
            return lives - 1

def change_lives(user_difficulty):
        if user_difficulty == "hard":
            print("You chose hard! Lets begin")
            return 5
        if user_difficulty == "easy":
            print("You chose easy! Lets begin")
            return 10

def game():
    
    print(GuessArt.logo)

    guess_number = random.randint(1, 100)

    ask_continue = ("Play again? Type 'y' or 'n':")

    user_guess = 0

    difficulty = input("Welcome to the Number Guessing Game! \nI am thinking of a number between 1 and 100. \nChoose the difficulty. Type 'Easy' or 'Hard': ").lower()

    lives = change_lives(difficulty)

    while lives > 0 & user_guess != guess_number:

        print(f"You have {lives} attempts left")
        user_guess = int(input("Make a guess:"))
        lives = check_guess(user_guess, guess_number, lives) 
    
    print("Game Over!")
    if input(ask_continue) == "y":
                game()
                os.system("cls")
                
    return

game()