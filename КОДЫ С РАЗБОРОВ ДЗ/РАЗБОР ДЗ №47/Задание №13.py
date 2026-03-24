from itertools import *

nomer = -1
c = 0
for x in product(sorted(set('КАЛЕЙДОСКОП'), reverse=True), repeat=6):
    s = ''.join(x)
    nomer += 1

    if nomer % 2 == 0 and s[0] == 'К' and s.count('Й') >= 2 and s.count('С') == s.count('Е') == 0:
        print(nomer)
        break