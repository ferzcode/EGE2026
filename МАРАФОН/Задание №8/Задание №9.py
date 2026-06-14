from itertools import *
c = 0
for x in product('012345678', repeat=5):
    s = ''.join(x)

    if s[0] != '0' and s.count('0') == 1:
        for y in '1357':
            s = s.replace(y, '*')

        if '*0' not in s and '0*' not in s:
            c += 1
print(c)
