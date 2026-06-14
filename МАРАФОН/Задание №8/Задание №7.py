from itertools import *

c = 0
for x in permutations('0123456789', r=4):
    s = ''.join(x)

    if s[0] != '0':
        for y in '02468':
            s = s.replace(y, '*')
        for z in '13579':
            s = s.replace(z, '?')
        if '**' not in s and '??' not in s:
            c += 1
print(c)