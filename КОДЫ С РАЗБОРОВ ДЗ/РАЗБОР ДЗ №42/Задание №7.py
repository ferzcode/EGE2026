from itertools import *

k = 0
for x in product('01234567', repeat=7):
    s = ''.join(x)

    if s[0] != '0' and (s.count('0') + s.count('2') + s.count('4') + s.count('6')) == 2:
        for c in '135':
            s = s.replace(c, '*')

        if '*7' not in s and '7*' not in s and '77' not in s:
            k += 1
print(k)