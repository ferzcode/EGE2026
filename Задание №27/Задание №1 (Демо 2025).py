from math import dist

def Center(cl):
    m = []
    for p1 in cl:
        s = sum(dist(p1, p2) for p2 in cl)
        m.append([s, p1])

    return min(m)[1]

cl1 = []
cl2 = []
for s in open('27_A_17882.txt'):
    x, y = map(float, s.split())

    if y < 3:
        cl1.append([x, y])
    if y > 3:
        cl2.append([x, y])

center1 = Center(cl1)
center2 = Center(cl2)

Px = (center1[0] + center2[0]) / 2
Py = (center1[1] + center2[1]) / 2
print(Px * 10000, Py * 10000)