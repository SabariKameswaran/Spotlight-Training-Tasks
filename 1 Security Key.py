data = 578378923
data_str = str(data)
digit_count = [0] * 10
for digit in data_str:
    digit_count[int(digit)] += 1

repeated_count = 0
for count in digit_count:
    if count > 1:
        repeated_count += 1

if repeated_count == 0:
    security_key = -1
else:
    security_key = repeated_count
    
print(security_key)