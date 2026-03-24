from itertools import *

k = 0
for x in product('0123456789ABC', repeat=5):
    s = ''.join(x)

    if s[0] != '0' and s.count('0') == 1 and '00' not in s and '11' not in s \
            and '22' not in s and '33' not in s and '44' not in s and '55' not in s \
            and '66' not in s and '77' not in s and '88' not in s and '99' not in s \
            and 'AA' not in s and 'BB' not in s and 'CC' not in s:
        k += 1
print(k)