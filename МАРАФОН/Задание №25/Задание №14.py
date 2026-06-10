from math import *

st3 = [3 ** x for x in range(1, 15)]
d103 = [x for x in range(103, 1000_000, 103) if x % 2 != 0]

otvet = []
for c1 in st3:
    for c2 in d103:
        s = c1 + c2
        if 100_000 <= s <= 999_999 and str(s).count('1') == 0:
            otvet.append([s, c1])

for c1, c2 in sorted(otvet)[:5]:
    print(c1, round(log(c2, 3)))