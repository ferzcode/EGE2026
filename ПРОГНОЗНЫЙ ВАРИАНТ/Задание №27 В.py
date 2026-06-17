from math import *


def center(cl):
    m = []
    for p1 in cl:
        s = sum(dist(p1, p2) for p2 in cl)
        m.append([s, p1])

    return min(m)[1]


cl1 = []
cl2 = []
kk = []
for s in open('27A.txt'):
    z = s.replace(',', '.').split()

    x = float(z[0])
    y = float(z[1])
    h = z[2]

    if y > 15:
        cl1.append([x, y])
    if y < 15:
        cl2.append([x, y])
    if h[0] == 'M' and h[1] in '456789' and h[2] == 'V' and len(h) == 3: kk.append([x, y])

# print(len(cl1), len(cl2), len(kk))

c1 = center(cl1)  # 121
c2 = center(cl2)  # 114

A = []
for p1 in kk:
    a = dist(c2, p1)
    A.append([a, p1])

print(min(A)[1][0] * 10000)
print(min(A)[1][1] * 10000)

