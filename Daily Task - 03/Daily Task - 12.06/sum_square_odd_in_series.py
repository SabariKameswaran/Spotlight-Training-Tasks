num = int(input())
def odd_series(num):
    sq = 0
    for i in range(1, num + 1):
        if i % 2 != 0:
            sq += i**2
    return sq
print(odd_series(num))