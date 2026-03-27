from math import *

def delit(x):
    d = []

    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            d.append(i)
            d.append(x // i)
    return d

c = 0
for num in range(750_000, 0, -1):
    deliteli = delit(num)
    prostie = [d for d in deliteli if len(delit(d)) == 0 and d % 10 == 7]

    F = sum(prostie) // len(prostie) if len(prostie) > 0 else 0

    if F != 0 and F % 111 == 0:
        print(num, F)
        c += 1

    if c == 5:
        break
