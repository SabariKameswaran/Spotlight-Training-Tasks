def list_traverse(number):
    n=[num for num in number if num>=0]
    negative=[num for num in number if num<0]
    if len(n)==0:
        return "none"
    else:
        n.sort()
        if len(n)%2!=0:
            mid=len(n)//2
            return n[mid]
        else:
            mid=len(n)//2
            avg=n[mid]+n[mid-1]
            avg/=2
            return avg
a=input()
number=list(map(int,a.split()))
print(list_traverse(number))