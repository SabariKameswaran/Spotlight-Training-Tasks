input1=[1,2,4,5,7,9]
input2=9
def missing_value():
    # sum=0
    # sum1=0
    # n=len(input1)
    # for i in range(1,6):
    #     sum+=i
    # for j in range(0,len(input1)):
    #     sum1+=input1[j]
    # print(((n)*(n+1))/2-sum1)
    #Set Method
    sum=set(range(1,input2+1))
    sum1=set(input1)
    print(sum-sum1)
missing_value()