from itertools import *

k = 0
for x in product('0123456789AB', repeat=5):
    s = ''.join(x)

    if s[0] != '0' and s.count('7') == 1 and (s.count('9') + s.count('A') + s.count('B')) <= 3:
        k += 1
print(k)