def binaryToDecimal():
    binary=int(input("enter a Binary:"))
    decimal=0
    i=0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * (2**i)
        binary = binary//10
        i += 1
    print(decimal)
def decimalToBinary():
    decimal=int(input("Enter a Decimal:"))
    binary=0
    print(bin(decimal))
    # while(decimal!=0):
        
        
def main():
    print("Select one:  1.Binary to Decimal, 2.Decimal to Binary")
    choice=int(input())
    if choice == 1:
        binaryToDecimal()
    elif choice ==2:
        decimalToBinary()
    else:
        print("Choose a Correct Option")

main()