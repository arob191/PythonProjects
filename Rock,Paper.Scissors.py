rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

# This turns the user input into an integer
user_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))

# This will turn the rock, paper, and the scissors variable into a list
game_image = [rock, paper, scissors]

# This checks to make sure that the user typed something between 0 and 2
if user_selection > 2 or user_selection < 0:
    print("Not an option, you lose")
else:
    print(f"You chose {game_image[user_selection]}")

# This creates the randomly generated number for the computer to use
    bot_selection = random.randint(0, 2)

    print("Computer chose:")

# This picks out the variable to print based on the random number the computer chose and the index number in the list
    print(game_image[bot_selection])

    if user_selection == 0 and bot_selection == 2:
        print("You Win")
    elif bot_selection > user_selection:
        print("You Lose")
    elif user_selection == 2 and bot_selection == 0:
        print("You Lose")
    elif user_selection > bot_selection:
        print("You Win")
    elif user_selection == bot_selection:
        print("Draw")
