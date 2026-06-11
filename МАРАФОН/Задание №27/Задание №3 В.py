# АПРОБАЦИЯ 04.03.26 (№27780)

c1 = center(cl1)
c2 = center(cl2)

A1 = max(len(cl1), len(cl2))
A2 = dist(c1, [1.0, 1.5]) + dist(c2, [1.0, 1.5])

c1 = center(cl1)
c2 = center(cl2) # Cредний
c3 = center(cl3) # Наибольшее

B1 = len([p for p in cl2 if dist(p, c2) <= 1.2 and p != c2])
B2 = min([dist(p, c3) for p in cl3 if p != c3])

# ЗАДАЧА

c1 = center(cl1) # Наибольший
c2 = center(cl2) # Наименьший

zheltie_gigi = []

A1 = min([dist(c1, p) for p in zheltie_gigi])
A2 = max([dist(c2, p) for p in zheltie_gigi])

s1 = []
s2 = []
s3 = []

# MAX - cl1
# MIN - cl2, MED - cl3

B1 = sum(dist(p1, p2) for p1 in s1 for p2 in s1 if p1 != p2)
B2 = dist(c2, c3)