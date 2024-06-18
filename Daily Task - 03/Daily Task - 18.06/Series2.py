# Type 1
# n=int(input())
# def series(n):
#     a=1
#     b=1
#     while n>0:
#         print(a,end=" ")
#         a=b+a
#         b=b+1
#         n=n-1
# series(n)
# Type 2
n=int(input())
def series(n):
    a=1
    for i in range(1,n):
        print(a,end=" ")
        a=a+i

series(n)