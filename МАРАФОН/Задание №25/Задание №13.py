from math import *

def f(num, d = 2):
    for d in range(d, round(num ** 0.5) + 1):
        if num % d == 0:
            return [d] + f(num // d, d)
    return [num]

c = 0
for num in range(6_651_221, 10_000_000):
    d = f(num)
    d2 = [pd for pd in d if str(pd).count('2') == 1]

    if len(d2) == 2 and prod(d2) == num:
        print(num, max(d2))
        c += 1

    if c == 5:
        break