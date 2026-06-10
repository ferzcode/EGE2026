def f(n):
    d = set()
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return d


c = 0
for num in range(902_715, 10_000_000):
    d = f(num) # ВСЕ ДЕЛИТЕЛИ

    d5 = [n for n in d if (n % 10 == 5 and n != num and n != 5)]
    if len(d5) > 0:
        print(num, min(d5))
        c += 1

    if c == 6:
        break
