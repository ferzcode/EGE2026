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

cl1 = [] # НАИБОЛЬШИЙ
cl2 = [] # НАИМЕНЬШИЙ
krasnie_giganti = []

for stroka in open('27_A_29357.txt'):
    zv = stroka.replace(',','.').split()

    x = float(zv[0])
    y = float(zv[1])
    h = str(zv[2])

    if y > 15: cl1.append([x, y])
    if y < 15: cl2.append([x, y])

    if h[0] == 'M' and h[-3:] == 'III':
        krasnie_giganti.append([x, y])

c1 = center(cl1)
c2 = center(cl2)

rast = []
for p1 in krasnie_giganti:
    rast.append([dist(p1, c2), p1])

blizayshiy = min(rast)[1]

Ax = blizayshiy[0] * 10000
Ay = blizayshiy[1] * 10000
print(Ax, Ay)