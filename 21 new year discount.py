bill_amount = int(input())
discount = 0
for digit in str(bill_amount):
    digit = int(digit)
    if digit % 2 != 0:
        discount += digit
print(discount)