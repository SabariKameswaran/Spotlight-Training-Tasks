num = int(input())
numbers = list(map(int, input().split()))
evens = []
odds = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)
result = evens + odds
for number in result:
    print(number, end=' ')