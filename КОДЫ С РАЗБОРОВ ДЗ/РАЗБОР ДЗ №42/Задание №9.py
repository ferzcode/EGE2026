from itertools import *

k = 0
for x in product('0123456789ABCDEF', repeat=5):
    s = ''.join(x)

    if s[0] != '0' and s.count('6') == 2:
        for c in '0248ACE':
            s = s.replace(c, '*')

        if '*6' not in s and '6*' not in s and '66' not in s:
            k += 1
print(k)