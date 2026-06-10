from math import *


def f(num, d = 2):
    for d in range(d, round(num ** 0.5) + 1):
        if num % d == 0:
            return [d] + f(num // d, d)
    return [num]


c = 0
for num in range(1_324_728, 2_000_000):
    d = f(num) # ВСЕ ПРОСТЫЕ ДЕЛИТЕЛИ

    d5=  [pd for pd in d if str(pd).count('5') == 1]
    if len(d5) == 2 and prod(d5) == num:
        print(num, max(d5))
        c += 1

    if c == 5:
        break