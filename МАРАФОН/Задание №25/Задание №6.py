def f(n):
    d = set()
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return d

c = 0
for num in range(700_001, 1700_000):
    d = f(num)
    M = min(d) + max(d) if len(d) >= 2 else 0

    if M % 10 == 4:
        print(num, M)
        c += 1
    if c == 5:
        break
        