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
yellow_gig = []
for stroka in open('Задание №5 А.txt'):
    zv = stroka.replace(',','.').split()

    x = float(zv[0])
    y = float(zv[1])
    h = str(zv[2])

    if y < 10:
        cl1.append([x, y])

    if y > 10:
        cl2.append([x, y])

    if h[0] == 'Z' and h[-2:] == 'II' and h[-3] != 'I' and h[-3] != 'V':
        yellow_gig.append([x, y])

c1 = center(cl1) # наименьший
c2 = center(cl2) # наибольший

A1 = min([dist(c2, p) for p in yellow_gig])
A2 = max([dist(c1, p) for p in yellow_gig])
print(int(A1 * 10000), int(A2 * 10000))
