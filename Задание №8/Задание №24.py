from itertools import product

c = 0
nomer = 0
for x in product(sorted('ЦИФЕРБЛАТ'), repeat=5):
    s = ''.join(x)
    nomer += 1

    if nomer % 2 != 0 and s[0] not in 'ИЕА' and s.count('Ц') == s.count('Ф'):
        c += 1
print(c)