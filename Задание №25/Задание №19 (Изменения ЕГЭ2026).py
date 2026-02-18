from math import *

k103 = [x for x in range(103, 1_000_000, 103) if x % 2 != 0]
st3 = [3 ** x for x in range(1, 15)]

otvet = []
for chislo1 in k103:
    for chislo2 in st3:
        if 100_000 <= (chislo1 + chislo2) < 1_000_000 and str(chislo1 + chislo2).count('1') == 0:

            otvet.append([chislo1 + chislo2, chislo2])

for chislo, stepen in sorted(otvet)[:5]:
    print(chislo, ceil(log(stepen, 3)))

print(sorted(otvet)[:5])