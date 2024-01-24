# The following code will take the input and change one of the items in the list to an “X”

# First create the "map" by creating three list and then creating the variable "map" as a list of those lists

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]

# Print the map out

print("     A    B     C")
print(f"1 {line1}")
print(f"2 {line1}")
print(f"3 {line1}")

# Ask for the users input (Example B3)

print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? \n") 

# Take the input of the first character and make it lowercase so it matches the items in the letter list. Then assign letter_index the index number that the input matches

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)

# Next take the second character and assign number that character as an integer

number = int(position[1])

# Now user number to pick which line list, then the letter_index to select the index of that line list, then change that item to an "X"

map[number -1][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")