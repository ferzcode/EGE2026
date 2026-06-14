from itertools import *

nomer = 0
for x in product(sorted('СИМВОЛ'), repeat=5):
    s = ''.join(x)
    nomer += 1

    if nomer % 2 != 0 and s[0] not in 'ОС' and s.count('В') == 1 and s.count('С') <= 1:
        print(nomer)
