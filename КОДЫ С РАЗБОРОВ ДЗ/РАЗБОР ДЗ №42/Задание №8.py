from itertools import *

nomer = 0
c = 0
for x in product(sorted('АОЖПЮЗ'), repeat=6):
    s = ''.join(x)
    nomer += 1

    if nomer % 2 == 0 and s[0] == 'А' and s.count('З') >= 2:
        c += 1
print(c)
