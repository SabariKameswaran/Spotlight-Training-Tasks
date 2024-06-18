n=int(input())
def series(n):
    a=1
    for i in range(0,n):
        a=(i*i*i)+1
        print(a,end=" ")

series(n)