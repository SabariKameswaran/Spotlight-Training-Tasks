n=int(input())
arr1 = list(map(int,input().split()))
def array_manipulation(arr1):
    length=len(arr1)
    if length == n:
        for num in arr1:
            if num == 0:
                arr1.remove(num)
            while num > 0 :
                rev = num % 10
                if rev == 0:
                    arr1.remove(num)
                num = num//10
        print(arr1)
        lenght1=len(arr1)
        if lenght1%2 == 0:
            mid3 = lenght1//2 - 1
            mid2 = lenght1//2
            even_mid=arr1[mid3]+arr1[mid2]
            even_mid /=2
            print(even_mid)
        else:
            mid1 = lenght1//2
            print(arr1[mid1])
    else:
        print("Enter the Correct size of the array")
array_manipulation(arr1)