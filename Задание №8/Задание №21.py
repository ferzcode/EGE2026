# Сколько существует различных трёхзначных и пятизначных чисел,
# записанных в шестнадцатеричной системе счисления,
# в записи которых цифры следуют слева направо в строго убывающем порядке?

from itertools import product

c = 0
for x in product('0123456789ABCDEF', repeat=3):
    s = ''.join(x)
    if s[0] != '0' and s[0] > s[1] > s[2]:
        c = c + 1

for x in product('0123456789ABCDEF', repeat=5):
    s = ''.join(x)
    if s[0] != '0' and s[0] > s[1] > s[2] > s[3] > s[4]:
        c = c + 1

print(c)