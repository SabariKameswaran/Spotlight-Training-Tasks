erp = int(input())
if 30 <= erp <= 50:
    erg = 'D'
elif 51 <= erp <= 60:
    erg = 'C'
elif 61 <= erp <= 80:
    erg = 'B'
elif 81 <= erp <= 100:
    erg = 'A'
else:
    erg = 'Invalid ERP' 
print(erg)