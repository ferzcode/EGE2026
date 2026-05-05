from math import *

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
cl3 = []

sv1 = []
sv2 = []
sv3 = []

for stroka in open('27_B_29081.txt'):
    zv = stroka.replace(',','.').split()

    x = float(zv[0])
    y = float(zv[1])
    h = str(zv[2])

    if 20 < x < 30:
        cl1.append([x, y])
        if h[1] in '89':
            sv1.append([x, y])
    if 10 < x < 20 and 15 < y < 22:
        cl2.append([x, y])
        if h[1] in '89':
            sv2.append([x, y])
    if y > 22:
        cl3.append([x, y])
        if h[1] in '89':
            sv3.append([x, y])


c1 = center(cl1)
c2 = center(cl2)
c3 = center(cl3)

# print(len(sv1))
# print(len(sv2))
# print(len(sv3))


rast = []
for p1 in sv1:
    for p2 in sv3:
        rast.append(dist(p1, p2))

for p1 in sv1:
    for p2 in sv2:
        rast.append(dist(p1, p2))

for p1 in sv2:
    for p2 in sv3:
        rast.append(dist(p1, p2))

sr_rast = []
for p1 in sv1:
    for p2 in sv1:
        if p1 != p2:
            sr_rast.append(dist(p1, p2))

for p1 in sv2:
    for p2 in sv2:
        if p1 != p2:
            sr_rast.append(dist(p1, p2))

for p1 in sv3:
    for p2 in sv3:
        if p1 != p2:
            sr_rast.append(dist(p1, p2))

B1 = min(rast) * 10000
B2 = (sum(sr_rast) / len(sr_rast)) * 10000
print(B1, B2)