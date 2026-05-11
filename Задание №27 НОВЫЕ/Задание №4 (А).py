from cgi import print_form
from math import dist

def center(cl):
    m = []
    for p1 in cl:
        s = 0
        for p2 in cl:
            s += dist(p1, p2)
        m.append([s, p1])
    return min(m)[1]

cl1 = [] # сверхгига
cl2 = [] # субгиганты

belie_sverhgiganti = []
subgiga = []
for stroka in open('27_A.txt'):
    zv = stroka.replace(',','.').split()

    x = float(zv[0])
    y = float(zv[1])
    h = str(zv[2])


    if y < 36:
        cl1.append([x, y])
        if h[0] == 'A' and h[-1] == 'I' and h[-2] != 'I' and h[-3] != 'I' and h[-2] != 'V':
            belie_sverhgiganti.append([x, y])

    if y > 36:
        cl2.append([x, y])
        if h[-2:] == 'IV' and int(h[1]) >= 4:
            subgiga.append([x, y])

A1 = len(belie_sverhgiganti)
A2 = len(subgiga)
c2 = center(cl2) # G4III

print(A1, A2)



