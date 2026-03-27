from math import *

d113 = [x for x in range(0, 1_000_000, 113) if x % 2 != 0]
st3 = [3 ** x for x in range(1, 15)]

otvet = []
for c1 in d113:
    for c2 in st3:
        if 100_000 <= (c1 + c2) <= 999_999 and str(c1 + c2).count('0') == 0:
            otvet.append([c1 + c2, log(c2, 3)])

for chislo, stepen in sorted(otvet)[:5]:
    print(chislo, round(stepen))
