from math import dist

def plotnost(cl):
    m = []

    for p1 in cl:
        c = 0
        for p2 in cl:
            if dist(p1, p2) <= 1:
                c += 1
        m.append(c)
    return sum(m) / len(m)


cl1 = []
cl2 = []
cl3 = []
cl4 = []

for s in open('27A_20295.txt'):
    x, y = map(float, s.split())

    if x < 0 and y > 0:
        cl1.append([x, y])
    if x < 1 and y < 0:
        cl2.append([x, y])
    if 2 < x < 5 and 2 < y < 5:
        cl3.append([x, y])
    if 3.5 < x < 7.5 and -2.5 < y < 1.5:
        cl4.append([x, y])

pl1 = plotnost(cl1)
pl2 = plotnost(cl2)
pl3 = plotnost(cl3)
pl4 = plotnost(cl4)
Pmin = min(pl1, pl2, pl3, pl4)
Pavg = (pl1 + pl2 + pl3 + pl4) / 4

print(int(Pmin * 100000), int(Pavg * 100000))
