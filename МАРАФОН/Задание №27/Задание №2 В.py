from math import *

def center(cl):
    m = []
    for p1 in cl:
        s = sum(dist(p1, p2) for p2 in cl)
        m.append([s, p1])
    return min(m)[1]

cl1 = []
cl2 = []
cl3 = []

z1_max = []
z3_min = []

for p in open('27_B_29079.txt'):
    s = p.replace(',', '.').split()

    x = float(s[0])
    y = float(s[1])
    h = s[2]

    if x > 20:
        cl1.append([x, y])
        if h[0] == 'J' and h[-1] == 'V' and h[-2] != 'I':
            z1_max.append([x, y])
    if 10 < x < 20 and y < 22:
        cl2.append([x, y])

    if 10 < x < 20 and y > 22:
        cl3.append([x, y])
        if h[0] == 'J' and h[-1] == 'V' and h[-2] != 'I':
            z3_min.append([x, y])

B1 = max([p[0] for p in z1_max])
B2 = max([p[1] for p in z3_min])

print(B1 * 10000, B2 * 10000)