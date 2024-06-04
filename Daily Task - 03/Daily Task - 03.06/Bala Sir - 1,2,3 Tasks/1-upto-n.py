# base_num=0
# def print_upto_n(n):
#     if n>0:
#         base_num+=1
#         print(base_num)
#         if base_num == n:
#             return "End is reached"
#         else : 
#             print_upto_n(n)
# n=10
# print_upto_n(n)

def array_sorting(n):
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[i] > n[j]:
                temp = n[i]
                n[i] = n[j]
                n[j] = temp