from math import *

def Center(cl):
    m = []

    for p1 in cl:
        s = 0
        for p2 in cl:
            s += dist(p1, p2)
        m.append([s, p1])
    return min(m)[1]

cl1 = []
cl2 = []

for s in open('1. 27_A.txt'):
    x, y = map(float, s.replace(',', '.').split())

    if x < 1:
        cl1.append([x, y])
    if x > 1:
        cl2.append([x, y])


c1 = Center(cl1)
c2 = Center(cl2)

mX = []
for p in cl1:
    mX.append(abs(c1[0] - p[0]))

for p in cl2:
    mX.append(abs(c2[0] - p[0]))

mY = []
for p in cl1:
    mY.append(abs(c1[1] - p[1]))

for p in cl2:
    mY.append(abs(c2[1] - p[1]))

Px = max(mX)
Py = max(mY)
print(Px * 10000, Py * 10000)