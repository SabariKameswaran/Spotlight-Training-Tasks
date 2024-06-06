n=list(map(str,input().split()))
print(n)

# b = str(input("Enter a Letter:"))

# for i in range(0,len(a)):
#     c = chr(a)
#     if b == a:
#         print(a[b])
#     else:
#         print("Wrong")
for i in range(len(n)):
    if i in n:
        print(n[i])