target = int(input("Please type a whole number \n"))
for n in range(1, target +1):
    if n % 3 ==0 and n % 5 ==0:
        print("FizzBuzzz")
    elif n % 3 ==0:
        print("Fizz")
    elif n % 5 ==0:
        print("Buzz")
    else:
        print(f"{n}")
