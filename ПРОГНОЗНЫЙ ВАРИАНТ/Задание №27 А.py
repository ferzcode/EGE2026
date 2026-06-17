from math import *

def center(cl):
    m = []
    for p1 in cl:
        s = sum(dist(p1, p2) for p2 in cl)
        m.append([s, p1])

    return min(m)[1]

cl1 = []
cl2 = []
cl3 = []
osk = []
gz1 = []
gz2 = []
gz3 = []
bgg3 = []
zhg1 = []
for s in open('27B.txt'):
    z = s.replace(',', '.').split()

    x = float(z[0])
    y = float(z[1])
    h = z[2]

    if y < 30:
        cl1.append([x, y])
        if h[0] == 'O': gz1.append([x, y])
        if h[0] == 'F' and h[-3:] == 'III' and len(h) == 5: zhg1.append([x, y])
    if y > 30 and x < 16:
        cl2.append([x, y])
        if h[0] == 'O': gz2.append([x, y])
    if y > 30 and x > 16:
        cl3.append([x, y])
        if h[0] == 'O': gz3.append([x, y])
        if h[0] == 'B' and h[-3:] == 'III' and len(h) == 5: bgg3.append([x, y])
    if h[0] == 'K' and h[-2:] == 'VI' and len(h) == 4: osk.append([x, y])

# print(len(cl1), len(cl2), len(cl3), len(gz1), len(gz2), len(gz3))
# print(len(zhg1), len(bgg3))

c1 = center(cl1)  # 165
c2 = center(cl2)  # 68
c3 = center(cl3)  # 43

B1 = min([dist(c1, p1) for p1 in osk] + [dist(c3, p1) for p1 in osk] + [dist(c2, p1) for p1 in osk])
print(B1 * 10000)

B2 = max([dist(p1, p2) for p1 in zhg1 for p2 in bgg3])
print(B2 * 10000)
