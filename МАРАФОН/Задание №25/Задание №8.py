def f(num, d = 2):
    for d in range(d, round(num ** 0.5) + 1):
        if num % d == 0:
            return [d] + f(num // d, d)
    return [num]


c = 0
for num in range(32_500_001, 35_000_000):
    prostie = set(f(num))

    S = sum(prostie)
    if S != 0 and S % 145 == 0 and num not in prostie:
        print(num, S)
        c += 1

    if c == 7:
        break