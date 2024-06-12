def sum_dig(num):
    #For one num Adding one digit and another
    # if num < 10:
    #     return num
    #Adding Series of Numbers
    if num == 1:
        return 1
    else:
        #For one num Adding one digit and another
        # return num % 10 + sum_dig(num // 10)
        #Adding series of numbers
        return num + sum_dig(num-1) 
n=10
print(sum_dig(n))