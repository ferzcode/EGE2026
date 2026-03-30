summa = 0
nomer = 0
for stroka in open('Задание №1.txt'):
    s = sorted([int(x) for x in stroka.split()])
    nomer += 1

    # 1 2 3 4
    # 14 23 | 13 24 | 12 34

    if (s[0] + s[-1]) ** 2 > (s[1] ** 3 + s[2] ** 3):
        if (s[0] + s[3]) != (s[1] + s[2]) and (s[0] + s[2]) != (s[1] + s[3]) and (s[0] + s[1]) != (s[2] + s[3]):
            summa += nomer

print(summa)