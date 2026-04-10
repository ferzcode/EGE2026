def deliteli(num):
    d = set()

    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            d.add(i)
            d.add(num // i)

    return d

c = 0
for num in range(700_001, 1_000_000):
    d = deliteli(num)

    d7 = [delit for delit in d if delit % 10 == 7 and delit != num and delit != 7]

    if len(d7) > 0:
        c += 1
        print(num, min(d7))

    if c == 5:
        break

