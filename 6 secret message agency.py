message = input()
count = 0
for char in message:
    if not char.isalnum():
        count += 1
print(count)
