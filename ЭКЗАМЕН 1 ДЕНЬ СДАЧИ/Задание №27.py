# Найти абсциссу и ординату
# ближайшего оранжевого гиганта, ближайшего
# к центру кластера с наибольшим количеством
# точек

c1 = сenter(cl1) # 172
c2 = center(cl2) # 253
orange_gig = []

A = []
for p in orange_gig:
    A.append([dist(p, c2), p])

A1 = min(A)[1]
Ax = A1[0] * 10000
Ay = A1[1] * 10000

# ФАЙЛ В

# B1 - минимальное расстояние между
# желтыми карликами, находящимися
# в одном кластере

# B2 - максимальное расстояние между
# желтыми карликами, находящимися
# в одном кластере

B = []
jk1 = []
jk2 = []
jk3 = []

for p1 in jk1:
    for p2 in jk1:
        if p1 != p2:
            B.append(dist(p1, p2))

for p1 in jk2:
    for p2 in jk2:
        if p1 != p2:
            B.append(dist(p1, p2))

for p1 in jk3:
    for p2 in jk3:
        if p1 != p2:
            B.append(dist(p1, p2))
B1 = min(B)
B2 = max(B)