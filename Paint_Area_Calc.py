import math

def paint_calc(height, width, cover):  
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You will need {number_of_cans} paint cans")

test_h = int(input("Provide Height ")) # Height of wall (m)
test_w = int(input("Provide Width ")) # Width of wall (m)
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)