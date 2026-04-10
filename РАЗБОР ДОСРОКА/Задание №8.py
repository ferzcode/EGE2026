from itertools import *

nomer = 0
for x in product(sorted('АПРЕЛЬ'), repeat=5):
    s = ''.join(x)
    nomer += 1

    if nomer % 2 == 0 and s[0] != 'Ь' and s[0] != 'Р' and s.count('Л') >= 2:
        print(nomer)