from math import *

d111 = [x for x in range(0, 1_000_000, 111) if x % 2 == 0 and all(c not in str(x) for c in '13579')]
st5 = [5 ** x for x in range(1, 15)]

otvet = []
for c1 in d111:
    for c2 in st5:
        if (c1 + c2) >= 1_000_000:
            otvet.append([c1 + c2, log(c2, 5)])

for chislo, stepen in sorted(otvet)[:5]:
    print(chislo, round(stepen))
