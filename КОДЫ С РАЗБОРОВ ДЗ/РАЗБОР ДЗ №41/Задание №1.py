from math import prod

def delit(x):
    d = []

    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            d.append(i)
            d.append(x // i)
    return d

c = 0
for num in range(4_000_000, 5_000_000):
    deliteli = delit(num)
    prostie = [d for d in deliteli if len(delit(d)) == 0 and (str(d).count('1') > 0 or str(d).count('2') > 0)]

    if len(prostie) == 2 and prod(prostie) == num:
        print(num, max(prostie))
        c += 1

    if c == 5:
        break