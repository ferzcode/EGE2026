from math import dist

def center(cl):
    m = []
    for p1 in cl:
        s = 0
        for p2 in cl:
            s += dist(p1, p2)
        m.append([s, p1])
    return max(m)[1]

cl1 = []
cl2 = []
cl3 = []

for s in open('27A_22076.txt'):
    x, y = map(float, s.split())

    if y < 0:
        cl1.append([x, y])
    if 0 < y < 5:
        cl2.append([x, y])
    if 14 < y < 20:
        cl3.append([x, y])

ac1 = center(cl1)
ac2 = center(cl2)
ac3 = center(cl3)

rastoyania = []
for p in cl1 + cl2 + cl3:
    r = dist(p, ac1) + dist(p, ac2) + dist(p, ac3)
    rastoyania.append([r, p])

retranslator = max(rastoyania)[1]
print(retranslator[0] * 10000, retranslator[1] * 10000)