n = 10
def printing(n):
    if n > 0:
        printing(n-1)
        print(n)
printing(n)