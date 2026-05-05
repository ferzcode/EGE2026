from math import *

# def dist(p1, p2):
#     x1, y1 = p1
#     x2, y2 = p2
#     return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def center(cl):
    m = []
    for p1 in cl:
        s = 0
        for p2 in cl:
            s += dist(p1, p2)
        m.append([s, p1])
    return min(m)[1]

cl1 = []
cl2 = []

kvazar1 = []
kvazar2 = []

for stroka in open('27_A_29081.txt'):
    zv = stroka.replace(',','.').split()

    x = float(zv[0])
    y = float(zv[1])
    h = str(zv[2])

    if y > 10:
        cl1.append([x, y])
        if h[-3:] == 'VII':
            kvazar1.append([x, y])
    if y < 10:
        cl2.append([x, y])
        if h[-3:] == 'VII':
            kvazar2.append([x, y])

# print(len(cl1))
# print(len(cl2))
# print(len(kvazar1))
# print(len(kvazar2))


c1 = center(cl1)
c2 = center(cl2)

rast = []
for p1 in kvazar1:
    rast.append(dist(p1, c1))

for p1 in kvazar2:
    rast.append(dist(p1, c2))

A1 = min(rast)
A2 = max(rast)

print(A1 * 10000, A2 * 10000)
