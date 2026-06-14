from math import *

def center(cl):
    m = []
    for p1 in cl:
        c = 0
        for p2 in cl:
            c += dist(p1, p2)
        m.append([c, p1])
    return min(m)[1]

cl1 = []
cl2 = []
cl3 = []

for p in open('27_B.txt'):
    s = p.replace(',', '.').split()

    x = float(s[0])
    y = float(s[1])
    h = s[2]

    if 20 < x < 30:
        cl1.append([x, y])
    if 10 < x < 20 and 15 < y < 22:
        cl2.append([x, y])
    if y > 22:
        cl3.append([x, y])

print(len(cl1), len(cl2), len(cl3),