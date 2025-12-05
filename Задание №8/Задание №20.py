# Определите количество пятизначных чисел,
# записанных в двенадцатеричной системе счисления,
# в записи которых ровно две цифры A,
# и при этом никакая чётная цифра не стоит рядом с цифрой 7.

from itertools import product

c = 0
for x in product('0123456789AB', repeat=5):
    s = ''.join(x)

    if s[0] != '0' and s.count('A') == 2:
        for cifra in '02468A':
            s = s.replace(cifra, '*')
        if '*7' not in s and '7*' not in s:
            c = c + 1
print(c)