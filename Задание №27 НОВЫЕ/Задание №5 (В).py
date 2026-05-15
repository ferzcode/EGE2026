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
karlik1 = []
karlik2 = []
karlik3 = []
for stroka in open('Задание №5 В.txt'):
    zv = stroka.replace(',', '.').split()

    x = float(zv[0])
    y = float(zv[1])
    h = str(zv[2])

    if y < -10: # МИНИМУМ
        cl1.append([x, y])
        if h[0] == 'L' and h[-1] == 'V' and h[-2] != 'I':
            karlik1.append([x, y])
    if -5 < y < 5: # МЕДИАНА
        cl2.append([x, y])
        if h[0] == 'L' and h[-1] == 'V' and h[-2] != 'I':
            karlik2.append([x, y])
    if y > 5: # МАКСИМУМ
        cl3.append([x, y])
        if h[0] == 'L' and h[-1] == 'V' and h[-2] != 'I':
            karlik3.append([x, y])

rast = []
for p1 in karlik3:
    for p2 in karlik3:
        if p1 != p2:
            rast.append(dist(p1, p2))
B1 = sum(set(rast))

c1 = center(cl1)
c2 = center(cl2)
B2 = dist(c1, c2)
x = print(B1 * 10000, B2 * 10000)
