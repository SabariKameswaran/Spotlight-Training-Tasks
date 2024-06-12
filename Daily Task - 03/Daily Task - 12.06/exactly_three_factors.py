n=int(input())
def factors(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    result = []
    for num in range(1, n + 1):
        if num <= 1:
            continue
        for i in range(2, num):
            if i * i == num and is_prime(i):
                result.append(num)
                break
    return result

print(factors(n))