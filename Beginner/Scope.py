enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()

print(f"enemies outside function: {enemies}")

# There is no Block Scope

game_level = 3
def create_enemy():
    enemies = ["Seleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

#Global Constant

pi = 3.14159

URL = "https://austinrulerobertson.com"
