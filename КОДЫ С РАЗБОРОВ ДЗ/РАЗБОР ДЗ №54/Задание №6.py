def f(num):
    d = set()
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            d.add(i)
            d.add(num // i)
    return d


c = 0
for num in range(500_001, 1_000_000):
    d = f(num)
    R = sum(d)

    if R % 10 == 9:
        print(num, R)
        c += 1

    if c == 5:
        break