from math import dist

def center(cl):
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
kar1 = []
kar2 = []
kar3 = []
for stroka in open('Задание №3 В.txt'):
    zv = stroka.replace(',','.').split()

    x = float(zv[0])
    y = float(zv[1])
    h = str(zv[2])

    if y < 15:
        cl1.append([x, y])
        if h[0] == 'L' and h[-1] == 'V' and h[-2] != 'I':
            kar1.append([x, y])
    if 15 < y < 22:
        cl2.append([x, y])
        if h[0] == 'L' and h[-1] == 'V' and h[-2] != 'I':
            kar2.append([x, y])
    if y > 22:
        cl3.append([x, y])
        if h[0] == 'L' and h[-1] == 'V' and h[-2] != 'I':
            kar3.append([x, y])

c1 = center(cl1)
c2 = center(cl2)
c3 = center(cl3)

rast = []
for p in kar1:
    rast.append(dist(p, c1))

for p in kar2:
    rast.append(dist(p, c2))

for p in kar3:
    rast.append(dist(p, c3))

B1 = min(rast) * 10000
B2 = max(rast) * 10000
print(B1, B2)



