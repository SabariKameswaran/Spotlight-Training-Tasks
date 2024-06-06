def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)
    
def sum_fact(num):
    sum = 0
    while num > 0:
        sum = sum+(fact(num)/num)
        num=num-1
    return sum

num=int(input("Enter a number:"))
factorial = fact(num)
print("The factorial is:",fact(num))
sum_factorial = sum_fact(num)
print("The Sum of Factorial and Divide is:",sum_fact(num))
