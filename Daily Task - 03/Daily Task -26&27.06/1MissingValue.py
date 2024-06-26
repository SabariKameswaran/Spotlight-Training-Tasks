input1=[1,2,4,5]
input2=5
def missing_value():
    sum=0
    sum1=0
    for i in range(1,6):
        sum+=i
    for j in range(0,len(input1)):
        sum1+=input1[j]
    print(sum-sum1)
missing_value()