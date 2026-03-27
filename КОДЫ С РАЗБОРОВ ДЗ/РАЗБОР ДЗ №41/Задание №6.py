from math import *

def delit(x):
    d = []

    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            d.append(i)
            d.append(x // i)
    return d

c = 0
for num in range(6_086_055, 7_000_000):
    deliteli = delit(num)

    prostie = [d for d in deliteli if len(delit(d)) == 0 and str(d).count('6') == 1]
    if len(prostie) == 2 and prod(prostie) == num:
        print(num, max(prostie))
        c += 1

    if c == 5:
        break
