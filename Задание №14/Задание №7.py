for x in range(1, 2031):
    num = 6 ** 260 + 6 ** 160 + 6 ** 60 - x

    c = 0
    while num > 0:
        if num % 6 == 0:
            c = c + 1
        num = num // 6

    if c == 202:
        print(x)