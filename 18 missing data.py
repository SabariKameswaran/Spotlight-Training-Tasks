stringSent, stringRec = input().split()
ascii_diff = 0
for char in stringSent:
    ascii_diff += ord(char)
for char in stringRec:
    ascii_diff -= ord(char)
missing_char = chr(ascii_diff)
print(missing_char)