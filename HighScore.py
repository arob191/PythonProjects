# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
MaxScore = None
for n in student_scores:
  if MaxScore is None or n > MaxScore: MaxScore = n

print(f"The High Score is {MaxScore}")