arr1=list(map(int,input("Enter your Array:").split()))
n=len(arr1)
new=[]
def array_manipulation(arr1):
    length=len(arr1)
    print(length)
    for num in arr1:
        if num > 0:
            new.append[num]
    lenght1=len(new)
    arr1.sort()
    if lenght1 == 0:
        print("None")
    else:
        if lenght1%2 == 0:
            mid3 = lenght1//2 - 1
            mid2 = lenght1//2
            even_mid=new[mid3]+new[mid2]
            even_mid /=2
            print(even_mid)
        else:
            mid1 = lenght1//2
            print(new[mid1])

array_manipulation(arr1)       