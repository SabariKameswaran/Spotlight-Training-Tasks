#Method 1
#  numbers = list(map(int, input().split()))
# evens = []
# odds = []
# def print_even_and_odd(numbers):
#     for number in numbers:
#         if number % 2 == 0:
#             evens.append(number)
#         else:
#             odds.append(number)
#     def sort_odd(odds):
#         for i in range(len(odds)):
#             for j in range(i+1,len(odds)):
#                 temp = 0
#                 if odds[i] > odds[j]:
#                     temp=odds[i]
#                     odds[i]=odds[j]
#                     odds[j]=temp
#     sort_odd(odds)
#     sort_odd(evens)
#     # def sort_even(evens):
#     #     for i in range(len(evens)):
#     #         for j in range(i+1,len(evens)):
#     #             temp = 0
#     #             if evens[i] > evens[j]:
#     #                 temp=evens[i]
#     #                 evens[i]=evens[j]
#     #                 evens[j]=temp
#     # sort_even(evens)
#     for s in odds:
#         evens.append(s)
#     print(evens)

# print_even_and_odd(numbers)

#Array method with only one new list
numbers = list(map(int, input().split()))
evens = []
def print_even_and_odd(numbers):
    num = len(numbers)
    for k in range(0,num-1):
        if numbers[k] % 2 == 0:
            evens.append(numbers[k])
        else:
            numbers.append(numbers[k])
    del numbers[:num-1]
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
    print(evens)

print_even_and_odd(numbers)