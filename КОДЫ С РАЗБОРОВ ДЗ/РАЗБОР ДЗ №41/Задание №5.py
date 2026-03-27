def delit(x):
    d = set()

    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return d

c = 0
for num in range(860_000, 1_000_000):
    deliteli = delit(num)

    M = max(deliteli) - min(deliteli) if len(deliteli) > 0 else 0

    if M % 100 == 30:
        print(num, M)
        c += 1

    if c == 5:
        break