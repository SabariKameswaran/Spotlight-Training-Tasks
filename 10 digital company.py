input_data = input().split()
character = input_data[0]
key = int(input_data[1])
if 'A' <= character <= 'Z':
    base = ord('A')
elif 'a' <= character <= 'z':
    base = ord('a')
encrypted_character = chr((ord(character) - base + key) % 26 + base)
print(encrypted_character)