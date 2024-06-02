first_number, second_number = map(int, input().split())
smallest_prime = None
largest_prime = None
for number in range(first_number, second_number + 1):
    if number > 1:
        is_prime = True
        if number == 2 or number == 3:
            is_prime = True
        elif number % 2 == 0 or number % 3 == 0:
            is_prime = False
        else:
            i = 5
            while i * i <= number:
                if number % i == 0 or number % (i + 2) == 0:
                    is_prime = False
                    break
                i += 6
        if is_prime:
            if smallest_prime is None:
                smallest_prime = number
            largest_prime = number
if smallest_prime is not None and largest_prime is not None:
    otp = smallest_prime + largest_prime
    print(otp)
else:
    print("No primes in the given range")
