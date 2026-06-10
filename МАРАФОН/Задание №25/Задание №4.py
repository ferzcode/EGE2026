def f(n):
    d = set()
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return d


c = 0
for num in range(500_001, 10_000_000):
    d = f(num) # РАЗЛИЧНЫЕ
    R = sum(d)

    if R % 10 == 9:
        print(num, R)
        c += 1

    if c == 5:
        break