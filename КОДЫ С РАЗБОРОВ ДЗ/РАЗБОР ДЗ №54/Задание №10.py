from math import *

def f(n, d=2):
    for d in range(d, round(n ** 0.5) + 1):
        if n % d == 0:
            return [d] + f(n // d, d)
    return [n]


c = 0
for num in range(1_324_728, 2_000_000):
    d = f(num) # ПРОСТЫЕ ДЕЛИТЕЛИ
    podh = [dp for dp in d if str(dp).count('5') == 1]

    if len(podh) == 2 and prod(podh) == num:
        print(num, max(podh))
        c += 1

    if c == 5:
        break