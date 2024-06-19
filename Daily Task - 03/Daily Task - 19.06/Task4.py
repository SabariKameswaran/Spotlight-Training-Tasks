a=int(input())
b=int(input())
c=int(input())

# def large(a,b,c):
#     if a<b and a<c:
#         return b+c
#     elif b<a and b<c:
#         return a+c
#     else:
#         return a+b
    


def large(a,b,c):
    if (a>b and a>c) or (b>a and b>c):
        print(a+b)
    elif (b>a and b>c) or (c>b and c>a):
        print(b+c)
    else:
        print(a+c)
large(a,b,c)
