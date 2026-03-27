def delit(x):
    d = set()

    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return d

c = 0
for num in range(900_000, 1_000_000):
    deliteli = delit(num)

    R = sum(deliteli) if len(deliteli) > 0 else 0

    if R % 10 == 5:
        print(num, R)
        c += 1

    if c == 5:
        break