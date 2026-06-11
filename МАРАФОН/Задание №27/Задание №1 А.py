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
sinie_zvezdi = []
for p in open('27_A_29080.txt'):
    s = p.replace(',', '.').split()

    x = float(s[0])
    y = float(s[1])
    h = s[2]

    if y < 10:
        cl1.append([x, y])
    else:
        cl2.append([x, y])

    if h[0] == 'L' and h[1] == '3':
        sinie_zvezdi.append([x, y])

c1 = center(cl1) # 131
c2 = center(cl2) # 92

A1 = max([dist(p, c2) for p in sinie_zvezdi])
A2 = max([dist(p, c1) for p in sinie_zvezdi])
print(A1 * 10000, A2 * 10000)