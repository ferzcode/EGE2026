def f(num):
    d = set()
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            d.add(i)
            d.add(num // i)
    return d


c = 0
for num in range(902_715, 1_000_000):
    d = f(num)
    delit5 = [d5 for d5 in d if d5 != num and d5 != 5 and d5 % 10 == 5]

    if len(delit5) > 0:
        c += 1
        print(num, min(delit5))

    if c == 6:
        break

