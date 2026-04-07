from math import dist

def Center(cl):
    m = []

    for p1 in cl:
        s = 0
        for p2 in cl:
            s += dist(p1, p2)
        m.append([s, p1])
    return min(m)[1]

cl1 = []
cl2 = []
cl3 = []
for s in open('27B_25447.txt'):
    x, y = map(float, s.replace(',', '.').split())

    if 15 < x < 25 and -5 < y < 5:
        cl1.append([x ,y])
    if 10 < x < 15 and 5 < y < 15:
        cl2.append([x, y])
    if 15 < x < 20 and 10 < y < 20:
        cl3.append([x, y])

c1 = Center(cl1)
c2 = Center(cl2)
c3 = Center(cl3)


# print(len(cl1)) # max
# print(len(cl2))
# print(len(cl3)) # min

Q1 = []
for p1 in cl3:
    if p1 != c3:
        Q1.append(dist(p1, c3))

print((sum(Q1) / len(Q1)) * 10000)


Q2 = []
for p1 in cl1:
    if p1 != c1:
        Q2.append(dist(p1, c1))

print((sum(Q2) / len(Q2)) * 10000)