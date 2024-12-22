print("Prime numbers between 1 and 100:")

for num in range(2, 101):  # Start from 2 as 1 is not a prime number
    is_prime = True
    for i in range(2, num):
        if num % i == 0:  # If divisible, mark as not prime
            is_prime = False
    if is_prime:
        print(num, end=" ")