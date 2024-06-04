# Method 1
def iseven(number):
    if (number & 1) == 0:
        return "Even"
    else:
        return "Odd"
number = int(input("Enter a number: "))
result = iseven(number)
print(result)

#Method 2
def is_even(number):
    return (number & 1) == 0

number = int(input("Enter a number: "))
result = is_even(number)
if result:
    print("Even")
else:
    print("Odd")
