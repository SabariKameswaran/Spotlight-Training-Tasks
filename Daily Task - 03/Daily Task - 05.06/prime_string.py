def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return "It is not Prime"
    return "It is Prime"

number = int(input("Enter a number: "))
print(is_prime(number))