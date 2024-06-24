str1="My Name is Sabari"
str3="'My Name is Sabari'"
str4="My-Name-is-Sabari"
str5="My.Name.is.Sabari"
def reverse_string(str1):
    str2=""
    for i in range(len(str1)-1,-1,-1):
        str2+=str1[i]
    print(str2)
reverse_string(str1)
reverse_string(str3)
reverse_string(str4)
reverse_string(str5)