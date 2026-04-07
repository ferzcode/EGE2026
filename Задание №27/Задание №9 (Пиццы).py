from math import *

def Center(cl):
            #      0       1
    m = [] # (Расстоние, точка)
    for p1 in cl:
        s = 0
        for p2 in cl:
            s += dist(p1, p2)
        m.append([s, p1])
    return min(m)[1]


cl1 = []
cl2 = []
cl3 = []

for s in open('27_A_21599 (1).txt'):
    x, y = map(float, s.replace(',', '.').split())

    if y > 2 * x - 25:
        cl1.append([x, y])
    if y < 2 * x - 25 and y > -5:
        cl2.append([x, y])
    if y < -5:
        cl3.append([x, y])

c1 = Center(cl1) # [x, y]
c2 = Center(cl2)
c3 = Center(cl3)
Px = (c1[0] + c2[0] + c3[0]) / 3
Py = (c1[1] + c2[1] + c3[1]) / 3

print(abs(int(Px * 10000)), abs(int(Py * 10000)))