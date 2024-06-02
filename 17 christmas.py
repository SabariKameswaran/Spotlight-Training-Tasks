bill_amount = input().strip()
sum_odd = 0
sum_even = 0
for char in bill_amount:
    digit = int(char)
    if digit % 2 == 0:
        sum_even += digit
    else:
        sum_odd += digit
discount_amount = sum_odd * sum_even
print(discount_amount)