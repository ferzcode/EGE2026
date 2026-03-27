from math import *
from xml.etree.ElementInclude import default_loader


def delit(x):
    d = []

    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            d.append(i)
            d.append(x // i)
    return d

c = 0
for num in range(800_000, 1_000_000):
    deliteli = delit(num)
    M = min(deliteli) + max(deliteli) if len(deliteli) > 0 else 0

    if M % 10 == 4:
        print(num, M)
        c += 1

    if c == 5:
        break
