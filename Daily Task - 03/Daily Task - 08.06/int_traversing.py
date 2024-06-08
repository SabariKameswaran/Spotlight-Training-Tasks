number = int(input())
evens = 0
odds = 0
def print_even_and_odd(numbers):
    while numbers > 0:
        digit = numbers % 10
        if digit % 2 == 0:
            evens.append(digit)
            
        else:
            odds.append(digit)
    def sort_odd(inp):
        for i in range(len(inp)):
            for j in range(i+1,len(inp)):
                temp = 0
                if inp[i] > inp[j]:
                    temp=inp[i]
                    inp[i]=inp[j]
                    inp[j]=temp
    sort_odd(numbers)
    sort_odd(evens)
    for s in numbers:
        evens.append(s)
    print(int(evens))

print_even_and_odd(number)