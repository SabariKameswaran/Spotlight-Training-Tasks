num = int(input())
count = 0
for i in range(5, num + 1, 5):
    count += num // i
print(count)