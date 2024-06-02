numOfChem = int(input())
energies = list(map(int, input().split()))
max1 = float('-inf')
max2 = float('-inf')
for energy in energies:
    if energy > max1:
        max2 = max1
        max1 = energy
    elif energy > max2:
        max2 = energy
total_energy = max1 + max2
print(total_energy)