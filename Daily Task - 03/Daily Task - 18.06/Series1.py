# #10 1 9 2 8 3 7 4 6 5 5 6 4 7 3 8 2 9  1 10
a=10
b=1
n=int(input())
def series(n):
    a=10
    b=1
    while n>0:
        print(a,end=" ")
        print(b,end=" ")
        a=a-1
        b=b+1
        n=n-1
series(n)