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

bg = []
for s in open('27_A.txt'):
    zvezda = s.replace(',', '.').split()

    x = float(zvezda[0])
    y = float(zvezda[1])
    h = zvezda[2]

    if 10 < x < 20:
        cl1.append([x, y])
    if 35 < x < 45:
        cl2.append([x, y])

    if h[0] == 'A' and h[-3:] == 'III':
        bg.append([x, y])

c1 = Center(cl1) # 250
c2 = Center(cl2) # 229


tochka = []
for p in bg:
    tochka.append([dist(p, c2), p])
A1 = min(tochka)[1][0]
A2 = min(tochka)[1][1]

print(A1 * 10000, A2 * 10000)