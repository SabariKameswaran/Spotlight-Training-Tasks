n=int(input())
choice=int(input())
def option1(n,operator):
    result=0
    new=0
    new1=0
    for i in range(n,0,-1):
        result = i
        new = i*operator 
        new1=result+new+1
        operator=1
    print(abs(new1))
def option2(n,operator):
    result=0
    new=0
    new1=0
    for i in range(n,0,-1):
        new= i*operator
        new1=result+new
        operator=-1
    print(abs(new1))

if choice == 1:
    operator=-1
    option1(n,operator)
else:
    operator=1
    option2(n,operator)
