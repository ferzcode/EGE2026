for x in range(1, 2006):
    num = 4 ** 163 * 5 + 12 ** 62 - x

    c1 = 0
    c4 = 0

    while num > 0:
        if num % 5 == 1:
            c1 += 1
        if num % 5 == 4:
            c4 += 1

        num //= 5

    if c1 < c4:
        print(x)
