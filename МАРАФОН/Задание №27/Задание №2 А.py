from math import *

def center(cl):
    m = []
    for p1 in cl:
        c = 0
        for p2 in cl:
            c += dist(p1, p2)
        m.append([c, p1])
    return min(m)[1]

cl1 = []
cl2 = []
orange1 = []
orange2 = []

for p in open('27_A_29079.txt'):
    s = p.replace(',', '.').split()

    x = float(s[0])
    y = float(s[1])
    h = s[2]

    if y < 10:
        cl1.append([x, y])
        if h[0] == 'N' and h[-2:] == 'IV':
            orange1.append([x, y])

    else:
        cl2.append([x, y])
        if h[0] == 'N' and h[-2:] == 'IV':
            orange2.append([x, y])


c1 = center(cl1)
c2 = center(cl2)

A = [dist(c1, p) for p in orange2] + [dist(c2, p) for p in orange1]
A1 = min(A) * 10000
A2 = max(A) * 10000
print(A1, A2)
