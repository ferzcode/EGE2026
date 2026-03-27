from itertools import *

k = 0
for x in product('0123456789ABC', repeat=6):
    s = ''.join(x)

    if s[0] != '0' and s.count('5') <= 1:
        for c in '13579B':
            s = s.replace(c, '*')

        if '**' not in s:
            k += 1

print(k)