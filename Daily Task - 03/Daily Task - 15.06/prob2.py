def generate_series_a():
    A = []
    a=int(input("Start value:"))
    increment=int(input("Increment:"))
    while a <= 50:
        A.append(a)
        a += increment
        increment += 1
    return A

def generate_sequence_b():
    start = int(input("Enter the Start Digit:"))
    length = int(input("Enter the length"))
    sequence = []
    for i in range(start, start + length):
        number_str = str(i) + str(i + 1) + str(i + 2)
        number = int(number_str)
        sequence.append(number)
    return sequence


print(generate_series_a())
print(generate_sequence_b())
