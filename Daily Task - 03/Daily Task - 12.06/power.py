num=3
pow=5
def power(pow):
    if pow == 1:
        return num
    else:
        return num*power(pow-1)
    
print(power(pow))