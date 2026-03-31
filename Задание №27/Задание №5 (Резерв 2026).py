from math import *

def Center(cl):
    m = []
    for p1 in cl:
        s = sum(dist(p1, p2) for p2 in cl)
        m.append([s, p1])
    return min(m)[1]

clA = [[], []]

for s in open('27_A_23384.txt'):
    x, y = map(float, s.replace(',', '.').split())

    if 2 < x < 6 and 4 < y < 10:
        clA[0].append([x, y])
    if 4 < x < 10 and 10 < y < 16:
        clA[1].append([x, y])

center1 = Center(clA[0])
center2 = Center(clA[1])
Px = (center1[0] + center2[0])
Py = (center1[1] + center2[1])
print(Px * 10000, Py * 10000)

clB = [[], [], []]
for s in open('27_B_23384.txt'):
    x, y = map(float, s.replace(',', '.').split())

    if 10 < x < 20 and 12 < y < 21:
        clB[0].append([x, y])
    if 20 < x < 30:
        clB[1].append([x, y])
    if 21 < y < 27 and 10 < x < 20:
        clB[2].append([x, y])

center1 = Center(clB[0])
center2 = Center(clB[1])
center3 = Center(clB[2])

Q1 = min(dist(center1, [0, 0]), dist(center2, [0, 0]), dist(center3, [0, 0]))
Q2 = max(dist(center1, [0, 0]), dist(center2, [0, 0]), dist(center3, [0, 0]))
print(Q1 * 10000, Q2 * 10000)