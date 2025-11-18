for x in range(1, 2031):
    num = 7 ** 91 + 7 ** 160 - x

    c = 0
    while num > 0:
        if num % 7 == 0:
            c = c + 1
        num //= 7

    if c == 70:
        print(x)