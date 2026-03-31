from math import *

def diametr(cl):
    m = []
    for p1 in cl:
        for p2 in cl:
            #             0            1
            m.append([dist(p1, p2), [p1, p2]])

    return max(m)[1]

clA = [[], []]

for stroka in open('27A_27591.txt'):
    x, y = map(float, stroka.replace(',', '.').split())

    if y > 8:
        clA[0].append([x, y])
    if y < 8:
        clA[1].append([x, y])

d1 = diametr(clA[0])
d2 = diametr(clA[1])

Px = min((d1[0][0] + d1[1][0]), (d2[0][0] + d2[1][0]))
Py = max((d1[0][1] + d1[1][1]), (d2[0][1] + d2[1][1]))

# print(Px * 10000)
# print(Py * 10000)

clB = [[], [], []]
for stroka in open('27B_27591.txt'):
    x, y = map(float, stroka.replace(',', '.').split())

    if 10 < y < 20 and 6 < x < 15:
        clB[0].append([x, y])
    if 10 < x < 18 and 20 < y < 30:
        clB[1].append([x, y])
    if 18 < x < 24 and 20 < y < 30:
        clB[2].append([x, y])

dmin = diametr(clB[2]) # 2 ТОЧКИ КОТОРЫЕ ЕГО ОБРАЗУЮТ
Q1 = dist(dmin[0], dmin[1]) * 10000

d1 = diametr(clB[0])
d2 = diametr(clB[1])
d3 = diametr(clB[2])

print(dist(d1[1], d3[0]) * 10000)