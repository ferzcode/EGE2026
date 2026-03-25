c = 0

for stroka in open('Задание №1.txt'):
    s = [int(x) for x in stroka.split()]

    tri = [x for x in s if s.count(x) == 3] # len() == 3
    odinochki = [x for x in s if s.count(x) == 1] # len() == 3

    if len(tri) == 3 and len(odinochki) == 3:
        if (max(s) ** 2 + min(s) ** 2) >= (sum(s) - min(s) - max(s)) ** 2:
            c += 1
print(c)