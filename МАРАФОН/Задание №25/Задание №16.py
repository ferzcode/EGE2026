from math import *

st5 = [5 ** x for x in range(1, 15)]
d111 = [x for x in range(111, 10_000_000, 111) if x % 2 == 0 and '1' not in str(x) and '3' not in str(x) and '5' not in str(x) and '7' not in str(x) and '9' not in str(x)]

otvet = []
for c1 in st5:
    for c2 in d111:
        s = c1 + c2

        if s > 1_000_000:
            otvet.append([s, c1])

for c1, c2 in sorted(otvet)[:5]:
    print(c1, round(log(c2, 5)))