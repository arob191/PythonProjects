target = int(input())
SumEvenNumbers = 0
for n in range(1, target + 1):
    if n % 2 == 0:
        SumEvenNumbers += n

# A more efficient way of looking for even number is to have the range start at 2 and skip every other number 
# for number in range(2, target + 1, 2) The 2 at the end tells the range to skip every other number.

print(f"The sum for all the even numbers is {SumEvenNumbers}")