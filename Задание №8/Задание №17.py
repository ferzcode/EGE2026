# Сколько существует десятичных четырёхзначных чисел,
# в которых все цифры различны и
# никакие две чётные или две нечётные цифры не стоят рядом?


from itertools import permutations

c = 0
for x in permutations('0123456789', r=4):
    s = ''.join(x)

    if s[0] != '0':
        for cifra in '02468':
            s = s.replace(cifra, '*')
        for cifra in '13579':
            s = s.replace(cifra, '?')
        if '**' not in s and '??' not in s:
            c = c + 1
print(c)