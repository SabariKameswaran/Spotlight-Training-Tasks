arr1=[num for num in map(int, input().split()) if num > 0]
def array_manipulation(arr1):
    arr1.sort()
    if len(arr1) == 0:
        return "none" 
    elif len(arr1)%2==0:
        return (arr1[len(arr1)//2-1]+arr1[len(arr1)//2])/2
    else:
        return arr1[len(arr1)//2]
print(array_manipulation(arr1))