num, start, end = map(int, input().split())
distances = list(map(int, input().split()))
result = []
for distance in distances:
    if start <= distance <= end:
        result.append(distance)
print(result)