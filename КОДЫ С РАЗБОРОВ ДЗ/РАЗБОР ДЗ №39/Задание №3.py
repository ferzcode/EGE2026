c = 0

for stroka in open('Задание №3.txt'):
    s = [int(x) for x in stroka.split()]

    tri = [x for x in s if s.count(x) == 3] # len() == 3
    odin = [x for x in s if s.count(x) == 1] # len() == 3

    if len(tri) == 3 and len(odin) == 3:
        if sum(tri) ** 2 > sum(odin) ** 2:
            c += 1
print(c)