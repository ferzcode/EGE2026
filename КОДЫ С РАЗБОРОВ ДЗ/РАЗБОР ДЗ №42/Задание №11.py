from itertools import *

k = 0
nomer = 0
for x in product(sorted('ЛОГАРИФМ'), repeat=5):
    s = ''.join(x)
    nomer += 1

    if nomer % 2 == 0 and s[:2] != 'ЛМ' and s.count('И') >= 2:
        k += 1
print(k)
