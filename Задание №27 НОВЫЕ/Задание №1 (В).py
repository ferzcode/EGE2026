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

orange_gigachat1 = []
orange_gigachat2 = []
orange_gigachat3 = []

yellow_karlik1 = []
yellow_karlik2 = []
yellow_karlik3 = []

for stroka in open('27_B_29357.txt'):
    zv = stroka.replace(',','.').split()

    x = float(zv[0])
    y = float(zv[1])
    h = str(zv[2])

    if y < 30:
        cl1.append([x, y])
        if h[0] == 'K' and h[-3:] == 'III':
            orange_gigachat1.append([x, y])
        if h[0] == 'G' and h[-1] == 'V' and h[-2] != 'I':
            yellow_karlik1.append([x, y])
    if x < 16 and y > 30:
        cl2.append([x, y])
        if h[0] == 'K' and h[-3:] == 'III':
            orange_gigachat2.append([x, y])
        if h[0] == 'G' and h[-1] == 'V' and h[-2] != 'I':
            yellow_karlik2.append([x, y])

    if x > 16 and y > 30:
        cl3.append([x, y])
        if h[0] == 'K' and h[-3:] == 'III':
            orange_gigachat3.append([x, y])
        if h[0] == 'G' and h[-1] == 'V' and h[-2] != 'I':
            yellow_karlik3.append([x, y])

c1 = center(cl1) # НАИБОЛЬШЕЕ
c2 = center(cl2)
c3 = center(cl3) # НАИМЕНЬШЕЕ

# print(len(orange_gigachat1))
# print(len(orange_gigachat2))
# print(len(orange_gigachat3))

B1 = dist(c1, c3)
max_dist = []
for p1 in yellow_karlik1:
    for p2 in yellow_karlik1:
        max_dist.append(dist(p1, p2))

for p1 in yellow_karlik2:
    for p2 in yellow_karlik2:
        max_dist.append(dist(p1, p2))

for p1 in yellow_karlik3:
    for p2 in yellow_karlik3:
        max_dist.append(dist(p1, p2))

B2 = max(max_dist)
print(B1 * 10000, B2 * 10000)