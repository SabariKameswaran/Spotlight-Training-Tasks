def is_armstrong(number):
    num = 0
    temp = number
    sum = 0
    while temp > 0:
        remainder = temp % 10
        sum += remainder ** num
        temp //= 10
       
    return number == sum

number = int(input())
if is_armstrong(number):
    print("Armstrong")
else:
    print("Not Armstrong")