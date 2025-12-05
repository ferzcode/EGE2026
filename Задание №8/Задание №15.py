# Сколько существует тринадцатеричных семизначных чисел,
# в которых все цифры различны
# и никакая нечётная цифра не стоит рядом с цифрой B?

from itertools import permutations

c = 0
for x in permutations('0123456789ABC', r=7):
    s = ''.join(x)

    # 1 3 5 7 9
    # 1B B1 3B B3 5B B5 B7 7B 9B B9
    # *B B*

    if s[0] != '0':
        for cifra in '13579':
            s = s.replace(cifra, '*')
        if '*B' not in s and 'B*' not in s:
            c += 1
print(c)