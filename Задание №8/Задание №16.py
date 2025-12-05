# Сколько существует шестизначных чисел, записанных в семнадцатеричной системе счисления,
# в которых все цифры различны и никакие три чётные или три нечётные цифры не стоят рядом?

from itertools import permutations

c = 0
for x in permutations('0123456789ABCDEFG', r=6):
    s = ''.join(x)

    if s[0] != '0':
        # ЧЕТНЫЕ - 0 2 4 6 8 A C E G
        for cifra in '02468ACEG':
            s = s.replace(cifra, '*')
        # НЕЧЕТНЫЕ - 1 3 5 7 9 B D F
        for cifra in '13579BDF':
            s = s.replace(cifra, '?')

        if '***' not in s and '???' not in s:
            c = c + 1
print(c)
