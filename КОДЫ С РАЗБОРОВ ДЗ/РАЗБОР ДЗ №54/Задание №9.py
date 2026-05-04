def f(n, d=2):
    for d in range(d, round(n ** 0.5) + 1):
        if n % d == 0:
            return [d] + f(n // d, d)
    return [n]


c = 0
for num in range(9_500_001, 10_000_000):
    d = sorted(set(f(num)))

    F = sum(d) // len(d) if len(d) > 0 else 0
    if F != 0 and F % 813 == 0:
        print(num, F)
        c += 1

    if c == 5:
        break