def Fibonacci_with_Recursion(num):
    if num>0:
        return (Fibonacci_with_Recursion(num-1)+Fibonacci_with_Recursion(num-2))
    else:
        return 1
num=5
for i in range(num):
    print(Fibonacci_with_Recursion(i))
Fibonacci_with_Recursion(num)