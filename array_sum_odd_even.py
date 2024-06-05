arr1 = list(map(int,input("Enter the value of the Array: ").split()))
index1 = int(input("Enter the number of value that you need to print:"))
arr2 =[]
arr3=[]
def index_retrievel(index1):
    index2 = index1 - 1
    return arr1[index2]

def index_ev_odd(arr1):
    for i in range(0,len(arr1)):
        if arr1[i] % 2 == 0:
            arr2.append(arr1[i])
        else:
            arr3.append(arr1[i])
        
print("The value is:",index_retrievel(index1))
print(index_ev_odd(arr1))
print(arr2)
print(arr3)