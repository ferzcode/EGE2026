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

ksvg1 = [] # 10
ksvg2 = [] # 5
ksvg3 = [] # 2

yk1 = []
yk2 = []
yk3 = []

for s in open('27_B.txt'):
    zvezda = s.replace(',', '.').split()

    x = float(zvezda[0])
    y = float(zvezda[1])
    h = zvezda[2]

    if 4 < y < 8:
        cl1.append([x, y])
        if h[0] == 'M' and h[-1] == 'I':
            ksvg1.append([x, y])
        if h[0] == 'G' and h[-1] == 'V':
            yk1.append([x, y])

    if 9 < y < 14:
        cl2.append([x, y])
        if h[0] == 'M' and h[-1] == 'I':
            ksvg2.append([x, y])
        if h[0] == 'G' and h[-1] == 'V':
            yk2.append([x, y])

    if y > 14:
        cl3.append([x, y])
        if h[0] == 'M' and h[-1] == 'I':
            ksvg3.append([x, y])
        if h[0] == 'G' and h[-1] == 'V':
            yk3.append([x, y])

c1 = Center(cl1)
c2 = Center(cl2)
c3 = Center(cl3)

B1 = dist(c1, c3)

B2 = []
for p1 in yk1:
    for p2 in yk1:
        if p1 != p2:
            B2.append(dist(p1, p2))

for p1 in yk2:
    for p2 in yk2:
        if p1 != p2:
            B2.append(dist(p1, p2))

for p1 in yk3:
    for p2 in yk3:
        if p1 != p2:
            B2.append(dist(p1, p2))

B2 = max(B2)
print(B1 * 10000, B2 * 10000)