def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Number is Prime")
    else:
        print("Number is not prime")

n = int(input("Provide a number"))
prime_checker(number=n)