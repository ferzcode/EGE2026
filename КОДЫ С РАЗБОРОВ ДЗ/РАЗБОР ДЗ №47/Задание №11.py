from itertools import *

k = 0
for x in product('0123456', repeat=5):
    s = ''.join(x)

    if s[0] != '0' and s.count('0') == 1 and s.count('1') <= 2:
        k += 1
print(k)