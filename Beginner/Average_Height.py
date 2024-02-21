# Input a Python list of student heights
heights = input("Give the hights or students in CM \n")
student_heights = heights.split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
# Adding up all the individual heights
tt_heights = 0
for height in student_heights:
  tt_heights += height
print(f"Total height = {tt_heights}")

# Adding up the number of students
num_students = 0
for num in student_heights:
  num_students += 1
print(f"Total number of students = {num_students}")

# Calculating the average height
print(round(tt_heights / num_students))