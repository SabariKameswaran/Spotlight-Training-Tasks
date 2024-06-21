in1=int(input())
in2=int(input())
in3=int(input())
def first_large(in1,in2,in3):
    first=[int(digit) for digit in str(in1)]
    second=[int(digit) for digit in str(in2)]
    third=[int(digit) for digit in str(in3)]
    one=first[0],second[0],third[0]
    two=first[1],second[1],third[1]
    three=first[2],second[2],third[2]
    four=first[3],second[3],third[3]
    print(f"{min(one),max(two),min(three),max(four)}")
first_large(in1,in2,in3)