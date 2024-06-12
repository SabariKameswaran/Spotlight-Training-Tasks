# def range_oe(num1):
#     if num1 == 1:
#         return 1
#     elif num1 % 2 == 0:
#         print("Even",num1)
#     else:
#         print("Odd",num1)
#     return range_oe(num1-1)
# num1=11
# range_oe(num1)

n1=10
n2=100
def odd(n1):
    if n1 == n2:
        return 1
    elif n1 < n2:
        if n1%2==0:
            print("Even",n1)
        else:
            print("Odd",n1)
    return odd(n1+1)
odd(n1)