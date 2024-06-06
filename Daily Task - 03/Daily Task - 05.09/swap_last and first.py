n=list(map(int,input().split()))
print(n)
temp=0
temp=n[0]
n[0]=n[-1]
n[-1]=temp
print(n)