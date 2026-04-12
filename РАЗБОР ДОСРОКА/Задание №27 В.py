from math import dist

def Center(cl):
    m = []
    for p1 in cl: # [x, y, h]
        s = 0
        for p2 in cl:
            s += dist(p1[:2], p2[:2])
        m.append([s, p1])
    return min(m)[1]

clB = [[], [], []]


for s in open('27_B.txt'):
    zvezda = s.replace(',', '.').split()
    x, y = float(zvezda[0]), float(zvezda[1])
    h = zvezda[2]

    if 20 < x < 30:
        clB[0].append([x, y, h])
    if 10 < x < 20 and 15 < y < 22:
        clB[1].append([x, y, h])
    if 22 < y < 30:
        clB[2].append([x, y, h])


# Z ... IV
zg1 = [] # 10

for p1 in clB[0]:
    h = p1[2]

    if h[0] == 'Z' and h[-2:] == 'IV':
        zg1.append(p1)

zg2 = [] # 3

for p1 in clB[1]:
    h = p1[2]

    if h[0] == 'Z' and h[-2:] == 'IV':
        zg2.append(p1)

zg3 = [] # 1
for p1 in clB[2]:
    h = p1[2]

    if h[0] == 'Z' and h[-2:] == 'IV':
        zg3.append(p1)

d = []
for p1 in zg1:
    for p2 in zg1:
        if p1 != p2:
            d.append(dist(p1[:2], p2[:2]))

for p1 in zg2:
    for p2 in zg2:
        if p1 != p2:
            d.append(dist(p1[:2], p2[:2]))

B1 = min(d)
print(B1 * 10000)

c1 = Center(clB[0])
c3 = Center(clB[2])

B2 = dist(c1[:2], c3[:2])
print(B2 * 10000)