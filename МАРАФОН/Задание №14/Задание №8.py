for x in range(1, 10001):
    num = 6 ** 900 + 6 ** 10 - x

    c3 = 0
    c5 = 0
    while num > 0:
        if num % 6 == 3:
            c3 += 1
        if num % 6 == 5:
            c5 += 1

        num //= 6

    if c3 == c5:
        print(x)