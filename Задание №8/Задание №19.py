# Определите количество 12-ричных шестизначных чисел,
# в записи которых содержится
# ровно одна цифра «B» и равное количество чётных и нечётных цифр.

from itertools import product

c = 0
for x in product('0123456789AB', repeat=6):
    s = ''.join(x)

    chetnie = s.count('0') + s.count('2') + s.count('4') + s.count('6') + s.count('8') + s.count('A')
    nechetnie = s.count('1') + s.count('3') + s.count('5') + s.count('7') + s.count('9') + s.count('B')

    if s[0] != '0' and s.count('B') == 1 and chetnie == nechetnie:
        c = c + 1
print(c)