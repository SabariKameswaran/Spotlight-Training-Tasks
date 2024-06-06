def sorting_array(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):   
            temp = 0
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a

a =[1,7,3,9,5,8]
print(sorting_array(a))