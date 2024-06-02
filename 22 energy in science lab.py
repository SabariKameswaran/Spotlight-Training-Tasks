initial, rate, time = map(int, input().split())
energy_list = []
for i in range(1, time + 1):
    energy = initial * (rate ** (i - 1))
    energy_list.append(energy)
print(energy_list)