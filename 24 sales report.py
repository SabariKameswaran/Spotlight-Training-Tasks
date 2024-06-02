days, products = map(int, input().split())
max_revenues = []
for _ in range(days):
    sales_data = list(map(int, input().split()))
    max_revenue = max(sales_data)
    max_revenues.append(max_revenue)
print(max_revenues)