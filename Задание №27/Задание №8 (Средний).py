from math import dist

def center(cl):
    m = []
    for p1 in cl:
        s = 0
        for p2 in cl:
            s += dist(p1, p2)

        m.append([s, p1])
    return min(m)[1]


# cl1 = []
# cl2 = []
#
# for s in open('27A_27138.txt'):
#     x, y = map(float, s.replace(',', '.').split())
#
#     if y < 0:
#         cl1.append([x, y])
#     if y > 0:
#         cl2.append([x, y])
#
# center1 = center(cl1)
# center2 = center(cl2)
#
# Sx = abs(center1[0] - center2[0])
# Sy = abs(center1[1] - center2[1])
# print(Sx * 10000, Sy * 10000)

cl1 = []
cl2 = []
cl3 = []
c = 0
for s in open('27B_27138.txt'):
    x, y = map(float, s.replace(',', '.').split())
    c += 1
    if 30 < x < 50 and -35 < y < -20:
        cl1.append([x, y])
    if -50 < x < -40 and 15 < y < 25:
        cl2.append([x, y])
    if 20 < x < 40 and 15 < y < 27:
        cl3.append([x, y])

Q1 = -10000000000
for p in cl2:
    Q1 = max(Q1, p[0])

m = []
for p in cl1:
    s = 0
    for p2 in cl2 + cl3:
        s += dist(p, p2)
    m.append([s, p])

for p in cl2:
    s = 0
    for p2 in cl1 + cl3:
        s += dist(p, p2)
    m.append([s, p])

for p in cl3:
    s = 0
    for p2 in cl1 + cl2:
        s += dist(p, p2)
    m.append([s, p])

Q2 = max(m)[1]
print(abs(Q1) * 10000)
Q2 = Q2[0] + Q2[1]
print(abs(Q2) * 10000)