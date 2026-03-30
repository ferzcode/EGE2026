c = 0
for stroka in open('Задание №5.txt'):
    s = sorted([int(x) for x in stroka.split()])

    povt = [x for x in s if s.count(x) == 3] # len == 3
    odin = [x for x in s if s.count(x) == 1] # len == 3

    if (len(povt) == 3 and len(odin) == 3) or (s[0] + s[5]) ** 2 > (s[1] ** 2 + s[2] ** 2 + s[3] ** 2 + s[4] ** 2):
            c += 1
print(c)