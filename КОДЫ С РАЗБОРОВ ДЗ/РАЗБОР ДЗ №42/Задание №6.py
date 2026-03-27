from itertools import *

nomer = 0
for x in product(sorted('ГИРЛЯНДА'), repeat=6):
    s = ''.join(x)
    nomer += 1

    if nomer % 2 == 0 and s[0] != 'Я' and s.count('Д') == 3:
        print(nomer)

