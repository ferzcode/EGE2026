c = 0

for stroka in open('Задание №4.txt'):
    s = [int(x) for x in stroka.split()]

    povt = [x for x in s if s.count(x) == 2] # len == 6
    odin = [x for x in s if s.count(x) == 1] # len == 1

    if len(povt) == 6 and len(odin) == 1:
        if (min(povt) + max(povt)) / 2 < odin[0]:
            c += 1
print(c)