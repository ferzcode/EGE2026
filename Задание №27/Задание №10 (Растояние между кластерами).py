from math import dist

def kraynie(cl1, cl2):
    #              0         1
    m = [] # ([расстояние, [p1, p2]])
    for p1 in cl1:
        for p2 in cl2:
            r = dist(p1, p2)
            m.append([r, [p1, p2]])
    return min(m)[1]

cl1 = []
cl2 = []
for s in open('27A_1_20132 (1).txt'):
    x, y = map(float, s.replace(',', '.').split())

    if y < 6:
        cl1.append([x, y])
    if y > 6:
        cl2.append([x, y])

kr1 = kraynie(cl1, cl2)
print(kr1)
Px = (kr1[0][0] + kr1[1][0]) / 2
Py = (kr1[0][1] + kr1[1][1]) / 2

print(Px * 10000, Py * 10000)