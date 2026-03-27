for x in range(1, 27001):
    num = 3 * 27 ** 9 + 2 * 27 ** 6 + 27 ** 3 - x

    c0 = 0
    while num > 0:
        if num % 27 == 0:
            c0 += 1
        num //= 27

    if c0 == 6:
        print(x)
        break