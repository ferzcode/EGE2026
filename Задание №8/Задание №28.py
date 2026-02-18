from itertools import permutations

c = 0
for x in permutations('01234567', r=5):
    s = ''.join(x)

    if s[0] != '0' and s.count('1') == 0:
        for chetnie in '0246':
            s = s.replace(chetnie, '*')
        for nechetnie in '1357':
            s = s.replace(nechetnie, '?')

        if '**' not in s and '??' not in s:
            c += 1
print(c)