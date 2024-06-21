n=int(input("Enter the Number : "))
arr1=[]
def count_repeat(n,arr1):
    Value=n%10
    if Value>0:
        arr1.append(Value)
    num=n//10
    if n>0:
        return count_repeat(num,arr1)
count_repeat(n,arr1)
arr2=[]
count=0
for i in arr1:
    if i not in arr2:
        arr2.append(i)
print(arr2)
for j in arr2:
    count=0
    for s in arr1:
        if s==j:
            count=count+1
    print(j," = ",count)