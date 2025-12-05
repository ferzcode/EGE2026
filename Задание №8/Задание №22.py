# Сколько существует восьмеричных шестизначных чисел,
# не содержащих в своей записи цифру 3,
# в которых все цифры различны и хотя бы две чётные стоят рядом?

from itertools import permutations

c = 0
for x in permutations('01234567', r=6):
    s = ''.join(x)

    if s[0] != '0' and '3' not in s:
        for cifra in '0246':
            s = s.replace(cifra, '*')

        # if '**' in s or '***' in s or '****' in s:
        #     c = c + 1

        if '**' in s:
            c = c + 1
print(c)