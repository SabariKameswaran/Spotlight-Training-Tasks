def count_repeated_digits(data):
  data_str = str(data)
  digit_count = [0] * 10
  for digit in data_str:
    digit_count[int(digit)] += 1

  repeated_count = 0
  for count in digit_count:
    if count > 1:
      repeated_count += 1

  return -1 if repeated_count == 0 else repeated_count

data = int(input())
security_key = count_repeated_digits(data)
print(security_key) 