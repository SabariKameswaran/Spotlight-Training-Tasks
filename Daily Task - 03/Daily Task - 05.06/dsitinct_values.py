arr1 = list(map(int,input().split()))
count = 0
distinct=[]
def print_only_distinct(arr1):
    for i in arr1:
        if arr1.count(i) == 1:
            distinct.append(i)
    print(distinct)
print_only_distinct(arr1)