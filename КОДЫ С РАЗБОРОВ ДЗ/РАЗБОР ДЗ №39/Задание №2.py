from math import *

c = 0

for stroka in open('Задание №2.txt'):
    s = [int(x) for x in stroka.split()]

    povtorki = [x for x in s if s.count(x) > 1]
    nepovtorki = [x for x in s if s.count(x) == 1]

    if len(povtorki) > 0:
        if sum(nepovtorki) * 3 <= prod(povtorki):
            c += 1
print(c)