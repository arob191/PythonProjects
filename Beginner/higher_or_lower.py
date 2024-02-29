import os
import random
import higher_or_lower_art
import higher_or_lower_data


# First we need to print the logo 
print(higher_or_lower_art.logo)

# We need to randomly select two people and assign them person 1 and person 2

def set_person():
    return random.choice(higher_or_lower_data.data)

person1 = set_person()
person2 = set_person()

print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")

# Next we need to provide a comparison line the shows the first random person vs the second random person

# We need to ask the user which one has more followers

# We need to dermine who has more followers

# We need to compare the answer of the user to the randomly selected people

# If the user answer is wrong we need end the game

# If the user answer is right we continue and retrieve two more random people

