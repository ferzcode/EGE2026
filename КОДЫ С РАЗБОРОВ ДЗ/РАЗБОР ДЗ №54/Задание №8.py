def f(n, d=2):
    for d in range(d, round(n ** 0.5) + 1):
        if n % d == 0:
            return [d] + f(n // d, d)
    return [n]


c = 0
for num in range(456_790, 1_000_000):
    d = sorted(set(f(num)))

    M = d[0] + d[1] + d[-1] + d[-2] if len(d) >= 4 else 0

    if M % 114 == 39:
        print(num, M)
        c += 1

    if c == 5:
        break



