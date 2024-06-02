num_of_plots = int(input())
areas = list(map(int, input().split()))
square_plots_count = 0
for area in areas:
    sqrt_area = int(area**0.5)
    if sqrt_area * sqrt_area == area:
        square_plots_count += 1
print(square_plots_count)