num = int(input())
def new(num):
    count = 0
    for i in range(num + 1):
        num = i
        while num > 0:
            if num % 10 == 4:
                count += 1
            num //= 10
    return count
print(new(num))