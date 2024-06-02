N = int(input())
K = int(input())
prices = list(map(int, input().split()))
lucky_customers = 0
for i in range(N):
    for j in range(i + 1, N):
        if abs(prices[i] - prices[j]) == K:
            lucky_customers += 1
print(lucky_customers)