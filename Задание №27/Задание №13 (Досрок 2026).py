from math import *

def Center(cl):
    m = []
    for p1 in cl:
        s = 0
        for p2 in cl:
            s += dist(p1[:2], p2[:2])
        m.append([s, p1])
    return min(m)[1]

cl1 = []
cl2 = []
for s in open('27_A.txt'):
    zvezda = s.replace(',', '.').split()

    x = float(zvezda[0])
    y = float(zvezda[1])
    h = zvezda[2]

    if y > 10:
        cl1.append([x, y, h])
    if y < 10:
        cl2.append([x, y, h])

c1 = Center(cl1) # 92 звезды
c2 = Center(cl2) # 131 звезда

kg = []
for p in cl1 + cl2: # [x, y, h]
    h = p[2]

    if h[0] == 'Y' and h[-3:] == 'III':
        kg.append(p) # [x, y, h]

A1 = min([dist(c1[:2], p[:2]) for p in kg])
A2 = max([dist(c1[:2], p[:2]) for p in kg])
print(A1 * 10000, A2 * 10000)

