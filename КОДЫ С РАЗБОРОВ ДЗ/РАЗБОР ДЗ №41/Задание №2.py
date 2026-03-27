def delit(x):
    d = set()

    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return d

c = 0
for num in range(1_000_000, 2_000_000):
    deliteli = delit(num)

    M = min(deliteli) + max(deliteli) if len(deliteli) > 0 else 0
    if M % 10 == 6:
        print(num, M)
        c += 1

    if c == 5:
        break