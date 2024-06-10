n=int(input())
arr1 = list(map(int,input().split()))
# arr2 =[]
def array_manipulation(arr1):
    rev = 0
    for i in range(0,n-1):
        if arr1[i] == 0:
            del arr1[i]
        while i>0:
            r=n%10
            if r == 0:
                del arr1[i]
    print(arr1)

array_manipulation(arr1)