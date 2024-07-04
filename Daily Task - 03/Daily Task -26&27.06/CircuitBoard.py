innput1=8
input2=[1,-6,-5,-12,1,3,8,-3]
def circuit():
    new=0
    p=[]
    n=[]
    # input2.sort(reverse=True)
    for i in input2:
        if i<0:
            n.append(i)
            # input2.remove(i)
        else:
            p.append(i)
    p.sort(reverse=True)
    print(p)
    # input2.sort()
    n.sort()
    print(n)
    # print(input2)
    # print(input2[0],input2[-1])
    # mid=int(len(input2)/2)

    # print(((input[i]-input[j]+circuit() for j in range(-1,-mid,-1))for i in range(0,mid)))
    for i in p:
        for j in n:
            new=i-j
    # new=sum(abs(x)for x in input2)

    print(new)
circuit()