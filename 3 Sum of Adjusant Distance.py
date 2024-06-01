size = 5
arr = [10, 11, 7, 12, 14]
total_distance = 0
for i in range(1, size):
        total_distance += abs(arr[i] - arr[i - 1])

print(total_distance)