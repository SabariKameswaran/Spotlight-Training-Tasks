str1=input()
def string_manipulation(str1):
    upper=0
    lower=0
    for char in str1:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1
    if upper>lower:
        print(str1.upper())
    else:
        print(str1.lower())
string_manipulation(str1)