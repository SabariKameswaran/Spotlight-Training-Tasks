innput1=8
input2=[1,-6,-5,-12,1,3,8,-3]
def circuit():
    new=0
    input2.sort(reverse=True)
    print(input2)
    print(input2[0],input2[-1])
    mid=int(len(input2)/2)
    print(((input[i]-input[j]for j in range(-1,-mid,-1))for i in range(0,mid)))
    # for i in range(0,mid):
    #     for j in range(-1,-mid,-1):
    #         new=input2[i]-input2[j]
    #         print(input2[i])
    #         print(input2[j])
    # print(new)
circuit()