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

s1 = []
s2 = []
s3 = []

for p in open('27_B_29080.txt'):
    s = p.replace(',', '.').split()

    x = float(s[0])
    y = float(s[1])
    h = s[2]

    if x > 20:
        cl1.append([x, y])
        if h[0] == 'L':
            s1.append([x, y])
    if 10 < x < 20 and y < 22:
        cl2.append([x, y])
        if h[0] == 'L':
            s2.append([x, y])
    if 10 < x < 20 and y > 22:
        cl3.append([x, y])
        if h[0] == 'L':
            s3.append([x, y])

c1 = center(cl1)
c2 = center(cl2)
c3 = center(cl3)

B1 = dist(c3, c1)
B2 = [dist(p1, p2) for p1 in s1 for p2 in s2] + [dist(p1, p2) for p1 in s1 for p2 in s3] + [dist(p1, p2) for p1 in s2 for p2 in s3]

# for p1 in s1:
#     for p2 in s2:
#         B2.append(dist(p1, p2))
#
# for p1 in s1:
#     for p2 in s3:
#         B2.append(dist(p1, p2))
#
# for p1 in s2:
#     for p2 in s3:
#         B2.append(dist(p1, p2))

print(B1 * 10000, max(B2) * 10000)

# print(len(s1)) # 66
# print(len(s2)) # 13
# print(len(s3)) # 7