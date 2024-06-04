def sorting_array(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):   
            temp = 0
            if a[i] > a[j]:
                #Method 1
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
                #Method 2
                # a[i]= a[i]+a[j]
                # a[j] = a[i] - a[j]
                # a[i] = a[i] - a[j]
                #Method 3
                #a[i], a[j] = a[j], a[i]
    return a

a =[1,7,3,9,5,8]
print(sorting_array(a))