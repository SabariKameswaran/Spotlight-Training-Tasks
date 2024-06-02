num_cards = int(input())
cards = list(map(int, input().split()))
max_val = float('-inf')
second_max_val = float('-inf')
for val in cards:
    if val > max_val:
        second_max_val = max_val
        max_val = val
    elif val > second_max_val:
        second_max_val = val
winning_amount = max_val * second_max_val
print(winning_amount)