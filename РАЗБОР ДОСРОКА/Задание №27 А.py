from math import dist

def Center(cl):
    m = []
    for p1 in cl: # [x, y, h]
        s = 0
        for p2 in cl:
            s += dist(p1[:2], p2[:2])
        m.append([s, p1])
    return min(m)[1]


clA = [[], []]

kg = []
for s in open('27_A.txt'):
    zvezda = s.replace(',', '.').split()
    x, y = float(zvezda[0]), float(zvezda[1])
    h = zvezda[2]

    if y > 10:
        clA[0].append([x, y, h])
    else:
        clA[1].append([x, y, h])

c1 = Center(clA[0]) # 92
c2 = Center(clA[1]) # 131


kg = []
for p in clA[0] + clA[1]:
    h = p[2]               # [x, y, h]

    if h[0] == 'Y' and h[-3:] == 'III':
        kg.append(p)

A1 = min([dist(c1[:2], p[:2]) for p in kg])
A2 = max([dist(c1[:2], p[:2]) for p in kg])
print(A1 * 10000, A2 * 10000)