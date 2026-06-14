from itertools import *

c = 0
for x in product('0123456789ABC', repeat=5):
    s = ''.join(x)

    if s[0] != '0' and s.count('0') == 1 and \
        all(y + y not in s for y in '0123456789ABC'):
            c += 1
print(c)
