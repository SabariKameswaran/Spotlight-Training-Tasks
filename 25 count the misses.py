text_input = input()
miss_count = 0
for char in text_input:
    if not (char.isalnum() or char.isspace()):
        miss_count += 1
print(miss_count)