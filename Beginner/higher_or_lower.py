import os
import random
import higher_or_lower_art
import higher_or_lower_data


# First we need to print the logo 
print(higher_or_lower_art.logo)

# We need to randomly select two people and assign them person 1 and person 2


def set_person():
    return random.choice(higher_or_lower_data.data)

def set_user_geuss(guess, p1, p2):
    if guess == "a":
        return p1['follower_count']
    else:
        return p2['follower_count']

def determine_higher(p1, p2):
    if p1['follower_count'] > p2['follower_count']:
        return p1['follower_count']
    else:
        return p2['follower_count']

def compare_answer(higher, guess, score, lives):
    if higher == guess:
        return 1
    else:
        print(f"Game Over! Score: {score}")
        return lives - 1

def game():
    
    score = 0
    lives = 1

    while lives != 0:

        person1 = set_person()
        person2 = set_person()

        print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")
        print(higher_or_lower_art.vs)
        print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}")

        guess = input("Who has more followers? 'A' or 'B': ").lower()

        higher = determine_higher(person1, person2)

        user_guess = set_user_geuss(guess, person1, person2)

        lives = compare_answer(higher, user_guess, score, lives)

        if lives == 1:
            score + 1
    
    if input("Play again? Type 'y' or 'n': ").lower() == 'y':
        os.system('cls')
        game()
    else:
        return

game()