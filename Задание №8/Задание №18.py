# Определите количество девятеричных пятизначных чисел,
# в записи которых ровно одна цифра 0,
# при этом никакая нечётная цифра не стоит рядом с цифрой 0.


from itertools import product

c = 0
for x in product('012345678', repeat=5):
    s = ''.join(x)

    if s[0] != '0' and s.count('0') == 1:
        for cifra in '1357':
            s = s.replace(cifra, '*')
        if '0*' not in s and '*0' not in s:
            c = c + 1
print(c)
