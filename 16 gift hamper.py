base1, height1 = map(int, input().split())
base2, height2 = map(int, input().split())
tri1 = base1 + height1
tri2 = base2 + height2
if tri1 < tri2:
    area = (base2 * height2) / 2
else:
    area = (base1 * height1) / 2
print(f"{area:.2f}")