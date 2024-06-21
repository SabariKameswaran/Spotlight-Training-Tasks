in1=int(input())
in2=int(input())
in3=int(input())
def thousand_digit(number):
    while number >10:
        number//=1000
        return number
def hundred_digit(new):
    while new >10:
        new=(new%1000)//100
        return new
def tens_digit(new):
    while new >10:
        new=(new%100)//10
        return new
def ones_digit(new):
    while new >10:
        new%=10
        return new
def main(in1,in2,in3):
    n1=thousand_digit(in1)
    n2=thousand_digit(in2)
    n3=thousand_digit(in3)
    first=min(n1,n2,n3)
    m1=hundred_digit(in1)
    m2=hundred_digit(in2)
    m3=hundred_digit(in3)
    second=max(m1,m2,m3)
    o1=tens_digit(in1)
    o2=tens_digit(in2)
    o3=tens_digit(in3)
    third=min(o1,o2,o3)
    p1=ones_digit(in1)
    p2=ones_digit(in2)
    p3=ones_digit(in3)
    fourth=max(p1,p2,p3)
    print(f"{first}{second}{third}{fourth}")
main(in1,in2,in3)

    # first=[in1//1000,(in1%1000)//100,(in1%100)//10,in1%10]
    # second=[in2//1000,(in2%1000)//100,(in2%100)//10,in2%10]
    # third=[in3//1000,(in3%1000)//100,(in3%100)//10,in3%10]