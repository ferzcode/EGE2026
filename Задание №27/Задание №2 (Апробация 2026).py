from math import dist

def Center(cl):
    m = []
    for p1 in cl:
        s = sum(dist(p1, p2) for p2 in cl)
        m.append([s, p1])
    return min(m)[1]

cl1 = []
cl2 = []

for s in open('27A_27780.txt'):
    x, y = map(float, s.replace(',', '.').split())

    if y > 15:
        cl1.append([x, y])
    if y < 15:
        cl2.append([x, y])

center1 = Center(cl1)
center2 = Center(cl2)
A1 = max(len(cl1), len(cl2))
A2 = dist(center1, [1.0, 1.5]) + dist(center2, [1.0, 1.5])
# print(A1, int(A2 * 10000))


cl1 = []
cl2 = []
cl3 = []
for s in open('27B_27780.txt'):
    x, y = map(float, s.replace(',', '.').split())

    if y > 23:
        cl1.append([x, y])
    if y < 23 and x < 25:
        cl2.append([x, y])
    if x > 25:
        cl3.append([x, y])

center1 = Center(cl1)
center2 = Center(cl2)
center3 = Center(cl3)

B1 = 0
for p1 in cl2:
    if dist(center2, p1) <= 1.2 and p1 != center2:
        B1 += 1
print(B1)

B2 = []
for p1 in cl1:
    if p1 != center1:
        B2.append(dist(center1, p1))

print(min(B2) * 10000)