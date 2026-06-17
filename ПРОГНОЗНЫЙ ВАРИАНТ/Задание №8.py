from itertools import *

nomer = 0
for x in product(sorted('АПРЕЛЬ'), repeat=6):
    s = ''.join(x)

    nomer += 1

    if nomer % 2 != 0 and s[0] not in 'АЛ' and s.count('П') >= 2:
        print(nomer)
        break