def largest_possible_number():
    n = int(input("Enter an integer: "))
    digits = list(str(n))
    count=0
    for i in range(len(digits)):
        max_idx = i
        for j in range(i + 1, len(digits)):
            if digits[j] > digits[max_idx]:
                max_idx = j
        digits[i], digits[max_idx] = digits[max_idx], digits[i]
        count +=1
    print(count)
largest_possible_number()