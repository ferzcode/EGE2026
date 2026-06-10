from math import *

st3 = [3 ** x for x in range(1, 15)]
d113 = [x for x in range(113, 1000_000, 113) if x % 2 != 0]

otvet = []
for c1 in st3:
    for c2 in d113:
        s = c1 + c2
        if 100_000 <= s <= 999_999 and str(s).count('0') == 0:
            otvet.append([s, c1])

for c1, c2 in sorted(otvet)[:5]:
    print(c1, round(log(c2, 3)))