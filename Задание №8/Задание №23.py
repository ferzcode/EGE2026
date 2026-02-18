from itertools import product
c = 0
nomer = 0
for x in product(sorted('МУЖЧИНА'), repeat=6):
    s = ''.join(x)
    nomer += 1

    if nomer % 2 == 0 and s[0] != 'Ж' and s.count('Ч') <= 1:
        c += 1

print(c)