str1="My Name is Sabari"
str3="'My Name is Sabari'"
str4="My-Name-is-Sabari"
str5='My.Name.is.Sabari.'
def reverse_string(str1):
    str2=""
    for i in range(len(str1)-1,-1,-1):
        str2+=str1[i]
    print(f"'{str2.title()}'") #here we can use title() or capitalize() for it.
    # if str2:
    #     str2 = str2[0].upper() + str2[1:].lower() it doesnt give correct it only capitals the first letter.
reverse_string(str1)
reverse_string(str3)
reverse_string(str4)
reverse_string(str5)