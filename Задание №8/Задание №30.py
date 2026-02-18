from itertools import product, permutations

с = 0
for x in permutations('01234567', r=6):
    s = ''.join(x)

    if '3' not in s and s[0] != '0':
        for c in '0246':
            s = s.replace(c, '*')

        if '**' in s:
            с += 1
print(с)