value=int(input())
str_v=str(value)
def is_duck(str_v):
    if str_v[0] != '0' and '0' in str_v[:]:
        print("It is a Duck number")
    else:
        print("It is Not a Duck number")
    
is_duck(str_v)