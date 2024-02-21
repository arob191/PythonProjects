import random
import my_module

# random_integer = random.randint(1, 1000)
# print(random_integer)

print(my_module.pi)

# random_float = random.random(1, 10)
# print(random_float)

random_side = random.randint(0, 1)

if random_side == 1:
    print("Heads")
else:
    print("Tails")