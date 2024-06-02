no, discount = map(int, input().split())
orders = list(map(int, input().split()))
eligible_products = 0
for order in orders:
    if order > 0:
        if discount % abs(order) == 0:
            eligible_products += 1        
print(eligible_products)