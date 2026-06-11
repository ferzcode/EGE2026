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
orange = []
for p in open('27_A.txt'):
    s = p.replace(',', '.').split()

    x = float(s[0])
    y = float(s[1])
    h = s[2]

    if y < 23.5:
        cl1.append([x, y])
    else:
        cl2.append([x, y])

    if h[0] == 'K' and h[-2:] == 'VI':
        orange.append([x, y])

c1 = center(cl1)
c2 = center(cl2)

A2 = max([dist(c1, p) for p in orange] + [dist(c2, p) for p in orange])
print(A2 * 10000)