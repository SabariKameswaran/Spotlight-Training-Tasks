def perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return sum
    
def perfect_num(limit):
    div=[]
    for i in range(1, limit+1):
        if perfect(i) != None:
            div.append(perfect(i))
    print(div)

perfect_num(100)