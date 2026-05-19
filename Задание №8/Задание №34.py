from itertools import *

c = 0
for x in product('0123456789ABC', repeat=6):
    s = ''.join(x)

    if s[0] != '0':
        s = s.replace('A', '*')
        s = s.replace('B', '*')
        s = s.replace('C', '*')

        if s.count('0') >= 2 and s.count('*') == 2 and '**' in s:
            c += 1

print(c)