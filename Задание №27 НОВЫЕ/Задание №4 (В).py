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
golub_subgig = []
belie_karliki = []

belie_subgig = []
orange_karliki = []

for stroka in open('27_B.txt'):
    zv = stroka.replace(',','.').split()

    x = float(zv[0])
    y = float(zv[1])
    h = str(zv[2])

    if y > 14:
        cl1.append([x, y])
        if h[0] == 'A' and h[-1] == 'V' and h[-2] != 'I':
            belie_karliki.append([x, y])
        if h[0] == 'K' and h[-1] == 'V' and h[-2] != 'I':
            orange_karliki.append([x, y])

    if 8 < y < 14:
        cl2.append([x, y])
    if y < 8:
        cl3.append([x, y])
        if h[0] == 'O' and h[-2:] == 'IV':
            golub_subgig.append([x, y])
        if h[0] == 'A' and h[-2:] == 'IV':
            belie_subgig.append([x, y])

rast1 = []
for p1 in golub_subgig:
    for p2 in belie_karliki:
        rast1.append(dist(p1, p2))

B1 = min(rast1)
rast2 = []
for p1 in belie_subgig:
    for p2 in orange_karliki:
        rast2.append(dist(p1, p2))

B2 = max(rast2)
print(int(B1 * 10000), int(B2 * 10000))