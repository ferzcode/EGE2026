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
cl3 = []

zg1 = []
zg2 = []
zg3 = []

for s in open('27_B.txt'):
    zvezda = s.replace(',', '.').split()
    x = float(zvezda[0])
    y = float(zvezda[1])
    h = zvezda[2]

    if 22 < x < 30:
        cl1.append([x, y])
        if h[0] == 'Z' and h[-2:] == 'IV':
            zg1.append([x, y])

    if 10 < x < 20 and 15 < y < 22:
        cl2.append([x, y])
        if h[0] == 'Z' and h[-2:] == 'IV':
            zg2.append([x, y])

    if 10 < x < 17 and y > 22:
        cl3.append([x, y])
        if h[0] == 'Z' and h[-2:] == 'IV':
            zg3.append([x, y])


c1 = Center(cl1) # 10
c2 = Center(cl2) # 3
c3 = Center(cl3) # 1

dist1 = []
for p1 in zg1:
    for p2 in zg1:
        if p1 != p2:
            dist1.append(dist(p1, p2))

for p1 in zg2:
    for p2 in zg2:
        if p1 != p2:
            dist1.append(dist(p1, p2))

B1 = min(dist1)
B2 = dist(c1, c3)

print(B1 * 10000, B2 * 10000)