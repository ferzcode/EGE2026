from math import *

def f(num, d=2):
    for d in range(d, round(num ** 0.5) + 1):
        if num % d == 0:
            return [d] + f(num // d, d)
    return [num]


c = 0
for num in range(8_996_452, 10_000_000):
    d = f(num) # ВСЕ ПРОСТЫЕ МНОЖИТЕЛИ
    d3 = [x for x in d if str(x).count('3') == 2]

    if len(d3) == 2 and prod(d3) == num and len(d) == 2:
        print(num, max(d3))
        c += 1

    if c == 5:
        break

