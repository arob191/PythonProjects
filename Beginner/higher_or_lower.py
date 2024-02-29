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

# Next we need to provide a comparison line the shows the first random person vs the second random person

print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")
print(higher_or_lower_art.vs)
print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}")

# We need to ask the user which one has more followers

input("Who has more followers? 'A' or 'B': ").lower()

# We need to dermine who has more followers
def determine_higher(p1, p2):
    if p1 > p2:
        return p1
    else:
        return p2

print(determine_higher(person1['follower_count'], person2['follower_count']))
# We need to compare the answer of the user to the randomly selected people

# If the user answer is wrong we need end the game

# If the user answer is right we continue and retrieve two more random people

