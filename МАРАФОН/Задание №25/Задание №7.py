def f(n):
    d = set()
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return d


c = 0
for num in range(699_999, 0, -1):
    d = f(num) # ДЕЛИТЕЛИ
    M = sum(d) // len(d) if len(d) > 0 else 0

    # M % 1000 == 313
    if str(M)[-3:] == '313':
        print(num, M)
        c += 1

    if c == 7:
        break