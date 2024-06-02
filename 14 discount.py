# Example input: 7 18
# Orders list: 9 -3 8 -7 -8 18 10
numOfProducts, disAmount = map(int, input().split())
orders = list(map(int, input().split()))
eligible_products = 0
for order in orders:
    if order != 0 and disAmount % abs(order) == 0:
        eligible_products += 1
print(eligible_products)