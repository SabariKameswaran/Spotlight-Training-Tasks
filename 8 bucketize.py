item_id = input()
max_digit = 0
for char in item_id:
    digit = int(char)
    if digit > max_digit:
        max_digit = digit
print(max_digit)
