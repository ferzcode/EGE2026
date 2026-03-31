from math import *

from Tools.demo.spreadsheet import center


def plotnost(cl):
    return len(cl) / 16

def Center(cl):
    m = []
    for p1 in cl:
        s = sum(dist(p1, p2) for p2 in cl)
        m.append([s, p1])
    return min(m)[1]


clA = [[], [], []]

for s in open('27A_22623.txt'):
    x, y = map(float, s.split())

    if 0 < x < 5 and 0 < y < 10:
        clA[0].append([x, y])
    if 15 < x < 21 and 0 < y < 10:
        clA[1].append([x, y])
    if 0 < x < 5 and 20 < y < 25:
        clA[2].append([x, y])


pl1 = plotnost(clA[0])
pl2 = plotnost(clA[1])
pl3 = plotnost(clA[2])
Ps = (pl1 + pl2 + pl3) / 3
print(Ps * 1000)

center1 = Center(clA[0])
center2 = Center(clA[1])
Sp = dist(center1, center2)
print(Sp * 1000)