def f(num, d = 2):
    for d in range(d, round(num ** 0.5) + 1):
        if num % d == 0:
            return [d] + f(num // d, d)
    return [num]


c = 0
for num in range(23_600_000, 30_000_000):
    d = set(f(num))

    M = min(d) + max(d) if len(d) >= 2 else 0
    if M % 213 == 171:
        print(num, M)
        c += 1

    if c == 6:
        break
        