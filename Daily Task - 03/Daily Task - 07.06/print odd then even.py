def rearrange_digits(N):
    Num_str = str(N)
    odd = []
    even = []
    for digit in Num_str:
        num = int(digit)
        if num % 2 != 0:
            odd.append(digit)
        else:
            even.append(digit)
    result = ''.join(odd + even)
    print(result)
N = int(input("Enter a number: "))
rearrange_digits(N)