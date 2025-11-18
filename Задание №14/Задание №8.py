for x in range(1, 2031):
    n = 7 ** 170 + 7 ** 100 - x

    c = 0
    while n > 0:
        if n % 7 == 0:
            c = c + 1
        n = n // 7

    if c == 71:
        print(x)