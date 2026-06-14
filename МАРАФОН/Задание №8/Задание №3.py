
from itertools import *

c = 0
for x in product('0123456789ABC', repeat=6):
    s = ''.join(x)

    if s[0] != '0' and s.count('0') >= 2:
        for y in 'ABC':
            s = s.replace(y, 'A')
        if s.count('AA') == 1 and s.count('A') == 2:
            c += 1
print(c)